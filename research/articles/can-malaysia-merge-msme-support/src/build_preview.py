"""Make an offline review copy from Hugo's actual rendered article content.

Input: .cache/msme-essay-preview-build/posts/<slug>/index.html.
No browser action, publication or deployment is performed.
"""
from pathlib import Path
from html.parser import HTMLParser
from html import escape
from urllib.parse import urlparse
import os
import tomllib

ROOT=Path(__file__).resolve().parents[4]
PACKET=Path(__file__).resolve().parents[1]
SLUG='can-malaysia-merge-msme-support'
BUNDLE=ROOT/'site/content/posts'/SLUG
OUT=PACKET/'to_human'
OUT.mkdir(exist_ok=True)
asset_root=os.path.relpath(BUNDLE,OUT).replace('\\','/')
article=(BUNDLE/'index.md').read_text(encoding='utf-8')
meta=tomllib.loads(article.split('+++',2)[1])

def local_url(value):
    parsed=urlparse(value)
    if parsed.scheme in ('http','https') and parsed.netloc != 'meorajrul.com':
        return value
    prefix=f'/posts/{SLUG}/'
    if parsed.path.startswith(prefix):
        return asset_root+'/'+parsed.path[len(prefix):]
    if not parsed.scheme and not value.startswith(('/','#')):
        return asset_root+'/'+value
    return value

class ExtractContent(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.depth=0
        self.parts=[]
        self.done=False
    def handle_starttag(self,tag,attrs):
        values=dict(attrs)
        if not self.depth and not self.done and tag=='div' and 'post-content' in values.get('class','').split():
            self.depth=1
            return
        if not self.depth:
            return
        if tag=='div':
            self.depth+=1
        cleaned=[]
        for name,value in attrs:
            if name in ('src','href') and value:
                value=local_url(value)
            if name=='srcset':
                continue
            cleaned.append(' '+name if value is None else f' {name}="{escape(value,quote=True)}"')
        self.parts.append('<'+tag+''.join(cleaned)+'>')
    def handle_endtag(self,tag):
        if not self.depth:
            return
        if tag=='div':
            self.depth-=1
            if not self.depth:
                self.done=True
                return
        self.parts.append(f'</{tag}>')
    def handle_data(self,data):
        if self.depth:self.parts.append(data)
    def handle_entityref(self,name):
        if self.depth:self.parts.append('&'+name+';')
    def handle_charref(self,name):
        if self.depth:self.parts.append('&#'+name+';')

source=ROOT/'.cache/msme-essay-preview-build/posts'/SLUG/'index.html'
parser=ExtractContent();parser.feed(source.read_text(encoding='utf-8'))
assert parser.done and len(''.join(parser.parts))>5000
style='''
:root{color-scheme:light;--ink:#253839;--paper:#fbfaf6;--muted:#596967;--accent:#9f4f2b}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:19px/1.8 Georgia,serif}
main{max-width:920px;margin:auto;padding:36px 28px 90px}.draft{font:600 12px/1.5 system-ui;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);border-bottom:1px solid #d8d6cc;padding-bottom:14px}
h1{font-size:clamp(34px,5vw,53px);line-height:1.12;letter-spacing:-.025em;margin:32px 0 20px}.deck{font:19px/1.55 system-ui;color:var(--muted)}
.cover{margin:30px -34px 42px}.cover img{display:block;width:100%;height:auto;border-radius:4px}.cover figcaption{font:13px/1.5 system-ui;color:var(--muted);padding:10px 34px}
.post-content>p{margin:0 0 24px}.post-content img{display:block;max-width:100%;height:auto;margin:36px auto 12px}.post-content p:has(>em:only-child){font:14px/1.6 system-ui;color:var(--muted);margin-top:10px;margin-bottom:34px}
a{color:#2c6573;text-underline-offset:3px;overflow-wrap:anywhere}strong{font-weight:700}table{display:table;width:100%;border-collapse:collapse;font:14px/1.6 system-ui;margin:30px 0 12px}th,td{text-align:left;vertical-align:top;padding:12px 10px;border-bottom:1px solid #d8d6cc}th{background:#eaf0ed}
footer{font:14px/1.6 system-ui;border-top:1px solid #d8d6cc;margin-top:44px;padding-top:20px;color:var(--muted)}
@media(max-width:600px){body{font-size:18px}main{padding:22px 19px 60px}.cover{margin:25px -19px 32px}.cover figcaption{padding:10px 19px}table{display:block;overflow-x:auto;font-size:12px}th,td{min-width:130px}}
'''
content=''.join(parser.parts)
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{escape(meta['title'])} — working draft</title><style>{style}</style></head><body><main><div class="draft">Approved release planned · 20 October 2026, 09:00 MYT · Final deployment owner-managed</div><h1>{escape(meta['title'])}</h1><p class="deck">{escape(meta['description'])}</p><figure class="cover"><img src="{asset_root}/hero.png" alt="{escape(meta['cover']['alt'],quote=True)}"><figcaption>{escape(meta['cover']['caption'])}</figcaption></figure><div class="post-content">{content}</div><footer>Research checked against the selected source register. Reported programme results, analyst judgments and illustrative savings remain distinct. <a href="../review.md">Editorial review and limits</a> · <a href="../hero-prompt.md">Hero prompt and provenance</a> · <a href="{asset_root}/index.md">Editable essay source</a></footer></main></body></html>'''
(OUT/'essay-preview.html').write_text(html,encoding='utf-8')
print(f'Built offline review copy: {(OUT/"essay-preview.html").relative_to(ROOT)}')
