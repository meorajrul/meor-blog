from pathlib import Path
import sys,os,csv,json,shutil
root=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(root/'.tools/research-figure/python-packages'))
os.environ.setdefault('MPLCONFIGDIR',str(root/'.tools/research-figure/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
folder=Path(__file__).resolve().parent
bundle=root/'site/content/posts/ai-beginner-work-malaysia'
BG,INK,MUTED='#FBF9F4','#272A26','#626D63'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':INK,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.spines.bottom':False,'pdf.fonttype':42})
def csvsave(name,fields,rows):
    with (folder/(name+'.csv')).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(fields);w.writerows(rows)
    shutil.copyfile(folder/(name+'.csv'),bundle/(name+'.csv'))
def export(fig,name):
    fig.savefig(bundle/(name+'.png'),dpi=300,facecolor=BG)
    fig.savefig(folder/(name+'.pdf'),facecolor=BG)
    plt.close(fig)
name='us-young-worker-employment'
csvsave(name,['exposure_group','employment_change_percent_approx','age','start','end','source'],[
 ['Top two quintiles',-11,'22-25','2022-11','2026-06','Stanford Canaries August 2026, printed p3'],
 ['Bottom three quintiles',10,'22-25','2022-11','2026-06','Stanford Canaries August 2026, printed p3']])
fig=plt.figure(figsize=(11.6,6.8),facecolor=BG)
fig.text(.055,.925,'Young-worker employment diverged in this US sample',fontsize=22,weight='bold')
fig.text(.055,.855,'Ages 22–25 · November 2022 to June 2026 · ADP payroll panel',fontsize=15,color=MUTED)
ax=fig.add_axes([.30,.32,.63,.39],facecolor=BG)
values=[-11,10]
ax.barh([0,1],values,height=.48,color=['#D55E00','#0072B2'],zorder=3)
ax.set_yticks([0,1],['More AI-exposed\nTop two quintiles','Less AI-exposed\nBottom three quintiles']);ax.invert_yaxis()
ax.set_xlim(-16,16);ax.set_xticks([-15,-10,-5,0,5,10,15]);ax.set_xticklabels(['−15','−10','−5','0','+5','+10','+15'])
ax.tick_params(axis='both',length=0,pad=12);ax.grid(axis='x',color='#DEE2D8',lw=.8,zorder=0)
ax.axvline(0,color='#626D63',lw=1.1,zorder=2)
for y,v in enumerate(values): ax.text(v+(-.7 if v<0 else .7),y,('≈ −11%' if v<0 else '≈ +10%'),ha='right' if v<0 else 'left',va='center',fontsize=17,weight='bold')
ax.set_xlabel('Employment change (%)',fontsize=14,labelpad=10)
fig.text(.055,.16,'Descriptive changes; not a causal AI estimate or a graduate-only sample.',fontsize=13,color=MUTED)
fig.text(.055,.102,'Quintiles rank occupations by AI exposure. Values are approximate.',fontsize=13,color=MUTED)
fig.text(.055,.045,'Source: Brynjolfsson, Chandar & Chen, Canaries in the Coal Mine, August 2026.',fontsize=12,color=MUTED)
export(fig,name)
name='singapore-ai-employer-responses'
labels=['Redesigned roles','Created AI-related jobs','Lowered hiring','Reduced headcount'];values=[19,14,8,6]
csvsave(name,['reported_response','share_of_ai_adopting_firms_percent','reported_on','survey_fieldwork','source'],[[l,v,'2026-08-05','Not specified in cited parliamentary answer','Singapore MOM, answer paragraph 2'] for l,v in zip(labels,values)])
fig=plt.figure(figsize=(11.6,6.8),facecolor=BG)
fig.text(.055,.925,'Singapore firms reported more redesign than cuts',fontsize=22,weight='bold')
fig.text(.055,.855,'Among firms adopting AI · Reported by MOM on 5 August 2026',fontsize=15,color=MUTED)
ax=fig.add_axes([.30,.31,.61,.43],facecolor=BG)
ax.barh(range(4),values,height=.5,color=['#0072B2','#0072B2','#D55E00','#D55E00'],zorder=3)
ax.set_yticks(range(4),labels);ax.invert_yaxis();ax.set_xlim(0,23);ax.set_xticks([0,5,10,15,20]);ax.tick_params(axis='both',length=0,pad=12)
ax.grid(axis='x',color='#DEE2D8',lw=.8,zorder=0)
for y,v in enumerate(values): ax.text(v+.5,y,f'{v}%',va='center',fontsize=16,weight='bold')
ax.set_xlabel('Share of AI-adopting firms (%)',fontsize=14,labelpad=10)
fig.text(.055,.16,'Firm responses, not shares of workers. Categories must not be added.',fontsize=13,color=MUTED)
fig.text(.055,.102,'Survey fieldwork dates are not specified in the parliamentary answer.',fontsize=13,color=MUTED)
fig.text(.055,.045,'Source: Singapore Ministry of Manpower, Trends in Job Vacancies, answer ¶2.',fontsize=12,color=MUTED)
export(fig,name)
(folder/'first-jobs-plot-environment.json').write_text(json.dumps({'python':sys.version.split()[0],'matplotlib':matplotlib.__version__,'method':'Direct transcription of published approximate US changes and Singapore firm percentages. No interpolation, model, forecast or new uncertainty interval. Original chart artwork. Both zero baselines displayed.'},indent=2)+'\n',encoding='utf-8')
print('Created two PNG charts, vector PDFs, CSVs and environment record.')
