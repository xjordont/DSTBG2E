#!/usr/bin/env python3
"""Apply manual corrections to the auto-extracted p.32 icon units and regenerate assets/icons.
Also samples the colour palette -> work/palette.json"""
import os, json, re, glob, colorsys
import numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # repo root, checkout-independent
TGN='DS-TG-Rulebook-Compressed_compressed.pdf'
REND='work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p32_600dpi-32.png'; S=600/72
page=Image.open(REND).convert('RGB')
units={r['id']:r for r in json.load(open('work/extraction_records_icons.json'))}
DROP={'ICO-020','ICO-021','ICO-027','ICO-028','ICO-029','ICO-043','ICO-044','ICO-045','ICO-062','ICO-063','ICO-068','ICO-069','ICO-032','ICO-013','ICO-014','ICO-015','ICO-001'}
# (name, section, bbox_pt (no margin), margin, kind, note)
EXTRA=[
 ('Primary spawn node','Encounter Cards',(98.5,99,122.5,123),0.5,'raster','red circle with slash'),
 ('Secondary spawn node','Encounter Cards',(98.5,123,122.5,147),0.5,'raster','red circle with X'),
 ('Primary terrain node','Encounter Cards',(98.5,147,122.5,171),0.5,'raster','magenta circle with star'),
 ('Secondary terrain node','Encounter Cards',(98.5,171,122.5,195),0.5,'raster','magenta circle with trident'),
 ('Trapped encounter (trap icon, three spears)','Encounter Cards',(98.9,195.7,122.1,226.1),1.0,'raster','placed as three 6.3×30.4 pt strips of the same image'),
]
RENAME={
 'ICO-022':('Threat level','Enemy Statistics',None),
 'ICO-023':('Behaviour deck size','Enemy Statistics',None),
 'ICO-024':('Block / Resist shield (enemy statistics)','Enemy Statistics',0.3),
 'ICO-025':('Starting Health','Enemy Statistics',None),
 'ICO-026':('Heat Up Point','Enemy Statistics',None),
 'ICO-030':('Push-with-damage satellite glyph (push crest with value)','Enemy Movement',None),
 'ICO-031':('Target: nearest character (ring glyph)','Enemy Movement',None),
 'ICO-033':('Enemy Movement composite symbol (Move icon with push, aggro and leap satellites)','Enemy Movement',0.3),
 'ICO-034':('Enemy Attack composite symbol (Attack icon with push, aggro, node and magic satellites)','Enemy Attacks',0.3),
 'ICO-035':('Area attack icon (damage all nodes in specified arcs)','Enemy Attacks',None),
 'ICO-036':('Turn 90° right','Enemy Movement',None),
 'ICO-037':('Turn 90° left','Enemy Movement',None),
 'ICO-038':('Turn around (180°)','Enemy Movement',None),
 'ICO-039':('Neutral boss arc','Enemy Attacks',None),
 'ICO-040':('Attack boss arc','Enemy Attacks',None),
 'ICO-041':('Weak boss arc','Enemy Attacks',None),
 'ICO-042':('Deal magical damage (enemy attack star)','Enemy Attacks',None),
 'ICO-046':('Deal magical damage (character attack orb)','Character Attacks',None),
 'ICO-047':('One-handed weapon','Equipment Icons',None),
 'ICO-050':('Two-handed weapon','Equipment Icons',None),
 'ICO-054':('Armour','Equipment Icons',None),
 'ICO-058':('Upgrade slots','Equipment Icons',None),
 'ICO-049':('Black dice','Character Attacks',None),
 'ICO-052':('Blue dice','Character Attacks',None),
 'ICO-056':('Orange dice','Character Attacks',None),
 'ICO-053':('Node attack (damage all enemies on target node)','Character Attacks',None),
 'ICO-057':('Shaft (cannot attack at Range 0)','Character Attacks',None),
 'ICO-060':('Shift (move indicated number of nodes in any direction)','Character Attacks',None),
 'ICO-061':('Push affected enemies','Character Attacks',None),
 'ICO-064':('Taunt','Other Icons',None),
 'ICO-067':('Dodge','Other Icons',None),
 'ICO-070':('Bleed','Conditions',0.3),'ICO-071':('Frostbite','Conditions',0.3),'ICO-072':('Poison','Conditions',0.3),'ICO-073':('Stagger','Conditions',0.3),
}
def slug(t): t=re.sub(r'\(.*?\)','',t); t=re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-'); return t[:48]
def key_alpha(im,soft=(14,60)):
    a=np.asarray(im.convert('RGB')).astype(int)
    border=np.concatenate([a[0],a[-1],a[:,0],a[:,-1]]); bg=np.median(border,axis=0)
    d=np.abs(a-bg).max(axis=2); alpha=np.clip((d-soft[0])/(soft[1]-soft[0]),0,1)
    return Image.fromarray(np.dstack([a,alpha*255]).astype(np.uint8),'RGBA'),tuple(int(v) for v in bg)
for f in glob.glob('assets/icons/*.png'): os.remove(f)
for f in glob.glob('work/icons_parchment/*.png'): os.remove(f)
final=[]
for uid,u in units.items():
    if uid in DROP: continue
    m=2.5; bb=u['bbox_pt']; bb=(bb[0]+m,bb[1]+m,bb[2]-m,bb[3]-m)  # undo stored margin
    name,sec,note=u['name'],u['section'],''
    if uid in RENAME:
        name,sec,mm=RENAME[uid]; 
        if mm is not None: m=mm
    final.append(dict(name=name,section=sec,bbox=bb,margin=m,kind=u['kind'],note=note,orig=uid))
for name,sec,bb,m,kind,note in EXTRA: final.append(dict(name=name,section=sec,bbox=bb,margin=m,kind=kind,note=note,orig='manual'))
order=['Encounter Cards','Enemy Statistics','Enemy Movement','Enemy Attacks','Equipment Icons','Character Attacks','Other Icons','Conditions']
final.sort(key=lambda f:(order.index(f['section']),round(f['bbox'][1]/10),f['bbox'][0]))
REC=[]
for n,f in enumerate(final,1):
    m=f['margin']; bb=f['bbox']; bbm=(bb[0]-m,bb[1]-m,bb[2]+m,bb[3]+m)
    px=tuple(int(round(v*S)) for v in bbm); crop=page.crop(px)
    pid=f'ICO-{n:03d}'; sl=slug(f['name'])
    pf=f'work/icons_parchment/{pid}-{sl}.png'; crop.save(pf)
    al,bg=key_alpha(crop); bbx=al.getchannel('A').getbbox()
    if bbx: al=al.crop((max(0,bbx[0]-3),max(0,bbx[1]-3),min(al.width,bbx[2]+3),min(al.height,bbx[3]+3)))
    af=f'assets/icons/{pid.lower()}-{sl}.png'; al.save(af)
    REC.append(dict(id=pid,name=f['name'],section=f['section'],kind=f['kind'],type='icon',src=TGN,page=32,bbox_pt=tuple(round(v,1) for v in bbm),method=f'pdftoppm 600 dpi render crop → parchment-key alpha (bg {bg}); {"vector artwork in PDF (also croppable from work/svg/tg_p32.svg)" if f["kind"]=="vector" else "raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)"}',file=af,dims=f'{al.width}×{al.height} px',format='png',parchment_crop=pf,note=f['note']))
json.dump(REC,open('work/extraction_records_icons_final.json','w'),indent=1,default=str)
print(len(REC),'icons final'); 
for r in REC: print(r['id'],r['section'],'|',r['name'],r['dims'])

# ---------- palette ----------
def hx(c): return '#%02x%02x%02x'%tuple(int(round(v)) for v in c)
def cmyk(c):
    r,g,b=[v/255 for v in c]; k=1-max(r,g,b)
    if k>=0.999: return 'C0 M0 Y0 K100'
    return 'C%d M%d Y%d K%d'%tuple(round(v*100) for v in ((1-r-k)/(1-k),(1-g-k)/(1-k),(1-b-k)/(1-k),k))
def sat_median(path,smin=0.35,vmin=0.25,hue=None):
    a=np.asarray(Image.open(path).convert('RGB')).reshape(-1,3)/255
    hsv=np.array([colorsys.rgb_to_hsv(*p) for p in a[::3]])
    m=(hsv[:,1]>smin)&(hsv[:,2]>vmin)
    if hue: m&=((hsv[:,0]*360>=hue[0])&(hsv[:,0]*360<=hue[1])) if hue[0]<hue[1] else ((hsv[:,0]*360>=hue[0])|(hsv[:,0]*360<=hue[1]))
    sel=a[::3][m]
    if len(sel)<20: return None
    return tuple(np.median(sel,axis=0)*255)
P={}
def put(k,c,use): 
    if c is not None: P[k]=dict(hex=hx(c),cmyk=cmyk(c),use=use)
def region_median(path,box,dark_pct=None):
    im=Image.open(path).convert('RGB'); im=im.crop(box) if box else im
    a=np.asarray(im).reshape(-1,3).astype(float)
    if dark_pct: 
        lum=a.sum(1); a=a[lum<np.percentile(lum,dark_pct)]
    return tuple(np.median(a,axis=0))
s4=400/72; s6=600/72
put('parchment_page_2022',region_median('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p13_400dpi-13.png',(int(300*s4),int(430*s4),int(520*s4),int(560*s4))),'page background (2022 book, mid-page parchment, text-free zone p.13 right col below diagram)')
put('parchment_page_2017',region_median('work/renders/hires/DS-Core-Rules-lores_p07_400dpi-07.png',(int(60*s4),int(60*s4),int(280*s4),int(300*s4))),'page background (2017 book, p.7 token column incl. small icons)')
put('parchment_panel_backcover',region_median('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p32_600dpi-32.png',(int(120*s6),int(250*s6),int(300*s6),int(300*s6))),'back-cover reference panel fill (brightest parchment)')
put('heading_ink',region_median('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p13_400dpi-13.png',(int(150*s4),int(60*s4),int(480*s4),int(85*s4)),3),'chapter title ink (darkest 3% of title zone)')
put('body_ink',region_median('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p13_400dpi-13.png',(int(60*s4),int(440*s4),int(300*s4),int(600*s4)),2),'body text ink (darkest 2% of body zone)')
put('cover_black',region_median('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p01_600dpi-01.png',(0,int(650*s6),int(629*s6),int(811*s6))),'cover / back-cover ground')
put('gutter_leather_dark',region_median('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p13_400dpi-13.png',(int(600*s4),0,int(629*s4),int(811*s4))),'outer page-edge shadow of the open-book background')
def pc(name): 
    g=glob.glob(f'work/icons_parchment/*-{name}*.png'); return g[0] if g else None
put('node_gold_ring',sat_median(pc('taunt'),0.3,0.4,(30,60)) or sat_median(pc('attack-range'),0.3,0.4,(30,60)),'gold ring / node outline / dashboard lettering accent')
put('spawn_node_red',sat_median(pc('primary-spawn-node'),0.45,0.4,(340,20)),'enemy spawn nodes, Attack boss arc, bleed')
put('terrain_node_magenta',sat_median(pc('primary-terrain-node'),0.35,0.4,(270,330)),'terrain nodes')
put('encounter_level1_blue',sat_median(pc('encounter-level-1'),0.2,0.5,(190,240)),'encounter level 1 orb')
put('encounter_level3_purple',sat_median(pc('encounter-level-3'),0.25,0.3,(240,300)),'encounter level 3 orb')
put('dice_blue',sat_median(pc('blue-dice'),0.4,0.4,(185,215)),'blue die')
put('dice_orange',sat_median(pc('orange-dice'),0.5,0.5,(15,45)),'orange die')
put('attack_arc_green',sat_median(pc('attack-boss-arc'),0.3,0.3,(120,180)),'Attack boss arc, dodge/green nodes')
put('weak_arc_red',sat_median(pc('weak-boss-arc'),0.4,0.4,(350,25)),'Weak boss arc')
put('magic_yellow',sat_median(pc('deal-magical-damage-'),0.3,0.6,(45,70)) or sat_median(pc('deal-magical-damage'),0.3,0.6,(45,70)),'magical damage orb')
put('poison_green',sat_median(pc('poison'),0.4,0.3,(90,150)),'poison condition')
put('frostbite_blue',sat_median(pc('frostbite'),0.25,0.5,(180,230)),'frostbite condition')
put('endurance_bar_red',region_median('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p08_400dpi-08.png',(int(93*s4),int(700*s4),int(583*s4),int(730*s4)),None),'dashboard endurance bar (median incl. squares) — see also sampled red below')
a=np.asarray(Image.open('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p08_400dpi-08.png').convert('RGB').crop((int(93*s4),int(700*s4),int(583*s4),int(730*s4)))).reshape(-1,3).astype(int); red=a[(a[:,0]>90)&(a[:,1]<60)&(a[:,2]<70)]
put('endurance_bar_red',tuple(np.median(red,axis=0)),'character dashboard endurance bar deep red')
a=np.asarray(Image.open('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p08_400dpi-08.png').convert('RGB').crop((int(93*s4),int(346*s4),int(135*s4),int(700*s4)))).reshape(-1,3).astype(int); g=a[(a[:,0]>150)&(a[:,1]>100)&(a[:,2]<90)&(a[:,0]-a[:,2]>80)]
if len(g)>50: put('dashboard_gold',tuple(np.median(g,axis=0)),'dashboard slot lettering ("ARMOUR", "LEFT HAND") gold')
a=np.asarray(Image.open('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p10_400dpi-10.png').convert('RGB').crop((int(154*s4),int(351*s4),int(273*s4),int(530*s4)))).reshape(-1,3).astype(int); lum=a.sum(1); dk=a[(lum<150)]
put('card_frame_charcoal',tuple(np.median(dk,axis=0)),'card frame ground (equipment / enemy cards)')
json.dump(P,open('work/palette.json','w'),indent=1)
for k,v in P.items(): print(f'{k:28s} {v["hex"]}  {v["cmyk"]:22s} {v["use"]}')
