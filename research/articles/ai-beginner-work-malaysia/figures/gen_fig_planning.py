"""Reproduce administrative counts and survey estimates; no demand forecasting."""
from pathlib import Path
import csv, json, os, sys, shutil
root=Path(__file__).resolve().parents[4]
packages=root/'.tools/research-figure/python-packages'
if packages.exists(): sys.path.insert(0,str(packages))
os.environ.setdefault('MPLCONFIGDIR',str(root/'.tools/research-figure/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
folder=Path(__file__).resolve().parent
bundle=root/'site/content/posts/ai-beginner-work-malaysia'
BG,INK,MUTED,BLUE='#FBF9F4','#272A26','#626D63','#0072B2'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':INK,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#BEC5BB','pdf.fonttype':42})
def rows(name):
 with (folder/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def save(fig,name):
 fig.savefig(bundle/(name+'.png'),dpi=300,facecolor=BG)
 fig.savefig(folder/(name+'.pdf'),facecolor=BG)
 plt.close(fig)
 shutil.copyfile(folder/(name+'.csv'),bundle/(name+'.csv'))

china=rows('china-programme-changes.csv')
values=[int(r['programme_offerings']) for r in china]
assert values==[1839,2220,1428,157]
fig=plt.figure(figsize=(12,7.4),facecolor=BG)
fig.text(.055,.935,'China is changing its education provision',fontsize=24,weight='bold')
fig.text(.055,.875,'2024 undergraduate programme decisions • announced April 2025',fontsize=15,color=MUTED)
ax=fig.add_axes([.285,.27,.60,.49],facecolor=BG)
labels=['Added','Admissions stopped','Withdrawn','Degree category or\nduration changed']
bars=ax.barh(np.arange(4),values,height=.52,color=BLUE,zorder=3)
for bar,v in zip(bars,values):ax.text(v+45,bar.get_y()+bar.get_height()/2,f'{v:,}',va='center',weight='bold',fontsize=17)
ax.set_yticks(np.arange(4),labels);ax.invert_yaxis();ax.set_xlim(0,2600)
ax.set_xticks([0,500,1000,1500,2000,2500],['0','500','1,000','1,500','2,000','2,500'])
ax.tick_params(axis='both',length=0,pad=10);ax.grid(axis='x',color='#DEE2D8',lw=.8,zorder=0)
ax.set_xlabel('Institution-level programme offerings',labelpad=12,fontsize=15)
fig.text(.055,.13,'Administrative changes; these counts do not measure jobs or reduced shortages.',fontsize=13,color=MUTED)
fig.text(.055,.065,'Source: China Ministry of Education, 22 April 2025. Original chart; no forecast.',fontsize=12,color=MUTED)
save(fig,'china-programme-changes')

malaysia=rows('malaysia-vacancies-q2-2026.csv')
values=[float(r['vacancies_thousands']) for r in malaysia]
assert values==[107.3,50.2,38.2] and round(sum(values),1)==195.7
fig=plt.figure(figsize=(10.8,6.9),facecolor=BG)
fig.text(.055,.93,'Malaysia: vacancies already recorded',fontsize=24,weight='bold')
fig.text(.055,.865,'Q2 2026 • registered private-sector businesses covered by the survey',fontsize=14,color=MUTED)
ax=fig.add_axes([.19,.29,.68,.45],facecolor=BG)
bars=ax.barh(np.arange(3),values,height=.5,color=BLUE,zorder=3)
for bar,v in zip(bars,values):ax.text(v+2.2,bar.get_y()+bar.get_height()/2,f'{v:.1f}',va='center',fontsize=18,weight='bold')
ax.set_yticks(np.arange(3),[r['skill_category'] for r in malaysia]);ax.invert_yaxis();ax.set_xlim(0,130)
ax.set_xticks([0,20,40,60,80,100,120]);ax.tick_params(axis='both',length=0,pad=10)
ax.grid(axis='x',color='#DEE2D8',lw=.8,zorder=0);ax.set_xlabel('Vacancies (thousands)',labelpad=12,fontsize=15)
fig.text(.055,.16,'Survey estimates. Skill groups are not counts of TVET or first-job openings.',fontsize=12.5,color=MUTED)
fig.text(.055,.105,'Total: 195.7 thousand. Values rounded to the nearest hundred; no forecast.',fontsize=12.5,color=MUTED)
fig.text(.055,.045,'Source: DOSM, Employment Statistics, Q2 2026, released 13 August 2026.',fontsize=12,color=MUTED)
save(fig,'malaysia-vacancies-q2-2026')
(folder/'planning-plot-environment.json').write_text(json.dumps({'python':sys.version.split()[0],'matplotlib':matplotlib.__version__,'numpy':np.__version__,'method':'Direct transcription of published administrative counts and rounded survey estimates. No interpolation, forecast, causal model or invented counterfactual.','source_checks':'MOE 2024-round announcement inspected via official hudong mirror; DOSM full release overview directly downloaded and inspected.'},indent=2)+'\n',encoding='utf-8')
print('Created two PNG charts, two vector PDFs and CSV downloads.')
