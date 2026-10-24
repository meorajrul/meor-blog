"""Original charts from published summaries; no microdata or causal re-estimation."""
from pathlib import Path
import csv, json, os, sys, shutil
root = Path(__file__).resolve().parents[4]
packages = root / '.tools/research-figure/python-packages'
if packages.exists(): sys.path.insert(0, str(packages))
os.environ.setdefault('MPLCONFIGDIR', str(root / '.tools/research-figure/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
folder = Path(__file__).resolve().parent
bundle = root / 'site/content/posts/ai-beginner-work-malaysia'
BG, INK, MUTED = '#FBF9F4', '#272A26', '#626D63'
BLUE, ORANGE = '#0072B2', '#D55E00'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'axes.spines.top':False,
 'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#BEC5BB',
 'text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':INK,'pdf.fonttype':42})
with (folder/'ai-learning-curve.csv').open(encoding='utf-8-sig',newline='') as f:
    learning=list(csv.DictReader(f))
assert [(float(r['months_lower']),float(r['months_upper'])) for r in learning]==[(2,2),(8,10)]
fig=plt.figure(figsize=(10.8,6.5),facecolor=BG)
fig.text(.055,.93,'Customer support: faster early learning',fontsize=24,weight='bold')
fig.text(.055,.86,'2020–21 rollout: authors’ approximate time to',fontsize=15,color=MUTED)
fig.text(.055,.815,'about 2.5 resolved issues per hour',fontsize=15,color=MUTED)
ax=fig.add_axes([.27,.33,.64,.36],facecolor=BG)
for i,row in enumerate(learning):
    lo,hi=float(row['months_lower']),float(row['months_upper'])
    color=BLUE if i==0 else ORANGE
    ax.plot([0,lo],[1-i,1-i],color='#D2D8CD',lw=2,zorder=1)
    if lo==hi:
        ax.scatter([lo],[1-i],s=180,color=color,zorder=3)
        label='About 2 months'
    else:
        ax.plot([lo,hi],[1-i,1-i],color=color,lw=9,solid_capstyle='butt',zorder=3)
        ax.plot([lo,lo],[1-i-.1,1-i+.1],color=color,lw=2)
        ax.plot([hi,hi],[1-i-.1,1-i+.1],color=color,lw=2)
        label='About 8–10 months'
    ax.text((lo+hi)/2,1-i+.22,label,ha='center',fontsize=16,weight='bold',color=color)
ax.set_yticks([1,0],['AI from joining','Without AI'])
ax.tick_params(axis='both',length=0,pad=12)
ax.set_ylim(-.4,1.6); ax.set_xlim(0,12)
ax.set_xticks([0,2,4,6,8,10,12])
ax.grid(axis='x',color='#E0E3DC',linewidth=.7)
ax.set_xlabel('Months of experience',fontsize=15,labelpad=12)
fig.text(.055,.15,'Authors’ approximate curve summaries; the range is not a confidence interval.',fontsize=12.5,color=MUTED)
fig.text(.055,.095,'Employed agents, not graduate hiring. This is not a Malaysian forecast.',fontsize=12.5,color=MUTED)
fig.text(.055,.04,'Source: Brynjolfsson, Li & Raymond (2025), QJE, section V.B.3 / Figure V.',fontsize=12,color=MUTED)
fig.savefig(bundle/'ai-learning-curve.png',dpi=300,facecolor=BG)
fig.savefig(folder/'ai-learning-curve.pdf',facecolor=BG)
plt.close(fig)
for name in ['ai-learning-curve.csv']:
    shutil.copyfile(folder/name,bundle/name)
(folder/'plot-environment.json').write_text(json.dumps({
 'python':sys.version.split()[0],'matplotlib':matplotlib.__version__,'numpy':np.__version__,
 'method':'Learning chart uses only authors narrative approximations, no graph digitization, interpolation or re-estimation.',
 'source_checks':'QJE V.B.3 and Figure V caption inspected.',
},indent=2)+'\n',encoding='utf-8')
print('Created the current learning-curve PNG, vector PDF and CSV input.')
