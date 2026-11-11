#!/usr/bin/env python3
"""Derive the layout's working images from the logged source assets (never edits the sources).
 - build/tex/lava_scales_clean.jpg : logo-free crop of AST-0142 (the 2017 lava-scale texture carries the game's
   logo lock-up in its upper half; the wordmark is used nominatively only, so banners and the cover use the
   lower, logo-free field of scales)
 - build/icons/*.png : each icon in assets/icons trimmed to its inked bounds, so that inline icons share a
   consistent optical height
Derivatives are regenerated on demand and are not tracked; they are recorded in 22_asset_extraction_log.md."""
import pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'build'


def lava():
    src = Image.open(ROOT / 'assets/textures/ast-0142-lava-scale-cover-texture.png').convert('RGB')
    w, h = src.size
    crop = src.crop((int(w * 0.13), int(h * 0.455), int(w * 0.87), int(h * 0.845)))
    (OUT / 'tex').mkdir(parents=True, exist_ok=True)
    crop.save(OUT / 'tex/lava_scales_clean.jpg', quality=90)
    return crop.size


def icons():
    (OUT / 'icons').mkdir(parents=True, exist_ok=True)
    n = 0
    for p in sorted((ROOT / 'assets/icons').glob('*.png')):
        im = Image.open(p).convert('RGBA')
        box = im.getchannel('A').point(lambda a: 255 if a > 12 else 0).getbbox()
        if box:
            im = im.crop(box)
        if im.height > 160:   # 160 px is ample for a 10 pt inline icon at 600 dpi
            im = im.resize((max(1, round(im.width * 160 / im.height)), 160), Image.LANCZOS)
        im.save(OUT / 'icons' / p.name); n += 1
    return n


def figures():
    """Figures placed by layout/tuning.json: composite onto the parchment ground and apply the crop given there
    (fractions of width and height: left, top, right, bottom). Written to build/fig/<source name>.png."""
    import json
    tun = json.loads((ROOT / 'layout/tuning.json').read_text(encoding='utf-8'))
    (OUT / 'fig').mkdir(parents=True, exist_ok=True); n = 0
    for f in tun.get('figures', []):
        im = Image.open(ROOT / f['file']).convert('RGBA')
        if f.get('crop'):
            l, t, r, b = f['crop']; w, h = im.size
            im = im.crop((int(w * l), int(h * t), int(w * r), int(h * b)))
        if max(im.size) > 1600:
            s = 1600 / max(im.size); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        im.save(OUT / 'fig' / pathlib.Path(f['file']).name); n += 1
    return n


if __name__ == '__main__':
    print('lava crop', lava(), '· icons trimmed', icons(), '· figures', figures())
