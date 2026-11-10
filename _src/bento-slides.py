IO='io/pf-io-'
def d(n): return IO+n+'-d.png'
def m(n): return IO+n+'-mns.png'
io=dict(bg='#e9e8e4',fg='#141414',sub='#4a4a4a',r=10,rpct=1,rp=7)
P='pga/pga-'
pga=dict(bg='#10213f',fg='#ffffff',sub='#b9c3d6',r=10,rpct=1,rp=9,shadow='0 24px 50px -20px rgba(0,0,0,.6)')
HK='hk/hk-'
hk=dict(bg='#22382a',fg='#f4f1ea',sub='#b8c4b6',r=8,shadow='0 24px 50px -22px rgba(0,0,0,.6)')
RH=dict(bg='#f2e21b',fg='#111111',sub='#3a3500',r=8,shadow='0 24px 50px -22px rgba(60,50,0,.55)')
DK='dk/dk-'
dk=dict(bg='#1f2f55',fg='#ffffff',sub='#b8c2da',r=8,rpct=1,rp=6,shadow='0 24px 50px -22px rgba(0,0,0,.6)')
SW='sw/sw-'
sw=dict(bg='#2d4a3e',fg='#f3efe2',sub='#c3cfc4',r=8,rpct=1,rp=6,shadow='0 24px 50px -22px rgba(0,0,0,.55)')
BC='bc/'
bc=dict(bg='#0d2240',fg='#ffffff',sub='#a9b8cf',r=8,shadow='0 24px 50px -22px rgba(0,0,0,.6)')
cv=dict(bg='#454b5b',fg='#ffffff',sub='#d5dae6',r=10,shadow='0 24px 50px -22px rgba(0,0,0,.5)')
SLIDES={
 'io-hero':dict(io,title=dict(label='Google I/O 2026 · Date reveal',h='Play to<br>reveal.',p='A set of puzzle games the whole community played to unlock the I/O date.',toc=['Direction','The games','On every screen','The reveal','The payoff']),
   cols=[[d('homepage-landing'),d('play-builds-build-4')],[d('bundle-complete-finish'),d('reveal-4')]]),
 'io-direction':dict(io,cols=[[d('bundle-select-entry'),d('bundle-complete-1')],[d('bundle-complete-2'),d('bundle-complete-3')]]),
 'io-games':dict(io,cols=[[d('play-builds-default'),d('play-builds-build-2')],[d('play-builds-build-4'),d('play-builds-finish')]]),
 'io-mobile':dict(io,cols=[[m('bundle-select-entry')],[m('play-builds-default')],[m('play-builds-build-4')],[m('bundle-complete-finish')],[m('reveal-4')]]),
 'io-reveal':dict(io,cols=[[d('reveal-1'),d('reveal-5')],[d('reveal-2'),d('reveal-6')]]),
 'io-payoff':dict(io,cols=[[d('finish-1'),d('easter-egg-unlock')],[d('finish-3'),d('remix')]]),
 'pga-hero':dict(pga,title=dict(label='PGA Tour · Mobile app',h='Follow the players.',p='The PGA Tour app, rebuilt around the golfers fans actually follow.',toc=['Onboarding','Live golf','Coverage','Stories']),
   cols=[[P+'yourtour-fx-av.png'],[P+'leaderboard-fx.png'],[P+'hole-2-ns.png']]),
 'pga-onboard':dict(pga,cols=[[P+'onboard-tour-ns.png'],[P+'onboard-photo-ns.png'],[P+'yourtour-fx-av.png'],[P+'me-ns.png']]),
 'pga-live':dict(pga,cols=[[P+'leaderboard-fx.png'],[P+'scorecard-named-ns.png'],[P+'hole-1-ns.png'],[P+'tourcast-fx-ns.png'],[P+'course-ns.png']]),
 'pga-coverage':dict(pga,cols=[[P+'news-fx.png'],[P+'profile-ns.png'],[P+'stats-ns-av.png'],[P+'watch-fx.png']]),
 'pga-stories':dict(pga,cols=[[P+'story-round-fx.png'],[P+'story-champ-fx.png'],[P+'tourn-1-ns.png'],[P+'tourn-2-ns.png']]),

 'hk-hero':dict(hk,hs=86,title=dict(label='PGA Tour · Design system',h='One system under it all.',p='Haskell: the foundations, specs and art direction behind every PGA Tour screen.',toc=['Principles','Foundations','Specs','Themes','Art direction']),
   cols=[[HK+'evolution.png',HK+'theme-palette.png'],[HK+'spec-icons.png',HK+'topdown.png']]),
 'hk-principles':dict(hk,cols=[[HK+'p-fan.png'],[HK+'p-immersive.png']]),
 'hk-found':dict(hk,cols=[[HK+'tokens.png'],[HK+'spacing.png'],[HK+'spacing-methods.png',HK+'radii.png',HK+'easing.png']]),
 'hk-specs':dict(hk,cols=[[HK+'spec-color.png',HK+'spec-logo.png'],[HK+'spec-icons.png',HK+'logo.png']]),
 'hk-themes':dict(hk,cols=[[HK+'theme-palette.png',HK+'theme-screens.png'],[HK+'tourn-themes.png',HK+'theme-app.png']]),
 'hk-art':dict(hk,cols=[[HK+'imagery-mood.png',HK+'aerial.png'],[HK+'topdown.png',HK+'tourcast.png']]),
 'rh-hero':dict(RH,hs=84,title=dict(label='Rock & Roll Hall of Fame · Digital',h='The museum, on every screen.',p='Inductee pages that turn the collection into a story, told here through the Rolling Stones.',toc=['Artifacts','Their sound','Their voice','The archive','The system']),
   cols=[['rhds/x-hero-stones-d.png','rh2/x-poster-d.png'],['rh8/x-art-d.png','rh2/x-sound-d.png']]),
 'rh-artifacts':dict(RH,cols=[['rh8/x-art-d.png'],['rh2/x-poster-d.png']]),
 'rh-sound':dict(RH,cols=[['rh2/x-sound-d.png'],['rh2/x-collage-d.png']]),
 'rh-voice':dict(RH,cols=[['rh8/x-back-d.png','rh2/x-essay-d.png'],['rh8/x-quote-d.png']]),
 'rh-archive':dict(RH,cols=[['rh2/x-influence-d.png'],['rhds/x-timeline-d.png']]),
 'rh-system':dict(RH,cols=[['rhds/rhds-hero-kendrick-desktop.png','rhds/rhds-classes-desktop.png','rhds/rhds-secondary-desktop.png'],['rhds/rhds-feature-block-desktop.png','rhds/rhds-primary-desktop.png']]),
 'dk-hero':dict(dk,title=dict(label='Dickies · E-commerce',h='A store that works.',p='Dickies.com, redesigned for people who wear the clothes to work.',toc=['Shopping','Mobile-first','Categories','Stories']),
   cols=[[DK+'home-d-top.png',DK+'pdp-d-top.png'],[DK+'plp-d-top.png',DK+'skate-d-top.png']]),
 'dk-shop':dict(dk,cols=[[DK+'plp-d-top.png',DK+'cart-d-top.png'],[DK+'pdp-d-top.png',DK+'mens-d-top.png']]),
 'dk-mobile':dict(dk,cols=[[DK+'home-m-top.png'],[DK+'plp-m-top.png'],[DK+'pdp-m-top.png'],[DK+'cart-m-top.png'],[DK+'skate-m-top.png']]),
 'dk-cats':dict(dk,cols=[[DK+'skate-d-top.png',DK+'biz-d-top.png'],[DK+'scrubs-d-top.png',DK+'home-d-top.png']]),
 'dk-stories':dict(dk,cols=[[DK+'stories-d-top.png'],[DK+'team-d-top.png']]),
 'sw-hero':dict(sw,title=dict(label='Smartwool · E-commerce',h='Find your way in.',p='A site architecture that meets shoppers where they are: by activity, by need, by story.',toc=['Directions','Architecture','Discovery','On mobile']),
   cols=[[SW+'home-d.png',SW+'prod-d.png'],[SW+'act-d.png',SW+'plant-d.png']]),
 'sw-dirs':dict(sw,cols=[[SW+'home-d.png'],[SW+'v2-d.png']]),
 'sw-arch':dict(sw,cols=[[SW+'act-d.png',SW+'coll-d.png'],[SW+'prod-d.png',SW+'gear-d.png']]),
 'sw-disc':dict(sw,cols=[[SW+'plant-d.png'],[SW+'gear-d.png']]),
 'sw-mobile':dict(sw,cols=[[SW+'home-m.png'],[SW+'act-m.png'],[SW+'prod-m.png'],[SW+'plant-m.png'],[SW+'coll-m.png']]),
 'bc-hero':dict(bc,title=dict(label='Morgan Stanley · Design system',h='Great work starts here.',p='Beacon: the documentation site that made designers want to use the system.',toc=['Getting started','Components','Patterns','Foundations']),
   cols=[[BC+'bc-home-top.png',BC+'bcd-gallery.png'],[BC+'bc-components.png',BC+'bcd-color.png']]),
 'bc-start':dict(bc,cols=[[BC+'bc-home-top.png'],[BC+'bc-getstarted.png']]),
 'bc-comps':dict(bc,cols=[[BC+'bc-components.png'],[BC+'bcd-gallery.png']]),
 'bc-pattern':dict(bc,cols=[[BC+'bcd-pattern.png']]),
 'bc-found':dict(bc,cols=[[BC+'bcd-color.png'],[BC+'bcd-type.png']]),
 'cv-buttons':dict(cv,cols=[[('cv/cv-buttons.png',(0,0,1,.5))],[('cv/cv-buttons.png',(0,.5,1,1))]]),
 'cv-tnf':dict(cv,cols=[['tnf-dl/tnf-pdpd.png']]),
}
