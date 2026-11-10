#!/usr/bin/env python3
"""Batch 1: logo, ornaments, textures, diagrams, specimens, cover art.
Records every extraction in work/extraction_records.json (list of dicts)."""
import os, json, subprocess, shutil, sys
import numpy as np
from PIL import Image
import pdfplumber
Image.MAX_IMAGE_PIXELS=None
ROOT='/home/user/DSTBG2E'; os.chdir(ROOT)
TG='work/pdf_decrypted/DS-TG-Rulebook-Compressed_compressed.pdf'
FAQ='work/pdf_decrypted/Dark_Souls_The_Board_Game_FAQ.pdf'
CORE='sources/DS-Core-Rules-lores.pdf'
TGN='DS-TG-Rulebook-Compressed_compressed.pdf'; FAQN='Dark_Souls_The_Board_Game_FAQ.pdf'; COREN='DS-Core-Rules-lores.pdf'
REC=[]
def rec(**k):
    if 'file' in k and k['file'] and os.path.exists(k['file']):
        im=Image.open(k['file']) if k['file'].endswith('.png') else None
        if im: k['dims']=f'{im.width}×{im.height} px'
        k['bytes']=os.path.getsize(k['file'])
    REC.append(k); print(k.get('id'),k.get('name'),'->',k.get('file'),k.get('dims',''))
def pt2px(b,dpi): s=dpi/72; return tuple(int(round(v*s)) for v in b)
def render_crop(pdf,page,bbox,dpi,out):
    x0,y0,x1,y1=pt2px(bbox,dpi)
    base=out[:-4]
    subprocess.run(['pdftoppm','-r',str(dpi),'-f',str(page),'-l',str(page),'-png','-x',str(x0),'-y',str(y0),'-W',str(x1-x0),'-H',str(y1-y0),'-singlefile',pdf,base],check=True)
    return out
def key_alpha(im, bg=None, soft=(16,70), force_rgb=None):
    a=np.asarray(im.convert('RGB')).astype(int)
    if bg is None:
        border=np.concatenate([a[0],a[-1],a[:,0],a[:,-1]]); bg=np.median(border,axis=0)
    d=np.abs(a-bg).max(axis=2)
    alpha=np.clip((d-soft[0])/(soft[1]-soft[0]),0,1)
    rgb=a.copy()
    if force_rgb is not None: rgb[:]=force_rgb
    rgba=np.dstack([rgb,(alpha*255)]).astype(np.uint8)
    return Image.fromarray(rgba,'RGBA'), tuple(int(v) for v in bg)
def trim(im,pad=0):
    bb=im.getchannel('A').getbbox()
    if not bb: return im
    bb=(max(0,bb[0]-pad),max(0,bb[1]-pad),min(im.width,bb[2]+pad),min(im.height,bb[3]+pad))
    return im.crop(bb)
def svgcrop(src,out,bbox,extra=()):
    subprocess.run(['python3','tools/svg_crop.py',src,out,*map(str,bbox),*extra],check=True)
SP='/tmp/claude-0/-home-user-DSTBG2E/ff710c3a-8948-5673-b38b-8c94b4dc4aee/scratchpad/b1'; os.makedirs(SP,exist_ok=True)

# ---------------- LOGOS ----------------
A='assets/logos/'
bb=(176,41,392,134)
svgcrop('work/svg/faq_p1.svg',A+'ast-0001-ds-tbg-logo-black.svg',bb)
rec(id='AST-0001',name='Dark Souls: The Board Game logo lock-up (vector, black)',type='logo',src=FAQN,page=1,bbox_pt=bb,method='pdftocairo -svg p.1 → tools/svg_crop.py (image/text removed, 1 compound path kept)',file=A+'ast-0001-ds-tbg-logo-black.svg',format='svg')
png=render_crop(FAQ,1,bb,1200,SP+'/logo.png')
im,bg=key_alpha(Image.open(png),soft=(20,90),force_rgb=(0,0,0)); im=trim(im,8); im.save(A+'ast-0002-ds-tbg-logo-black.png')
rec(id='AST-0002',name='Dark Souls: The Board Game logo lock-up (raster, black on transparent)',type='logo',src=FAQN,page=1,bbox_pt=bb,method=f'pdftoppm 1200 dpi crop → parchment-key alpha (bg {bg}) → trim',file=A+'ast-0002-ds-tbg-logo-black.png',format='png')
w=im.copy(); arr=np.asarray(w).copy(); arr[...,:3]=255; Image.fromarray(arr,'RGBA').save(A+'ast-0003-ds-tbg-logo-white.png')
rec(id='AST-0003',name='Dark Souls: The Board Game logo lock-up (raster, white on transparent)',type='logo',src=FAQN,page=1,bbox_pt=bb,method='AST-0002 alpha with RGB forced to white (matches cover usage)',file=A+'ast-0003-ds-tbg-logo-white.png',format='png')
bb=(113,475,518,647)
svgcrop('work/svg/tg_p1.svg',A+'ast-0004-ds-tbg-logo-white-cover.svg',bb)
rec(id='AST-0004',name='Logo lock-up as used on covers (vector, white fill)',type='logo',src=TGN,page=1,bbox_pt=bb,method='pdftocairo -svg p.1 → svg_crop (cover raster removed)',file=A+'ast-0004-ds-tbg-logo-white-cover.svg',format='svg')
shutil.copy('work/pdfimages/DS-TG-Rulebook-Compressed_compressed_p01/img-001.png',A+'ast-0005-logo-glow-mask.png')
rec(id='AST-0005',name='Logo glow (soft white halo raster placed behind cover logo)',type='logo',src=TGN,page=1,bbox_pt=None,method='pdfimages -png p.1 image #1 (1276×629 grey, 200 ppi)',file=A+'ast-0005-logo-glow-mask.png',format='png')

# ---------------- ORNAMENTS ----------------
O='assets/ornaments/'
bb=(42,168,55,181)
svgcrop('work/svg/faq_p1.svg',O+'ast-0010-knot-square.svg',bb)
rec(id='AST-0010',name='Celtic-knot square ornament (rule terminal / corner)',type='ornament',src=FAQN,page=1,bbox_pt=bb,method='pdftocairo -svg → svg_crop (12 paths)',file=O+'ast-0010-knot-square.svg',format='svg')
png=render_crop(FAQ,1,bb,2400,SP+'/knot.png'); im,bg=key_alpha(Image.open(png),soft=(20,90),force_rgb=(0,0,0)); trim(im,4).save(O+'ast-0011-knot-square.png')
rec(id='AST-0011',name='Celtic-knot square ornament (raster, black on transparent)',type='ornament',src=FAQN,page=1,bbox_pt=bb,method=f'pdftoppm 2400 dpi crop → parchment-key alpha (bg {bg})',file=O+'ast-0011-knot-square.png',format='png')
bb=(344,440.5,356.5,453.5)
svgcrop('work/svg/tg_p30.svg',O+'ast-0012-compass-corner.svg',bb)
rec(id='AST-0012',name='Compass/diamond corner ornament (example-box and art-frame corners)',type='ornament',src=TGN,page=30,bbox_pt=bb,method='pdftocairo -svg → svg_crop',file=O+'ast-0012-compass-corner.svg',format='svg')
png=render_crop(TG,30,bb,2400,SP+'/compass.png'); im,bg=key_alpha(Image.open(png),soft=(20,90),force_rgb=(0,0,0)); trim(im,4).save(O+'ast-0013-compass-corner.png')
rec(id='AST-0013',name='Compass/diamond corner ornament (raster)',type='ornament',src=TGN,page=30,bbox_pt=bb,method=f'pdftoppm 2400 dpi crop → parchment-key alpha (bg {bg})',file=O+'ast-0013-compass-corner.png',format='png')
bb=(95,61,580,77)
svgcrop('work/svg/tg_p30.svg',O+'ast-0014-chapter-title-rule-lockup.svg',bb)
rec(id='AST-0014',name='Chapter/section title rule lock-up: knot – rule – [title] – rule – knot (vector, title text removed)',type='ornament',src=TGN,page=30,bbox_pt=bb,method='pdftocairo -svg → svg_crop (text glyphs dropped)',file=O+'ast-0014-chapter-title-rule-lockup.svg',format='svg')
bb=(95,61,249,77)
png=render_crop(TG,30,bb,1200,SP+'/rule.png'); im,bg=key_alpha(Image.open(png),soft=(20,90),force_rgb=(0,0,0)); trim(im,4).save(O+'ast-0015-title-rule-left-half.png')
rec(id='AST-0015',name='Title rule, left half (knot + hairline), raster',type='ornament',src=TGN,page=30,bbox_pt=bb,method=f'pdftoppm 1200 dpi crop → parchment-key alpha (bg {bg}); mirror for right half',file=O+'ast-0015-title-rule-left-half.png',format='png')
bb=(95,760,580,776)
svgcrop('work/svg/tg_p30.svg',O+'ast-0016-folio-footer-rule-lockup.svg',bb)
rec(id='AST-0016',name='Folio footer lock-up: knot – rule – [page number] – rule (vector, number removed)',type='ornament',src=TGN,page=30,bbox_pt=bb,method='pdftocairo -svg → svg_crop',file=O+'ast-0016-folio-footer-rule-lockup.svg',format='svg')
# example box frame
bb=(343,439,580,521)
svgcrop('work/svg/tg_p30.svg','assets/frames/ast-0020-example-box-frame-small.svg',bb)
rec(id='AST-0020',name='Example/sidebar box frame: compass corners + hairline rules (vector template, content removed)',type='frame',src=TGN,page=30,bbox_pt=bb,method='pdftocairo -svg → svg_crop (icons inside are rasters, dropped automatically)',file='assets/frames/ast-0020-example-box-frame-small.svg',format='svg')
# section divider on TG p3: detect line ~300-360pt long
with pdfplumber.open(TG) as pdf:
    p=pdf.pages[2]
    cands=[l for l in p.lines if 250<(l['x1']-l['x0'])<420 and 150<l['top']<700]
    if cands:
        l=cands[0]; bb=(l['x0']-17,l['top']-8,l['x1']+17,l['top']+8)
        svgcrop('work/svg/tg_p3.svg',O+'ast-0017-section-divider-knot-rule-knot.svg',bb)
        rec(id='AST-0017',name='Mid-page section divider: knot – rule – knot',type='ornament',src=TGN,page=3,bbox_pt=tuple(round(v,1) for v in bb),method='pdftocairo -svg → svg_crop',file=O+'ast-0017-section-divider-knot-rule-knot.svg',format='svg')
        png=render_crop(TG,3,bb,1200,SP+'/div.png'); im,bg=key_alpha(Image.open(png),soft=(20,90),force_rgb=(0,0,0)); trim(im,4).save(O+'ast-0018-section-divider-knot-rule-knot.png')
        rec(id='AST-0018',name='Mid-page section divider (raster)',type='ornament',src=TGN,page=3,bbox_pt=tuple(round(v,1) for v in bb),method=f'pdftoppm 1200 dpi crop → parchment-key alpha (bg {bg})',file=O+'ast-0018-section-divider-knot-rule-knot.png',format='png')
    else: print('no divider line found on p3', [(l['x0'],l['x1'],l['top']) for l in p.lines])
# big art frame corners from TG p30 whole page example frame? use core p18 frame (compass corners) - vector on core_p27? skip; use TG p26 table frame
with pdfplumber.open(TG) as pdf:
    p=pdf.pages[25]
    # table rules on p26 right column (Base to Tier table)
    ls=[l for l in p.lines if l['x0']>330 and 300<l['top']<420]
    if ls:
        x0=min(l['x0'] for l in ls)-14; x1=max(l['x1'] for l in ls)+14; y0=min(l['top'] for l in ls)-12; y1=max(l['bottom'] for l in ls)+12
        bb=(x0,y0,x1,y1)
        svgcrop('work/svg/tg_p26.svg','assets/frames/ast-0021-table-frame-knot-corners.svg',bb)
        rec(id='AST-0021',name='Table frame: knot corners + horizontal rules (vector template, text removed)',type='frame',src=TGN,page=26,bbox_pt=tuple(round(v,1) for v in bb),method='pdftocairo -svg → svg_crop',file='assets/frames/ast-0021-table-frame-knot-corners.svg',format='svg')
        png=render_crop(TG,26,bb,600,SP+'/table.png'); Image.open(png).save('assets/type-specimens/ast-0070-table-specimen-firekeeper-costs.png')
        rec(id='AST-0070',name='Table styling specimen (Firekeeper upgrade costs): knot corners, hairline rules, Caslon body',type='typographic specimen',src=TGN,page=26,bbox_pt=tuple(round(v,1) for v in bb),method='pdftoppm 600 dpi crop',file='assets/type-specimens/ast-0070-table-specimen-firekeeper-costs.png',format='png')

# ---------------- TEXTURES ----------------
T='assets/textures/'
shutil.copy('work/pdfimages/DS-TG-Rulebook-Compressed_compressed_p02/img-000.png',T+'ast-0030-parchment-book-spread-bg.png')
rec(id='AST-0030',name='Open-book parchment page background, full spread (2022 print master)',type='texture',src=TGN,page=2,bbox_pt=None,method='pdfimages -png p.2 image #0 (5174×3378 CMYK JPEG @300 ppi → sRGB)',file=T+'ast-0030-parchment-book-spread-bg.png',format='png')
im=Image.open(T+'ast-0030-parchment-book-spread-bg.png'); im.crop((im.width//2,0,im.width,im.height)).save(T+'ast-0031-parchment-right-page-bg.png')
rec(id='AST-0031',name='Open-book parchment background, right-hand page only',type='texture',src=TGN,page=2,bbox_pt=None,method='AST-0030 cropped to right half (x 2587–5174 px)',file=T+'ast-0031-parchment-right-page-bg.png',format='png')
im.crop((0,0,im.width//2,im.height)).save(T+'ast-0032-parchment-left-page-bg.png')
rec(id='AST-0032',name='Open-book parchment background, left-hand page only',type='texture',src=TGN,page=2,bbox_pt=None,method='AST-0030 cropped to left half (x 0–2587 px)',file=T+'ast-0032-parchment-left-page-bg.png',format='png')
shutil.copy('work/pdfimages/DS-Core-Rules-lores_p01/img-001.png',T+'ast-0033-lava-scale-cover-texture.png')
rec(id='AST-0033',name='Cracked lava-scale cover texture (2017 box-lid artwork; SFG "Texture Design" credit)',type='texture',src=COREN,page=1,bbox_pt=None,method='pdfimages -png p.1 image #1 (1245×1688 RGB JPEG @150 ppi)',file=T+'ast-0033-lava-scale-cover-texture.png',format='png')
bc=Image.open('work/pdfimages/DS-TG-Rulebook-Compressed_compressed_p32/img-000.png'); arr=np.asarray(bc.convert('L')); centre=arr[arr.shape[0]//3:2*arr.shape[0]//3, arr.shape[1]//3:2*arr.shape[1]//3].mean(); edge=arr[:40].mean()
shutil.copy('work/pdfimages/DS-TG-Rulebook-Compressed_compressed_p32/img-000.png',T+'ast-0034-back-cover-dark-stone-bg.png')
rec(id='AST-0034',name='Back-cover dark stone/leather background'+(' (includes baked-in parchment panel)' if centre>150 else ''),type='texture',src=TGN,page=32,bbox_pt=None,method=f'pdfimages -png p.32 image #0 (1312×1690 CMYK @150 ppi); centre luminance {centre:.0f}, edge {edge:.0f}',file=T+'ast-0034-back-cover-dark-stone-bg.png',format='png')
shutil.copy('work/pdfimages/DS-Core-Rules-lores_p01/img-000.png',T+'ast-0035-parchment-spread-bg-2017.png')
rec(id='AST-0035',name='Open-book parchment spread background, 2017 web edition (RGB, lower res)',type='texture',src=COREN,page=1,bbox_pt=None,method='pdfimages -png p.1 image #0 (2516×1719 RGB @150 ppi)',file=T+'ast-0035-parchment-spread-bg-2017.png',format='png')

# ---------------- DIAGRAMS ----------------
D='assets/diagrams/'
def diag(idn,name,pdf,pdfn,page,bb,dpi,fn,note=''):
    out=render_crop(pdf,page,bb,dpi,SP+'/d.png'); shutil.copy(out,D+fn)
    rec(id=idn,name=name,type='diagram',src=pdfn,page=page,bbox_pt=tuple(round(v,1) for v in bb),method=f'pdftoppm {dpi} dpi crop'+(' — '+note if note else ''),file=D+fn,format='png')
diag('AST-0040','Character dashboard anatomy (Cleric) with numbered call-outs 1–10',TG,TGN,8,(78,330,600,748),400,'ast-0040-character-dashboard-anatomy-2022.png')
diag('AST-0041','Equipment card anatomy (Shortbow) with call-outs 1–11',TG,TGN,10,(136,335,292,548),600,'ast-0041-equipment-card-anatomy-2022.png')
diag('AST-0042','Campaign dashboard anatomy (two strips) with call-outs 1–9',TG,TGN,13,(45,113,540,400),400,'ast-0042-campaign-dashboard-anatomy-2022.png')
diag('AST-0043','Encounter card anatomy (Grave Matters) with call-outs 1–8',TG,TGN,16,(375,335,548,605),600,'ast-0043-encounter-card-anatomy-2022.png')
with pdfplumber.open(TG) as pdf:
    p=pdf.pages[23]; ims=[i for i in p.images if 100<(i['x1']-i['x0'])<400]
    if ims:
        i=ims[0]; bb=(i['x0']-22,i['top']-18,i['x1']+22,i['bottom']+14)
        diag('AST-0044','Enemy data card anatomy (Skeleton Soldier) with call-outs 1–10',TG,TGN,24,bb,600,'ast-0044-enemy-data-card-anatomy-2022.png')
    # movement symbol diagram: curves cluster in right column upper
    cs=[c for c in p.curves if c['x0']>380 and 170<c['top']<300]
    if cs:
        bb=(min(c['x0'] for c in cs)-14,min(c['top'] for c in cs)-14,max(c['x1'] for c in cs)+14,max(c['bottom'] for c in cs)+14)
        diag('AST-0045','Enemy movement symbol anatomy (Move icon with call-outs 1–5)',TG,TGN,24,bb,600,'ast-0045-enemy-movement-symbol-anatomy.png')
    p=pdf.pages[24]
    cs=[c for c in p.curves if c['x0']<300 and 230<c['top']<340]
    if cs:
        bb=(min(c['x0'] for c in cs)-14,min(c['top'] for c in cs)-14,max(c['x1'] for c in cs)+14,max(c['bottom'] for c in cs)+14)
        diag('AST-0046','Enemy attack symbol anatomy (Attack icon with call-outs 1–4)',TG,TGN,25,bb,600,'ast-0046-enemy-attack-symbol-anatomy.png')
    p=pdf.pages[27]; ims=sorted([i for i in p.images if 100<(i['x1']-i['x0'])<400],key=lambda i:i['top'])
    for k,i in enumerate(ims[:2]):
        bb=(i['x0']-22,i['top']-18,i['x1']+22,i['bottom']+14)
        nm='Boss data card anatomy (Gravelord Nito) with call-outs 1–10' if (i['x1']-i['x0'])>(i['bottom']-i['top'])*0.6 and i['x0']<300 else 'Boss behaviour card anatomy (Death\'s Embrace) with call-outs 1–5'
        fn='ast-0047-boss-data-card-anatomy-2022.png' if 'data' in nm else 'ast-0048-boss-behaviour-card-anatomy-2022.png'
        diag('AST-0047' if 'data' in nm else 'AST-0048',nm,TG,TGN,28,bb,600,fn)
diag('AST-0049','Boss arcs diagram A: boss base with four arcs on tile (front/left/right/back)',TG,TGN,29,(53,412,283,626),400,'ast-0049-boss-arcs-tile-diagram-a.png')
diag('AST-0050','Boss arcs diagram B: arcs with highlighted node sets',TG,TGN,29,(301,376,531,596),400,'ast-0050-boss-arcs-tile-diagram-b.png')
diag('AST-0051','Boss base photo showing arc markings (X on base)',TG,TGN,29,(106,95,258,202),400,'ast-0051-boss-base-arc-markings.png')
diag('AST-0052','Boss activation worked example, six stages (full-page diagram)',TG,TGN,30,(55,40,585,790),300,'ast-0052-boss-activation-example-6-stages.png')
diag('AST-0053','Movement example: walk + three runs on a tile (arrows over tile)',TG,TGN,20,(300,560,590,780),400,'ast-0053-movement-example-tile.png')
diag('AST-0054','Getting Underway: encounter track + card draw diagram',TG,TGN,16,(55,440,335,790),400,'ast-0054-encounter-track-getting-underway.png')
# core 2017 anatomy diagrams
with pdfplumber.open(CORE) as pdf:
    for pg,idn,nm,fn in [(11,'AST-0055','Character board anatomy (Herald, 2017) call-outs 1–11','ast-0055-character-board-anatomy-2017.png'),(13,'AST-0056','Bonfire tile anatomy (2017) call-outs 1–6','ast-0056-bonfire-tile-anatomy-2017.png'),(12,'AST-0057','Equipment card anatomy (Greataxe, 2017) call-outs 1–12','ast-0057-equipment-card-anatomy-2017.png'),(27,'AST-0058','Boss arcs diagram (Dancer, 2017): arcs and node colours','ast-0058-boss-arcs-diagram-2017.png')]:
        p=pdf.pages[pg-1]; ims=[i for i in p.images if 100<(i['x1']-i['x0'])<500 and (i['bottom']-i['top'])>80]
        if pg==27: ims=[i for i in ims if i['top']>400]
        if pg==12: ims=[i for i in ims if i['x0']<350]
        if not ims: print('no image for core p',pg); continue
        ims.sort(key=lambda i:-(i['x1']-i['x0'])*(i['bottom']-i['top'])); i=ims[0]
        bb=(i['x0']-20,i['top']-16,i['x1']+20,i['bottom']+14)
        diag(idn,nm,CORE,COREN,pg,bb,600 if pg in (12,) else 400,fn)
# icon key pages (whole panels)
r=Image.open('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p32_600dpi-32.png').convert('L'); a=np.asarray(r); s=600/72
mask=a>200; mask[:int(30*s)]=False
ys,xs=np.where(mask); bb=(xs.min()/s,ys.min()/s,xs.max()/s,ys.max()/s)
Image.open('work/renders/hires/DS-TG-Rulebook-Compressed_compressed_p32_600dpi-32.png').crop((xs.min(),ys.min(),xs.max(),ys.max())).save(D+'ast-0059-icon-key-reference-page-2022.png')
rec(id='AST-0059',name='Icon key / reference page panel (2022 back cover) — complete symbol legend',type='diagram',src=TGN,page=32,bbox_pt=tuple(round(v,1) for v in bb),method='600 dpi render; panel bbox auto-detected as bright region (L>200) excluding top 30 pt',file=D+'ast-0059-icon-key-reference-page-2022.png',format='png')
diag('AST-0060','Icon key / reference page (2017 back cover)',CORE,COREN,40,(40,38,555,770),400,'ast-0060-icon-key-reference-page-2017.png')

# ---------------- TYPE SPECIMENS ----------------
S='assets/type-specimens/'
def spec(idn,name,pdf,pdfn,page,bb,dpi,fn,note=''):
    out=render_crop(pdf,page,bb,dpi,SP+'/s.png'); shutil.copy(out,S+fn)
    rec(id=idn,name=name,type='typographic specimen',src=pdfn,page=page,bbox_pt=tuple(round(v,1) for v in bb),method=f'pdftoppm {dpi} dpi crop'+(' — '+note if note else ''),file=S+fn,format='png')
with pdfplumber.open(TG) as pdf:
    p=pdf.pages[12]
    ch=[c for c in p.chars if 'Optimus' in c['fontname'] and c['size']>18]
    bb=(min(c['x0'] for c in ch)-70,min(c['top'] for c in ch)-8,max(c['x1'] for c in ch)+70,max(c['bottom'] for c in ch)+8)
    spec('AST-0071','Chapter title specimen: OptimusPrinceps caps with rule + knot terminals ("The Campaign Dashboard")',TG,TGN,13,bb,600,'ast-0071-chapter-title-optimusprinceps.png',f'title size {ch[0]["size"]:.1f} pt')
    ch=[c for c in p.chars if 'ACaslonPro-Regular' in c['fontname'] and c['x0']<300 and 440<c['top']<560]
    bb=(min(c['x0'] for c in ch)-6,min(c['top'] for c in ch)-6,max(c['x1'] for c in ch)+6,max(c['bottom'] for c in ch)+6)
    sizes=sorted(set(round(c['size'],1) for c in ch))
    spec('AST-0072','Body text specimen: Adobe Caslon Pro Regular + Bold run-in heads, numbered list',TG,TGN,13,bb,600,'ast-0072-body-text-caslon.png',f'sizes {sizes} pt')
    p=pdf.pages[15]
    ch=[c for c in p.chars if 'Optimus' in c['fontname'] and 9<c['size']<18 and c['top']<140]
    bb=(min(c['x0'] for c in ch)-10,min(c['top'] for c in ch)-6,max(c['x1'] for c in ch)+10,max(c['bottom'] for c in ch)+6)
    spec('AST-0073','Sub-head specimen: OptimusPrinceps small caps ("Exploration Basics / Encounter Cards")',TG,TGN,16,bb,600,'ast-0073-subhead-optimusprinceps.png',f'size {sorted(set(round(c["size"],1) for c in ch))} pt')
    p=pdf.pages[25]
    ch=[c for c in p.chars if 'Italic' in c['fontname'] and c['x0']>330 and c['top']>600]
    if ch:
        bb=(min(c['x0'] for c in ch)-6,min(c['top'] for c in ch)-6,max(c['x1'] for c in ch)+6,max(c['bottom'] for c in ch)+6)
        spec('AST-0074','Caption / flavour specimen: Adobe Caslon Pro Italic',TG,TGN,26,bb,600,'ast-0074-caption-caslon-italic.png',f'size {sorted(set(round(c["size"],1) for c in ch))} pt')
    p=pdf.pages[12]
    spec('AST-0075','Folio specimen: footer rule with knot and page number',TG,TGN,13,(90,757,585,781),600,'ast-0075-folio-footer.png')
    p=pdf.pages[0]
    ch=[c for c in p.chars if 'Optimus' in c['fontname']]
    bb=(min(c['x0'] for c in ch)-20,min(c['top'] for c in ch)-10,max(c['x1'] for c in ch)+20,max(c['bottom'] for c in ch)+10)
    spec('AST-0076','Cover subtitle specimen: "Tomb of Giants" in OptimusPrinceps SemiBold, white',TG,TGN,1,bb,600,'ast-0076-cover-subtitle-optimusprinceps-semibold.png',f'size {sorted(set(round(c["size"],1) for c in ch))} pt')
    p=pdf.pages[2]
    ch=[c for c in p.chars if 'Italic' in c['fontname'] and c['top']<300]
    bb=(min(c['x0'] for c in ch)-6,min(c['top'] for c in ch)-6,max(c['x1'] for c in ch)+6,max(c['bottom'] for c in ch)+6)
    spec('AST-0077','Introduction / lore block specimen: Caslon Italic paragraphs',TG,TGN,3,bb,400,'ast-0077-lore-block-caslon-italic.png')

# ---------------- ART ----------------
AR='assets/art/'
png=render_crop(CORE,1,(0,0,595.276,807.874),300,SP+'/cover.png'); shutil.copy(png,AR+'ast-0080-core-2017-front-cover-composition.png')
rec(id='AST-0080',name='2017 core rulebook front cover composition (lava-scale texture + white logo lock-up)',type='art',src=COREN,page=1,bbox_pt=(0,0,595.3,807.9),method='pdftoppm 300 dpi full page',file=AR+'ast-0080-core-2017-front-cover-composition.png',format='png')
shutil.copy('work/pdfimages/DS-TG-Rulebook-Compressed_compressed_p01/img-000.png',AR+'ast-0081-tg-2022-cover-art-gravelord-nito.png')
rec(id='AST-0081',name='2022 Tomb of Giants cover art (Gravelord Nito on black) — PROVENANCE REVIEW',type='art',src=TGN,page=1,bbox_pt=None,method='pdfimages -png p.1 image #0 (1312×1690 CMYK @150 ppi)',file=AR+'ast-0081-tg-2022-cover-art-gravelord-nito.png',format='png')

json.dump(REC,open('work/extraction_records_batch1.json','w'),indent=1,default=str)
print('\nrecords:',len(REC))
