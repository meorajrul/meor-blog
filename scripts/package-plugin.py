"""Validate the plugin and create a reproducible source ZIP and SHA256 file."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

root = Path(__file__).resolve().parents[1]
plugin = root/'plugins/meor-journal'
manifest = json.loads((plugin/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
assert manifest['name'] == 'meor-journal'
assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
assert manifest['skills'] == './skills/'
market = json.loads((root/'.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
entry = next(e for e in market['plugins'] if e['name'] == manifest['name'])
assert (root/entry['source']['path']).resolve() == plugin.resolve()
skills = sorted((plugin/'skills').glob('*/SKILL.md'))
assert len(skills) == 7
for skill in skills:
    text = skill.read_text(encoding='utf-8')
    fm = re.match(r'\A---\n(.*?)\n---\n',text,re.S)
    assert fm, f'Missing frontmatter: {skill}'
    assert re.search(r'^name: '+re.escape(skill.parent.name)+r'$',fm[1],re.M)
    assert re.search(r'^description: .+',fm[1],re.M)
for file in plugin.rglob('*.md'):
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
        if re.match(r'[a-z]+:',link) or link.startswith('#'):
            continue
        target=(file.parent/link.split('#')[0]).resolve()
        assert target.is_relative_to(plugin.resolve()), f'Nonportable plugin link: {file}: {link}'
        assert target.exists(), f'Missing plugin reference: {file}: {link}'
out=root/'plugins/packages'; out.mkdir(parents=True,exist_ok=True)
archive=out/f'meor-journal-{manifest["version"]}.zip'
files=[f for f in plugin.rglob('*') if f.is_file() and not any(part in ('.git','__pycache__') for part in f.parts) and f.suffix != '.pyc']
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for file in sorted(files):
        info=zipfile.ZipInfo('meor-journal/'+file.relative_to(plugin).as_posix(),date_time=(2026,10,18,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o100644 << 16
        z.writestr(info,file.read_bytes())
sha=hashlib.sha256(archive.read_bytes()).hexdigest()
archive.with_suffix('.zip.sha256').write_text(f'{sha}  {archive.name}\n',encoding='utf-8')
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files)
print(json.dumps({'plugin':manifest['name'],'version':manifest['version'],'skills':len(skills),'source_files':len(files),'archive':str(archive),'sha256':sha},indent=2))
