"""Reproduce the bounded review's calculations, data tables and standalone briefing."""
from pathlib import Path
import csv
import hashlib
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent
AS_OF = '2026-10-19'
VIZ = Path('C:/Users/meor2/.codex/visualizations/2026/10/18/01a14fe6-9c67-7fd0-aad7-04494cbcf8c6/msme-agency-quadrant.html')

def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def csv_out(path, rows):
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

sources = [
 ('D01','KUSKOP detailed federal estimates 2027','https://belanjawan.mof.gov.my/pdf/belanjawan2027/perbelanjaan/BP.26.pdf','Ministry of Finance','Printed pp.309–317; B.26 and P.26','2027 proposal with 2026 comparator; grants are not entity overhead. Operating estimates and amended development estimates have different labels.'),
 ('D02','KUSKOP detailed federal estimates 2026','https://belanjawan.mof.gov.my/pdf/belanjawan2026/perbelanjaan/BP.26.pdf','Ministry of Finance','B.26 operating and P.26 development tables','Original vote; reconcile later programme reclassification and amended numbers. No separately named 2027 line is not proof of closure.'),
 ('D03','SMEIPA 2025, reporting 2024 outcomes','https://smecorp.gov.my/index.php/my/artikel-popular/9-uncategorised/5133-sme-integrated-plan-of-action-smeipa-2025','SME Corp Malaysia','Printed pp.12–13,16,23,28–32,41,48,56,66–67','Official page iframe src confirmed in browser: https://online.anyflip.com/wtvjw/huat/mobile/index.html. Matching HTML text inspected at https://anyflip.com/wtvjw/huat/basic and /basic/51-100. Scores classify reported programmes, not whole entities or causal effects; varying portfolios and no independently appraised common causal design.'),
 ('D04','KUSKOP internal audit annual report 2024','https://www.kuskop.gov.my/admin/files/med/image/portal/PDF/Penerbitan/FULL%20LAPORAN%20TAHUNAN%20UAD%20KUSKOP%202024.pdf','KUSKOP Internal Audit Unit','Printed pp.94–98;103–108;119–140;148–157;161','Primary internal audit; findings have scope and date limits. Read management responses and Table89 closure status. Micro Connector counts conflict: Tables51 and54. Not a current whole-agency failure finding.'),
 ('D05','KUSKOP internal audit annual report 2025','https://www.kuskop.gov.my/admin/files/med/image/portal/PDF/Penerbitan/LAPORAN%20TAHUNAN%20UAD%20KUSKOP%202025.pdf','KUSKOP Internal Audit Unit','Printed pp.26–37; PPKUIH Tables3–14','Audited reconciliation differs from initial reported counts. Certification application KPI is at least50%, not100%. Management says multiple grants can have different purposes. Responses are not independently verified completion here.'),
 ('D06','SME Bank integrated annual report 2025','https://www.smebank.com.my/documents/d/guest/sme-bank_iar-2025-final','SME Bank','Printed pp.38–39;210–211;235;298; opening group overview','Audited financial statements distinguished from management performance statements. Bank-only and group amounts kept separate. Existing BPMB integration not new proposed reform savings.'),
 ('D07','Budget speech 2026 and appendices','https://belanjawan.mof.gov.my/pdf/belanjawan2026/ucapan/ub26.pdf','Ministry of Finance','Printed pp.84,187,210','AIM funds available and PUNB financing pool sizes are not entity operating expenses. Rates and individual products may subsequently change; not used for current lending advice.'),
 ('D08','KKDW detailed federal estimates 2027','https://belanjawan.mof.gov.my/pdf/belanjawan2027/perbelanjaan/BP.22.pdf','Ministry of Finance','Printed pp.250–251,256,260','MARA and RISDA wider duties; operating grants cover more than MSME programmes. 2027 proposed, 2026 estimates/amended development. Do not compare 2025 actuals with 2026 targets as same-year KPIs.'),
 ('D09','Current TERAJU mandate and department','https://teraju.gov.my/tentang-teraju/','TERAJU','Mengenai TERAJU','Inspected current mandate page states return to PM Department effective26June2026, superseding February release affiliation.'),
 ('D10','TERAJU media release 11 February 2026','https://teraju.gov.my/wp-content/uploads/2026/02/TERAJU-Siaran-Media.pdf','TERAJU','p.2, Rekod pembiayaan2025','Self-reported volume target; no counterfactual or audited entity overhead. 1.07bn plus158m is1.228bn; do not infer unique beneficiary counts from rounded figures.'),
 ('D11','TEMAN TEKUN 2025 financing versus target','https://www.bernama.com/bm/news.php?id=2519326','Bernama reporting minister statement','2February2026, national TEMAN financing paragraph','Attributed first-hand minister statement, not independent audit. Single programme volume metric, not total TEKUN outcome or current whole-agency KPI.'),
 ('D12','INSKEN current services','https://www.insken.gov.my/home/','INSKEN','Mengenai INSKEN; counters through December2025','Current training/coaching mandate. Cumulative counters are not annual target attainment.'),
 ('D13','PERNAS current services','https://www.pernas.my/en','PERNAS','Corporate and service description','Franchise financing/development and commercial activities; current full accounts not established.'),
 ('D14','PUNB financing service','https://rakanusahawan.punb.com.my/business-financing/rakan-usahawan','PUNB','Business financing overview','Bumiputera business finance role; no audited entity operating cost established.'),
 ('D15','BSN sustainability and inclusion mandate','https://www.bsn.com.my/page/Sustainability?lang=en','BSN','Our mission; Advancing financial inclusion','Current stated wider mandate; not independent proof of additionality or every programme outcome.'),
 ('D16','RISDA official profile','https://www.risda.gov.my/ms/mengenai-risda/profil','RISDA','Profile, powers and functions','Statutory smallholder remit wider than entrepreneurship; no whole-entity failure inference from MSME portfolio score.'),
 ('D17','TEKUN Niaga terms and client scope','https://www.tekun.gov.my/skim-pembiayaan-tekun-niaga-syarat-syarat/','TEKUN','Skim pembiayaan TEKUN Niaga, eligibility','One product is not the full TEKUN mandate; generic microfinance role also corroborated in budget and SMEIPA.'),
]
registered = []
for sid,title,url,publisher,locator,appraisal in sources:
    registered.append(dict(id=sid,title=title,url=url,publisher=publisher,accessed=AS_OF,inspection='inspected',locator=locator,origin_group=sid.lower(),appraisal=appraisal))
import os
originals = Path(os.environ.get('TEMP',''))/'msme-deep-dive'
for sid,filename in {'D01':'budget2027.pdf','D02':'budget2026.pdf','D04':'audit2024.pdf','D05':'audit2025.pdf','D06':'smebank2025.pdf','D07':'speech2026.pdf','D08':'budget2027-22.pdf'}.items():
    file=originals/filename
    if file.exists():
        entry=next(s for s in registered if s['id']==sid)
        entry['inspected_original_sha256']=hashlib.sha256(file.read_bytes()).hexdigest()
kri = next(x for x in json.loads((PARENT/'sources.json').read_text(encoding='utf-8')) if x['id']=='K01')
registered.append(kri)
write_json(ROOT/'sources.json', registered)

agency_rows = [
 ('insken','INSKEN',95.4,10.92,10513,'transfer','Training and coaching can move to an existing host with protected access; specialised coaches remain useful.','D01;D03;D04;D12',11.4701,9.4,12.0009,9.4),
 ('pernas','PERNAS',87.1,39.07,678,'transfer','Common lending administration is transferable; franchise assets, expertise and obligations complicate whole-entity closure.','D02;D03;D13',None,9.0,None,None),
 ('punb','PUNB',99.5,327.78,719,'transfer','Preserve Bumiputera objective while testing financing administration in existing infrastructure.','D03;D07;D14',None,None,None,None),
 ('smecorp','SME Corp',99.5,89.49,43168,'retain','Central MSME coordination and evaluation justify a distinct role; routine delivery can merge.','D01;D03;D04',44.4224,117.0,42.7564,137.0),
 ('smebank','SME Bank',70.3,261.50,346,'retain','A regulated development-finance capability has funding and risk duties beyond generic programme administration.','D03;D06',None,6.0,None,None),
 ('tekun','TEKUN',87.2,968.30,40433,'retain','Microfinance access and outreach justify retaining delivery while testing common administration.','D01;D03;D11;D17',3.0,530.0,3.0,550.0),
 ('aim','AIM',97.2,2678.96,285712,'retain','Inclusive microfinance access remains needed; distinct client access must be tested before structural consolidation.','D03;D07',None,None,None,None),
 ('mara','MARA',99.1,109.71,17140,'retain','Wider education, skills and entrepreneurship responsibilities prevent a closure case based on MSME overlap alone.','D03;D08',1610.0,2578.3109,1710.0,2670.8759),
 ('bsn','BSN',41.8,624.57,18965,'retain','The financial-inclusion mission is wider than the measured MSME programmes; investigate weak programmes.','D03;D15',None,None,None,None),
 ('cgc','CGC',66.7,4015.10,6569,'retain','Credit guarantees have a distinct financing function; weaker reported sustainability scores require programme review. Public-linked entity.','D03',None,None,None,None),
 ('risda','RISDA',67.4,13.39,1171,'retain','Smallholder statutory and access roles exceed its entrepreneurship portfolio.','D03;D08;D16',245.5364,None,267.2755,None),
 ('skm','SKM',None,None,None,'retain','Cooperative regulatory role remains distinct; separate MSME portfolio index not established here.','D01;D04',90.5,10.8,91.0,10.5),
 ('teraju','TERAJU',None,None,None,'mixed','Coordination plus scaling delivery must be separated before a whole-entity classification.','D09;D10',None,None,None,None),
]
agencies=[]
for aid,name,score,flow,people,side,rationale,source_ids,op26,dev26,op27,dev27 in agency_rows:
    agencies.append(dict(id=aid,name=name,performance_score=score,performance_year=2024 if score is not None else None,framework='IAFSP as reported in SMEIPA2025',meeting_threshold=70,programme_flow_2024_rm_million=flow,reported_beneficiaries_2024=people,institution_case=side,classification_type='analyst qualitative judgement, not official or validated score',rationale=rationale,source_ids=source_ids.split(';'),federal_operating_estimate_2026_rm_million=op26,federal_development_2026_rm_million=dev26,federal_operating_proposed_2027_rm_million=op27,federal_development_proposed_2027_rm_million=dev27,budget_caveat='Not whole-entity expense. PERNAS and SME Bank development entries use original2026 vote; others use latest2027 comparator. MARA includes education. Null means not established.'))
write_json(ROOT/'data/agencies.json', agencies)
csv_out(ROOT/'data/agency-comparison.csv',[{k:v for k,v in x.items() if k not in ['source_ids']} for x in agencies])

kpis = [
 dict(id='KPI01',agency='SME Corp',programme='Micro Connector',year='2023',actual=877,target=1060,unit='participants',higher_is_better=True,source='D04',locator='Table54 printedp98',limit='Table51 instead reports886; detailed table sums877. Historical programme output, not agency-wide current failure.'),
 dict(id='KPI02',agency='INSKEN',programme='IBBC employment',year='2022–2023',actual=314/1119*100,target=50,unit='percent of outcome dataset offering jobs',higher_is_better=True,source='D04',locator='Tables58–59 printedp106',limit='Reported outcome dataset1119; not enrolment denominator. Changed targets2024. Committee issues reported completedJan2025.'),
 dict(id='KPI03',agency='SKM',programme='SCOPE existing centre upgrades',year='audit2024 scope2021–2024',actual=9,target=20,unit='centres',higher_is_better=True,source='D04',locator='SCOPE chapter printedpp119–140',limit='One output; new-centre output exceeded target. Not entire regulatory role.'),
 dict(id='KPI04',agency='SKM',programme='SCOPE new centres',year='audit2024 scope2021–2024',actual=30,target=20,unit='centres',higher_is_better=True,source='D04',locator='SCOPE chapter',limit='Output, not independently measured business outcome.'),
 dict(id='KPI05',agency='SME Bank',programme='Financing approvals',year='2025',actual=4300,target=3300,unit='RMmillion',higher_is_better=True,source='D06',locator='Printedpp38–39',limit='Management volume report; no causal attribution.'),
 dict(id='KPI06',agency='SME Bank',programme='Average turnaround time',year='2025',actual=88,target=104,unit='days upper limit',higher_is_better=False,source='D06',locator='Printedpp210–211',limit='Average can hide distribution and client experiences.'),
 dict(id='KPI07',agency='TEKUN',programme='TEMAN financing',year='2025',actual=162.05,target=155,unit='RMmillion',higher_is_better=True,source='D11',locator='National programme volume paragraph',limit='Minister statement; one programme, not whole entity.'),
 dict(id='KPI08',agency='TERAJU',programme='Financing volume',year='2025',actual=1070+158,target=1000,unit='RMmillion',higher_is_better=True,source='D10',locator='p2',limit='Self-reported; facilitated/distributed financing not own operating budget.'),
 dict(id='KPI09',agency='Multiple agencies',programme='PPKUIH applications reconciled',year='2021–June2025',actual=288/351*100,target=50,unit='percent grant recipients applying',higher_is_better=True,source='D05',locator='Printedpp27–29 Tables5–8',limit='288 reconciled versus initial348. Outcome target50%; cannot call24/27 at PERNAS a failure of that target.'),
]
for r in kpis:
    r['target_attainment_percent']=(r['actual']/r['target'] if r['higher_is_better'] else r['target']/r['actual'])*100
    r['meets_stated_target']=r['actual']>=r['target'] if r['higher_is_better'] else r['actual']<=r['target']
write_json(ROOT/'data/kpi-records.json',kpis)
csv_out(ROOT/'data/kpi-records.csv',kpis)

anchors={'SME Corp operating grant':42.7564,'INSKEN operating grant':12.0009,'KUSKOP management supplies and services':29.836}
parameters={
 'low':dict(shares=[(.10,.15),(.20,.20),(.10,.10)],recurring=2.0,transition=6.0),
 'central':dict(shares=[(.15,.20),(.275,.25),(.15,.15)],recurring=1.5,transition=4.5),
 'high':dict(shares=[(.20,.25),(.35,.30),(.20,.20)],recurring=1.0,transition=3.0),
}
scenarios=[]; details=[]
for name,p in parameters.items():
    gross=0
    for (anchor,amount),(addressable,retire) in zip(anchors.items(),p['shares']):
        saved=amount*addressable*retire;gross+=saved
        details.append(dict(scenario=name,anchor=anchor,baseline_rm_million=amount,baseline='Proposed2027; D01 B.26',assumed_addressable_share=addressable,assumed_retired_share=retire,gross_rm_million=saved))
    yearly=[gross*ramp-p['recurring']-(p['transition'] if i==0 else 0) for i,ramp in enumerate([.25,.75,1.0])]
    net=gross-p['recurring']; cumulative=sum(yearly)
    payback=3+(-cumulative/net) if net>0 and cumulative<0 else None
    scenarios.append(dict(scenario=name,gross_annual_rm_million=gross,incremental_annual_rm_million=p['recurring'],net_mature_annual_rm_million=net,transition_once_rm_million=p['transition'],year1_net_rm_million=yearly[0],year2_net_rm_million=yearly[1],year3_net_rm_million=yearly[2],three_year_net_rm_million=cumulative,approx_payback_years=payback,model_status='Conditional sensitivity; unverified addressable overhead, retirement fractions and delivery costs. Not a forecast or observed saving.'))
csv_out(ROOT/'data/savings-assumptions.csv',details)
csv_out(ROOT/'data/savings-scenarios.csv',scenarios)
write_json(ROOT/'data/savings-model.json',dict(currency='RMmillion nominal',source='D01',anchors=anchors,rollout=[.25,.75,1],discounting=False,scenarios=scenarios,central_max_transition_for_three_year_break_even=2*scenarios[1]['gross_annual_rm_million']-3*scenarios[1]['incremental_annual_rm_million'],bank_separate=dict(source='D06 Note25 p298',expense_pool=6.241+12.784,assumed_retirement_range=[.05,.10],gross_range=[19.025*.05,19.025*.10],net_estimate=None,federal_savings=None)))

claims=[]
def claim(cid,text,kind,ids,locator,limitations,confidence='Bounded by source scope'):
    claims.append(dict(id=cid,text=text,kind=kind,source_ids=ids,locator=locator,status='supported' if kind not in ['policy-proposal','scenario'] else 'explicitly-conditional',confidence=confidence,limitations=limitations))
claim('M01','Current mandates and funding lines differ; no common entity-wide overhead base exists in the inspected evidence.','source-based-inference',['D01','D02','D06','D07','D08','D09','D12','D13','D14','D15','D16','D17'],'Budget and mandate tables','Missing current expense not zero or failure.')
claim('M02','The 2024 IAFSP scores and programme flows are recorded in agency data. All six selected KUSKOP core delivery agencies meet the source threshold.','external-fact',['D03'],'Printedpp12,28–32,56','Reported programme framework, not all duties or causal impact.')
claim('M03','BSN41.8, CGC66.7, RISDA67.4 are below the published70-point threshold for the measured2024 MSME programmes.','external-fact',['D03'],'Printedpp48,66–67','Do not generalise to whole organisation.')
claim('M04','Historical Micro Connector, IBBC employment and SCOPE upgrades missed selected targets; other outputs and overall audit ratings differ.','calculation',['D04'],'Tables51,54,58–59 and SCOPE chapter','Data conflicts, changed cohorts and mixed outputs disclosed.')
claim('M05','Audit committee table reports presented INSKEN and BIZME issues completed by14January2025.','external-fact',['D04'],'Table89 p161','Issue closure not proof of sustained outcome recovery.')
claim('M06','Halal audit reconciles288/351 applications and identifies inconsistent cross-agency administration;50% outcome target differs from full-cohort count.','external-fact',['D05'],'Printedpp26–35','Management responses included; complementary grants not all duplicate spend.')
claim('M07','2025 financing target comparisons for SME Bank, TEMAN and TERAJU pass their respective reported volume targets.','calculation',['D06','D10','D11'],'KPI05–08 in data','Different programmes; self-report/minister statement; not causal outcomes.')
claim('M08','SME Bank bank-only2025 operating expense303.201m and candidate expense pool19.025m derive from accounts.','external-fact',['D06'],'Printedpp235,298 Note25','Own-bank costs not federal spending; candidate pool not verified cash or duplicated.')
claim('M09','INSKEN and PERNAS are conditional standalone closure candidates following service transfer.','policy-proposal',['D01','D03','D04','D05','D06','D12','D13'],'Report sections5–6','No completed legal, workforce or costed transfer case; not whole-agency failure findings.',confidence='Moderate function merger; low whole-entity closure')
claim('M10','Budget-supported savings scenarios range from−0.580m to3.591m net annually; central1.279m, three-year−3.442m.','scenario',['D01'],'Data savings-assumptions and savings-scenarios','Assumed overhead share, retirement fractions, recurring cost and transition; grants may contain pass-through spending. No observed savings.',confidence='Arithmetic high; forecast confidence not established')
claim('M11','Old deferred grants are not current or annual savings; management identified9.97m without commitments in2024 response.','external-fact',['D04'],'Printedpp148–157','End2022 stock and later management plan; current recoverability unverified.')
claim('M12','Institutional distinctiveness classification is analyst judgement, independent of reported programme score.','policy-proposal',['D01','D03','D08','D09','D12','D13','D14','D15','D16'],'Quadrant and agency rationale records','Not official relevance rating, empirical validation or automatic closure rule.')
claim('M13','KRI establishes governance-coordination and capacity concerns; proposed named closure cases and savings are this extension.','source-based-inference',['K01'],'Prior report relevant passages and present model','No KRI endorsement of proposals.')
claim('M14','SME Bank already joined the BPMB group inMay2025.','external-fact',['D06'],'Opening overview and leadership discussion','Do not count existing integration again as new savings.')
write_json(ROOT/'claims.json',claims)

def inline(s):
    s=html.escape(s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:f'<a href="{m[2]}">{m[1]}</a>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    return s

def render_md(md):
    lines=md.splitlines();out=[];paragraph=[];listing=False;i=0
    def flush():
        if paragraph:out.append('<p>'+inline(' '.join(paragraph))+'</p>');paragraph.clear()
    while i<len(lines):
        line=lines[i]
        if line.startswith('|'):
            flush()
            if listing:out.append('</ul>');listing=False
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                vals=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',x.replace(' ','')) for x in vals):rows.append(vals)
                i+=1
            out.append('<div class="table-wrap"><table><thead><tr>'+''.join('<th scope="col">'+inline(x)+'</th>' for x in rows[0])+'</tr></thead><tbody>')
            out.extend('<tr>'+''.join('<td>'+inline(x)+'</td>' for x in row)+'</tr>' for row in rows[1:]);out.append('</tbody></table></div>');continue
        if line.startswith('#'):
            flush()
            if listing:out.append('</ul>');listing=False
            n=len(line)-len(line.lstrip('#'));t=line[n:].strip();slug=re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')
            out.append(f'<h{n} id="{slug}">{inline(t)}</h{n}>')
        elif line.startswith('- '):
            flush()
            if not listing:out.append('<ul>');listing=True
            out.append('<li>'+inline(line[2:])+'</li>')
        elif not line.strip():
            flush()
            if listing:out.append('</ul>');listing=False
        else:paragraph.append(line)
        i+=1
    flush()
    if listing:out.append('</ul>')
    return '\n'.join(out)

md=(ROOT/'to_human/msme-agency-review.md').read_text(encoding='utf-8')
fragment_source=VIZ if VIZ.exists() else ROOT/'to_human/quadrant-fragment.html'
fragment=fragment_source.read_text(encoding='utf-8')
(ROOT/'to_human/quadrant-fragment.html').write_text(fragment,encoding='utf-8')
body=render_md(md)
body=body.replace('<h2 id="evidence-and-reproducibility">',fragment+'<h2 id="evidence-and-reproducibility">')
nav=''.join(f'<a href="#{m[1]}">{m[2]}</a>' for m in re.finditer(r'<h2 id="([^"]+)">(.+?)</h2>',body))
style='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f7f4ec;color:#25322f;font:17px/1.65 Georgia,serif}header{background:#173f39;color:#fff;padding:24px max(6vw,24px);font:500 14px/1.5 system-ui}main{max-width:1120px;margin:auto;padding:44px 28px 80px}h1,h2,h3{font-family:system-ui;line-height:1.2}h1{font-size:clamp(32px,5vw,54px);max-width:950px}h2{font-size:27px;margin-top:60px;border-top:1px solid #c8d3cb;padding-top:24px}h3{font-size:21px;margin-top:32px}a{color:#15695b;text-underline-offset:3px}nav{display:flex;flex-wrap:wrap;gap:10px 22px;font:14px/1.5 system-ui;padding:20px 0;border-bottom:1px solid #c8d3cb}p{max-width:90ch}li{margin:10px 0}.table-wrap{overflow:auto;margin:24px 0}table{border-collapse:collapse;width:100%;font:14px/1.55 system-ui;min-width:620px}th,td{text-align:left;vertical-align:top;padding:12px;border-bottom:1px solid #ced8d0}th{background:#dce7de}tbody tr:nth-child(even){background:#eef1e9}footer{font:13px system-ui;margin-top:50px;border-top:1px solid #c8d3cb;padding-top:20px}#msme-quadrant-261019{font:14px/1.5 system-ui;--foreground:#25322f;--muted-foreground:#56675d;--border:#bdccc2;--viz-series-1:#327464;--viz-series-2:#bd7e3a;--primary:#173f39;--primary-foreground:#fff;margin:35px 0}#msme-quadrant-261019 .btn{font:inherit;min-height:38px;padding:8px 12px;border:1px solid #c9d5cb;background:transparent;color:inherit;border-radius:6px}#msme-quadrant-261019 .btn[aria-pressed=true]{background:var(--primary);color:var(--primary-foreground)}#msme-quadrant-261019 .card{padding:16px;border:1px solid #cad6cc;border-radius:8px;background:#edf2e9}#msme-quadrant-261019 .text-small{font-size:12px}#msme-quadrant-261019 .text-muted{color:var(--muted-foreground)}#msme-quadrant-261019 .viz-row{display:flex;gap:8px;flex-wrap:wrap}#msme-quadrant-261019 h3{font-size:21px}#msme-quadrant-261019 .tabular-nums{font-variant-numeric:tabular-nums}a:focus-visible,button:focus-visible{outline:3px solid #c27e20;outline-offset:3px}@media(max-width:640px){main{padding:28px 18px}h2{font-size:24px}}@media print{body{background:white;font-size:10pt}header,nav{display:none}main{max-width:none;padding:0}.table-wrap{overflow:visible}table{min-width:0;font-size:8pt}tr{break-inside:avoid}h2,h3{break-after:avoid}a{color:inherit}#msme-quadrant-261019{break-inside:avoid}}'''
page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Malaysia MSME agency review</title><style>'+style+'</style></head><body><header>MSME SUPPORT · INSTITUTIONAL REVIEW<br>Prepared for Meor · 19 October2026 · Unpublished</header><main><nav aria-label="Contents">'+nav+'</nav>'+body+'<footer>Exploratory desk research. Source scope, dates and conditional calculations are part of the findings. No publication or author approval recorded.</footer></main></body></html>'
(ROOT/'to_human/msme-agency-review.html').write_text(page,encoding='utf-8')

write_json(ROOT/'assets.json',[dict(id='A01',path=str((ROOT/'to_human/quadrant-fragment.html').relative_to(PARENT.parents[2])).replace('\\','/'),alt='Quadrant of13 selected MSME institutions: passing transferable delivery, passing distinct role, below-framework distinct role, and unknown evidence.',rights='Original analysis and layout; factual numeric data from cited official publications. No source images reproduced.',attribution='Codex-assisted analysis for Meor; performance data SME Corp SMEIPA2025',source_url=sources[2][2],kind='interactive-conceptual-classification',input_paths=['research/articles/ai-native-malaysia-government/msme/data/agencies.json','research/articles/ai-native-malaysia-government/msme/src/build_outputs.py'])])

assert abs(sum(anchors.values())-84.5933)<1e-9
assert len(agencies)==13 and sum(x['performance_score'] is not None for x in agencies)==11
assert all(x['performance_score']>=70 for x in agencies if x['id'] in ['insken','pernas','punb'])
assert abs(scenarios[1]['net_mature_annual_rm_million']-1.279063875)<1e-8
assert abs(scenarios[1]['three_year_net_rm_million']+3.44187225)<1e-8
assert abs(kpis[1]['target_attainment_percent']-56.12153708668454)<1e-8
assert '\\"' not in fragment and '\\n' not in fragment
assert not re.search(r'<(?:!doctype|html|head|body)\b',fragment,re.I)
assert 'fetch(' not in fragment and 'XMLHttpRequest' not in fragment
assert all(x['source_ids'] for x in claims)
source_ids={x['id'] for x in registered}
assert all(set(c['source_ids'])<=source_ids for c in claims)
assert len(re.findall(r'<table>',page))==7
print(json.dumps(dict(agencies=len(agencies),sources=len(registered),claims=len(claims),kpis=len(kpis),scenarios=len(scenarios),central=scenarios[1],report_words=len(md.split()),html_bytes=len(page.encode()),arithmetic_and_integrity='passed'),indent=2))
