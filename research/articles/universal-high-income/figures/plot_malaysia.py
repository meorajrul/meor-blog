"""Plot published administrative figures; no simulated inputs or projections."""
from pathlib import Path
import csv,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
bundle=p.parents[3]/'site/content/posts/universal-high-income'
# p = research/articles/<slug>/figures; parents[3] is workspace root.
bundle.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.labelsize':13,
'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,
'axes.edgecolor':'#b8bdb9','text.color':'#23382e','axes.labelcolor':'#23382e',
'xtick.color':'#526055','ytick.color':'#23382e','savefig.facecolor':'#fcfbf6','figure.facecolor':'#fcfbf6',
'svg.fonttype':'none','savefig.bbox':'tight','savefig.pad_inches':0.25})
def rows(name):return list(csv.DictReader((p/name).open()))
def base(title,subtitle):
 f,ax=plt.subplots(figsize=(10.8,5.4));f.subplots_adjust(left=.27,right=.94,top=.73,bottom=.24)
 f.text(.04,.94,title,fontsize=22,fontweight='bold',va='top')
 f.text(.04,.84,subtitle,fontsize=13,color='#526055',va='top')
 ax.set_axisbelow(True);ax.grid(axis='x',alpha=.18);ax.tick_params(axis='both',length=0,pad=10)
 return f,ax
def save(f,name,foot):
 f.text(.04,.07,foot,fontsize=11,color='#526055',va='bottom')
 for ext in ('png','pdf','svg'):
  target=p/(name+'.'+ext);f.savefig(target,dpi=300);shutil.copyfile(target,bundle/target.name)
 plt.close(f)
r=rows('sara-usage-2025.csv'); f,ax=base('Reported use of SARA credits in 2025','2025 administrative figures reported in Parliament on 5 February 2026')
y=[1,0];v=[float(a['reported_user_share_pct']) for a in r]
ax.barh(y,v,height=.5,color=['#0072B2','#009E73']);ax.set_yticks(y,[a['programme'] for a in r]);ax.set_xlim(0,108);ax.set_xticks([0,25,50,75,100]);ax.set_xlabel('Recipients reported to have used credits (%)')
for i,val in zip(y,v):ax.text(val+1,i,f'{val:.0f}%',va='center',fontsize=17,fontweight='bold')
save(f,'sara-usage-2025','Separate programme denominators. Reported rounded rates; not poverty or exclusion rates.\nSource: Dewan Rakyat Hansard, 5 February 2026, printed p. 2 (PDF p. 10).')
r=rows('sara-monthly-spending-2025.csv');f,ax=base('Monthly SARA: allocation and purchases','Monthly SARA programme, 2025 · reported amounts in RM billion')
v=[float(a['rm_billion']) for a in r];ax.barh(y,v,height=.5,color=['#9aa7ad','#0072B2']);ax.set_yticks(y,['Allocation','Purchases']);ax.set_xlim(0,5.7);ax.set_xticks([0,1,2,3,4,5]);ax.set_xlabel('RM billion')
for i,val in zip(y,v):ax.text(val+.1,i,f'{val:g}',va='center',fontsize=17,fontweight='bold')
save(f,'sara-monthly-spending-2025','Transaction value is not additional output or an estimated economic multiplier.\nSource: Dewan Rakyat Hansard, 5 February 2026, printed p. 2 (PDF p. 10).')
r=rows('str-sara-allocations.csv');f,ax=base('STR and SARA: 2026 and announced 2027 allocations','Combined STR and SARA · announced allocations, not actual spending')
v=[float(a['rm_billion']) for a in r];bars=ax.barh(y,v,height=.5,color=['#0072B2','#ffffff'],edgecolor=['#0072B2','#D55E00'],linewidth=1.8);bars[1].set_hatch('///')
ax.set_yticks(y,['2026 allocation','2027 announced\nallocation']);ax.set_xlim(0,18.3);ax.set_xticks([0,4,8,12,16]);ax.set_xlabel('RM billion')
for i,val in zip(y,v):ax.text(val+.25,i,f'{val:g}',va='center',fontsize=17,fontweight='bold')
save(f,'str-sara-allocations','2027 was announced on 9 October 2026; its design differs from 2026.\nSources: MOF, 15 August 2026; Budget 2027 speech, paragraph 26.')
for name in ('sara-usage-2025.csv','sara-monthly-spending-2025.csv','str-sara-allocations.csv'):shutil.copyfile(p/name,bundle/name)
print('Exported 3 charts in PNG, SVG and PDF; copied the 3 source CSVs to the article bundle.')
