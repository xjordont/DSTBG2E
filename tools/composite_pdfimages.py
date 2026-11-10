#!/usr/bin/env python3
"""Pair pdfimages -png output with soft masks (using pdfimages -list order) and
write RGBA composites + a labelled contact sheet for identification.
usage: composite_pdfimages.py <pdf> <page> <imgdir> <outdir>"""
import sys, subprocess, os, glob
from PIL import Image, ImageDraw
pdf, page, imgdir, outdir = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
os.makedirs(outdir, exist_ok=True)
lst = subprocess.run(['pdfimages','-list','-f',str(page),'-l',str(page),pdf],capture_output=True,text=True).stdout.splitlines()[2:]
rows=[]
for ln in lst:
    p=ln.split()
    if len(p)<16: continue
    rows.append(dict(num=int(p[1]),type=p[2],w=int(p[3]),h=int(p[4]),color=p[5]))
# pdfimages -png numbers output sequentially in list order: img-000, img-001...
files=sorted(glob.glob(os.path.join(imgdir,'img-*.png')))
assert len(files)==len(rows), (len(files),len(rows))
out=[]
i=0
while i<len(rows):
    r=rows[i]
    if r['type']!='image': i+=1; continue
    img=Image.open(files[i]).convert('RGB')
    alpha=None
    if i+1<len(rows) and rows[i+1]['type']=='smask':
        m=Image.open(files[i+1]).convert('L')
        if m.size!=img.size: m=m.resize(img.size, Image.LANCZOS)
        alpha=m; i+=2
    else:
        i+=1
    rgba=img.convert('RGBA')
    if alpha is not None: rgba.putalpha(alpha)
    name=f"{r['num']:03d}_{r['w']}x{r['h']}{'_a' if alpha is not None else ''}.png"
    rgba.save(os.path.join(outdir,name))
    out.append((name,rgba))
# contact sheet: skip giant background
cells=[(n,im) for n,im in out if im.width*im.height < 1500*1500]
cell=140; cols=12
rowsN=(len(cells)+cols-1)//cols
sheet=Image.new('RGB',(cols*cell, rowsN*(cell+18)),(90,90,90))
d=ImageDraw.Draw(sheet)
for k,(n,im) in enumerate(cells):
    t=im.copy(); t.thumbnail((cell-8,cell-8))
    x=(k%cols)*cell; y=(k//cols)*(cell+18)
    # checker bg
    bg=Image.new('RGBA',t.size,(200,200,200,255)); bg.alpha_composite(t)
    sheet.paste(bg.convert('RGB'),(x+4,y+4))
    d.text((x+4,y+cell-2),n.split('_')[0]+' '+n.split('_')[1].replace('.png',''),fill=(255,255,0))
sheet.save(os.path.join(outdir,'_contact.png'))
print(len(out),'composites;',len(cells),'on contact sheet')
