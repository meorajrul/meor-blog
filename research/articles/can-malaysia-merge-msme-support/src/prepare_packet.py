"""Preserve the selected outline's evidence and chart inputs, without publication."""
from pathlib import Path
import csv
import json
import shutil

ROOT = Path(__file__).resolve().parents[4]
PACKET = Path(__file__).resolve().parents[1]
UPSTREAM = ROOT / 'research/articles/ai-native-malaysia-government/msme'
BUNDLE = ROOT / 'site/content/posts/can-malaysia-merge-msme-support'
DATA = PACKET / 'data'
DATA.mkdir(exist_ok=True)

def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def write_csv(path, rows):
    with path.open('w', encoding='utf-8', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

regional = read_json(UPSTREAM / 'regional/sources.json')
domestic = read_json(UPSTREAM / 'sources.json')
ids = {'K01','R01','S01','S03','S04','S06','T02','T03','I02','I03',
       'D01','D03','D05','D06','D08','D12','D13','D14','D15','D16'}
all_sources = {s['id']:s for s in domestic + regional}
sources = [all_sources[i] for i in sorted(ids)]
assert all(s['inspection'] == 'inspected' for s in sources)
for source in sources:
    source['provenance'] = 'Carried forward from inspected KRI-first, MSME and regional packets; no new inspection claimed by this preparation script.'
    if source['id'] == 'K01':
        source['publication_url'] = source['url']
        source['url'] = source['original_pdf_url']
write_json(PACKET / 'sources.json', sources)

claims = []
def claim(cid, text, kind, source_ids, locator, limitations, confidence='High within stated scope'):
    claims.append(dict(id=cid, text=text, kind=kind, source_ids=source_ids,
                       locator=locator, status='qualified', confidence=confidence,
                       limitations=limitations))

claim('C01','KRI identifies coordination and capacity concerns in Malaysian AI governance.',
      'external-fact',['K01'],'Executive summary vii–viii; printed pp.39–48',
      'Qualitative governance study; no endorsement of this essay’s agency closures or fiscal model.')
claim('C02','ASEAN SME Policy Index 2024 describes an advanced Malaysian institutional framework and recommends better Thai coordination and data sharing.',
      'external-fact',['R01'],'Printed pp.337 and 429',
      'Policy-framework assessment, not an outcome ranking or a current ministry census.')
claim('C03','IE Singapore and SPRING merged into Enterprise Singapore on 1 April 2018; related capability and internationalisation grants became EDG.',
      'external-fact',['S01','S03'],'Directory description; evaluation introduction p.42',
      'Completed organisational and programme changes do not isolate merger benefits.')
claim('C04','For EDG recipients in 2019–2022, a typical grant was associated with annual revenue 1.9% higher and value added 1.6% higher.',
      'external-fact',['S03'],'Printed pp.42–45, especially p.44',
      'Observational firm/year fixed-effects analysis controlling other grants; remaining time-varying selection possible. Not an agency-merger evaluation.')
claim('C05','EnterpriseSG’s S$118m expected annual cost reductions for 2025-supported businesses are recipient benefits.',
      'external-fact',['S04'],'Release pp.1–2',
      'Expected company benefits; not audited public expenditure savings.')
claim('C06','EnterpriseSG financial highlights report S$326.5m FY2024 operating expense for the year ended March 2025.',
      'external-fact',['S06'],'Printed pp.25–26',
      'Agency financial highlights, not total MSME support or an unmerged counterfactual. No audit opinion inferred.')
claim('C07','Thailand’s BDS uses SME ONE ID, proposals and support agreements; its December 2025 release reports over 1,000 services and THB300m funding for fiscal 2026.',
      'external-fact',['T02','T03'],'Results release; SME application steps',
      'Agency-reported operating integration; funding is not a saving; no causal merger return established.')
claim('C08','Indonesia’s UMi holding retains BRI, PNM and Pegadaian specialisms; BRI reported 1,035 shared SenyuM outlets in September 2025 and describes a differentiated customer journey.',
      'external-fact',['I02','I03'],'Holding/outlet and customer-journey paragraphs',
      'Bank self-report and operating stocks; additional inclusion and net government savings not isolated.')
claim('C09','SME Bank joined the BPMB group in May 2025.',
      'external-fact',['D06'],'Opening overview and leadership discussion',
      'Existing integration must not be counted again as a new saving. No net integration saving established here.')
claim('C10','The preserved data reproduce eleven 2024 IAFSP scores: eight at or above 70; BSN 41.8, CGC 66.7 and RISDA 67.4 below; no comparable SKM/TERAJU score established here.',
      'external-fact',['D03'],'Printed p.12 framework; agency profiles pp.28–32,48,56,66–67; data/agencies.json',
      'Reported MSME programme framework, not whole-agency KPI attainment, percentage of targets achieved or causal impact. Unknowns are not zero.')
claim('C11','KUSKOP’s 2025 internal audit identifies inconsistent payment processes and beneficiary records in cross-agency halal support.',
      'external-fact',['D05'],'Printed pp.26–35',
      'Different grants can fund complementary activities; repeated beneficiaries alone do not prove duplication or recoverable savings.')
claim('C12','INSKEN supplies training/coaching; PERNAS has franchise and commercial functions; PUNB offers Bumiputera business financing.',
      'external-fact',['D12','D13','D14'],'Current service descriptions',
      'Mandates do not establish legal transferability, full costs or net closure savings.')
claim('C13','MARA’s budget covers education, RISDA has wider statutory smallholder functions and BSN states a financial-inclusion mission.',
      'external-fact',['D08','D16','D15'],'MARA budget programmes; official profiles',
      'Wider mandates do not prove every programme effective; measured MSME scores cannot justify whole-entity closure alone.')
claim('C14','Proposed 2027 budget anchors are SME Corp operating grant RM42.7564m, INSKEN RM12.0009m and ministry management supplies/services RM29.836m.',
      'external-fact',['D01'],'B.26, selected grant lines and P1 management supplies/services',
      'Proposed estimates, not actual expenditure or verified duplicated overhead. Management services aggregate not added to its own subcomponents.')
claim('C15','Conditional central model: mature gross RM2.779063875m minus recurring RM1.5m yields RM1.279063875m annual net; RM4.5m transition and staged rollout yield -RM3.44187225m cumulatively over three years.',
      'calculation',['D01'],'data/savings-model.json; data/savings-assumptions.csv; src/build_charts.py',
      'Shares, retirement fractions and new costs are analyst assumptions. Nominal MYR, no discounting or forecast probability; no observed AI savings.',
      'Arithmetic verified; forecast confidence not established')
claim('C16','Illustrative three-year balances are low -RM9.160516m, central -RM3.44187225m, high +RM3.182709m.',
      'calculation',['D01'],'Same model and annual/cumulative CSV; formula recomputed in chart builder',
      'Planning cases, not confidence intervals. Savings require actual cost retirement.',
      'Arithmetic verified; forecast confidence not established')
claim('C17','Function transfer, a shared business case, generic procurement and conditional INSKEN/PERNAS/PUNB administration reviews are the essay’s policy proposals.',
      'inference',['K01','S01','T02','T03','I02','I03','D05','D12','D13','D14'],
      'Draft proposal paragraphs; upstream domestic and regional synthesis',
      'No implementation, agency endorsement, priced transfer or legal/workforce assessment claimed.',
      'Conditional policy judgment')
claim('C18','The quadrant separates analyst institutional-distinctiveness categories from reported programme scores; all three transfer-review candidates meet the threshold.',
      'inference',['D03','D08','D12','D13','D14','D15','D16'],
      'data/agencies.json and agency-quadrant.csv; upstream agency rationales',
      'Not an official relevance score, a validated metric or an automatic closure rule. SKM/TERAJU unplaced. CGC is public-linked.',
      'Programme scores sourced; institutional classifications are contestable judgments')
claim('C19','None of the selected inspected case records establishes a reconciled net government saving attributable to the restructuring.',
      'inference',['S03','S04','S06','T02','I02','I03','D06'],
      'Upstream regional money ledger and source appraisals',
      'Bounded desk review, not proof that savings are zero or that no further evidence exists. Full BRI 2025 accounts inaccessible.',
      'Bounded by selected records and documented access limits')
claim('C20','AI document checks, sourced rule explanations, summaries and inconsistency flags are proposed tasks with human review and appeals.',
      'opinion',['K01','D05'],'Draft AI paragraph',
      'Proposed design, not demonstrated efficacy, deployment or fiscal benefit.',
      'Explicit proposal')
write_json(PACKET / 'claims.json', claims)

agencies = read_json(UPSTREAM / 'data/agencies.json')
write_json(DATA / 'agencies.json', agencies)
write_json(DATA / 'savings-model.json', read_json(UPSTREAM / 'data/savings-model.json'))
for name in ['savings-assumptions.csv']:
    shutil.copy2(UPSTREAM / 'data' / name, DATA / name)
    shutil.copy2(DATA / name, BUNDLE / name)

performance = []
quadrant = []
for a in agencies:
    score = a['performance_score']
    assessment = 'not established' if score is None else ('meets or exceeds' if score >= 70 else 'below threshold')
    performance.append(dict(agency=a['name'], score='' if score is None else score,
                            year='' if score is None else 2024, threshold=70,
                            assessment=assessment, source='D03 / SMEIPA 2025',
                            scope='Reported MSME programme performance, not whole-organisation KPI attainment.'))
    quadrant.append(dict(agency=a['name'], programme_score='' if score is None else score,
                         programme_assessment=assessment,
                         institutional_assessment=('unplaced' if score is None else ('review standalone administration' if a['institution_case']=='transfer' else 'stronger case to retain distinct institution')),
                         analyst_rationale=a['rationale'],
                         status='Institutional judgment is analyst interpretation; score is reported 2024 programme evidence.'))
write_csv(DATA / 'programme-performance.csv', performance)
write_csv(DATA / 'agency-quadrant.csv', quadrant)
for name in ['programme-performance.csv','agency-quadrant.csv']:
    shutil.copy2(DATA / name, BUNDLE / name)

write_json(DATA / 'provenance.json', {
    'prepared':'2026-10-19',
    'selection':'User selected outline 1 from upstream regional essay-outlines.md.',
    'upstream_packet':str(UPSTREAM.relative_to(ROOT)).replace('\\','/'),
    'upstream_sources_preserved':True,
    'scope':'Selected inspected evidence carried forward. No new search or inspection is implied.',
    'unknowns':'No comparable score for SKM/TERAJU; no established reconciled net fiscal merger saving in selected regional records.',
    'partial_records_excluded':['S02','T01','I01','I04'],
    'data_rules':['No cross-country monetary bar chart: benefits and currencies are not comparable.',
                  'No percentage sign on IAFSP scores.',
                  'No numeric relevance score invented for the quadrant.',
                  'No probability band on illustrative scenarios.']
})
print(f'Prepared {len(sources)} inspected source records, {len(claims)} bounded claims, and chart input snapshots.')
