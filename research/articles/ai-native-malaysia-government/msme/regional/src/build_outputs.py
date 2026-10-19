"""Build the regional evidence packet and readable briefings. Standard library only."""
from pathlib import Path
import ast, csv, hashlib, html, json, os, re

ROOT=Path(__file__).resolve().parents[1]
AS_OF='2026-10-19'
DATA=ROOT/'data';DATA.mkdir(exist_ok=True)
def dump(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

source_rows=[
 ('S01','Enterprise Singapore government directory','https://www.sgdi.gov.sg/ministries/meti/statutory-boards/enterprisesg','Singapore Government Directory','Agency description, merger date','inspected','Primary current official record confirms IE/SPRING combined1April2018. Does not quantify merger savings.'),
 ('S02','Budget2018 support for firms','https://www.mof.gov.sg/docs/default-source/default-document-library/singapore-budget/budget-archives/2018/fy2018_budget_statement.pdf?sfvrsn=55b42e95_2','Singapore Ministry of Finance','AnnexA-3, Enterprise Development Grant','partial-indexed-text','Relevant original-publisher indexed passage inspected. Confirms harmonisation of CDG/GCP into EDG; not a full budget or savings appraisal.'),
 ('S03','Impact evaluation of EDG and EDG-I','https://isomer-user-content.by.gov.sg/1004/7cb36396-c58c-4bff-a50e-73a675a41bb7/FA_1Q26.pdf','Singapore economic survey; Ngoh Jia Hui and Jasmine Lee','Printedpp42–45, full four-page article','inspected','May2026 administrative-data fixed-effects evaluation. EDG2019–2022; other grants and firm/year effects controlled. Time-varying confounding and grant selection may remain; no merger counterfactual or fiscal return estimated.'),
 ('S04','EnterpriseSG annual media briefing2026','https://www.enterprisesg.gov.sg/-/media/esg/files/media-centre/media-releases/2026/january/mr00326_annual-media-briefing-2026.pdf','Enterprise Singapore','28January2026,pp1–2','inspected','Primary agency release. 2025 project counts and expected company revenue/cost benefits; not audited government savings. Average200k applies to relevant projects, not every supported enterprise.'),
 ('S05','Parliamentary reply on EDG broader impacts','https://www.meti.gov.sg/newsroom/written-reply-to-pq-on-broader-impact-of-projects-supported-by-enterprise-development-grant-beyond-revenue-and-value-add/','Singapore ministry; parliamentary reply','5August2026,answerparagraph1','inspected','Recipients reported average200k annual company cost reductions; paragraph also calls savings estimated. No independent verification or agency-merger savings bridge. Same policy system, not independent corroboration of release.'),
 ('S06','Enterprise Singapore annual report2024–2025','https://www.enterprisesg.gov.sg/-/media/esg/files/resources/publications/annual-reports/enterprisesg-annual-report-2024-2025.pdf','Enterprise Singapore','Financial highlights printedpp25–26,year ended31March2025','inspected','Original27-page report downloaded; relevant highlights inspected. Operating expenditure326.5m, manpower187.3m, other139.2m, grants305.5m, surplus2.5m. These are agency highlights, not all MSME support spending or an attributable merger saving. No audit opinion appraisal claimed.'),
 ('T01','OSMEP annual report2566/2023','https://www.sme.go.th/uploads/file/20240919-124025_SME_Annual_lowres_final.pdf','OSMEP Thailand','Printedp64,SME ONE ID project','partial-indexed-text','Original publisher indexed English passage inspected; full download/open timed out. FY2023 outputs119173 versus75500 target; expenditure5418423.72 versus5472000THB budget. Output and underspend not fiscal merger effect.'),
 ('T02','BDS programme results and FY2569 plans','https://bds.sme.go.th/News/Detail/103','OSMEP Thailand','1December2025,programme-results and budget paragraphs','inspected','Primary programme promotion in Thai; translated/paraphrased here. Distinguish registrations,verified firms,proposals and headline beneficiaries. Agency economic-value claim has no counterfactual method here.260m support and300m FY2026 budget are funding,not savings. Provider network includes public specialist and academic organisations;2026 private-provider extension described as planned.'),
 ('T03','BDS SME application process','https://bds.sme.go.th/Sme','OSMEP Thailand','Identity,membership,development-proposal and agreement steps','inspected','Live programme workflow. Confirms common entry process; no measured burden or savings outcome.'),
 ('I01','Four years of the Ultra Micro holding','https://www.pnm.co.id/berita/4-tahun-holding-ultra-mikro-pnm-hadirkan-senyum-jutaan-perempuan-indonesia','PNM Indonesia','13September2025 account,opening history','partial-indexed-text','Primary subsidiary account; relevant indexed formation passage inspected. Full page retrieval timed out. Holding formed13September2021; not three entities abolished. Self-report not independent merger evaluation.'),
 ('I02','BRI Q3 2025 results and Ultra Micro network','https://bri.co.id/web/guest/promo-news-detail/1279','BRI','30October2025,Ultra Micro paragraph,figures asSeptember2025','inspected','1035SenyuM outlets and34.5m active borrowers are operating stocks. Self-report; not newly included borrowers caused by holding or quantified net cost saving. General bank profit/funding claims not treated as holding-specific effects.'),
 ('I03','BRI customer journey and FY2024 UMi network','https://www.bri.co.id/web/guest/id/promo-news-detail/1076','BRI','20February2025,empower/integrate/upgrade paragraphs','inspected','Specialist client journey across PNM/Pegadaian/BRI. Different business models remain. No holding-specific net savings figure in inspected account.'),
 ('R01','SME Policy Index ASEAN2024','https://www.eria.org/uploads/ASPI_2024-Full_report-upload-20Sep.pdf','ASEAN,OECD,ERIA','Printedpp337,398,422,429; methodological context','inspected','Original517-page report downloaded; selected country/coordination passages inspected. Policy design/implementation/monitoring assessment,not causal impact or savings ranking. Malaysia described as advanced;Thailand coordination/data sharing still need improvement. Not a complete current2026 ministry map.'),
 ('I04','BRI annual report2025 full file','https://bri.co.id/web/guest/api/files?path=%2Fsites%2Fdefault%2Ffiles%2Fdocuments%2FAnnual+Report+BRI+Tahun+2025_Bahasa+%282%29.pdf','BRI','Full file access attempt','inaccessible','Web extraction rejected over10MiB; local response wasHTML,not a validPDF. Do not claim full financial statements inspected or derive fiscal savings from this file.'),
]
sources=[dict(id=i,title=t,url=u,publisher=p,accessed=AS_OF,inspection=s,locator=l,origin_group=('enterprise-singapore-system' if i in ['S01','S02','S04','S05','S06'] else 'osme-programmes' if i.startswith('T') else 'bri-umi-system' if i.startswith('I') else i.lower()),appraisal=a) for i,t,u,p,l,s,a in source_rows]
temp=Path(os.environ.get('TEMP',''))/'msme-regional'
for sid,file in [('S03','edg-evaluation2026.pdf'),('S06','enterprise2024-25.pdf'),('R01','asean2024.pdf')]:
 f=temp/file
 if f.exists() and f.read_bytes().startswith(b'%PDF'):
  next(s for s in sources if s['id']==sid)['inspected_original_sha256']=hashlib.sha256(f.read_bytes()).hexdigest()
previous=json.loads((ROOT.parent/'sources.json').read_text(encoding='utf-8'))
sources.extend(x for x in previous if x['id'] in ['D01','D04','D05','D06','K01'])
dump(ROOT/'sources.json',sources)

cases=[
 dict(country='Malaysia',mechanism='Existing coordinator plus BPMB-group integration',completed_change='SME Bank/EXIM/BPMB common group in2025',government_net_saving=None,saving_status='not established',assessment='Existing structure and measured programme outputs; fiscal scenario remains conditional',sources=['D01','D04','D05','D06','R01']),
 dict(country='Singapore',mechanism='Statutory agency merger plus programme harmonisation',completed_change='IE+SPRING formedEnterpriseSG1April2018;CDG+GCP harmonised intoEDG',government_net_saving=None,saving_status='not established',assessment='Institutional integration delivered; grant effects supported by bounded observational evaluation; merger effect not isolated',sources=['S01','S02','S03','S04','S05','S06']),
 dict(country='Thailand',mechanism='Shared identity and service-provider platform',completed_change='SME ONE ID andBDS operational;no comparable closure case established in inspected records',government_net_saving=None,saving_status='not established',assessment='Operating integration output; coordination and impact-evaluation gaps remain',sources=['T01','T02','T03','R01']),
 dict(country='Indonesia',mechanism='Public financial holding plus shared service outlets',completed_change='UMi holdingSeptember2021;specialist entities remain',government_net_saving=None,saving_status='not established',assessment='Shared outlets/referral journey delivered; access causality and net fiscal saving not established',sources=['I01','I02','I03']),
]
dump(DATA/'reform-cases.json',cases)

model=json.loads((ROOT.parent/'data/savings-model.json').read_text(encoding='utf-8'))
central=next(x for x in model['scenarios'] if x['scenario']=='central')
ledger=[]
def money(i,country,currency,amount,period,category,status,source,notes):
 ledger.append(dict(id=i,country=country,currency=currency,amount=amount,period=period,category=category,status=status,source_id=source,government_merger_saving=False,notes=notes))
money('N01','Singapore','SGD',118000000,'2025supportedprojects,expectedannualbenefit','recipient company operating-cost reduction','expected','S04','Not agency saving; do not add average saving from another population.')
money('N02','Singapore','SGD',200000,'2025,annualaverage','company cost reduction per relevant project/company','expected in release','S04','Not all11700 supportedfirms.')
money('N03','Singapore','SGD',200000,'2025,annualaverage','EDG recipient company cost reduction','reported/estimated in parliamentary reply','S05','Not an independent audit or additional amount to sum withN01.')
money('N04','Singapore','SGD',326500000,'FY2024,ended31March2025','agency operating expenditure','published financial highlights','S06','Not all SingaporeMSME funding;no unmerged counterfactual.')
money('N05','Singapore','SGD',187300000,'FY2024','agency manpower expenditure','published financial highlights','S06','Component ofN04;do not doublecount.')
money('N06','Singapore','SGD',139200000,'FY2024','agency other operating expenditure','published financial highlights','S06','Component ofN04.')
money('N07','Singapore','SGD',2500000,'FY2024','agency net surplus','published financial highlights','S06','Accounting surplus,not merger costavoidance.')
money('N08','Thailand','THB',6000000000,'cumulative asreported1December2025','programme economic value','agency claim;more than','T02','No counterfactual method in article;not savings orverifiedROI.')
money('N09','Thailand','THB',260000000,'earlier programme operation asreported1December2025','programme support funding','agency report;more than','T02','Source descriptions ofcumulativeperiod vary;not treatedasprecise costbase.')
money('N10','Thailand','THB',300000000,'FY2569/2026','BDS programme budget','approved funding described byagency','T02','Not wholeagencybudget or saving.')
money('N11','Thailand','THB',5418423.72,'FY2023','SMEONEID projectdisbursement','partial indexed annualreport','T01','Original fullreport inaccessible.')
money('N12','Thailand','THB',5472000,'FY2023','SMEONEID projectbudget','partial indexed annualreport','T01','Budgetminusdisbursement53576.28 isunderspend,notmergersaving.')
money('N13','Malaysia','MYR',central['net_mature_annual_rm_million']*1e6,'prospective,matureannual','net budget-supported savings scenario','conditional model,not forecast orachieved','D01','Based onprior packet assumptions;no crosscountry scaling.')
money('N14','Malaysia','MYR',central['three_year_net_rm_million']*1e6,'prospectiveyears1–3','cumulativenet savings scenario','conditional model;negative meansnetcost','D01','Includestransitionandrollout;notachieved.')
money('N15','Malaysia','MYR',model['central_max_transition_for_three_year_break_even']*1e6,'prospectivefirstthreeyears','max transition compatiblewithcentralbreak-even','derived ceiling,notprocurementestimate','D01','2timescentralgross less3timesincrementalcost.')
dump(DATA/'money-ledger.json',ledger)
with (DATA/'money-ledger.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(ledger[0]));w.writeheader();w.writerows(ledger)
dump(DATA/'malaysia-model-reference.json',dict(origin='../data/savings-model.json',central_case=central,three_year_transition_ceiling_rm_million=model['central_max_transition_for_three_year_break_even'],caveat='Conditional assumptions retained unchanged;no foreignsavingsmultiplierused.'))

claims=[]
def cl(i,text,kind,ids,locator,limit):claims.append(dict(id=i,text=text,kind=kind,source_ids=ids,locator=locator,status='supported-with-scope-limit' if kind!='policy-proposal' else 'conditional-proposal',confidence='Bounded by evidence design and access',limitations=limit))
cl('RC01','Singapore completed the IE/SPRING agency merger and CDG/GCP programme harmonisation.','external-fact',['S01','S02','S03'],'Official agency description; Budget Annex A-3; study introduction','No fiscal merger effect inferred.')
cl('RC02','The EDG study finds a typical grant associated with 1.9% revenue and 1.6% value-added annual gains in 2019–2022.','external-fact',['S03'],'Printed p.44','Observational fixed-effects programme analysis; not an evaluation of the merger.')
cl('RC03','Singapore S$118m expected annual cost reduction and S$200k average are company benefits.','external-fact',['S04','S05'],'Release pp.1–2; parliamentary reply paragraph 1','Different populations and measurement status; no multiplication across all firms or addition of overlapping benefits.')
cl('RC04','EnterpriseSG FY2024 operating expense was S$326.5m: manpower187.3m and other139.2m; surplus2.5m.','external-fact',['S06'],'Printed pp.25–26','Financial highlights; not all support funding or avoided merger cost.')
cl('RC05','Thailand BDS uses common membership/identity and service providers; reported programme funding and economic value are not government savings.','external-fact',['T02','T03'],'Results release; application steps','Agency self-report, not causal return on investment.')
cl('RC06','SME ONE ID FY2023 registrations were119,173 versus75,500 target, and disbursementTHB5,418,423.72 versus5,472,000 budget.','external-fact',['T01'],'Indexed original publisher passage, printed p.64','Partial access; not unique business outcomes or public merger savings.')
cl('RC07','Indonesia UMi holding preserves specialist entities and operates shared SenyuM outlets.','external-fact',['I01','I02','I03'],'Holding history and operating paragraphs','Partial history access; operating counts are not causal effects.')
cl('RC08','None of the selected inspected records establishes a reconciled net government saving attributable to the restructuring.','bounded-source-inference',['S03','S04','S05','S06','T01','T02','I02','I03'],'Inspected records and money ledger','Not a comprehensive claim that no such evidence exists. Unknown is not zero; full BRI accounts were not inspected.')
cl('RC09','ASEAN2024 describes Malaysia as advanced and still recommends better Thai coordination and data sharing.','external-fact',['R01'],'Printed pp.337,429','Policy-framework assessment, not a current2026 census or merger-savings ranking.')
cl('RC10','The Malaysian central case has RM1.279m annual net savings but−3.442m three-year cumulative savings, and a transition ceiling of1.058m.','calculation',['D01'],'Prior packet model and money ledger N13–15','Assumed overhead, retirement and new costs; not a forecast or actual saving.')
cl('RC11','Malaysia has already grouped SME Bank/EXIM/BPMB; that integration must not be booked again as a new reform.','external-fact',['D06'],'Bank2025 opening overview','No existing net integration benefit verified here.')
cl('RC12','Copy joined case ownership, shared provider procurement and assisted access before committing to full closure.','policy-proposal',['S01','S02','T02','T03','I02','I03','D04','D05','K01'],'Report section6','Analyst adaptation; legal, access and costed transfer work remains.')
cl('RC13','Regional comparison does not upgrade conditional INSKEN/PERNAS options to confirmed fiscal wins.','policy-proposal',['D01','D04','D05','D06','S03','T02','I02'],'Report sections1,6–7','Complete current agency ledgers and transfer obligations remain unavailable.')
dump(ROOT/'claims.json',claims)
dump(ROOT/'assets.json',[])

# Reuse the preceding briefing's small renderer without executing that builder.
prior_ast=ast.parse((ROOT.parent/'src/build_outputs.py').read_text(encoding='utf-8'))
functions=[n for n in prior_ast.body if isinstance(n,ast.FunctionDef) and n.name in ['inline','render_md']]
assert len(functions)==2
exec(compile(ast.Module(body=functions,type_ignores=[]),'<local-renderer>','exec'),globals())
style='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f6f3ec;color:#24332d;font:17px/1.65 Georgia,serif}header{background:#193e36;color:white;padding:24px max(6vw,20px);font:14px/1.5 system-ui}main{max-width:1100px;margin:auto;padding:38px 26px 80px}h1,h2,h3{font-family:system-ui;line-height:1.2}h1{font-size:clamp(32px,5vw,52px);max-width:900px}h2{font-size:27px;margin-top:56px;padding-top:22px;border-top:1px solid #cad5cb}h3{font-size:21px}p{max-width:90ch}a{color:#176557;text-underline-offset:3px}nav{font:14px/1.5 system-ui;display:flex;flex-wrap:wrap;gap:10px 22px;padding-bottom:22px;border-bottom:1px solid #cad5cb}.table-wrap{overflow:auto;margin:25px 0}table{border-collapse:collapse;min-width:680px;width:100%;font:14px/1.55 system-ui}td,th{padding:12px;text-align:left;vertical-align:top;border-bottom:1px solid #cbd6cd}th{background:#dce6dc}tbody tr:nth-child(even){background:#edf0e8}li{margin:10px 0}footer{font:13px/1.5 system-ui;border-top:1px solid #cad5cb;padding-top:20px;margin-top:50px}a:focus-visible{outline:3px solid #b87722;outline-offset:3px}@media(max-width:640px){main{padding:25px 18px}h2{font-size:24px}}@media print{body{background:white;font-size:10pt}header,nav{display:none}main{max-width:none;padding:0}.table-wrap{overflow:visible}table{min-width:0;font-size:8pt}tr{break-inside:avoid}h2,h3{break-after:avoid}a{color:inherit}}'''
for stem,title in [('regional-comparison','Malaysia and its neighbours: MSME reform'),('essay-outlines','Three essay outlines: MSME reform')]:
 md=(ROOT/'to_human'/f'{stem}.md').read_text(encoding='utf-8');body=render_md(md)
 nav=''.join(f'<a href="#{m[1]}">{m[2]}</a>' for m in re.finditer(r'<h2 id="([^"]+)">(.+?)</h2>',body))
 page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+style+'</style></head><body><header>MSME SUPPORT · REGIONAL COMPARISON<br>Prepared for Meor · 19 October 2026 · Unpublished</header><main><nav aria-label="Contents">'+nav+'</nav>'+body+'<footer>Exploratory desk research and working outlines. No publication or author approval recorded. Reported benefits, forecasts, costs and verified savings remain distinct.</footer></main></body></html>'
 (ROOT/'to_human'/f'{stem}.html').write_text(page,encoding='utf-8')

ids={s['id'] for s in sources}
assert all(set(c['source_ids'])<=ids for c in claims)
assert all(c['government_net_saving'] is None for c in cases)
assert abs(187300000+139200000-326500000)<.01
assert abs(5472000-5418423.72-53576.28)<.001
assert abs(central['three_year_net_rm_million']+3.44187225)<1e-8
assert abs(ledger[-1]['amount']-1058127.75)<.001
assert all(not x['government_merger_saving'] for x in ledger)
print(json.dumps(dict(sources=len(sources),claims=len(claims),reform_cases=len(cases),money_records=len(ledger),outlines=3,arithmetic_and_source_ids='passed',published=False),indent=2))
