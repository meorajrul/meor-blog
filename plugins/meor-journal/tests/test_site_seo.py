"""Render synthetic articles in a disposable site copy; never changes or publishes journal drafts."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[3]
LOCAL=ROOT/'.tools/hugo/hugo.exe'
HUGO=os.environ.get('JOURNAL_HUGO') or (str(LOCAL) if LOCAL.is_file() else shutil.which('hugo'))
spec=importlib.util.spec_from_file_location('site_gate',ROOT/'plugins/meor-journal/scripts/blog.py')
gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)

@unittest.skipUnless(HUGO,'Pinned Hugo must be installed to run render integration checks')
class SiteSEO(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        shutil.copytree(ROOT/'site',self.root/'site',ignore=shutil.ignore_patterns('public','resources','.hugo_build.lock'))
    def build(self,environment='production'):
        result=subprocess.run([HUGO,'--source',str(self.root/'site'),'--environment',environment,'--minify','--cleanDestinationDir'],capture_output=True,text=True,encoding='utf-8')
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        return self.root/'site/public'
    def page(self,out,rel):
        parser=gate.Links();parser.feed((out/rel).read_text(encoding='utf-8'));return parser
    def test_production_site(self):
        out=self.build();result=gate.check_output(self.root,out)
        self.assertEqual(result['sitemap_urls'],3)
        self.assertEqual(self.page(out,'index.html').titles,['Meor Ajrul — A Personal Journal'])
        self.assertEqual(self.page(out,'search/index.html').meta['robots'],['noindex, follow'])
        self.assertFalse((out/'posts/what-makes-a-source-worth-trusting/index.html').exists())
    def test_development_is_noindex(self):
        out=self.build('development')
        for rel in ('index.html','about/index.html','search/index.html','tags/index.html'):
            self.assertEqual(self.page(out,rel).meta['robots'],['noindex, nofollow'])
        with self.assertRaisesRegex(gate.GateError,'indexing directive'):gate.check_output(self.root,out)
    def test_real_post_render_pagination_taxonomy_and_escaping(self):
        for n in range(10):
            title='Synthetic "quotes" </script> & story '+str(n)
            path=self.root/f'site/content/posts/synthetic-{n}/index.md';path.parent.mkdir(parents=True)
            path.write_text('+++\ntitle = '+json.dumps(title)+'\ndescription = "Synthetic render fixture"\nslug = "synthetic-'+str(n)+'"\ndate = 2020-01-01T00:00:00+08:00\ndraft = false\nauthor = "Meor Ajrul"\ntags = ["synthetic"]\n+++\n\nSynthetic disposable render fixture. No actual author approval or publication.\n',encoding='utf-8')
        out=self.build();gate.check_output(self.root,out)
        for rel in ('page/2/index.html','posts/page/2/index.html','tags/synthetic/page/2/index.html'):
            page=self.page(out,rel)
            self.assertEqual(page.canonical,[gate.page_url(rel)])
            self.assertIn('Page 2',page.titles[0])
        for rel in ('tags/index.html','tags/synthetic/index.html'):
            self.assertEqual(self.page(out,rel).meta['robots'],['index, follow'])
        article=self.page(out,'posts/synthetic-0/index.html')
        nodes=list(gate.schema_nodes(article.jsonld))
        post=next(x for x in nodes if x.get('@type')=='BlogPosting')
        self.assertEqual(post['headline'],'Synthetic "quotes" & story 0')
        self.assertEqual(post['author'][0]['url'],gate.BASE+'about/')
        self.assertIn(gate.BASE+'about/',article.urls)
        self.assertNotIn('0001-01-01',json.dumps(article.jsonld))

if __name__=='__main__':unittest.main()
