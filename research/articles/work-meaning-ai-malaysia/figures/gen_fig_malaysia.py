"""Plot published Malaysian values verbatim; no AI-effect estimation."""
from pathlib import Path
import sys, os, csv, json
folder=Path(__file__).resolve().parent
root=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(root/'.tools/research-figure/python-packages'))
os.environ.setdefault('MPLCONFIGDIR',str(root/'.tools/research-figure/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
BG,INK,MUTED='#fbf9f4','#26352e','#526055'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':INK,
    'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':INK,
    'figure.facecolor':BG,'axes.facecolor':BG,'pdf.fonttype':42,'svg.fonttype':'none'})
def save(fig,stem):
    for ext in ('png','pdf','svg'):fig.savefig(folder/f'{stem}.{ext}',dpi=300,facecolor=BG)
    plt.close(fig)
def axis(ax):
    for spine in ax.spines.values():spine.set_visible(False)
    ax.tick_params(axis='y',length=0)
    ax.set_axisbelow(True)
    ax.grid(axis='x',alpha=.15)
    ax.xaxis.set_major_formatter(PercentFormatter(100,decimals=0))
with (folder/'malaysia-ai-exposure.csv').open(newline='',encoding='utf-8') as f:data=list(csv.DictReader(f))
fig=plt.figure(figsize=(12,9))
fig.text(.065,.945,'MALAYSIA  /  IMF EXPOSURE ESTIMATES',fontsize=10,weight='bold',color=MUTED)
fig.text(.065,.885,'AI could help some roles and disrupt others',fontsize=23,weight='bold')
fig.text(.065,.835,'Modelled task exposure using employment data extrapolated to 2018; published in 2025.',fontsize=11,color=MUTED)
axes=[fig.add_axes([.40,.49,.52,.23]),fig.add_axes([.40,.16,.52,.23])]
for ax,rows,title in zip(axes,[data[:2],data[2:]],['Share of all employed people','High exposure + low complementarity, by sex']):
    vals=[float(r['percent']) for r in rows]
    labels=[r['category'].replace(' / ',' /\n') for r in rows]
    ax.barh([1,0],vals,color=['#D55E00','#0072B2'],height=.48)
    ax.set_yticks([1,0],labels)
    ax.set_xlim(0,50);ax.set_xticks([0,10,20,30,40,50]);axis(ax)
    ax.set_title(title,loc='left',fontsize=13,pad=18,weight='bold')
    for y,v in zip([1,0],vals):ax.text(v+.7,y,f'{v:g}%',va='center',weight='bold')
axes[0].set_xlabel('Denominator: all employed people',fontsize=10)
axes[1].set_xlabel('Denominator: employed people within each sex',fontsize=10)
fig.text(.065,.055,'Exposure is not adoption, retrenchment, or a probability of job loss.',fontsize=12,weight='bold')
fig.text(.065,.023,'Source: IMF Country Report 25/57, Annex IV, paragraphs 7–10. Published rounded values; no re-estimation.',fontsize=9,color=MUTED)
save(fig,'malaysia-ai-exposure')
with (folder/'malaysia-income-shares.csv').open(newline='',encoding='utf-8') as f:income=list(csv.DictReader(f))
fig=plt.figure(figsize=(12,8))
fig.text(.065,.94,'MALAYSIA  /  NATIONAL INCOME ACCOUNTS',fontsize=10,weight='bold',color=MUTED)
fig.text(.065,.875,'How Malaysia’s GDP is distributed as income',fontsize=23,weight='bold')
fig.text(.065,.82,'Employee compensation: 33.6% in 2024 → 33.9% in 2025 (+0.3 percentage point).',fontsize=12,color=MUTED)
ax=fig.add_axes([.12,.37,.79,.34]);left=[0,0]
for key,label,color in [('compensation_of_employees','Employee compensation','#0072B2'),('gross_operating_surplus','Gross operating surplus*','#E69F00'),('net_taxes','Net taxes','#777777')]:
    vals=[float(r[key]) for r in income]
    ax.barh([1,0],vals,left=left,label=label,color=color,height=.48,edgecolor=BG,linewidth=1)
    for i,(v,l) in enumerate(zip(vals,left)):
        if key=='net_taxes':
            ax.annotate(f'{v:.1f}%',xy=(l+v/2,1-i+.25),xytext=(l+v/2,1-i+.37),
                        ha='center',va='bottom',fontsize=10,color=INK,weight='bold',
                        arrowprops={'arrowstyle':'-','color':MUTED,'lw':.8})
        else:
            ax.text(l+v/2,1-i,f'{v:.1f}%',ha='center',va='center',fontsize=10,
                    color='white' if key!='gross_operating_surplus' else INK,weight='bold')
    left=[a+b for a,b in zip(left,vals)]
assert all(abs(x-100)<.01 for x in left)
ax.set_yticks([1,0],[r['year'] for r in income]);ax.set_xlim(0,100);axis(ax)
ax.set_xlabel('Share of nominal GDP');ax.legend(loc='upper left',bbox_to_anchor=(-.01,-.25),ncol=3,frameon=False,fontsize=10)
fig.text(.065,.18,'*Includes mixed income and depreciation; it is not simply corporate profit or owners’ take-home income.',fontsize=11,color=MUTED)
fig.text(.065,.12,'This is an economic baseline. The chart does not measure AI’s effect on wages or profits.',fontsize=12,weight='bold')
fig.text(.065,.055,'Sources: DOSM, GDP Income Approach 2025, overview and technical notes. Published percentages plotted verbatim.',fontsize=9,color=MUTED)
save(fig,'malaysia-income-shares')
(folder/'malaysia-plot-environment.json').write_text(json.dumps({'python':sys.version.split()[0],
    'matplotlib':matplotlib.__version__,'method':'Published rounded percentages; no causal estimation or forecasting.',
    'inputs':['malaysia-ai-exposure.csv','malaysia-income-shares.csv'],
    'created_on':'2026-10-21'},indent=2)+'\n',encoding='utf-8')
print('Rendered two Malaysia data charts in PNG, PDF and SVG.')
