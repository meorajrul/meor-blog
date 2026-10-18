"""Synthetic output fixtures: no actual article approval, publication or source evidence."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('seo_gate',Path(__file__).resolve().parents[1]/'scripts/blog.py')
gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)

class OutputSEO(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.out=self.root/'site/public';self.out.mkdir(parents=True)
        self.write('index.html',self.page('',schema={'@type':'Person','url':gate.BASE+'about/'}))
        self.write('about/index.html',self.page('about/',schema={'@type':'ProfilePage'}))
        self.write('posts/index.html',self.page('posts/'))
        self.write('search/index.html',self.page('search/',robots='noindex, follow'))
        self.write('tags/index.html',self.page('tags/',robots='noindex, follow'))
        self.write('categories/index.html',self.page('categories/',robots='noindex, follow'))
        self.write('404.html',self.page('404.html',robots='noindex, follow'))
        for name in ('index.xml','index.json','.nojekyll'):self.write(name,'')
        self.write('robots.txt','User-agent: *\nDisallow:\nSitemap: '+gate.BASE+'sitemap.xml\n')
        self.write('CNAME','meorajrul.com\n');self.sitemap(['','about/','posts/'])
    def write(self,rel,text):
        path=self.out/rel;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')
    def page(self,path,robots='index, follow',schema=None):
        ld='<script type="application/ld+json">'+json.dumps(schema)+'</script>' if schema else ''
        return (f'<title>Synthetic {path or "home"}</title><meta name="description" content="Synthetic fixture">'
                f'<meta name="robots" content="{robots}"><link rel="canonical" href="{gate.BASE+path}">'+ld)
    def sitemap(self,paths):
        self.write('sitemap.xml','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+gate.BASE+p+'</loc></url>' for p in paths)+'</urlset>')
    def check(self):return gate.check_output(self.root,self.out)
    def rejects(self,word):
        with self.assertRaisesRegex(gate.GateError,word):self.check()
    def change(self,rel,old,new):self.write(rel,(self.out/rel).read_text(encoding='utf-8').replace(old,new))
    def post(self,draft=False):
        gate.new_article(self.root,'synthetic','reflection')
        article=self.root/'site/content/posts/synthetic/index.md'
        if draft:return
        article.write_text(article.read_text(encoding='utf-8').replace('draft = true','draft = false'),encoding='utf-8')
        url=gate.BASE+'posts/synthetic/'
        schema={'@type':'BlogPosting','url':url,'author':[{'@type':'Person','name':'Meor Ajrul','url':gate.BASE+'about/'}]}
        self.write('posts/synthetic/index.html',self.page('posts/synthetic/',schema=schema))
        with (self.out/'posts/index.html').open('a',encoding='utf-8') as f:f.write('<a href="'+url+'">Synthetic article</a>')
        self.sitemap(['','about/','posts/','posts/synthetic/'])
    def test_valid_artifact(self):self.assertEqual(self.check()['sitemap_urls'],3)
    def test_wrong_same_host_canonical(self):
        self.change('about/index.html','rel="canonical" href="'+gate.BASE+'about/','rel="canonical" href="'+gate.BASE+'posts/');self.rejects('exact canonical')
    def test_duplicate_canonical(self):
        with (self.out/'about/index.html').open('a') as f:f.write('<link rel="canonical" href="'+gate.BASE+'about/">')
        self.rejects('exact canonical')
    def test_production_home_noindex(self):self.change('index.html','index, follow','noindex, follow');self.rejects('indexing directive')
    def test_search_indexed(self):self.change('search/index.html','noindex, follow','index, follow');self.rejects('indexing directive')
    def test_empty_taxonomy_indexed(self):self.change('tags/index.html','noindex, follow','index, follow');self.rejects('indexing directive')
    def test_duplicate_robots(self):
        with (self.out/'search/index.html').open('a') as f:f.write('<meta name="robots" content="noindex">')
        self.rejects('robots directive')
    def test_missing_description(self):self.change('about/index.html','name="description"','name="unrelated"');self.rejects('description')
    def test_missing_title(self):self.change('about/index.html','Synthetic about/','');self.rejects('page title')
    def test_sitemap_noindex(self):self.sitemap(['','about/','posts/','search/']);self.rejects('noindex')
    def test_sitemap_duplicate(self):self.sitemap(['','about/','posts/','posts/']);self.rejects('duplicate')
    def test_sitemap_missing_main_page(self):self.sitemap(['','about/']);self.rejects('Sitemap missing')
    def test_sitemap_missing_target(self):self.sitemap(['','about/','posts/','missing/']);self.rejects('missing')
    def test_sitemap_invalid_xml(self):self.write('sitemap.xml','broken');self.rejects('sitemap XML')
    def test_invalid_schema_json(self):self.change('index.html','"@type": "Person"','broken');self.rejects('structured data JSON')
    def test_home_person_required(self):self.change('index.html','"Person"','"Organization"');self.rejects('Person identity')
    def test_about_profile_required(self):self.change('about/index.html','"ProfilePage"','"WebPage"');self.rejects('ProfilePage')
    def test_utility_blogposting(self):self.write('search/index.html',self.page('search/',robots='noindex, follow',schema={'@type':'BlogPosting'}));self.rejects('non-article')
    def test_unset_schema_date(self):self.write('about/index.html',self.page('about/',schema={'@type':'ProfilePage','dateModified':'0001-01-01T00:00:00Z'}));self.rejects('structured date')
    def test_valid_public_article(self):self.post();self.assertEqual(self.check()['article_discovery'],'passed')
    def test_orphan_article(self):self.post();self.write('posts/index.html',self.page('posts/'));self.rejects('inbound')
    def test_image_is_not_an_inbound_navigation_link(self):
        self.post();self.write('posts/index.html',self.page('posts/')+'<img src="'+gate.BASE+'posts/synthetic/">')
        self.rejects('inbound')
    def test_article_schema_required(self):self.post();self.write('posts/synthetic/index.html',self.page('posts/synthetic/'));self.rejects('article structured data')
    def test_author_profile_required(self):self.post();self.change('posts/synthetic/index.html','"url": "'+gate.BASE+'about/"','"url": "https://example.com/"');self.rejects('profile link')
    def test_drafts_not_in_discovery_outputs(self):
        self.post(draft=True)
        for name,text in [('index.xml','<rss>'+gate.BASE+'posts/synthetic/</rss>'),('index.json',json.dumps([{'permalink':gate.BASE+'posts/synthetic/'}])),('search/index.html',self.page('search/',robots='noindex, follow')+'<script>const url="/posts/synthetic/";</script>')]:
            with self.subTest(name=name):
                old=(self.out/name).read_text(encoding='utf-8');self.write(name,text);self.rejects('Draft leaked');self.write(name,old)
    def test_alias_allowed_but_not_in_sitemap(self):
        self.write('page/1/index.html','<meta http-equiv="refresh" content="0; url='+gate.BASE+'"><link rel="canonical" href="'+gate.BASE+'">')
        self.check();self.sitemap(['','about/','posts/','page/1/']);self.rejects('redirected')
    def test_broken_internal_link(self):
        with (self.out/'index.html').open('a') as f:f.write('<a href="/missing/">Missing</a>')
        self.rejects('Broken local link')
    def test_source_boundary(self):self.write('research/private.md','not public');self.rejects('Non-public source')
    def test_global_robots_block(self):self.change('robots.txt','Disallow:','Disallow: /');self.rejects('blocks all')

if __name__=='__main__':unittest.main()
