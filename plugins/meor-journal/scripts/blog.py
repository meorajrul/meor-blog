#!/usr/bin/env python3
"""Scaffold and structurally check a Hugo journal. Never approves or publishes."""
import argparse
import datetime as dt
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import tomllib
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urljoin, urlparse

GENRES = ('reflection', 'field-note', 'essay', 'review')
CHECKS = ('claims_complete', 'citations_checked', 'numbers_checked', 'rights_checked',
          'privacy_checked', 'first_person_checked', 'counterevidence_checked')
BASE = 'https://meorajrul.com/'
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')

class GateError(ValueError):
    pass

def today():
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date()

def slug_ok(slug):
    if not isinstance(slug, str) or not SLUG.fullmatch(slug) or len(slug) > 90:
        raise GateError('Use a lowercase slug of letters, numbers and single hyphens (max 90).')
    return slug

def load_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8-sig'))
    except (OSError, ValueError) as exc:
        raise GateError(f'{path.name}: {exc}') from exc

def parse_article(path):
    text = path.read_text(encoding='utf-8-sig').replace('\r\n','\n')
    match = re.match(r'\A\+\+\+\n(.*?)\n\+\+\+(?:\n|$)(.*)', text, re.S)
    if not match:
        raise GateError(f'{path}: expected TOML frontmatter between +++ lines')
    try:
        meta = tomllib.loads(match[1])
    except ValueError as exc:
        raise GateError(f'{path}: {exc}') from exc
    return meta, match[2]

def safe_path(root, value):
    if not isinstance(value, str) or not value or '\\' in value or value.startswith('/') or ':' in value:
        raise GateError('Asset paths must be relative, use forward slashes, and stay within the workspace.')
    result = (root / value).resolve()
    if not result.is_relative_to(root.resolve()):
        raise GateError('Path escapes the workspace.')
    return result

def digest(root, slug):
    slug_ok(slug)
    article = root / 'site/content/posts' / slug / 'index.md'
    packet = root / 'research/articles' / slug
    paths = [article] + [packet / name for name in
       ('brief.md','search-log.csv','sources.json','claims.json','assets.json','review.md')]
    assets = load_json(packet/'assets.json')
    if not isinstance(assets, list):
        raise GateError('assets.json must be an array')
    for asset in assets:
        paths.append(safe_path(root, asset.get('path')))
        for value in asset.get('input_paths', []):
            paths.append(safe_path(root, value))
    hash_obj = hashlib.sha256()
    for path in sorted(set(paths), key=lambda x: x.as_posix()):
        if not path.is_file():
            raise GateError(f'Missing digest input: {path}')
        raw = path.read_bytes().replace(b'\r\n', b'\n')
        if path == article:
            # Only the actual frontmatter draft field is normalized, not body text.
            front, body = raw.split(b'+++', 2)[1:]
            front = re.sub(rb'(?m)^draft\s*=\s*(?:true|false)\s*$', b'draft = false', front)
            raw = b'+++' + front + b'+++' + body
        label = path.relative_to(root).as_posix().encode()
        for part in (label, raw):
            hash_obj.update(str(len(part)).encode()+b':'+part)
    return hash_obj.hexdigest()

def iso_date(value, name):
    try:
        return dt.date.fromisoformat(value)
    except (ValueError, TypeError):
        raise GateError(f'{name} must be an ISO date YYYY-MM-DD')

def require_text(obj, keys, kind):
    for key in keys:
        if not isinstance(obj.get(key), str) or not obj[key].strip():
            raise GateError(f'{kind}: missing {key}')

def indexed(records, kind):
    if not isinstance(records, list):
        raise GateError(f'{kind} must be an array')
    out = {}
    for rec in records:
        if not isinstance(rec, dict):
            raise GateError(f'{kind}: expected objects')
        require_text(rec, ('id',), kind)
        if rec['id'] in out:
            raise GateError(f'{kind}: duplicate ID {rec["id"]}')
        out[rec['id']] = rec
    return out

def validate_article(root, article, as_of=None):
    as_of = as_of or today()
    meta, body = parse_article(article)
    require_text(meta, ('title','description','slug','article_id','genre'), str(article))
    slug = slug_ok(meta['article_id'])
    if meta['genre'] not in GENRES:
        raise GateError('Unknown genre')
    if meta['slug'] != slug or article.resolve() != (root/'site/content/posts'/slug/'index.md').resolve():
        raise GateError('Article ID, slug and page-bundle folder must match')
    if type(meta.get('draft')) is not bool:
        raise GateError('draft must be explicitly true or false')
    if type(meta.get('time_sensitive')) is not bool:
        raise GateError('time_sensitive must be explicitly true or false')
    if not isinstance(meta.get('date'), dt.datetime) or meta['date'].tzinfo is None:
        raise GateError('date must be a timezone-aware TOML datetime')
    packet = root/'research/articles'/slug
    for name in ('brief.md','search-log.csv','sources.json','claims.json','assets.json','review.json','review.md'):
        if not (packet/name).is_file():
            raise GateError(f'Missing packet file: {slug}/{name}')
    # Draft evidence may be incomplete. Publication checks below apply only to release candidates.
    if meta['draft']:
        return 'draft'
    if meta['date'].date() > as_of:
        raise GateError('Published date is in the future')
    if len(body.split()) < 30:
        raise GateError('Article is an empty scaffold')
    if re.search(r'\b(?:TODO|TBD|INSERT HERE)\b|\[AUTHOR INPUT', body):
        raise GateError('Unfinished author input or scaffold in article')
    sources = indexed(load_json(packet/'sources.json'), 'sources')
    claims = indexed(load_json(packet/'claims.json'), 'claims')
    assets = indexed(load_json(packet/'assets.json'), 'assets')
    if meta['genre'] in ('essay','review') and not claims:
        raise GateError('Essay/review requires a nonempty claim ledger')
    external = ('external-fact','inference','calculation')
    for claim in claims.values():
        require_text(claim, ('text','kind','status','confidence'), 'claim')
        if claim['kind'] not in external + ('opinion','personal-experience'):
            raise GateError('Unknown claim kind')
        if claim['status'] not in ('supported','qualified'):
            raise GateError(f'Unresolved claim {claim["id"]}')
        if claim['kind'] not in external:
            continue
        ids = claim.get('source_ids')
        if not isinstance(ids,list) or not ids or not all(isinstance(i,str) for i in ids):
            raise GateError(f'{claim["id"]}: evidence source IDs required')
        require_text(claim, ('locator',), 'claim')
        for sid in ids:
            if sid not in sources:
                raise GateError(f'{claim["id"]}: unknown source {sid}')
            src = sources[sid]
            require_text(src, ('title','url','publisher','locator','origin_group','appraisal'), 'source')
            if src.get('inspection') != 'inspected':
                raise GateError(f'{sid}: cited source was not inspected')
            accessed = iso_date(src.get('accessed'), 'accessed')
            if accessed > as_of:
                raise GateError('Source access date is in the future')
            if urlparse(src['url']).scheme not in ('http','https'):
                raise GateError('Source URL must use HTTP(S)')
            if src['url'] not in body:
                raise GateError(f'{sid}: missing readable citation URL in article')
    if meta['genre'] in ('essay','review') and not any(c['kind'] in external for c in claims.values()):
        raise GateError('Essay/review needs at least one source-based claim')
    for asset in assets.values():
        require_text(asset, ('path','alt','rights','attribution','kind'), 'asset')
        if asset['rights'].lower() in ('unknown','pending','unresolved'):
            raise GateError('Unresolved asset rights')
        if not safe_path(root,asset['path']).is_file():
            raise GateError('Missing asset file')
        if asset['kind'] == 'chart' and not asset.get('input_paths'):
            raise GateError('Chart needs preserved inputs')
        for value in asset.get('input_paths',[]):
            if not safe_path(root,value).is_file():
                raise GateError('Missing asset input')
    rev = load_json(packet/'review.json')
    if not isinstance(rev, dict):
        raise GateError('review.json must be an object')
    if rev.get('status') != 'approved' or rev.get('author_approved') is not True:
        raise GateError('Actual author approval and approved review are required')
    require_text(rev, ('reviewer',), 'review')
    reviewed = iso_date(rev.get('reviewed_on'), 'reviewed_on')
    if reviewed > as_of:
        raise GateError('Review date is in the future')
    if rev.get('unresolved_issues') != []:
        raise GateError('Unresolved review issues')
    for check in CHECKS:
        if rev.get(check) is not True:
            raise GateError(f'Review check pending: {check}')
    if meta['time_sensitive']:
        if iso_date(rev.get('review_by'),'review_by') < as_of:
            raise GateError('Time-sensitive evidence review has expired')
    if rev.get('content_sha256') != digest(root,slug):
        raise GateError('Article or evidence changed since review; record a fresh review and digest')
    return 'public'

def validate_workspace(root):
    posts = root/'site/content/posts'
    counts = {'public':0,'draft':0}
    errors = []
    for article in sorted(posts.rglob('*.md')):
        if article.name == '_index.md':
            continue
        try:
            counts[validate_article(root,article)] += 1
        except (GateError, OSError, TypeError, KeyError, AttributeError) as exc:
            errors.append(f'{article.relative_to(root)}: {exc}')
    if errors:
        raise GateError('\n'.join(errors))
    return counts

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls=[]; self.anchors=[]; self.canonical=[]; self.meta={}; self.titles=[]; self.jsonld=[]
        self.refresh=None; self._title=False; self._json=False; self._buffer=''
    def handle_starttag(self, tag, attrs):
        at=dict(attrs)
        for key in ('href','src'):
            if key in at: self.urls.append(at[key])
        if tag == 'a' and 'href' in at: self.anchors.append(at['href'])
        if tag == 'link' and 'canonical' in at.get('rel','').split():
            self.canonical.append(at.get('href','').strip())
        if tag == 'meta':
            name=at.get('name','').lower()
            if name: self.meta.setdefault(name,[]).append(at.get('content',''))
            if at.get('http-equiv','').lower() == 'refresh':
                self.refresh=at.get('content','')
        if tag == 'title': self._title=True; self.titles.append('')
        if tag == 'script' and at.get('type','').lower() == 'application/ld+json':
            self._json=True; self._buffer=''
    def handle_endtag(self,tag):
        if tag == 'title': self._title=False
        if tag == 'script' and self._json:
            try: self.jsonld.append(json.loads(self._buffer))
            except ValueError as exc: raise GateError('Invalid structured data JSON') from exc
            self._json=False
    def handle_data(self,data):
        if self._title: self.titles[-1]+=data
        if self._json: self._buffer+=data


def schema_nodes(value):
    if isinstance(value,list):
        for item in value: yield from schema_nodes(item)
    elif isinstance(value,dict):
        yield value
        for item in value.values(): yield from schema_nodes(item)


def page_url(rel):
    if rel == 'index.html': return BASE
    return BASE+(rel[:-len('index.html')] if rel.endswith('/index.html') else rel)


def check_output(root, directory):
    out = directory.resolve()
    if not out.is_dir(): raise GateError('Production output does not exist')
    for name in ('index.html','about/index.html','posts/index.html','search/index.html','index.xml','index.json','sitemap.xml','robots.txt','CNAME','.nojekyll'):
        if not (out/name).is_file(): raise GateError(f'Missing production file: {name}')
    if (out/'CNAME').read_text().strip() != urlparse(BASE).hostname:
        raise GateError('Unexpected custom domain')
    bad = ('admin','research','private','plugins','.git','editorial')
    for path in out.rglob('*'):
        rel=path.relative_to(out)
        if any(part in bad for part in rel.parts) or path.suffix in ('.md','.py','.toml'):
            raise GateError(f'Non-public source in production output: {rel}')
    public=set(); drafts=set(); noindex={'search/index.html','404.html'}
    for article in (root/'site/content/posts').rglob('index.md'):
        meta,_=parse_article(article)
        url=BASE+'posts/'+meta['slug']+'/'
        (drafts if meta.get('draft') is True else public).add(url)
    # Explicit noindex is checked against source, rather than trusting generated directives.
    for content in (root/'site/content').rglob('*.md'):
        meta,_=parse_article(content)
        if meta.get('robotsNoIndex') is True:
            rel=content.relative_to(root/'site/content')
            if content.name in ('index.md','_index.md'): rel=rel.parent/'index.html'
            else: rel=rel.with_suffix('')/'index.html'
            noindex.add(rel.as_posix())
    pages={}
    for file in out.rglob('*.html'):
        parser=Links(); parser.feed(file.read_text(encoding='utf-8'))
        pages[file.relative_to(out).as_posix()]=parser
    for taxonomy in ('tags','categories'):
        if not any(rel.startswith(taxonomy+'/') and rel != taxonomy+'/index.html' for rel in pages):
            noindex.add(taxonomy+'/index.html')
    aliases=set(); indexable={}; inbound=set(); titles=set()
    for rel,parser in pages.items():
        expected=page_url(rel)
        if parser.refresh is not None:
            match=re.fullmatch(r'\s*0\s*;\s*url\s*=\s*(.+?)\s*',parser.refresh,re.I)
            if not match or match[1] == expected or not match[1].startswith(BASE):
                raise GateError(f'Invalid redirect alias: {rel}')
            expected=match[1]; aliases.add(rel)
        if rel != '404.html' and parser.canonical != [expected]:
            raise GateError(f'Missing/incorrect exact canonical: {rel}')
        if rel not in aliases:
            if len(parser.titles) != 1 or not parser.titles[0].strip():
                raise GateError(f'Missing/duplicate page title: {rel}')
            if rel != '404.html' and (len(parser.meta.get('description',[])) != 1 or not parser.meta['description'][0].strip()):
                raise GateError(f'Missing/duplicate description: {rel}')
            robots=parser.meta.get('robots',[])
            if len(robots) != 1:
                raise GateError(f'Missing/duplicate robots directive: {rel}')
            directives={v.strip().lower() for v in robots[0].split(',')}
            required='noindex' if rel in noindex else 'index'
            if required not in directives or {'index','noindex'} <= directives or 'none' in directives:
                raise GateError(f'Unexpected indexing directive: {rel}')
            indexable[expected]=required == 'index'
            if required == 'index':
                if parser.titles[0] in titles: raise GateError(f'Duplicate indexable title: {rel}')
                titles.add(parser.titles[0])
            nodes=list(schema_nodes(parser.jsonld))
            for node in nodes:
                for key in ('datePublished','dateModified'):
                    if key in node:
                        try:
                            value=dt.datetime.fromisoformat(node[key].replace('Z','+00:00'))
                            if value.year == 1 or value.tzinfo is None: raise ValueError()
                        except (ValueError,TypeError,AttributeError):
                            raise GateError(f'Invalid structured date: {rel}')
            articles=[n for n in nodes if n.get('@type') == 'BlogPosting']
            if expected not in public and articles:
                raise GateError(f'BlogPosting on a non-article page: {rel}')
            if expected in public:
                if len(articles) != 1 or articles[0].get('url') != expected:
                    raise GateError(f'Missing/incorrect article structured data: {rel}')
                authors=articles[0].get('author',[])
                if isinstance(authors,dict): authors=[authors]
                if not isinstance(authors,list) or not authors or any(not isinstance(a,dict) or not a.get('name') for a in authors):
                    raise GateError(f'Missing article author: {rel}')
                if any(a.get('name') == 'Meor Ajrul' and a.get('url') != BASE+'about/' for a in authors):
                    raise GateError(f'Missing author profile link: {rel}')
            if rel == 'index.html' and not any(n.get('@type') == 'Person' and n.get('url') == BASE+'about/' for n in nodes):
                raise GateError('Missing homepage Person identity')
            if rel == 'about/index.html' and not any(n.get('@type') == 'ProfilePage' for n in nodes):
                raise GateError('Missing About ProfilePage metadata')
        for value in parser.urls:
            url=urlparse(urljoin(page_url(rel),value))
            if url.scheme not in ('http','https') or url.netloc != urlparse(BASE).netloc: continue
            local=unquote(url.path).lstrip('/')
            target=(out/local).resolve()
            if not target.is_relative_to(out): raise GateError('Production link escapes output')
            if not target.is_file() and not (target/'index.html').is_file():
                raise GateError(f'Broken local link in {rel}: {value}')
            destination=url._replace(query='',fragment='').geturl()
            if rel not in aliases and value in parser.anchors and destination != page_url(rel): inbound.add(destination)
    try:
        xml=ET.fromstring((out/'sitemap.xml').read_text(encoding='utf-8'))
    except ET.ParseError as exc: raise GateError('Invalid sitemap XML') from exc
    namespace='{http://www.sitemaps.org/schemas/sitemap/0.9}'
    if xml.tag != namespace+'urlset': raise GateError('Expected sitemap urlset')
    sitemap=[]
    for entry in xml.findall(namespace+'url'):
        value=entry.findtext(namespace+'loc','').strip()
        if value in sitemap or not indexable.get(value):
            raise GateError(f'Sitemap URL is duplicate, missing, redirected or noindex: {value}')
        sitemap.append(value)
    if not ({BASE,BASE+'about/',BASE+'posts/'} | public).issubset(sitemap):
        raise GateError('Sitemap missing an intended public page')
    for url in public:
        if url not in indexable or not indexable[url]: raise GateError(f'Public article missing or noindex: {url}')
        if url not in inbound: raise GateError(f'Public article has no inbound page link: {url}')
    for path in out.rglob('*'):
        if path.is_file() and path.suffix in ('.html','.xml','.json'):
            text=path.read_text(encoding='utf-8').replace('\\/','/')
            if any(url in text or urlparse(url).path in text for url in drafts):
                raise GateError(f'Draft leaked into production output: {path.relative_to(out)}')
    robots=(out/'robots.txt').read_text(encoding='utf-8')
    if re.search(r'^Disallow:\s*/\s*$',robots,re.M|re.I): raise GateError('Production robots blocks all crawling')
    if BASE+'sitemap.xml' not in robots: raise GateError('Robots is missing the canonical sitemap')
    return {'html_pages':len(pages),'sitemap_urls':len(sitemap),'internal_links':'passed',
            'source_boundary':'passed','draft_exclusion':'passed','seo_metadata':'passed',
            'sitemap_consistency':'passed','article_discovery':'passed'}


def new_article(root, slug, genre):
    slug_ok(slug)
    article=root/'site/content/posts'/slug/'index.md'
    packet=root/'research/articles'/slug
    if article.parent.exists() or packet.exists():
        raise GateError('Article or packet already exists; no files were overwritten')
    assets=Path(__file__).resolve().parent.parent/'assets'
    # Validate templates before creating either destination.
    names=['article.md','brief.md','search-log.csv','sources.json','claims.json','assets.json','review.json','review.md']
    templates={n:(assets/n).read_text(encoding='utf-8') for n in names}
    article.parent.mkdir(parents=True); packet.mkdir(parents=True)
    for name,text in templates.items():
        text=text.replace('{{SLUG}}',slug).replace('{{GENRE}}',genre).replace('{{DATE}}',today().isoformat())
        (article if name=='article.md' else packet/name).write_text(text,encoding='utf-8')
    return str(article)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path.cwd(),help='Journal workspace root')
    sub=ap.add_subparsers(dest='command',required=True)
    new=sub.add_parser('new',help='Create a draft and packet without overwriting')
    new.add_argument('slug'); new.add_argument('--genre',choices=GENRES,default='reflection')
    sub.add_parser('check',help='Validate draft structure and public-post release records')
    ha=sub.add_parser('hash',help='Print final article/evidence digest; never records approval')
    ha.add_argument('slug')
    out=sub.add_parser('check-output',help='Check production output and internal links')
    out.add_argument('--directory',type=Path,default=Path('site/public'))
    args=ap.parse_args(); root=args.root.resolve()
    try:
        if args.command=='new': result=new_article(root,args.slug,args.genre)
        elif args.command=='check': result=validate_workspace(root)
        elif args.command=='hash': result=digest(root,args.slug)
        else: result=check_output(root,root/args.directory)
        print(json.dumps(result,indent=2))
        return 0
    except (GateError,OSError,ValueError) as exc:
        print(f'CHECK FAILED: {exc}',file=sys.stderr); return 1

if __name__=='__main__':
    sys.exit(main())
