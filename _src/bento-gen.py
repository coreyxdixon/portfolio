# Bento slides: real screens and guide pages at their natural aspect, columns solved so every column ends at the same line. No cropping.
# usage: python3 gen.py slides.py [name ...]   (slides.py defines SLIDES = {name: {...}})
import sys, os, hashlib, runpy
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
ROOT='/home/claude/corey-dixon-site/src/'
W,H,PAD,G=1600,1000,56,16
CACHE=os.path.abspath('cache'); os.makedirs(CACHE,exist_ok=True)
def src(item):
    # item: "path" or ("path",(x0,y0,x1,y1)) with fractional crop
    p,c=(item,None) if isinstance(item,str) else item
    p=p if p.startswith('/') else ROOT+p
    if not c: return p
    key=hashlib.md5((p+str(c)).encode()).hexdigest()[:10]; out=f'{CACHE}/{key}.png'
    if not os.path.exists(out):
        im=Image.open(p); w,h=im.size; im.crop((int(c[0]*w),int(c[1]*h),int(c[2]*w),int(c[3]*h))).save(out)
    return out
_asp={}
def asp(p):
    if p not in _asp: im=Image.open(p); _asp[p]=im.width/im.height
    return _asp[p]
def layout(cols,x0,x1,top,bot,g):
    S=[sum(1/asp(n) for n in c) for c in cols]; avail=x1-x0-g*(len(cols)-1)
    h=(avail+g*sum((len(c)-1)/s for c,s in zip(cols,S)))/sum(1/s for s in S)
    scale=min(1,(bot-top)/h)
    ws=[(h-g*(len(c)-1))/s*scale for c,s in zip(cols,S)]
    hh=h*scale - g*0  # approx
    tot=sum(ws)+g*(len(cols)-1); x=x0+((x1-x0)-tot)/2
    colh=[sum(w/asp(n) for n in c)+g*(len(c)-1) for c,w in zip(cols,ws)]
    y0=top+((bot-top)-max(colh))/2
    T=[]
    for c,w in zip(cols,ws):
        y=y0
        for n in c: hh=w/asp(n); T.append((n,x,y,w,hh)); y+=hh+g
        x+=w+g
    return T
def build(name,v):
    bg=v.get('bg','#c9b99b'); fg=v.get('fg','#1a1a1a'); sub=v.get('sub',fg)
    rad=v.get('r',8); g=v.get('g',G)
    cols=[[src(i) for i in c] for c in v['cols']]
    x0=PAD+(400 if v.get('title') else 0)
    T=layout(cols,x0,W-PAD,PAD,H-PAD,g)
    sh=v.get('shadow','0 1px 0 rgba(0,0,0,.08),0 18px 40px -18px rgba(0,0,0,.45)')
    html=f'''<!doctype html><html><head><meta charset="utf-8"><style>*{{margin:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{bg};font-family:"Nimbus Sans",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;color:{fg}}}
img{{position:absolute;display:block;box-shadow:{sh}}}
.m{{font-family:"DejaVu Sans Mono",monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase}}
.t{{position:absolute;left:{PAD}px;top:{PAD}px;bottom:{PAD}px;width:356px;display:flex;flex-direction:column}}
.t h1{{font-size:{v.get('hs',96)}px;font-weight:700;letter-spacing:-.05em;line-height:.92;margin-top:18px}}
.t p{{font-size:22px;line-height:1.3;margin-top:22px;max-width:15em;color:{sub}}}
.toc{{margin-top:auto;display:flex;flex-direction:column}}.toc div{{display:flex;justify-content:space-between;border-top:1.5px solid color-mix(in srgb,{fg} 28%,transparent);padding:11px 0}}
</style></head><body>'''
    t=v.get('title')
    if t:
        html+=f'<div class="t"><div class="m" style="color:{sub}">{t["label"]}</div><h1>{t["h"]}</h1><p>{t["p"]}</p><div class="toc m">'+''.join(f'<div><span>{a}</span><span>0{i+1}</span></div>' for i,a in enumerate(t['toc']))+'</div></div>'
    for n,x,y,w,h in T:
        r=v.get('rp',rad) if asp(n)<0.75 else rad
        r=r*w/100 if v.get('rpct') and asp(n)<0.75 else r
        html+=f'<img src="file://{n}" style="left:{x:.1f}px;top:{y:.1f}px;width:{w:.1f}px;height:{h:.1f}px;border-radius:{r:.1f}px">'
    open(f'v-{name}.html','w').write(html+'</body></html>')
    print(name,'min tile',round(min(w for n,x,y,w,h in T)),'px wide')
SL=runpy.run_path(sys.argv[1])['SLIDES']
for k,v in SL.items():
    if len(sys.argv)<3 or k in sys.argv[2:]: build(k,v)
