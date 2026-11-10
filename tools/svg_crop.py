#!/usr/bin/env python3
"""Crop a pdftocairo page SVG to a bbox (pt), dropping raster <image>, text glyph <use>,
and any <path> whose coordinate extent lies wholly outside the bbox.
usage: svg_crop.py in.svg out.svg x0 y0 x1 y1 [--keep-text] [--fill COLOUR]
Writes a standalone SVG whose viewBox is the bbox (width/height in pt)."""
import sys, re, xml.etree.ElementTree as ET
NS={'svg':'http://www.w3.org/2000/svg','xlink':'http://www.w3.org/1999/xlink'}
ET.register_namespace('', NS['svg']); ET.register_namespace('xlink', NS['xlink'])
inp,out=sys.argv[1],sys.argv[2]; x0,y0,x1,y1=map(float,sys.argv[3:7])
keep_text='--keep-text' in sys.argv
fill=None
if '--fill' in sys.argv: fill=sys.argv[sys.argv.index('--fill')+1]
num=re.compile(r'-?\d+(?:\.\d+)?(?:e-?\d+)?')
def path_extent(d):
    xs=[];ys=[]
    toks=num.findall(d)
    vals=list(map(float,toks))
    # pdftocairo emits absolute coords in x y pairs for M/L/C/Z; pair them
    for i in range(0,len(vals)-1,2):
        xs.append(vals[i]); ys.append(vals[i+1])
    if not xs: return None
    return min(xs),min(ys),max(xs),max(ys)
tree=ET.parse(inp); root=tree.getroot()
SVG='{%s}'%NS['svg']; XL='{%s}'%NS['xlink']
kept=0; dropped=0
def prune(el, in_defs=False):
    global kept,dropped
    for ch in list(el):
        tag=ch.tag.replace(SVG,'')
        if tag=='image': el.remove(ch); continue
        if tag=='use':
            href=ch.get(XL+'href','')
            if href.startswith('#glyph') and not keep_text: el.remove(ch); continue
            if href.startswith('#source'): el.remove(ch); continue
        if tag=='defs':
            # keep clipPaths, drop glyph groups unless keep_text
            for d in list(ch):
                if d.tag==SVG+'g' and not keep_text: ch.remove(d)
                elif d.tag==SVG+'image': ch.remove(d)
            continue
        if tag=='path' and not in_defs:
            ext=path_extent(ch.get('d',''))
            if ext is None or ext[2]<x0 or ext[0]>x1 or ext[3]<y0 or ext[1]>y1:
                el.remove(ch); dropped+=1; continue
            kept+=1
            if fill and ch.get('fill','none')!='none': ch.set('fill',fill)
        prune(ch, in_defs or tag=='defs')
prune(root)
# remove now-empty groups
def strip_empty(el):
    for ch in list(el):
        strip_empty(ch)
        if ch.tag==SVG+'g' and len(ch)==0: el.remove(ch)
strip_empty(root)
root.set('viewBox',f'{x0} {y0} {x1-x0} {y1-y0}')
root.set('width',f'{x1-x0}pt'); root.set('height',f'{y1-y0}pt')
tree.write(out, xml_declaration=True, encoding='UTF-8')
import os
print(f'{out}: kept {kept} paths, dropped {dropped}, {os.path.getsize(out)//1024} KB')
