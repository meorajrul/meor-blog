"""Plot observed NVD publication counts; no interpolation or forecast.
Run fetch_cve_data.py first. Raw API totalResults are the observed inputs.
"""
from pathlib import Path
import json,csv,itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter,MaxNLocator
BASE=Path(__file__).resolve().parent
OUT=BASE.parents[3]/'site/content/posts/php-ai-security-hardening'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.spines.bottom':False,'axes.labelcolor':'#303b40','text.color':'#223137','xtick.color':'#536168','ytick.color':'#536168','figure.facecolor':'#faf8f3','axes.facecolor':'#faf8f3','svg.fonttype':'none','pdf.fonttype':42})
monthly=json.loads((BASE/'monthly-counts.json').read_text());daily=json.loads((BASE/'daily-counts.json').read_text())
assert [m['month'] for m in monthly]==[f'2026-{n:02}' for n in range(1,11)]
assert [d['date_utc'] for d in daily]==[f'2026-10-{n:02}' for n in range(1,22)]
assert sum(d['count'] for d in daily)==monthly[-1]['count']
ytd=sum(m['count'] for m in monthly);october=monthly[-1]['count']
for data,name,datekey in [(monthly,'cve-monthly-2026','month'),(daily,'cve-daily-october-2026','date_utc')]:
 cumulative=0
 with (BASE/(name+'.csv')).open('w',newline='') as f:
  w=csv.writer(f);w.writerow([datekey,'published_cves','cumulative_in_period','partial_month'])
  for item in data:
   cumulative+=item['count'];w.writerow([item[datekey],item['count'],cumulative,str(item.get('partial',False)).lower()])
summary=dict(period_start_utc='2026-01-01T00:00:00.000Z',period_end_utc='2026-10-21T23:59:59.999Z',retrieval_date='2026-10-22',ytd_total=ytd,october_total=october,months=monthly,days=daily,excluded='Rejected records; CVE ID year is not a filter',method='Direct API totalResults by non-overlapping UTC publication windows; cumulative sums of observed counts; no extrapolation, severity split or AI attribution.')
(BASE/'summary.json').write_text(json.dumps(summary,indent=2))

def style(ax):
 ax.set_axisbelow(True);ax.grid(axis='y',color='#dfe3df',linewidth=.8);ax.tick_params(axis='both',length=0,pad=7);ax.yaxis.set_major_formatter(FuncFormatter(lambda x,p:f'{int(x):,}'));ax.yaxis.set_major_locator(MaxNLocator(nbins=4,integer=True))
def exports(fig,name):
 for ext in ['png','svg','pdf']:fig.savefig(OUT/f'{name}.{ext}',dpi=180,facecolor=fig.get_facecolor())
 plt.close(fig)

fig,(ax,ax2)=plt.subplots(2,1,figsize=(12,9),gridspec_kw={'height_ratios':[2.8,1],'hspace':.54});fig.subplots_adjust(left=.13,right=.96,bottom=.24,top=.72)
fig.text(.07,.94,'THE DISCLOSURE TIMELINE',fontsize=10,fontweight='bold',color='#6a7779')
fig.text(.07,.885,'2026: CVE publications by month',fontsize=23,fontweight='bold')
fig.text(.07,.835,f'{ytd:,} year to date   ·   {october:,} in October so far',fontsize=16,color='#4b6064')
vals=[m['count'] for m in monthly];bars=ax.bar(range(10),vals,color=['#56747d']*9+['#c67a2e'],width=.62)
bars[-1].set_hatch('///');bars[-1].set_edgecolor('#8c5a2b')
for b,v in zip(bars,vals):ax.text(b.get_x()+b.get_width()/2,v+max(vals)*.035,f'{v:,}',ha='center',fontsize=11,fontweight='bold')
labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct*'];ax.set_xticks(range(10),labels);ax.set_ylim(0,max(vals)*1.20);ax.set_ylabel('Published CVE records',labelpad=18);style(ax)
cumulative=list(itertools.accumulate(vals));ax2.plot(range(10),cumulative,color='#56747d',linewidth=2.5,marker='o',markersize=4);ax2.set_xticks(range(10),labels);ax2.set_ylabel('YTD total',labelpad=18);ax2.set_ylim(0,ytd*1.12);style(ax2)
fig.text(.07,.125,'* October covers 1–21 October only. Other bars are complete calendar months.',fontsize=11,color='#536168')
fig.text(.07,.085,'Source: NIST NVD API · Retrieved 22 Oct 2026 · UTC publication dates · Rejected records excluded.',fontsize=10,color='#536168')
fig.text(.07,.048,'Publication counts do not measure attacks, discovery dates, or AI involvement.',fontsize=10,color='#536168')
exports(fig,'cve-ytd-2026')

fig,(ax,ax2)=plt.subplots(2,1,figsize=(12,9),gridspec_kw={'height_ratios':[2.8,1],'hspace':.54});fig.subplots_adjust(left=.13,right=.96,bottom=.24,top=.72)
fig.text(.07,.94,'THIS MONTH, DAY BY DAY',fontsize=10,fontweight='bold',color='#6a7779')
fig.text(.07,.885,'October 2026: CVE publications',fontsize=23,fontweight='bold')
fig.text(.07,.835,f'{october:,} published records   ·   1–21 October',fontsize=16,color='#4b6064')
x=list(range(1,22));vals=[d['count'] for d in daily];ax.bar(x,vals,color='#c67a2e',width=.72);ax.set_xticks(range(1,22,2),[f'{n:02}' for n in range(1,22,2)]);ax.set_xlim(.2,21.8);ax.set_ylabel('Published CVE records',labelpad=18);style(ax)
cumulative=list(itertools.accumulate(vals));ax2.plot(x,cumulative,color='#c67a2e',linewidth=2.5);ax2.set_xticks(range(1,22,2),[f'{n:02}' for n in range(1,22,2)]);ax2.set_xlim(.2,21.8);ax2.set_ylim(0,october*1.1);ax2.set_ylabel('Month total',labelpad=18);ax2.set_xlabel('Publication day · October 2026 (UTC)',labelpad=8);style(ax2)
fig.text(.07,.125,'Bars show daily publications; the line adds them cumulatively. October is incomplete.',fontsize=11,color='#536168')
fig.text(.07,.085,'Source: NIST NVD API · Retrieved 22 Oct 2026 · Rejected records excluded · No forecast.',fontsize=10,color='#536168')
fig.text(.07,.048,'CVE publication volume does not establish how fast bugs were found or who found them.',fontsize=10,color='#536168')
exports(fig,'cve-october-2026')
print(f'{ytd:,} YTD; {october:,} October; all 21 daily counts reconcile to monthly total.')
