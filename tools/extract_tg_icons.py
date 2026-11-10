#!/usr/bin/env python3
"""Batch 2: every icon on the 2022 rulebook back-cover key (p.32).
Units = raster placements + vector clusters merged by overlap; labelled from the adjacent text.
Cleaned file = 600 dpi crop keyed against parchment (alpha). Records -> work/extraction_records_icons.json"""
import os, json, re, difflib
import numpy as np
from PIL import Image, ImageDraw
import pdfplumber
Image.MAX_IMAGE_PIXELS=None
os.chdir('/home/user/DSTBG2E')
TG='work/pdf_decrypted/DS-TG-Rulebook-Compressed_compressed.pdf'; TGN='DS-TG-Rulebook-Compressed_compressed.pdf'
REND='work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p32_600dpi-32.png'; S=600/72
page=Image.open(REND).convert('RGB')
pdf=pdfplumber.open(TG); p=pdf.pages[31]
words=p.extract_words(x_tolerance=1.5)
lines=[]
for w in sorted(words,key=lambda w:(round(w['top']),w['x0'])):
    if lines and abs(lines[-1]['top']-w['top'])<2.5 and w['x0']-lines[-1]['x1']<10:
        lines[-1]['text']+=' '+w['text']; lines[-1]['x1']=w['x1']
    else: lines.append(dict(text=w['text'],x0=w['x0'],x1=w['x1'],top=w['top'],bottom=w['bottom']))
# raster placements
ras=[dict(x0=i['x0'],y0=i['top'],x1=i['x1'],y1=i['bottom'],kind='raster',src=i.get('srcsize')) for i in p.images if (i['x1']-i['x0'])<300]
# vector clusters
objs=[dict(x0=c['x0'],y0=c['top'],x1=c['x1'],y1=c['bottom']) for c in p.curves+p.rects+p.lines]
def inter(a,b,gap): return not (a['x1']+gap<b['x0'] or b['x1']+gap<a['x0'] or a['y1']+gap<b['y0'] or b['y1']+gap<a['y0'])
def cluster(items,gap):
    items=[dict(i) for i in items]; merged=True
    while merged:
        merged=False; out=[]
        while items:
            a=items.pop(); i=0
            while i<len(items):
                b=items[i]
                if inter(a,b,gap):
                    a=dict(a,x0=min(a['x0'],b['x0']),y0=min(a['y0'],b['y0']),x1=max(a['x1'],b['x1']),y1=max(a['y1'],b['y1']),kind=a.get('kind','vector') if a.get('kind')==b.get('kind') else 'mixed',src=a.get('src') or b.get('src'))
                    items.pop(i); merged=True
                else: i+=1
            out.append(a)
        items=out
    return items
vec=[dict(o,kind='vector',src=None) for o in cluster(objs,1.5) if (o['x1']-o['x0'])<70 and (o['y1']-o['y0'])<70 and (o['x1']-o['x0'])>3 and (o['y1']-o['y0'])>3]
# drop rules (very thin) 
vec=[v for v in vec if min(v['x1']-v['x0'],v['y1']-v['y0'])>4]
units=cluster(ras+vec,0.5)
units=[u for u in units if (u['x1']-u['x0'])<120 and (u['y1']-u['y0'])<120]
# labels
def label_for(u):
    cy=(u['y0']+u['y1'])/2; h=u['y1']-u['y0']
    right=[l for l in lines if l['x0']>=u['x1']-2 and l['x0']-u['x1']<40 and abs((l['top']+l['bottom'])/2-cy)<max(h*0.75,6)]
    if right:
        right.sort(key=lambda l:(l['x0']-u['x1'])+abs((l['top']+l['bottom'])/2-cy)*0.5); 
        lab=right[0]['text']
        # two-line labels: pick following line directly beneath with same x0
        nxt=[l for l in lines if abs(l['x0']-right[0]['x0'])<3 and 0<l['top']-right[0]['bottom']<4]
        if nxt: lab+=' '+nxt[0]['text']
        return lab,'right'
    cx=(u['x0']+u['x1'])/2
    below=[l for l in lines if 0<l['top']-u['y1']<16 and l['x0']-8<cx<l['x1']+8]
    if below:
        below.sort(key=lambda l:l['top']); lab=below[0]['text']
        nxt=[l for l in lines if 0<l['top']-below[0]['bottom']<4 and l['x0']-8<cx<l['x1']+8]
        if nxt: lab+=' '+nxt[0]['text']
        return lab,'below'
    return '','none'
def slug(t): 
    t=re.sub(r'\(.*?\)','',t); t=re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-'); return t[:48] or 'unlabelled'
def key_alpha(im,soft=(14,60)):
    a=np.asarray(im.convert('RGB')).astype(int)
    border=np.concatenate([a[0],a[-1],a[:,0],a[:,-1]]); bg=np.median(border,axis=0)
    d=np.abs(a-bg).max(axis=2); alpha=np.clip((d-soft[0])/(soft[1]-soft[0]),0,1)
    return Image.fromarray(np.dstack([a,alpha*255]).astype(np.uint8),'RGBA'),tuple(int(v) for v in bg)
units.sort(key=lambda u:(round(u['y0']/12),u['x0']))
os.makedirs('work/icons_parchment',exist_ok=True); os.makedirs('assets/icons',exist_ok=True)
REC=[]; cells=[]
# section header for context: nearest line above that is a known header
HEADERS=['Encounter Cards','Enemy Statistics','Enemy Movement','Enemy Attacks','Equipment Icons','Character Attacks','Other Icons','Conditions']
hdrs=[l for l in lines if l['text'] in HEADERS]
for n,u in enumerate(units):
    lab,how=label_for(u)
    above=[h for h in hdrs if h['bottom']<=u['y0']+2]
    sec=max(above,key=lambda h:h['bottom'])['text'] if above else ''
    if sec=='Enemy Attacks' and u['x0']<300: sec='Enemy Movement'
    m=2.5; bb=(u['x0']-m,u['y0']-m,u['x1']+m,u['y1']+m)
    px=tuple(int(round(v*S)) for v in bb); crop=page.crop(px)
    pid=f'ICO-{n+1:03d}'; sl=slug(lab) if lab else f'unlabelled-{n+1:02d}'
    pf=f'work/icons_parchment/{pid}-{sl}.png'; crop.save(pf)
    al,bg=key_alpha(crop); bbx=al.getchannel('A').getbbox()
    if bbx: al=al.crop((max(0,bbx[0]-3),max(0,bbx[1]-3),min(al.width,bbx[2]+3),min(al.height,bbx[3]+3)))
    af=f'assets/icons/{pid.lower()}-{sl}.png'; al.save(af)
    REC.append(dict(id=pid,name=lab or f'(unlabelled icon {n+1})',section=sec,label_how=how,kind=u['kind'],srcsize=u.get('src'),type='icon',src=TGN,page=32,bbox_pt=tuple(round(v,1) for v in bb),method=f'pdftoppm 600 dpi crop → parchment-key alpha (bg {bg})',file=af,dims=f'{al.width}×{al.height} px',format='png',parchment_crop=pf))
    cells.append((pid,lab,sec,crop))
json.dump(REC,open('work/extraction_records_icons.json','w'),indent=1,default=str)
# contact sheet
cell=150; cols=10; rows=(len(cells)+cols-1)//cols
sheet=Image.new('RGB',(cols*cell,rows*(cell+34)),(70,70,70)); d=ImageDraw.Draw(sheet)
for k,(pid,lab,sec,im) in enumerate(cells):
    t=im.copy(); t.thumbnail((cell-10,cell-10)); x=(k%cols)*cell; y=(k//cols)*(cell+34)
    sheet.paste(t,(x+5,y+5)); d.text((x+4,y+cell-2),pid[4:]+' '+lab[:24],fill=(255,255,0)); d.text((x+4,y+cell+12),lab[24:48] if len(lab)>24 else sec[:22],fill=(180,255,180))
sheet.save('work/icons_contact.png')
print(len(units),'units;',sum(1 for r in REC if r['name'].startswith('(unlabelled')),'unlabelled')
for r in REC: print(r['id'],r['kind'],r['bbox_pt'],'|',r['section'],'|',r['name'],'|',r['dims'])
