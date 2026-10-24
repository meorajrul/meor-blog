from pathlib import Path
import csv,sys,os,shutil,json
root=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(root/'.tools/research-figure/python-packages'))
os.environ.setdefault('MPLCONFIGDIR',str(root/'.tools/research-figure/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
folder=Path(__file__).resolve().parent
bundle=root/'site/content/posts/ai-beginner-work-malaysia'
BG,INK,MUTED,BLUE='#FBF9F4','#272A26','#626D63','#0072B2'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':INK,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#BEC5BB','pdf.fonttype':42})
def make(name,labels,counts,denominator,title,subtitle,note,table):
    assert sum(counts)==denominator
    rates=[round(c/denominator*100,1) for c in counts]
    with (folder/(name+'.csv')).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['category','graduates','denominator','percent','reference_year','table']);w.writerows(zip(labels,counts,[denominator]*len(labels),rates,[2025]*len(labels),[table]*len(labels)))
    fig=plt.figure(figsize=(11.6,6.8),facecolor=BG)
    fig.text(.055,.93,title,fontsize=24,weight='bold')
    fig.text(.055,.86,subtitle,fontsize=14,color=MUTED)
    ax=fig.add_axes([.20,.30,.69,.43],facecolor=BG)
    bars=ax.barh(range(len(labels)),rates,height=.52,color=[BLUE]+['#8B9B88']*(len(labels)-1),zorder=3)
    for bar,v,c in zip(bars,rates,counts):
        ax.text(v+1.1,bar.get_y()+bar.get_height()/2,f'{v:.1f}%  ({c:,})',va='center',fontsize=15,weight='bold')
    ax.set_yticks(range(len(labels)),labels);ax.invert_yaxis();ax.set_xlim(0,115)
    ax.set_xticks([0,20,40,60,80,100]);ax.tick_params(axis='both',length=0,pad=10)
    ax.grid(axis='x',color='#DEE2D8',lw=.8,zorder=0);ax.set_xlabel('Share of stated denominator (%)',labelpad=10,fontsize=14)
    fig.text(.055,.155,f'Denominator: {denominator:,} graduates. {note}',fontsize=12,color=MUTED)
    fig.text(.055,.098,'Status at survey time; not a measure of pay, job match or later progression.',fontsize=12,color=MUTED)
    fig.text(.055,.04,f'Source: MOHE Graduate Tracer Study 2025, Table {table}. Original chart.',fontsize=12,color=MUTED)
    fig.savefig(bundle/(name+'.png'),dpi=300,facecolor=BG)
    fig.savefig(folder/(name+'.pdf'),facecolor=BG);plt.close(fig)
    shutil.copyfile(folder/(name+'.csv'),bundle/(name+'.csv'))
make('kesuma-graduate-employment-2025',['Employed','Unemployed'],[5367,339],5706,'KESUMA graduates: employment in 2025','Malaysian graduates of KESUMA institutions in the reported labour-force group','Outside-labour-force graduates excluded.','7.1 / 7.2')
make('kesuma-graduate-position-2025',['Permanent','Contract','Temporary','Part-time'],[2501,1557,513,123],4694,'Employment does not always mean a permanent post','KESUMA graduate government and private-sector employees, 2025','Other employment categories excluded.','7.7')
(folder/'graduate-plot-environment.json').write_text(json.dumps({'python':sys.version.split()[0],'matplotlib':matplotlib.__version__,'method':'Counts transcribed directly from MOHE 2025 tables; percentage=count/row denominator*100 rounded one decimal, agrees with published percentages. No forecast or causal estimate. Source tables bilingual with English labels. Survey response rate and CI not supplied in inspected chapter.'},indent=2)+'\n',encoding='utf-8')
print('Created two graduate charts, PDFs and CSVs')
