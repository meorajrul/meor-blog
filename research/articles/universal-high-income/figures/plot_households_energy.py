"""Observed data only. Separate productivity/wage scales; no causal comparison."""
from pathlib import Path
import csv,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent;b=p.parents[3]/'site/content/posts/universal-high-income'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False,'text.color':'#23382e','axes.labelcolor':'#23382e','figure.facecolor':'#fcfbf6','savefig.facecolor':'#fcfbf6','svg.fonttype':'none','svg.hashsalt':'uhi-household','savefig.bbox':'tight','savefig.pad_inches':.25})
def save(f,n):
 for ext in ['png','pdf','svg']:
  out=p/(n+'.'+ext);f.savefig(out,dpi=240)
  if ext=='svg':out.write_text('\n'.join(x.rstrip() for x in out.read_text().splitlines())+'\n')
  shutil.copyfile(out,b/out.name)
 shutil.copyfile(p/(n+'.csv'),b/(n+'.csv'));plt.close(f)
r=list(csv.DictReader((p/'production-and-real-wages.csv').open()));years=[int(x['year']) for x in r]
f,ax=plt.subplots(1,2,figsize=(12,5.8));f.subplots_adjust(top=.73,bottom=.28,wspace=.34)
f.text(.05,.95,'Production and purchasing power have different paths',fontsize=21,weight='bold');f.text(.05,.86,'Malaysia, 2019–2025 · separate measures, populations and price bases',fontsize=13)
for a,col,title,color in zip(ax,['output_per_hour_2015_rm','median_monthly_wage_2010_rm'],['Output per hour\nRM at 2015 prices · whole economy','Median monthly employee wage\nRM at 2010 prices · citizens + non-citizens'],['#0072B2','#009E73']):
 v=[float(x[col]) for x in r];a.plot(years,v,'o-',color=color,lw=2);a.set_title(title,fontsize=12,pad=16);a.grid(alpha=.16);a.set_xticks(years);a.tick_params(axis='x',rotation=40)
 for i in [0,1,6]:a.annotate(f'{v[i]:g}',(years[i],v[i]),xytext=(0,10),textcoords='offset points',ha='center')
 a.margins(y=.25)
f.text(.05,.08,'Sources: OpenDOSM annual productivity and real-wage CSVs, retrieved 25 October 2026.\nAxes do not start at zero. These series do not measure the share of productivity gains captured by workers.',fontsize=10)
save(f,'production-and-real-wages')
r=list(csv.DictReader((p/'data-centre-load.csv').open()));f,a=plt.subplots(figsize=(10.8,5.6));f.subplots_adjust(top=.74,bottom=.25,left=.13)
f.text(.05,.94,'Data centres are drawing more electricity',fontsize=22,weight='bold');f.text(.05,.85,'TNB-reported actual load · June 2025 to June 2026',fontsize=13)
v=[int(x['actual_load_mw']) for x in r];a.plot([x['period'] for x in r],v,'o-',color='#0072B2',lw=2.5);a.set_ylim(0,1500);a.set_ylabel('Actual load (MW)');a.grid(axis='y',alpha=.18)
for i,x in enumerate(v):a.annotate(f'{x:,}',(i,x),xytext=(0,12),textcoords='offset points',ha='center',weight='bold')
f.text(.05,.07,'Source: TNB, Analyst Briefing 2QFY2026, 28 August 2026, slide 3.\nActual load is distinct from contracted maximum demand. Data centres are not exclusively AI workloads.',fontsize=10)
save(f,'data-centre-load')
f,ax=plt.subplots(1,2,figsize=(12,5.2));f.subplots_adjust(top=.70,bottom=.27,wspace=.7,left=.16,right=.94)
f.text(.05,.94,'SARA demonstrates delivery and use',fontsize=22,weight='bold');f.text(.05,.84,'2025 administrative figures · two different measures',fontsize=13)
ax[0].barh([1,0],[99,96],color=['#0072B2','#009E73']);ax[0].set_yticks([1,0],['Monthly','One-off']);ax[0].set_xlim(0,115);ax[0].set_xlabel('Recipients who used credits (%)')
ax[1].barh([1,0],[5,4.8],color=['#9aa7ad','#0072B2']);ax[1].set_yticks([1,0],['Allocation','Purchases']);ax[1].set_xlim(0,5.8);ax[1].set_xlabel('Monthly SARA only (RM billion)')
for a,vals in zip(ax,[[99,96],[5,4.8]]):
 a.grid(axis='x',alpha=.15);a.set_axisbelow(True)
 for y,x in zip([1,0],vals):a.text(x+max(vals)*.025,y,f'{x:g}',va='center',weight='bold')
f.text(.05,.06,'Source: Dewan Rakyat, 5 February 2026, printed p. 2. Separate recipient denominators.\nPurchases are transaction values; neither panel estimates poverty reduction or additional output.',fontsize=10)
save(f,'sara-delivery')
