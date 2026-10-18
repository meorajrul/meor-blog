"""Synthetic engineering fixtures only: no real author approval or source inspection."""
import copy
import datetime as dt
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('journal_gate',Path(__file__).resolve().parents[1]/'scripts/blog.py')
gate=importlib.util.module_from_spec(spec); spec.loader.exec_module(gate)

class PublicationGate(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name); self.slug='synthetic-test'
        gate.new_article(self.root,self.slug,'reflection')
        self.article=self.root/'site/content/posts'/self.slug/'index.md'
        self.packet=self.root/'research/articles'/self.slug
        text=self.article.read_text().replace('draft = true','draft = false')
        text=text.replace('[AUTHOR INPUT: supply your notes or a real question before drafting.]',
            'This is a synthetic engineering fixture. It represents no real person, event, approval or inspected source. '
            'Its only purpose is to exercise the publication checks with enough body text to represent a nonempty article. '
            'It must never be published as a real journal entry.')
        self.article.write_text(text,encoding='utf-8')
        rev=gate.load_json(self.packet/'review.json')
        rev.update(status='approved',author_approved=True,reviewer='Synthetic reviewer (test fixture only)',
            reviewed_on=gate.today().isoformat(),unresolved_issues=[])
        rev.update({key:True for key in gate.CHECKS})
        self.write('review.json',rev); self.seal()
    def write(self,name,value):
        (self.packet/name).write_text(json.dumps(value,indent=2),encoding='utf-8')
    def seal(self):
        rev=gate.load_json(self.packet/'review.json'); rev['content_sha256']=gate.digest(self.root,self.slug)
        self.write('review.json',rev)
    def check(self):
        return gate.validate_article(self.root,self.article)
    def rejects(self,word):
        with self.assertRaisesRegex(gate.GateError,word): self.check()
    def external(self):
        src={'id':'S1','title':'Synthetic source; never inspected in reality','url':'https://example.com/synthetic',
            'publisher':'Synthetic test fixture','accessed':gate.today().isoformat(),'inspection':'inspected',
            'locator':'Synthetic section','origin_group':'test-origin','appraisal':'Not real evidence; structural test only'}
        claim={'id':'C1','text':'Synthetic assertion only','kind':'external-fact','status':'supported',
            'confidence':'synthetic','source_ids':['S1'],'locator':'Synthetic section','limitations':'Not real evidence'}
        self.write('sources.json',[src]); self.write('claims.json',[claim])
        with self.article.open('a',encoding='utf-8') as f: f.write('\n[Synthetic source](https://example.com/synthetic)\n')
        self.seal(); return src,claim
    def test_complete_reflection(self): self.assertEqual(self.check(),'public')
    def test_complete_structural_essay(self):
        self.external(); self.article.write_text(self.article.read_text().replace('genre = "reflection"','genre = "essay"'))
        self.seal(); self.assertEqual(self.check(),'public')
    def test_author_approval_required(self):
        rev=gate.load_json(self.packet/'review.json'); rev['author_approved']=False; self.write('review.json',rev)
        self.rejects('author approval')
    def test_pending_issue(self):
        rev=gate.load_json(self.packet/'review.json'); rev['unresolved_issues']=['Unresolved']; self.write('review.json',rev)
        self.rejects('Unresolved review')
    def test_uninspected_source(self):
        src,_=self.external(); src['inspection']='abstract-only'; self.write('sources.json',[src]); self.seal()
        self.rejects('not inspected')
    def test_missing_locator(self):
        src,_=self.external(); src['locator']=''; self.write('sources.json',[src]); self.seal()
        self.rejects('missing locator')
    def test_unsupported_claim(self):
        _,claim=self.external(); claim['status']='unsupported'; self.write('claims.json',[claim]); self.seal()
        self.rejects('Unresolved claim')
    def test_unknown_source(self):
        _,claim=self.external(); claim['source_ids']=['S9']; self.write('claims.json',[claim]); self.seal()
        self.rejects('unknown source')
    def test_duplicate_sources(self):
        src,_=self.external(); self.write('sources.json',[src,copy.deepcopy(src)]); self.seal(); self.rejects('duplicate ID')
    def test_missing_prose_citation(self):
        self.external(); self.article.write_text(self.article.read_text().replace('https://example.com/synthetic','https://example.org/unrelated'))
        self.seal(); self.rejects('missing readable citation')
    def test_changed_article(self):
        with self.article.open('a') as f:f.write(' Changed wording.')
        self.rejects('changed since review')
    def test_changed_evidence(self):
        src,_=self.external(); src['appraisal']='Different evidence appraisal'; self.write('sources.json',[src])
        self.rejects('changed since review')
    def test_draft_hash_normalization(self):
        old=gate.digest(self.root,self.slug)
        self.article.write_text(self.article.read_text().replace('draft = false','draft = true'))
        self.assertEqual(old,gate.digest(self.root,self.slug)); self.assertEqual(self.check(),'draft')
    def test_expired_freshness(self):
        self.article.write_text(self.article.read_text().replace('time_sensitive = false','time_sensitive = true'))
        rev=gate.load_json(self.packet/'review.json'); rev['review_by']=(gate.today()-dt.timedelta(days=1)).isoformat()
        self.write('review.json',rev); self.seal(); self.rejects('expired')
    def test_future_review(self):
        rev=gate.load_json(self.packet/'review.json'); rev['reviewed_on']=(gate.today()+dt.timedelta(days=1)).isoformat()
        self.write('review.json',rev); self.rejects('future')
    def test_missing_check(self):
        rev=gate.load_json(self.packet/'review.json'); rev['privacy_checked']=False; self.write('review.json',rev)
        self.rejects('privacy_checked')
    def test_no_overwrite(self):
        before=self.article.read_bytes()
        with self.assertRaises(gate.GateError):gate.new_article(self.root,self.slug,'reflection')
        self.assertEqual(before,self.article.read_bytes())
    def test_traversal_rejected(self):
        with self.assertRaises(gate.GateError):gate.new_article(self.root,'../escape','reflection')
    def test_essay_cannot_have_empty_ledger(self):
        self.article.write_text(self.article.read_text().replace('genre = "reflection"','genre = "essay"'))
        self.seal(); self.rejects('nonempty claim ledger')
    def test_asset_rights(self):
        (self.root/'asset.svg').write_text('<svg/>')
        self.write('assets.json',[dict(id='A1',path='asset.svg',kind='illustration',alt='Synthetic image',rights='unknown',attribution='Synthetic test')])
        self.seal(); self.rejects('Unresolved asset rights')
    def test_asset_escape(self):
        self.write('assets.json',[dict(id='A1',path='../escape.svg')])
        with self.assertRaises(gate.GateError):gate.digest(self.root,self.slug)
    def test_missing_packet(self):
        (self.packet/'brief.md').unlink(); self.rejects('Missing packet')
    def test_missing_draft_flag(self):
        self.article.write_text(self.article.read_text().replace('draft = false\n','')); self.rejects('draft must')

if __name__=='__main__':unittest.main()
