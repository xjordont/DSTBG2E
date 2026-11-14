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
    import json
    from PIL import ImageDraw, ImageFilter
    fixes = json.loads((ROOT / 'layout/tuning.json').read_text(encoding='utf-8')).get('icon_fixes', {})
    for p in sorted((ROOT / 'assets/icons').glob('*.png')):
        im = Image.open(p).convert('RGBA')
        # stray marks cut in with the icon (fragments of neighbouring text in the source plate) are erased
        for l, t, r, b in fixes.get(p.stem, {}).get('erase', []):
            ImageDraw.Draw(im).rectangle((int(im.width * l), int(im.height * t), int(im.width * r), int(im.height * b)), fill=(0, 0, 0, 0))
        # an icon cut out with a half-transparent square of parchment around it loses the square: everything
        # joined to a corner and less than fully opaque is cleared
        al = im.getchannel('A'); w, h = im.size
        corners = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
        if max(al.getpixel(c) for c in corners) > 8:
            # background = not fully opaque AND (nearly clear OR close to the corner's own grey); a pale disc
            # behind a silhouette is a different colour and stays
            refs = [im.getpixel(c)[:3] for c in corners if al.getpixel(c) > 8]
            px = im.load(); m = Image.new('L', im.size, 0); mp = m.load()
            for y in range(h):
                for x in range(w):
                    r_, g_, b_, a_ = px[x, y]
                    if a_ < 40 or (a_ < 235 and min(max(abs(r_ - q[0]), abs(g_ - q[1]), abs(b_ - q[2])) for q in refs) < 48):
                        mp[x, y] = 128
            for c in corners:
                if m.getpixel(c) == 128:
                    ImageDraw.floodfill(m, c, 255)
            keep = m.point(lambda v: 0 if v == 255 else 255).filter(ImageFilter.GaussianBlur(0.7))
            im.putalpha(Image.composite(al, Image.new('L', im.size, 0), keep.point(lambda v: 255 if v > 127 else 0)))
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
        im = withhold(im, f.get('masks', []), f.get('badges', []))
        for side in f.get('fade', []):
            im = fade_edge(im, side)
        im.save(OUT / 'fig' / pathlib.Path(f['file']).name); n += 1
    return n


def fade_edge(im, side, share=0.14):
    """Fade one edge of a cut-out to nothing. Used where the source render is cut off by its own frame (a wing
    tip, a sword point): the model then leaves the picture softly instead of ending in a straight cut."""
    im = im.convert('RGBA'); w, h = im.size
    n = max(2, int((w if side in ('left', 'right') else h) * share))
    ramp = Image.new('L', (w, h), 255); px = ramp.load()
    for i in range(n):
        v = int(255 * (i / n) ** 1.5)
        if side == 'right':
            for y in range(h): px[w - 1 - i, y] = v
        elif side == 'left':
            for y in range(h): px[i, y] = v
        elif side == 'top':
            for x in range(w): px[x, i] = v
        else:
            for x in range(w): px[x, h - 1 - i] = v
    from PIL import ImageChops
    im.putalpha(ImageChops.multiply(im.getchannel('A'), ramp))
    return im


def withhold(im, masks, badges):
    """Blank the areas of a plate that are withheld from the book (painted illustrations under provenance
    review) and redraw any call-out badge the blanking removed. Boxes and badge centres are fractions of the
    cropped plate. A mask is {"box": [l, t, r, b], "shape": "rect" | "ellipse", "fill": "auto" | "#rrggbb",
    "feather": px}; "auto" takes the median colour of a thin ring just outside the box."""
    from PIL import ImageDraw, ImageFilter, ImageFont
    if not masks and not badges:
        return im
    im = im.convert('RGBA'); w, h = im.size; orig = im.convert('RGB')
    for m in masks:
        l, t, r, b = m['box']; box = (int(w * l), int(h * t), int(w * r), int(h * b))
        fill = m.get('fill', 'auto')
        if fill == 'auto':
            g = max(4, w // 160); px = im.convert('RGB').load(); ring = []
            for x in range(max(0, box[0] - g), min(w, box[2] + g), 3):
                for y in (max(0, box[1] - g), min(h - 1, box[3] + g - 1)):
                    ring.append(px[x, y])
            for y in range(max(0, box[1] - g), min(h, box[3] + g), 3):
                for x in (max(0, box[0] - g), min(w - 1, box[2] + g - 1)):
                    ring.append(px[x, y])
            ring.sort(key=lambda c: sum(c)); fill = ring[len(ring) // 2]
        if isinstance(fill, dict):
            # ground-matched fill: every row takes the colour the plate has at a clean reference column, so the
            # blanked area follows the card's own gradient and leaves no seam
            rx = int(w * fill['ref_x']); src = orig.load(); layer = Image.new('RGBA', im.size, (0, 0, 0, 0)); lp = layer.load()
            for y in range(max(0, box[1] - 12), min(h, box[3] + 12)):
                px = sorted(src[x, y] for x in range(max(0, rx - 4), min(w, rx + 5)))
                col = px[len(px) // 2] + (255,)
                for x in range(max(0, box[0] - 12), min(w, box[2] + 12)):
                    lp[x, y] = col
            mk = Image.new('L', im.size, 0); d = ImageDraw.Draw(mk)
        else:
            layer = Image.new('RGBA', im.size, fill); mk = Image.new('L', im.size, 0); d = ImageDraw.Draw(mk)
        (d.ellipse if m.get('shape') == 'ellipse' else d.rectangle)(box, fill=255)
        if m.get('feather', 8):
            mk = mk.filter(ImageFilter.GaussianBlur(m.get('feather', 8)))
        im.paste(layer, (0, 0), mk)
        if m.get('outline'):
            d = ImageDraw.Draw(im)
            (d.ellipse if m.get('shape') == 'ellipse' else d.rectangle)(box, outline=m['outline'], width=m.get('outline_width', max(2, w // 300)))
    if badges:
        font_file = ROOT / 'assets/fonts/static/LibreCaslonText-Regular.ttf'
        for x, y, label, *rest in badges:
            rad = int(w * (rest[0] if rest else 0.03)); cx, cy = int(w * x), int(h * y)
            glow = Image.new('RGBA', im.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
            gd.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=(226, 234, 170, 255))
            im.alpha_composite(glow.filter(ImageFilter.GaussianBlur(max(1, rad // 9))))
            font = ImageFont.truetype(str(font_file), int(rad * 1.45))
            d = ImageDraw.Draw(im); bb = d.textbbox((0, 0), str(label), font=font)
            d.text((cx - (bb[0] + bb[2]) / 2, cy - (bb[1] + bb[3]) / 2), str(label), font=font, fill=(52, 54, 40, 255))
    return im


if __name__ == '__main__':
    print('lava crop', lava(), '· icons trimmed', icons(), '· figures', figures())
