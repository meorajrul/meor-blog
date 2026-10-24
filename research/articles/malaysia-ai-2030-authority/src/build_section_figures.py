from pathlib import Path
import json, textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[4]
PACKET = ROOT / 'research/articles/malaysia-ai-2030-authority'
OUT = ROOT / 'site/content/posts/malaysia-ai-2030-authority'
SPECS = json.loads((PACKET / 'data/section-figures.json').read_text(encoding='utf-8'))
BG, INK, MUTED, TEAL, GOLD, CARD = '#f5f2e9', '#142f38', '#52636a', '#177e89', '#b36b35', '#e8e9df'
plt.rcParams.update({'font.family':'DejaVu Sans', 'text.color':INK, 'axes.labelcolor':MUTED, 'xtick.color':MUTED, 'ytick.color':INK})

def wrap(s, width):
    return '\n'.join(textwrap.wrap(s, width=width, break_long_words=False))

for spec in SPECS:
    fig = plt.figure(figsize=(12, 6.2), dpi=160, facecolor=BG)
    base = fig.add_axes([0,0,1,1]); base.set_axis_off()
    base.text(.055,.93,spec['eyebrow'],size=11,weight='bold',color=TEAL,va='top')
    base.text(.055,.865,wrap(spec['title'],62),size=23,weight='bold',va='top',linespacing=1.15)
    base.plot([.055,.945],[.16,.16],color='#c7cfc8',lw=.8,transform=base.transAxes)
    base.text(.055,.125,wrap(spec['footer'],105),size=10.5,va='top',color=MUTED)
    base.text(.055,.045,wrap('SOURCE: '+', '.join(spec['source_ids'])+' | '+spec['locator'],125),size=9,va='bottom',color=MUTED)
    base.set_xlim(0,1);base.set_ylim(0,1)
    if spec['type']=='bar':
        ax=fig.add_axes([.30,.31,.59,.36], facecolor=BG)
        vals=spec['values']; labels=[wrap(s,23) for s in spec['labels']]
        ax.barh(range(len(vals)), vals, color=[TEAL,GOLD],height=.43)
        ax.set_yticks(range(len(vals)),labels=labels,size=12)
        ax.invert_yaxis(); ax.set_xlim(0,max(vals)*1.30)
        ax.set_xlabel(spec['unit'],size=11,labelpad=12)
        ax.spines[['top','right','left']].set_visible(False)
        ax.spines['bottom'].set_color('#bec9c4');ax.tick_params(axis='y',length=0,pad=12)
        ax.grid(axis='x',color='#dce1d9',zorder=0);ax.set_axisbelow(True)
        if max(vals)<=40: ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True,nbins=5))
        for i,v in enumerate(vals):
            label=spec.get('formats',[str(x) for x in vals])[i]
            ax.text(v+max(vals)*.025,i,label,va='center',size=15,weight='bold')
    elif spec['type']=='cards':
        cards=spec['cards']; n=len(cards); gap=.018; width=(.89-gap*(n-1))/n
        for i,(head,body,note) in enumerate(cards):
            x=.055+i*(width+gap)
            base.add_patch(FancyBboxPatch((x,.265),width,.43,boxstyle='round,pad=0.008,rounding_size=.012',facecolor=CARD,edgecolor='none'))
            base.text(x+.02,.657,wrap(head,23 if n==2 else 20),va='top',size=14,weight='bold',color=TEAL)
            base.text(x+.02,.545,wrap(body,29 if n==2 else 22),va='top',size=16,linespacing=1.3)
            base.text(x+.02,.315,wrap(note,35 if n==2 else 29),va='top',size=10,color=MUTED)
    elif spec['type']=='list':
        rows=spec['rows']; top=.70; step=.48/len(rows)
        for i,(label,body) in enumerate(rows):
            y=top-i*step
            base.text(.07,y,label,size=12,weight='bold',color=TEAL,va='center')
            base.text(.25,y,body,size=15,va='center')
            if i<len(rows)-1: base.plot([.07,.93],[y-step*.48]*2,color='#d9ddd4',lw=.7)
    elif spec['type']=='metric':
        base.text(.07,.49,spec['value'],size=112,weight='bold',va='center',color=TEAL)
        base.text(.38,.49,wrap(spec['label'],32),size=26,va='center',linespacing=1.3)
    fig.savefig(OUT/spec['file'],facecolor=BG,dpi=160)
    plt.close(fig)

# QA contact sheet only; each exported figure remains an original rendering.
thumbs=[]
for spec in SPECS:
    im=Image.open(OUT/spec['file']).convert('RGB');im.thumbnail((576,298))
    tile=Image.new('RGB',(600,330),'white');tile.paste(im,((600-im.width)//2,0))
    ImageDraw.Draw(tile).text((14,307),spec['id']+' '+spec['file'],fill=INK)
    thumbs.append(tile)
sheet=Image.new('RGB',(1800,330*((len(thumbs)+2)//3)),'#d4d8d2')
for i,im in enumerate(thumbs):sheet.paste(im,((i%3)*600,(i//3)*330))
sheet.save(PACKET/'data/section-figures-contact-sheet.jpg',quality=90)
print(f'Rendered {len(SPECS)} figures and contact sheet.')
