# Package index.html (artifact source) into site/index.html for Cloudflare Pages.
import re
s=open('index.html').read()
s=re.sub(r'url\(data:font/woff2;base64,[^)]+\)','url(/fonts/OverusedGrotesk-VF.woff2)',s,count=1)
s=re.sub(r'<link rel="icon" type="image/svg\+xml" href="data:[^"]+">',
 '<link rel="icon" href="/favicon.ico" sizes="32x32">\n<link rel="icon" type="image/svg+xml" href="/brand/favicon.svg">\n<link rel="apple-touch-icon" href="/brand/apple-touch-icon.png">',s,count=1)
s=s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
BASE='https://coreydixon.design'
head=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Corey Dixon, senior and lead product designer in Richmond, VA. 14 years of design systems, mobile apps and web products for fintech, enterprise, e-commerce and sports brands, including Google, PayPal, Capital One, Morgan Stanley, PGA Tour and Dickies.">
<link rel="canonical" href="{BASE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Corey Dixon©">
<meta property="og:url" content="{BASE}/">
<meta property="og:title" content="Corey Dixon© — Senior &amp; Lead Product Designer">
<meta property="og:description" content="Senior &amp; lead product designer. Design systems, mobile apps and web products for fintech, enterprise, e-commerce and sports brands.">
<meta property="og:image" content="{BASE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Corey Dixon© — Shaping scalable digital systems across enterprise, culture, and global brands.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Corey Dixon© — Senior &amp; Lead Product Designer">
<meta name="twitter:description" content="Senior &amp; lead product designer. Design systems, mobile apps and web products for fintech, enterprise, e-commerce and sports brands.">
<meta name="twitter:image" content="{BASE}/og.png">
<meta name="theme-color" content="#0C0C0B">
<meta name="author" content="Corey Dixon">
<link rel="manifest" href="/site.webmanifest">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Person","name":"Corey Dixon","jobTitle":"Senior & Lead Product Designer","url":"{BASE}/","email":"mailto:hi@coreydixon.design","address":{{"@type":"PostalAddress","addressLocality":"Richmond","addressRegion":"VA","addressCountry":"US"}},"sameAs":["https://linkedin.com/in/corey-dixon"],"knowsAbout":["Product design","Design systems","Component libraries","Design tokens","Mobile app design","iOS","Android","Responsive web design","Fintech","Financial services","Payments","Enterprise software","B2B tools","E-commerce","Shopify","Retail","Sports media","Accessibility","WCAG","Art direction","Interaction design","Prototyping","UX research","Figma","AI-assisted design"]}}</script>
<link rel="preload" href="/fonts/OverusedGrotesk-VF.woff2" as="font" type="font/woff2" crossorigin>
'''
i=s.index('</style>')+len('</style>')
doc=head+s[:i]+'\n</head>\n<body>\n'+s[i:]+'\n</body>\n</html>\n'
doc=doc.replace('*{box-sizing:border-box}','*{box-sizing:border-box}\nhtml{-webkit-text-size-adjust:100%}\nbody{margin:0}\nimg{max-width:100%;display:block}\n[hidden]{display:none!important}',1)
doc=doc.replace('src="work/','src="/work/')
open('site/index.html','w').write(doc); print(len(doc))

open('site/robots.txt','w').write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open('site/sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}/</loc></url></urlset>\n')
open('site/site.webmanifest','w').write('{"name":"Corey Dixon©","short_name":"Corey Dixon","start_url":"/","display":"browser","background_color":"#0C0C0B","theme_color":"#0C0C0B","icons":[{"src":"/brand/apple-touch-icon.png","sizes":"180x180","type":"image/png"},{"src":"/brand/icon-512.png","sizes":"512x512","type":"image/png"}]}\n')

# One real page per case study and the resume, so shared links preview the right project.
import os, html as H
from PIL import Image
src=open('index.html').read()
def field(b,k):
    m=re.search(k+r':"((?:[^"\\]|\\.)*)"',b); return m.group(1) if m else ''
os.makedirs('site/og',exist_ok=True)
urls=[BASE+'/']
a=src.index('const P = [')
for m in re.finditer(r'\{id:"([\w-]+)"',src[a:src.index('const ROWS',a)]):
    pid=m.group(1); b=src[a+m.start():a+m.start()+6000]
    client=H.unescape(field(b,'client')); disc=field(b,'disc'); tag=H.unescape(field(b,'tagline')); co=H.unescape(field(b,'co')); role=H.unescape(field(b,'role'))
    award=H.unescape(field(b,'awardLong'))
    hero=re.search(r'hero:\["([^"]+)"',b).group(1)
    im=Image.open(f'site/work/{hero}.webp').convert('RGB'); w,h=im.size; t=630/1200
    if h/w>t: nh=int(w*t); im=im.crop((0,(h-nh)//2,w,(h-nh)//2+nh))
    else: nw=int(h/t); im=im.crop(((w-nw)//2,0,(w-nw)//2+nw,h))
    im.resize((1200,630),Image.LANCZOS).save(f'site/og/{pid}.jpg',quality=86)
    title=f'{client} · {disc} — Corey Dixon©'
    desc=f'{tag} {disc} for {co}. Role: {role}.'+(f' {award}.' if award else '')+' A case study by Corey Dixon, senior & lead product designer.'
    url=f'{BASE}/{pid}/'; urls.append(url)
    e=lambda x:H.escape(x,quote=True)
    d=doc
    d=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{e(desc)}">',d,count=1)
    d=d.replace(f'<link rel="canonical" href="{BASE}/">',f'<link rel="canonical" href="{url}">',1)
    d=d.replace(f'<meta property="og:url" content="{BASE}/">',f'<meta property="og:url" content="{url}">',1)
    d=d.replace('<meta property="og:type" content="website">','<meta property="og:type" content="article">',1)
    d=re.sub(r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{e(title)}">',d,count=1)
    d=re.sub(r'<meta name="twitter:title" content="[^"]*">',f'<meta name="twitter:title" content="{e(title)}">',d,count=1)
    d=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{e(desc)}">',d,count=1)
    d=re.sub(r'<meta name="twitter:description" content="[^"]*">',f'<meta name="twitter:description" content="{e(desc)}">',d,count=1)
    d=d.replace(f'content="{BASE}/og.png"',f'content="{BASE}/og/{pid}.jpg"')
    d=re.sub(r'<meta property="og:image:alt" content="[^"]*">',f'<meta property="og:image:alt" content="{e(client)}, a case study by Corey Dixon">',d,count=1)
    d=re.sub(r'<title>[^<]*</title>',f'<title>{e(title)}</title>',d,count=1)
    os.makedirs(f'site/{pid}',exist_ok=True); open(f'site/{pid}/index.html','w').write(d)
d=doc.replace(f'<link rel="canonical" href="{BASE}/">',f'<link rel="canonical" href="{BASE}/resume/">',1).replace(f'<meta property="og:url" content="{BASE}/">',f'<meta property="og:url" content="{BASE}/resume/">',1)
d=re.sub(r'<title>[^<]*</title>','<title>Resume — Corey Dixon©, Senior &amp; Lead Product Designer</title>',d,count=1)
os.makedirs('site/resume',exist_ok=True); open('site/resume/index.html','w').write(d); urls.append(BASE+'/resume/')
open('site/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{u}</loc></url>' for u in urls)+'</urlset>\n')
print('pages',len(urls))
