"""Plot published aggregate estimates; no raw observations or re-estimation.

Run with Python and matplotlib installed. This project can also use its ignored
.tools/research-figure/python-packages installation. Outputs: web PNG and vector PDF.
"""
from pathlib import Path
import csv, json, os, sys

root=Path(__file__).resolve().parents[4]
packages=root/'.tools/research-figure/python-packages'
if packages.exists(): sys.path.insert(0,str(packages))
os.environ.setdefault('MPLCONFIGDIR',str(root/'.tools/research-figure/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

folder=Path(__file__).resolve().parent
with (folder/'gps-navigation-effects.csv').open(encoding='utf-8',newline='') as f:
    rows=list(csv.DictReader(f))
expected=[(-.18,-.28,-.08),(-.25,-.39,-.12),(.07,-.28,.41)]
values=[tuple(float(row[k]) for k in ('pooled_r','ci95_lower','ci95_upper')) for row in rows]
assert values==expected
assert all(-1<=lo<=estimate<=hi<=1 for estimate,lo,hi in values)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#B5B8B3','text.color':'#272A26','axes.labelcolor':'#41463E','xtick.color':'#676D62','pdf.fonttype':42})
fig=plt.figure(figsize=(10.8,6.4),facecolor='#FBF9F4')
fig.text(.04,.93,'GPS use and navigation ability',fontsize=23,fontweight='bold')
fig.text(.04,.875,'2024 systematic review: 23 studies reviewed; 18 in the meta-analysis',fontsize=12.5,color='#676D62')
ax=fig.add_axes([.37,.32,.35,.43],facecolor='#FBF9F4')
ax.set_xlim(-.5,.5); ax.set_ylim(-.55,2.55); ax.set_yticks([])
ax.set_xticks([-.4,-.2,0,.2,.4])
ax.xaxis.set_major_formatter(FuncFormatter(lambda v,p: '0' if v==0 else f'{v:+.1f}'.replace('-', '\N{MINUS SIGN}')))
ax.tick_params(axis='x',labelsize=11,pad=8,length=0)
ax.grid(axis='x',color='#D8DDD5',linewidth=.65,zorder=0)
ax.axvline(0,color='#737C70',linewidth=1.2,linestyle=(0,(3,3)),zorder=1)
fig.text(.04,.79,'Outcome',fontsize=11.5,fontweight='bold',color='#676D62')
fig.text(.775,.79,'Pooled r [95% CI]',fontsize=11.5,fontweight='bold',color='#676D62')
for index,(row,(estimate,lo,hi)) in enumerate(zip(rows,values)):
    y=2-index
    color='#0072B2' if hi<0 or lo>0 else '#6C7567'
    ax.errorbar(estimate,y,xerr=[[estimate-lo],[hi-estimate]],fmt='o',markersize=9,color=color,ecolor=color,elinewidth=2.2,capsize=5,capthick=1.5,zorder=3)
    fy=.32+((y+.55)/3.1)*.43
    fig.text(.04,fy+.008,row['outcome'],fontsize=14,fontweight='medium',va='center')
    fig.text(.04,fy-.035,row['plain_language_label'],fontsize=11,color='#676D62',va='center')
    number=lambda x: f'{x:.2f}'.replace('-', '\N{MINUS SIGN}')
    fig.text(.775,fy+.003,f'{number(estimate)} [{number(lo)}, {number(hi)}]',fontsize=11.2,va='center')
    if lo<=0<=hi:
        fig.text(.775,fy-.04,'Inconclusive',fontsize=10.5,color='#676D62',va='center')
ax.text(.25,-.27,'Linked to lower scores',transform=ax.transAxes,ha='center',fontsize=10.5,color='#676D62')
ax.text(.78,-.27,'Linked to higher scores',transform=ax.transAxes,ha='center',fontsize=10.5,color='#676D62')
fig.text(.04,.17,'Points: pooled correlations (r). Lines: 95% confidence intervals; not percentages.',fontsize=10.5)
fig.text(.04,.125,'Mixed study designs and substantial bias concerns; this does not establish general reasoning decline.',fontsize=10.5,color='#676D62')
fig.text(.04,.075,'Source: Miola et al. (2024), Journal of Environmental Psychology 99, 102417.',fontsize=10.5,color='#676D62')
fig.text(.04,.035,'doi.org/10.1016/j.jenvp.2024.102417  |  Original chart of published estimates; outcome samples differ.',fontsize=9.5,color='#676D62')
article=root/'site/content/posts/when-everyone-can-write-who-still-understands'
fig.savefig(article/'gps-navigation-research.png',dpi=300,facecolor=fig.get_facecolor(),metadata={'Title':'GPS use and navigation ability','Description':'Original chart of pooled estimates and confidence intervals from Miola et al. (2024); not participant data.'})
fig.savefig(folder/'gps-navigation-research.pdf',facecolor=fig.get_facecolor(),metadata={'Title':'GPS use and navigation ability','Subject':'Published pooled estimates from Miola et al. 2024; not re-estimated.'})
plt.close(fig)
(folder/'plot-environment.json').write_text(json.dumps({'python':sys.version.split()[0],'matplotlib':matplotlib.__version__,'data':'gps-navigation-effects.csv','method':'Plot rounded published pooled r and CI values verbatim. No new meta-analysis, digitization, participant simulation or conversion to percentages.'},indent=2)+'\n',encoding='utf-8')
print(article/'gps-navigation-research.png')
