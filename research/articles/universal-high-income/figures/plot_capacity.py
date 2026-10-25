"""Original plots of published observations; no simulated or reconstructed firm data."""
from pathlib import Path
import csv, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
b=p.parents[3]/'site/content/posts/universal-high-income'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#adb7ae','text.color':'#23382e','axes.labelcolor':'#23382e','xtick.color':'#526055','ytick.color':'#23382e','savefig.facecolor':'#fcfbf6','figure.facecolor':'#fcfbf6','svg.fonttype':'none','savefig.bbox':'tight','savefig.pad_inches':.25,'svg.hashsalt':'uhi-capacity-2026'})
def plot(name,title,subtitle,key,label,foot):
 r=list(csv.DictReader((p/(name+'.csv')).open()));f,ax=plt.subplots(figsize=(11,6));f.subplots_adjust(left=.27,right=.94,top=.72,bottom=.24)
 f.text(.04,.95,title,fontsize=22,fontweight='bold',va='top');f.text(.04,.85,subtitle,fontsize=13,color='#526055',va='top')
 v=[float(a[key]) for a in r];y=list(range(len(r)))[::-1]
 ax.barh(y,v,color=['#D55E00' if x<0 else '#0072B2' for x in v],height=.55)
 ax.set_yticks(y,[a[label] for a in r]);ax.set_axisbelow(True);ax.grid(axis='x',alpha=.18);ax.tick_params(length=0,pad=9)
 if name.startswith('productivity'):
  ax.axvline(0,color='#526055',lw=.8);ax.axvline(5.5,color='#009E73',ls='--',lw=1.4,label='National: 5.5%');ax.legend(loc='lower right',frameon=False);ax.set_xlim(-7,12);ax.set_xlabel('Year-on-year change in value added per hour (%)')
 else:ax.set_xlim(0,69);ax.set_xlabel('Share of electricity energy mix (%)')
 for i,x in zip(y,v):ax.text(x+(.3 if x>=0 else -.3),i,f'{x:g}%',va='center',ha='left' if x>=0 else 'right',fontweight='bold')
 f.text(.04,.06,foot,fontsize=11,color='#526055',va='bottom')
 for ext in ['png','pdf','svg']:
  out=p/(name+'.'+ext);f.savefig(out,dpi=300,metadata={'Creator':'Original chart from cited public numerical data'});shutil.copyfile(out,b/out.name)
 shutil.copyfile(p/(name+'.csv'),b/(name+'.csv'));plt.close(f)
plot('productivity-q2-2026','Malaysia’s productivity gains differ across sectors','Q2 2026 · hourly labour productivity · observed year-on-year growth','hourly_productivity_yoy_pct','sector','Source: DOSM, Labour Productivity Q2 2026, 20 August 2026, PDF p. 2.\nOutput per hour, not wages. The release does not identify AI’s contribution.')
plot('electricity-mix-2025','Electricity generation still relies heavily on fossil fuels','2025 · Energy Commission booklet’s Peninsular electricity summary','energy_share_pct','source','Source: Energy Commission, 2025 performance booklet, printed pp. 2 and 4.\nEnergy mix, not installed capacity. Peninsular context, not nationwide shares.')
