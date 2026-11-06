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
<meta name="description" content="Corey Dixon, Senior Product &amp; Experience Designer in Richmond, VA. 14 years designing web and app experiences for Google, PGA Tour, Morgan Stanley, Dickies and more.">
<link rel="canonical" href="{BASE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Corey Dixon©">
<meta property="og:url" content="{BASE}/">
<meta property="og:title" content="Corey Dixon©">
<meta property="og:description" content="Senior Product &amp; Experience Designer. Design systems, e-commerce and platforms for global brands.">
<meta property="og:image" content="{BASE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Corey Dixon© — Shaping scalable digital systems across enterprise, culture, and global brands.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Corey Dixon©">
<meta name="twitter:description" content="Senior Product &amp; Experience Designer. Design systems, e-commerce and platforms for global brands.">
<meta name="twitter:image" content="{BASE}/og.png">
<meta name="theme-color" content="#0C0C0B">
<meta name="author" content="Corey Dixon">
<link rel="manifest" href="/site.webmanifest">
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
