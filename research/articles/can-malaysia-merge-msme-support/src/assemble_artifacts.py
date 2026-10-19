"""Assemble asset provenance and accessible model notes; never approve or publish."""
from pathlib import Path
import csv
import json
import shutil

ROOT=Path(__file__).resolve().parents[4]
PACKET=Path(__file__).resolve().parents[1]
BUNDLE=ROOT/'site/content/posts/can-malaysia-merge-msme-support'
UPSTREAM=ROOT/'research/articles/ai-native-malaysia-government/msme'

def relative(path):
    return path.relative_to(ROOT).as_posix()

(BUNDLE/'model-notes.txt').write_text((PACKET/'model-notes.md').read_text(encoding='utf-8'),encoding='utf-8')
assets=[dict(id='A01',path=relative(BUNDLE/'hero.png'),
             alt='Conceptual Malaysian civic courtyard: one gateway connects several specialist service pavilions.',
             rights='AI-generated conceptual illustration created for this draft. No third-party source image or real person supplied.',
             attribution='Created with the built-in OpenAI image-generation tool on 19 October 2026.',
             source_url='',kind='illustration',input_paths=[relative(PACKET/'hero-prompt.md')])]
figures={
    'programme-performance':('Eleven reported 2024 IAFSP scores; eight at or above 70, three below; not whole-agency KPI attainment.',
        ['data/programme-performance.csv','data/agencies.json'],
        'SME Corp, SMEIPA 2025 (D03), framework and agency profiles.'),
    'savings-scenarios':('Illustrative three-year cumulative net savings: low -RM9.16m, central -RM3.44m, high +RM3.18m. These are planning cases.',
        ['data/savings-model.json','data/savings-assumptions.csv','data/savings-scenarios.csv','model-notes.md'],
        'Proposed 2027 KUSKOP estimates (D01) and explicit analyst assumptions.'),
    'agency-quadrant':('Categorical matrix separates analyst institutional judgments from reported programme scores; three transfer-review candidates all meet the threshold.',
        ['data/agency-quadrant.csv','data/agencies.json'],
        'SMEIPA 2025 programme scores and the documented mandate review; classifications are analyst judgments.')
}
for name,(alt,inputs,attribution) in figures.items():
    for ext in ['png','pdf']:
        assets.append(dict(id=f'A{len(assets)+1:02}',path=relative(BUNDLE/f'{name}.{ext}'),alt=alt,
                           rights='Original figure rendering from attributed facts and explicit analyst assumptions; no source graphic reproduced.',
                           attribution=attribution,source_url='',kind='chart',
                           input_paths=[relative(PACKET/value) for value in inputs]+[
                               relative(PACKET/'src/build_charts.py'),relative(PACKET/'sources.json')]))
for asset in assets:
    assert (ROOT/asset['path']).is_file()
    for value in asset['input_paths']:
        assert (ROOT/value).is_file()
(PACKET/'assets.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Preserve actual earlier discovery queries and distinguish their provenance.
logs=[]
for label,path in [('Domestic',UPSTREAM/'search-log.csv'),('Regional',UPSTREAM/'regional/search-log.csv')]:
    shutil.copy2(path,PACKET/'data'/f'upstream-{label.lower()}-search-log.csv')
    with path.open(encoding='utf-8-sig',newline='') as handle:
        for row in csv.DictReader(handle):
            row['source_ids']=''
            row['selection_decision']=f"{label} research carried forward; {row['selection_decision']}"
            logs.append(row)
with (PACKET/'search-log.csv').open('w',encoding='utf-8',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=['date','platform','query','filters','source_ids','selection_decision'])
    writer.writeheader(); writer.writerows(logs)
print(f'Assembled {len(assets)} asset records, model text, and {len(logs)} carried-forward actual search entries.')
