"""Rebuild three data figures as 300 dpi PNG and vector PDF, plus CSV equivalents.

Run with matplotlib available. All figures use preserved input snapshots.
The institutional quadrant is a categorical matrix, not an invented numerical index.
"""
from pathlib import Path
import csv
import json
import math
import shutil
import sys

ROOT = Path(__file__).resolve().parents[4]
local_deps = ROOT / '.cache/msme-plot-deps'
if local_deps.exists():
    sys.path.insert(0, str(local_deps))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter

PACKET = Path(__file__).resolve().parents[1]
DATA = PACKET / 'data'
BUNDLE = ROOT / 'site/content/posts/can-malaysia-merge-msme-support'
FIGURES = PACKET / 'figures'
FIGURES.mkdir(exist_ok=True)
agencies = json.loads((DATA / 'agencies.json').read_text(encoding='utf-8'))
model = json.loads((DATA / 'savings-model.json').read_text(encoding='utf-8'))

INK = '#253839'
PAPER = '#FBFAF6'
BLUE = '#0072B2'
ORANGE = '#D55E00'
GREEN = '#009E73'
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':12,
                     'text.color':INK, 'axes.labelcolor':INK,
                     'xtick.color':INK, 'ytick.color':INK,
                     'figure.facecolor':PAPER, 'axes.facecolor':PAPER,
                     'axes.spines.top':False, 'axes.spines.right':False,
                     'axes.spines.left':False, 'axes.spines.bottom':False,
                     'pdf.fonttype':42, 'savefig.dpi':300})

def save(fig, name):
    for extension in ['png','pdf']:
        path = FIGURES / f'{name}.{extension}'
        fig.savefig(path, dpi=300, facecolor=PAPER)
        shutil.copy2(path, BUNDLE / path.name)
    plt.close(fig)

# 1. Reported performance: numerical source scores, all eleven selected scored bodies.
scored = sorted([a for a in agencies if a['performance_score'] is not None],
                key=lambda a: (-a['performance_score'], a['name']))
fig, ax = plt.subplots(figsize=(10,8.1))
fig.subplots_adjust(left=.19,right=.93,top=.77,bottom=.18)
fig.text(.055,.945,'A programme score is one part of the decision',fontsize=20,weight='bold')
fig.text(.055,.898,'Reported 2024 MSME programme performance · selected institutions',fontsize=12)
fig.text(.055,.851,'Meets or exceeds: 8     |     Below threshold: 3',fontsize=12,weight='bold')
scores = [a['performance_score'] for a in scored]
ax.barh(range(len(scored)),scores,height=.58,
        color=[BLUE if value>=70 else ORANGE for value in scores],zorder=3)
ax.set_yticks(range(len(scored)),[a['name'] for a in scored])
ax.invert_yaxis()
ax.set_xlim(0,105)
ax.set_xticks([0,20,40,60,80,100])
ax.set_xlabel('IAFSP score (points, not percent)',labelpad=12)
ax.grid(axis='x',alpha=.16,zorder=0)
ax.axvline(70,color=INK,linestyle='--',linewidth=1.4,zorder=4)
ax.text(70,-.85,'70: meeting threshold',fontsize=10,ha='center')
for n,value in enumerate(scores):
    ax.text(value+1.2,n,f'{value:.1f}',va='center',fontsize=11,weight='bold',
            zorder=6,bbox=dict(facecolor=PAPER,edgecolor='none',pad=1.2))
ax.tick_params(axis='both',length=0,pad=7)
fig.text(.055,.085,'Source: SME Corp, SMEIPA 2025, agency profiles and framework.',fontsize=10)
fig.text(.055,.053,'Scope: measured MSME programmes, not whole-agency KPIs or causal impact.',fontsize=10)
fig.text(.055,.021,'SKM and TERAJU: comparable scores not established in this review; not scored zero.',fontsize=10)
save(fig,'programme-performance')

# 2. Recompute annual and cumulative outcomes from the underlying assumptions.
with (DATA/'savings-assumptions.csv').open(encoding='utf-8-sig') as handle:
    assumptions=list(csv.DictReader(handle))
rows=[]
computed={}
for s in model['scenarios']:
    gross=sum(float(a['baseline_rm_million'])*float(a['assumed_addressable_share'])*float(a['assumed_retired_share'])
              for a in assumptions if a['scenario']==s['scenario'])
    assert math.isclose(gross,s['gross_annual_rm_million'],abs_tol=1e-9)
    cumulative=0.0
    values=[0.0]
    for year,rollout in enumerate(model['rollout'],start=1):
        transition=s['transition_once_rm_million'] if year==1 else 0.0
        annual=gross*rollout-s['incremental_annual_rm_million']-transition
        assert math.isclose(annual,s[f'year{year}_net_rm_million'],abs_tol=1e-9)
        cumulative+=annual
        values.append(cumulative)
        rows.append(dict(scenario=s['scenario'],year=year,rollout_share=rollout,
                         gross_realised_rm_million=round(gross*rollout,9),
                         new_recurring_rm_million=s['incremental_annual_rm_million'],
                         transition_rm_million=transition,
                         annual_net_rm_million=round(annual,9),
                         cumulative_net_rm_million=round(cumulative,9),
                         status='Illustrative planning case, not a forecast or observed saving'))
    assert math.isclose(cumulative,s['three_year_net_rm_million'],abs_tol=1e-9)
    computed[s['scenario']]=values
with (DATA/'savings-scenarios.csv').open('w',encoding='utf-8',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=list(rows[0]))
    writer.writeheader(); writer.writerows(rows)
shutil.copy2(DATA/'savings-scenarios.csv',BUNDLE/'savings-scenarios.csv')

fig,ax=plt.subplots(figsize=(10,7.1))
fig.subplots_adjust(left=.11,right=.75,top=.78,bottom=.25)
fig.text(.055,.94,'Savings depend on retiring actual costs',fontsize=20,weight='bold')
fig.text(.055,.888,'Illustrative cumulative net government savings · RM million, nominal',fontsize=12)
fig.text(.055,.842,'Planning cases, not forecasts or probability ranges',fontsize=11,weight='bold')
styles=[('low',ORANGE,'--','s'),('central',BLUE,'-','o'),('high',GREEN,'-.','^')]
for name,color,line,marker in styles:
    values=computed[name]
    ax.plot([0,1,2,3],values,color=color,linestyle=line,marker=marker,
            linewidth=2.6 if name=='central' else 1.8,markersize=6,clip_on=False)
    ax.annotate(f'{name.title()}  {values[-1]:+.2f}',xy=(3,values[-1]),
                xytext=(12,0),textcoords='offset points',va='center',color=color,
                weight='bold',fontsize=12)
ax.axhline(0,color=INK,linewidth=1)
ax.set_ylim(-10.5,5.2)
ax.set_xlim(-.06,3.05)
ax.set_xticks([0,1,2,3],['Before rollout','Year 1','Year 2','Year 3'])
ax.set_yticks([-10,-5,0,5])
ax.yaxis.set_major_formatter(FuncFormatter(lambda x,_:f'{x:+.0f}' if x else '0'))
ax.grid(axis='y',alpha=.18)
ax.tick_params(length=0,pad=8)
fig.text(.055,.14,'Central case at maturity: RM2.78m retired − RM1.50m new recurring cost = RM1.28m/year.',fontsize=10)
fig.text(.055,.105,'All cases: 25% / 75% / 100% gross-benefit rollout; recurring costs begin in year 1.',fontsize=10)
fig.text(.055,.07,'Transition costs in year 1: low RM6m, central RM4.5m, high RM3m. No discounting.',fontsize=10)
fig.text(.055,.035,'Source: proposed 2027 KUSKOP budget anchors and explicit analyst assumptions; full data accompany essay.',fontsize=9)
save(fig,'savings-scenarios')

# 3. A two-dimensional categorical matrix. No numeric institutional relevance is asserted.
fig,ax=plt.subplots(figsize=(10,8.6))
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
fig.text(.055,.952,'Two separate questions for an agency review',fontsize=20,weight='bold')
fig.text(.055,.907,'Institutional distinctiveness: analyst judgment · Performance: reported 2024 programme score',fontsize=10.5)
fig.text(.055,.872,'No numeric relevance rating or whole-agency failure label is assigned.',fontsize=11)
left=.22; right=.61; width=.345
top=.48; lower=.17; height=.285
ax.text(left+width/2,.815,'REVIEW STANDALONE\nADMINISTRATION',ha='center',va='center',fontsize=11,weight='bold',linespacing=1.5)
ax.text(right+width/2,.815,'STRONGER CASE TO RETAIN\nA DISTINCT INSTITUTION',ha='center',va='center',fontsize=10.5,weight='bold',linespacing=1.5)
ax.text(.04,top+height/2,'MEETS OR\nEXCEEDS\n70 points',va='center',fontsize=10.5,weight='bold',linespacing=1.5)
ax.text(.04,lower+height/2,'BELOW\n70 points',va='center',fontsize=10.5,weight='bold',linespacing=1.5)
groups={('transfer',True):[],('retain',True):[],('transfer',False):[],('retain',False):[]}
for a in agencies:
    if a['performance_score'] is not None:
        groups[(a['institution_case'],a['performance_score']>=70)].append(a)
for category,x in [('transfer',left),('retain',right)]:
    for meets,y in [(True,top),(False,lower)]:
        fill='#EAF2F6' if meets else '#F6EDE5'
        ax.add_patch(Rectangle((x,y),width,height,facecolor=fill,edgecolor='#D5D8D3',linewidth=.8))
        group=sorted(groups[(category,meets)],key=lambda a:-a['performance_score'])
        if group:
            for n,a in enumerate(group):
                ax.text(x+.022,y+height-.047-n*.047,f"{a['name']}  {a['performance_score']:.1f}",fontsize=12,va='top')
        else:
            ax.text(x+.022,y+height-.05,'No selected institution',fontsize=11,va='top',weight='bold')
            ax.text(x+.022,y+height-.115,'No case established in\nthis selected review.',fontsize=10.5,va='top',linespacing=1.6)
fig.text(.055,.09,'Unplaced: SKM and TERAJU — comparable programme scores not established here.',fontsize=10.5)
fig.text(.055,.055,'Source: SMEIPA 2025 scores; mandate and budget review. CGC is a public-linked guarantee institution.',fontsize=9.5)
fig.text(.055,.022,'Transfer review is conditional. Distinct functions may remain useful even when a programme underperforms.',fontsize=9.5)
save(fig,'agency-quadrant')
print('Built three figures in PNG (300 dpi) and vector PDF; scenario arithmetic reconciled to preserved inputs.')
