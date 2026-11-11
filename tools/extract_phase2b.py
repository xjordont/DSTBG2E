#!/usr/bin/env python3
"""Phase 2B asset extraction: component imagery (hero images), diagrams, icons, frames, textures.

Embedded image objects are decoded with `pdfimages -png` (poppler's colour conversion, i.e. the
same colours as the Phase 0 extractions and the page renders) and paired with their soft masks by
object ID from `pdfimages -list`; PyMuPDF is used only to read placement rectangles and draw order.
One record per written file goes to work/extraction_records_phase2b.json (id AST-NNNN.k, parent =
catalogue Asset ID). Files tracked by git under assets/ are never overwritten.

Watermark rule: the personalised PDFs carry a purchaser line (a text object) at y 11-20 pt of every
page. Embedded image objects cannot contain it. Page-region renders are made from a temporary copy
in which that text is redacted, and the crop box is also asserted clear of the top 30 pt and the
bottom 30 pt of the page. The line's text is never written to a record.

usage: extract_phase2b.py [photo] [other] [heroes]   (default: all three, in that order)
  photo  = priority 1 component imagery (assets/photography) incl. composites
  other  = diagrams, icons, frames/card backs, textures, statuses and provenance-review entries
  heroes = layout/hero_assets.json
"""
import os, sys, json, glob, subprocess, warnings
warnings.simplefilter('ignore')
import fitz
import numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DEC = 'work/pdf_decrypted/'
SRC = {  # key -> (working copy, source file name)
    'TG': (DEC + 'DS-TG-Rulebook-Compressed_compressed.pdf', 'DS-TG-Rulebook-Compressed_compressed.pdf'),
    'CORE': ('sources/DS-Core-Rules-lores.pdf', 'DS-Core-Rules-lores.pdf'),
    'PH': (DEC + 'DS-Phantoms-Rules-lores.pdf', 'DS-Phantoms-Rules-lores.pdf'),
    'BDK': (DEC + 'DS-BDK-Rules-web.pdf', 'DS-BDK-Rules-web.pdf'),
    'EC': (DEC + 'DS-EC-Rules-Web.pdf', 'DS-EC-Rules-Web.pdf'),
    'DR': (DEC + 'DS-Darkroot-Rules-web.pdf', 'DS-Darkroot-Rules-web.pdf'),
    'IK': (DEC + 'DS-IronKeep-Rules-Web.pdf', 'DS-IronKeep-Rules-Web.pdf'),
    'EX': (DEC + 'DS-Explorers-Rules-Web.pdf', 'DS-Explorers-Rules-Web.pdf'),
    'CH': (DEC + 'DS-Characters-Rules-lores.pdf', 'DS-Characters-Rules-lores.pdf'),
}
RECFILE = 'work/extraction_records_phase2b.json'
SCRATCH = 'work/pdfimages/phase2b'
TRACKED = set(subprocess.run(['git', 'ls-files', 'assets'], capture_output=True, text=True).stdout.split('\n'))
RECS = {r['id']: r for r in json.load(open(RECFILE))} if os.path.exists(RECFILE) else {}
PREV_FILES = {r['file'] for r in RECS.values() if r.get('file')}
PRODUCED = []
_docs, _pi = {}, {}


def doc(key):
    if key not in _docs:
        _docs[key] = fitz.open(SRC[key][0])
    return _docs[key]


def idkey(i):
    a, _, k = i.partition('.')
    return (int(a[4:]), 1000 + int(k[1:]) if k.startswith('R') else int(k or 0))


def save_records():
    for r in RECS.values():  # the purchaser line must never reach a record
        s = json.dumps(r)
        assert '@' not in s and 'Generated for' not in s, r['id']
    txt = json.dumps([RECS[k] for k in sorted(RECS, key=idkey)], indent=1, ensure_ascii=False)   # serialise first: never leave a partial file
    with open(RECFILE + '.tmp', 'w') as f:
        f.write(txt)
    os.replace(RECFILE + '.tmp', RECFILE)


def pdfimages(key, page):
    """{object id: {'image': (png, num, colour), 'smask': (png, num, colour)}} for one page."""
    if (key, page) not in _pi:
        out = f'{SCRATCH}/{key}_p{page:02d}'
        os.makedirs(out, exist_ok=True)
        path = SRC[key][0]
        rows = [l.split() for l in subprocess.run(['pdfimages', '-list', '-f', str(page), '-l', str(page), path],
                                                 capture_output=True, text=True).stdout.splitlines()[2:]]
        files = sorted(glob.glob(out + '/img-*.png'))
        if len(files) != len(rows):
            for f in files:
                os.remove(f)
            subprocess.run(['pdfimages', '-png', '-f', str(page), '-l', str(page), path, out + '/img'], check=True)
            files = sorted(glob.glob(out + '/img-*.png'))
        assert len(files) == len(rows), (key, page, len(files), len(rows))
        m = {}
        for r, f in zip(rows, files):
            m.setdefault(int(r[10]), {}).setdefault(r[2], (f, int(r[1]), r[5]))
        _pi[(key, page)] = m
    return _pi[(key, page)]


def emb(key, page, xref):
    """Embedded image object as RGBA (soft mask composited when present) + info dict."""
    e = pdfimages(key, page)[xref]
    im = Image.open(e['image'][0]).convert('RGB')
    info = dict(xref=xref, pdfimages_num=e['image'][1], colour=e['image'][2], native=f'{im.width}×{im.height}', has_mask=False)
    im = im.convert('RGBA')
    if 'smask' in e:
        a = Image.open(e['smask'][0]).convert('L')
        if a.size != im.size:
            a = a.resize(im.size, Image.LANCZOS)
        im.putalpha(a)
        info['has_mask'] = True
        info['smask_pdfimages_num'] = e['smask'][1]
    return im, info


def trim(im, thr=0):
    if im.mode != 'RGBA':
        return im
    bb = im.getchannel('A').point(lambda v: 255 if v > thr else 0).getbbox()
    return im.crop(bb) if bb else im


def clipped_edges(im):
    """Sides of an untrimmed RGBA object on which the subject is cut by the image boundary: a run of opaque
    border pixels at least 10 px and 6 % of that side long that is not just a tangent contact (the run 4 px
    further in is not much longer). Fully opaque rectangles and objects under 120 px are not tested."""
    al = np.asarray(im.getchannel('A'))
    if al.min() == 255 or max(im.size) < 120:
        return []
    a = al > 200

    def run(line):
        best = cur = 0
        for v in line:
            cur = cur + 1 if v else 0
            best = max(best, cur)
        return best
    out = []
    for name, l0, l4 in (('top', a[0], a[4]), ('bottom', a[-1], a[-5]), ('left', a[:, 0], a[:, 4]), ('right', a[:, -1], a[:, -5])):
        r0, r4 = run(l0), run(l4)
        if r0 >= max(10, 0.06 * len(l0)) and r0 >= 0.6 * r4:
            out.append(name)
    return out


def out_path(folder, aid, slug, subject):
    return f"assets/{folder}/{aid.lower()}-{slug}{'-' + subject if subject else ''}.png"


def write(im, path):
    assert path not in TRACKED, 'refusing to overwrite a tracked asset: ' + path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if im.mode == 'RGBA' and im.getchannel('A').getextrema()[0] == 255:
        im = im.convert('RGB')
    im.save(path, optimize=True)
    return im


def record(rid, parent, name, typ, key, page, path, im, method, bbox=None, image_object=None, notes='', **extra):
    r = dict(id=rid, parent=parent, name=name, type=typ, src=SRC[key][1], page=page,
             bbox_pt=[round(v, 1) for v in bbox] if bbox else None, image_object=image_object, method=method,
             file=path, format='png', dims=f'{im.width}×{im.height} px', has_alpha=im.mode == 'RGBA',
             bytes=os.path.getsize(path), notes=notes)
    r.update(extra)
    RECS[rid] = r
    PRODUCED.append(rid)
    save_records()
    return r


def single(rid, parent, name, typ, key, page, xref, folder, slug, subject, notes='', do_trim=True, crop=None):
    """One embedded image object -> one PNG at native resolution (optionally a pixel crop of it)."""
    im, info = emb(key, page, xref)
    if crop:
        im = im.crop(crop); info['crop_px'] = list(crop)
    clipped = clipped_edges(im) if info['has_mask'] and not crop else []
    if do_trim:
        im = trim(im)
    rects = doc(key)[page - 1].get_image_rects(xref)
    bbox = tuple(rects[0]) if rects else None
    ppi = round(int(info['native'].split('×')[0]) / ((bbox[2] - bbox[0]) / 72)) if bbox else None
    info['ppi_as_placed'] = ppi
    path = out_path(folder, parent, slug, subject)
    im = write(im, path)
    if clipped:
        info['clipped_edges'] = clipped
        notes = (notes + ' ' if notes else '') + 'Subject is cut by the ' + ', '.join(clipped) + ' edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it.'
    method = (f"pdfimages -png p.{page} image #{info['pdfimages_num']} (object {xref}, {info['native']} {info['colour']}"
              f"{' + soft mask #' + str(info['smask_pdfimages_num']) + ' composited to RGBA' if info['has_mask'] else ', no soft mask'})"
              f"{'; cropped to px box ' + str(tuple(crop)) + ' of the object' if crop else ''}"
              f"{'; trimmed to alpha bounds' if do_trim and info['has_mask'] else ''}; native resolution, no resampling")
    return record(rid, parent, name, typ, key, page, path, im, method, bbox=bbox, image_object=info, notes=notes)


# --------------------------------------------------------------------------- priority 1: photography
MINI = 'SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask.'
PHOTO = [
    # (parent, slug, [(subject slug, name, key, page, xref, notes)])
    ('AST-0131', 'miniature', [
        ('cleric', 'Cleric miniature render (2022 core)', 'TG', 4, 222, ''),
        ('pyromancer', 'Pyromancer miniature render (2022 core)', 'TG', 4, 224, ''),
        ('thief', 'Thief miniature render (2022 core)', 'TG', 4, 226, ''),
        ('giant-skeleton-archer', 'Giant Skeleton Archer miniature render', 'TG', 4, 216, ''),
        ('necromancer', 'Necromancer miniature render', 'TG', 4, 218, ''),
        ('giant-skeleton-soldier', 'Giant Skeleton Soldier miniature render', 'TG', 4, 220, ''),
        ('skeleton-archer', 'Skeleton Archer miniature render', 'TG', 4, 215, ''),
        ('skeleton-beast', 'Skeleton Beast miniature render', 'TG', 4, 206, ''),
        ('skeleton-soldier', 'Skeleton Soldier miniature render', 'TG', 4, 208, ''),
        ('black-knight', 'Black Knight mini-boss miniature render', 'TG', 5, 382, ''),
        ('gravelord-nito', 'Gravelord Nito main-boss miniature render', 'TG', 5, 380, ''),
    ]),
    ('AST-0138', 'expansion-miniature', [
        ('great-grey-wolf-sif', 'Great Grey Wolf Sif miniature render (Darkroot)', 'DR', 5, 347, ''),
        ('artorias', 'Artorias miniature render (Darkroot)', 'DR', 5, 349, ''),
        ('stone-knight', 'Stone Knight miniature render (Darkroot)', 'DR', 5, 355, ''),
        ('stone-guardian', 'Stone Guardian miniature render (Darkroot)', 'DR', 5, 353, ''),
        ('mushroom-parent', 'Mushroom Parent miniature render (Darkroot)', 'DR', 4, 177, ''),
        ('mushroom-child', 'Mushroom Child miniature render (Darkroot)', 'DR', 4, 175, ''),
        ('shears-scarecrow', 'Shears Scarecrow miniature render (Darkroot)', 'DR', 4, 181, ''),
        ('plow-scarecrow', 'Plow Scarecrow miniature render (Darkroot)', 'DR', 4, 179, ''),
        ('demonic-foliage', 'Demonic Foliage miniature render (Darkroot)', 'DR', 4, 173, ''),
        ('black-dragon-kalameet', 'Black Dragon Kalameet mega-boss miniature render', 'BDK', 4, 69, ''),
        ('executioners-chariot', "Executioner's Chariot mega-boss miniature render", 'EC', 4, 86, ''),
        ('black-hollow-mage', "Black Hollow Mage miniature render (Executioner's Chariot)", 'EC', 4, 84, ''),
        ('falchion-skeleton', "Falchion Skeleton miniature render (Executioner's Chariot)", 'EC', 4, 76, ''),
        ('smelter-demon', 'Smelter Demon miniature render (Iron Keep)', 'IK', 3, 289, ''),
        ('sir-alonne', 'Sir Alonne miniature render (Iron Keep)', 'IK', 3, 298, ''),
        ('ironclad-soldier', 'Ironclad Soldier miniature render (Iron Keep)', 'IK', 3, 302, ''),
        ('crystal-lizard', 'Crystal Lizard miniature render (Iron Keep)', 'IK', 3, 296, 'Only 149 px wide in the source (150 ppi): small-scale use only.'),
        ('mimic', 'Mimic miniature render, open (Explorers)', 'EX', 4, 250, ''),
        ('mimic-closed', 'Mimic miniature render, closed chest (Explorers)', 'EX', 4, 248, ''),
        ('the-pursuer', 'The Pursuer miniature render (Explorers)', 'EX', 5, 583, ''),
        ('silver-knight-spearman', 'Silver Knight Spearman miniature render (Explorers)', 'EX', 5, 591, ''),
        ('firebomb-hollow', 'Firebomb Hollow miniature render (Explorers)', 'EX', 5, 589, ''),
        # Phantoms: summons (white) and invaders (red)
        ('summon-ruined-aflis', 'Summon: Ruined Aflis miniature render (Phantoms)', 'PH', 4, 80, ''),
        ('summon-eygon-of-carim', 'Summon: Eygon of Carim miniature render (Phantoms)', 'PH', 4, 88, ''),
        ('summon-horace-the-hushed', 'Summon: Horace the Hushed miniature render (Phantoms)', 'PH', 4, 76, ''),
        ('summon-siegward-of-catarina', 'Summon: Siegward of Catarina miniature render (Phantoms)', 'PH', 4, 92, ''),
        ('summon-sword-master', 'Summon: Sword Master miniature render (Phantoms)', 'PH', 4, 84, ''),
        ('summon-rogue-witch-beatrice', 'Summon: Rogue Witch Beatrice miniature render (Phantoms)', 'PH', 4, 86, ''),
        ('summon-lucatiel-of-mirrah', 'Summon: Lucatiel of Mirrah miniature render (Phantoms)', 'PH', 4, 94, ''),
        ('summon-sellsword-luet', 'Summon: Sellsword Luet miniature render (Phantoms)', 'PH', 4, 82, ''),
        ('summon-sirris-of-the-sunless-realms', 'Summon: Sirris of the Sunless Realms miniature render (Phantoms)', 'PH', 4, 90, ''),
        ('summon-solaire-of-astora', 'Summon: Solaire of Astora miniature render (Phantoms)', 'PH', 4, 78, ''),
        ('invader-kirk-knight-of-thorns', 'Invader: Kirk, Knight of Thorns / Longfinger Kirk miniature render (Phantoms)', 'PH', 5, 129, ''),
        ('invader-melinda-the-butcher', 'Invader: Melinda the Butcher miniature render (Phantoms)', 'PH', 5, 143, ''),
        ('invader-maldron-the-assassin', 'Invader: Maldron the Assassin miniature render (Phantoms)', 'PH', 5, 139, ''),
        ('invader-maneater-mildred', 'Invader: Maneater Mildred miniature render (Phantoms)', 'PH', 5, 137, ''),
        ('invader-xanthous-king-jeremiah', 'Invader: Xanthous King Jeremiah miniature render (Phantoms)', 'PH', 5, 147, ''),
        ('invader-oliver-the-collector', 'Invader: Oliver the Collector miniature render (Phantoms)', 'PH', 5, 133, ''),
        ('invader-armorer-dennis', 'Invader: Armorer Dennis miniature render (Phantoms)', 'PH', 5, 123, ''),
        ('invader-marvelous-chester', 'Invader: Marvelous Chester miniature render (Phantoms)', 'PH', 5, 131, ''),
        ('invader-brylex', 'Invader: Invader Brylex miniature render (Phantoms)', 'PH', 5, 125, ''),
        ('invader-paladin-leeroy', 'Invader: Paladin Leeroy miniature render (Phantoms)', 'PH', 5, 135, ''),
        ('invader-fencer-sharron', 'Invader: Fencer Sharron miniature render (Phantoms)', 'PH', 5, 127, ''),
        # Characters expansion: 300 ppi renders (sharper than the 150 ppi 2022 core page)
        ('character-thief', 'Thief character miniature render (Characters expansion, 300 ppi)', 'CH', 4, 71, ''),
        ('character-mercenary', 'Mercenary character miniature render (Characters expansion)', 'CH', 4, 121, ''),
        ('character-cleric', 'Cleric character miniature render (Characters expansion, 300 ppi)', 'CH', 4, 117, ''),
        ('character-pyromancer', 'Pyromancer character miniature render (Characters expansion, 300 ppi)', 'CH', 4, 123, ''),
        ('character-sorcerer', 'Sorcerer character miniature render (Characters expansion)', 'CH', 4, 69, ''),
        ('character-deprived', 'Deprived character miniature render (Characters expansion)', 'CH', 4, 119, ''),
        ('armour-black-iron', 'Black Iron Armour set miniature render (Characters expansion)', 'CH', 5, 157, ''),
        ('armour-catarina', 'Catarina Armour set miniature render (Characters expansion)', 'CH', 5, 161, ''),
        ('armour-black-knight', 'Black Knight Armour set miniature render (Characters expansion)', 'CH', 5, 159, ''),
        ('armour-guardian', 'Guardian Armour set miniature render (Characters expansion)', 'CH', 5, 171, ''),
        ('armour-havels', "Havel's Armour set miniature render (Characters expansion)", 'CH', 5, 173, ''),
        ('armour-embraced-armour-of-favour', 'Embraced Armour of Favour set miniature render (Characters expansion)', 'CH', 5, 155, ''),
        ('armour-crimson-robes', 'Crimson Robes set miniature render (Characters expansion)', 'CH', 5, 167, ''),
        ('armour-adventurers', "Adventurer's Armour set miniature render (Characters expansion)", 'CH', 5, 165, ''),
        ('armour-dark', 'Dark Armour set miniature render (Characters expansion)', 'CH', 5, 163, ''),
        ('armour-gold-trimmed-black-robes', 'Gold-Trimmed Black Robes set miniature render (Characters expansion)', 'CH', 5, 169, ''),
    ]),
    ('AST-0117', 'mega-boss-board', [
        ('kalameet-forest', 'Black Dragon Kalameet mega-boss game board (forest clearing, node markers printed on the board)', 'BDK', 5, 663, 'Square board art with its own soft mask (rounded outline).'),
        ('executioners-chariot-arena', "Executioner's Chariot mega-boss game board (round arena)", 'EC', 5, 1127, ''),
        ('executioners-chariot-reverse', "Executioner's Chariot game board, second board image on p.9", 'EC', 9, 1823, ''),
    ]),
    ('AST-0133', 'game-tile', [
        ('tomb-of-giants-a', 'Tomb of Giants game tile A (2022 core, tile fan on p.6)', 'TG', 6, 774, '284 px at ~140 ppi: small-scale use only.'),
        ('tomb-of-giants-b', 'Tomb of Giants game tile B (2022 core)', 'TG', 6, 776, '284 px at ~140 ppi: small-scale use only.'),
        ('tomb-of-giants-c', 'Tomb of Giants game tile C (2022 core)', 'TG', 6, 778, '284 px at ~140 ppi: small-scale use only.'),
        ('tomb-of-giants-d', 'Tomb of Giants game tile D (2022 core)', 'TG', 6, 780, '284 px at ~140 ppi: small-scale use only.'),
        ('bonfire-2017', 'Bonfire tile (2017 core set), clean tile art without the anatomy call-outs', 'CORE', 13, 1198, 'Opaque square tile (no soft mask in the 2017 PDF). The numbered call-outs of the p.13 anatomy diagram are vector overlays and are not in this image.'),
    ]),
    ('AST-0134', 'campaign-board', [
        ('left-half', 'Campaign board, left half (2022 core, p.13)', 'TG', 13, 1080, ''),
        ('right-half', 'Campaign board, right half (2022 core, p.13)', 'TG', 13, 1088, ''),
        ('full-strip', 'Campaign board, full strip (2022 core, p.6)', 'TG', 6, 787, 'Lower resolution than the two halves (1004 px for the whole board).'),
    ]),
    ('AST-0135', 'character-dashboard', [
        ('lower-section-a', 'Character dashboard, lower section (ability box, stat grid, equipment-slot labels, endurance bar), clean, no call-outs', 'TG', 8, 809,
         'Cropped below the name band: the top 236 px of the dashboard object carry a painted class portrait and item roundels (see Provenance Review) and are left out. The cube slots of the grid and bar are transparent holes in the source mask.', (0, 236, 1019, 806)),
        ('lower-section-b', 'Character dashboard, lower section with printed stat values (second dashboard state on p.8), clean', 'TG', 8, 807,
         'Cropped below the name band (top 236 px with the painted class portrait left out, see Provenance Review). Opaque rectangle.', (0, 236, 1019, 685)),
    ]),
    ('AST-0136', 'dice', [
        ('black', 'Black die (2022 core, p.6)', 'TG', 6, 631, '~63 px at 150 ppi: inline size only; see the dice-set composite for a larger arrangement.'),
        ('blue', 'Blue die (2022 core, p.6)', 'TG', 6, 629, '~63 px at 150 ppi: inline size only.'),
        ('orange', 'Orange die (2022 core, p.6)', 'TG', 6, 627, '~63 px at 150 ppi: inline size only.'),
        ('green', 'Green die (2022 core, p.6)', 'TG', 6, 625, '~63 px at 150 ppi: inline size only.'),
    ]),
    ('AST-0132', 'token', [
        ('spark-dial', 'Spark dial (2022 core, p.6)', 'TG', 6, 720, ''),
        ('terrain-gravestone-render', 'Gravestone terrain piece render (Explorers)', 'EX', 5, 599, ''),
        ('terrain-bonfire-render', 'Bonfire terrain piece render (Explorers)', 'EX', 5, 595, ''),
        ('terrain-barrels-render', 'Barrels terrain piece render (Explorers)', 'EX', 5, 603, ''),
        ('terrain-treasure-chest-render', 'Treasure Chest terrain piece render (Explorers)', 'EX', 5, 597, ''),
    ]),
]


def run_photo():
    for parent, slug, items in PHOTO:
        for k, it in enumerate(items, 1):
            subject, name, key, page, xref, notes = it[:6]
            r = single(f'{parent}.{k}', parent, name, 'photography', key, page, xref, 'photography', slug, subject,
                       notes=(notes or (MINI if 'miniature' in name else '')), crop=it[6] if len(it) > 6 else None)
            print(r['id'], r['file'], r['dims'], 'alpha' if r['has_alpha'] else 'opaque', r['image_object']['ppi_as_placed'])


# --------------------------------------------------------------------------- composites of small objects
def compose(rid, parent, name, key, page, xrefs, folder, slug, subject, ppi=600, pad=3, notes='', typ='photography'):
    """Re-assemble a group of embedded objects (dice, tokens, tile fan) exactly as placed on the page,
    on a transparent ground. Each object is decoded natively and mapped with its placement matrix
    (draw order from the page); nothing else on the page (parchment, captions, watermark) is drawn."""
    pg = doc(key)[page - 1]
    infos = [i for i in pg.get_image_info(xrefs=True) if i['xref'] in xrefs]
    assert infos, rid
    x0 = min(i['bbox'][0] for i in infos) - pad; y0 = min(i['bbox'][1] for i in infos) - pad
    x1 = max(i['bbox'][2] for i in infos) + pad; y1 = max(i['bbox'][3] for i in infos) + pad
    s = ppi / 72
    W, H = round((x1 - x0) * s), round((y1 - y0) * s)
    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cache, nat = {}, []
    for i in infos:
        xr = i['xref']
        if xr not in cache:
            cache[xr] = emb(key, page, xr)[0]
        im = cache[xr]
        a, b, c, d, e, f = i['transform']
        # image pixel (px,py) -> canvas pixel
        F = np.array([[a / im.width * s, c / im.height * s, (e - x0) * s],
                      [b / im.width * s, d / im.height * s, (f - y0) * s], [0, 0, 1]])
        inv = np.linalg.inv(F)
        layer = im.transform((W, H), Image.AFFINE, tuple(inv[:2].flatten()), resample=Image.BICUBIC)
        canvas.alpha_composite(layer)
        nat.append(round(im.width / (abs(a) / 72)) if abs(a) > 1 else 0)
    canvas = trim(canvas)
    path = out_path(folder, parent, slug, subject)
    canvas = write(canvas, path)
    src_ppi = int(np.median([n for n in nat if n])) if any(nat) else None
    method = (f"composite of {len(infos)} placements of {len(cache)} embedded image objects (objects {', '.join(str(x) for x in sorted(cache))}) "
              f"decoded with pdfimages -png + soft masks, re-assembled with their page placement matrices in draw order on a transparent "
              f"ground at {ppi} px/in of page size (objects are ~{src_ppi} ppi as placed, i.e. upsampled ×{ppi / src_ppi:.1f} bicubic); "
              f"no page render involved")
    return record(rid, parent, name, typ, key, page, path, canvas, method, bbox=(x0, y0, x1, y1),
                  image_object=dict(xrefs=sorted(cache), placements=len(infos), ppi_as_placed=src_ppi, upsampled=round(ppi / src_ppi, 2)),
                  notes=notes)


LOW = 'Source objects are only ~150 ppi at page size; this composite is an upsample for layout convenience, keep it small in print (≤ the size it has in the source rulebook, about {w:.1f} in wide, for full sharpness).'
GROUPS = [
    # (id, parent, slug, subject, name, key, page, xrefs)
    ('AST-0136.5', 'AST-0136', 'dice', 'set', 'Dice set as arranged on p.6 (5 black, 4 blue, 2 orange, 4 green)', 'TG', 6, [631, 629, 625, 627]),
    ('AST-0132.6', 'AST-0132', 'token', 'array-souls-wounds-conditions-terrain',
     'Token and terrain-token array as arranged on p.6 (soul, wound, aggro, luck, heroic action, estus, ember, party, condition and terrain tokens, spark dial), captions omitted',
     'TG', 6, [679, 682, 688, 685, 673, 676, 667, 670, 720, 725, 746, 649, 655, 661, 664, 640, 643, 753, 646, 652, 658, 760, 767, 714, 717,
               693, 696, 699, 702, 705, 708, 711]),
    ('AST-0132.7', 'AST-0132', 'token', 'enemy-tokens', 'Enemy token set as arranged on p.6 (six enemy types)', 'TG', 6, [728, 737, 731, 740, 734, 743]),
    ('AST-0132.8', 'AST-0132', 'token', 'row-soul-and-wound-tokens', 'Soul and wound token row as arranged on p.6 (1/3/5 soul tokens, 1/3/5 wound tokens and neighbours)', 'TG', 6, [679, 682, 688, 685, 673, 676, 667, 670]),
    ('AST-0132.9', 'AST-0132', 'token', 'row-terrain-tokens', 'Terrain token row as arranged on p.6 (gravestone, shrine, barrel, lever, trap, skeleton ball and neighbours)', 'TG', 6, [693, 696, 699, 702, 705, 708, 711, 714, 717]),
    ('AST-0133.6', 'AST-0133', 'game-tile', 'tomb-of-giants-fan', 'Fan of the four double-sided Tomb of Giants game tiles as arranged on p.6', 'TG', 6, [774, 776, 778, 780]),
]


def run_groups():
    for rid, parent, slug, subject, name, key, page, xrefs in GROUPS:
        r = compose(rid, parent, name, key, page, xrefs, 'photography', slug, subject)
        w_in = (r['bbox_pt'][2] - r['bbox_pt'][0]) / 72
        r['notes'] = LOW.format(w=w_in); save_records()
        print(r['id'], r['file'], r['dims'], r['image_object'])


# --------------------------------------------------------------------------- hero list for the layout
HERO_FOR = [  # (record id, suggested_for); the first entry listed for a chapter is the primary suggestion
    ('AST-0131.11', 'chapter 01 Introduction'),
    ('AST-0132.6', 'chapter 02 Game Components'),
    ('AST-0138.46', 'chapter 03 Characters'), ('AST-0138.47', 'chapter 03 Characters'), ('AST-0138.44', 'chapter 03 Characters'),
    ('AST-0138.48', 'chapter 03 Characters'), ('AST-0138.49', 'chapter 03 Characters'),
    ('AST-0135.1', 'chapter 04 Equipment'), ('AST-0138.52', 'chapter 04 Equipment'), ('AST-0138.57', 'chapter 04 Equipment'),
    ('AST-0138.54', 'chapter 04 Equipment'),
    ('AST-0133.6', 'chapter 05 Tiles and Nodes'),
    ('AST-0135.2', 'chapter 06 Setup'),
    ('AST-0134.1', 'chapter 07 Gameplay'),
    ('AST-0136.5', 'chapter 08 Combat Basics'),
    ('AST-0138.3', 'chapter 09 Enemy Turn'), ('AST-0138.4', 'chapter 09 Enemy Turn'),
    ('AST-0138.45', 'chapter 10 Character Turn'), ('AST-0138.50', 'chapter 10 Character Turn'),
    ('AST-0133.5', 'chapter 11 Returning to the Bonfire'),
    ('AST-0138.23', 'chapter 12 Phantoms'), ('AST-0138.32', 'chapter 12 Phantoms'), ('AST-0138.33', 'chapter 12 Phantoms'),
    ('AST-0138.18', 'chapter 13 Mimics'),
    ('AST-0138.2', 'chapter 15 Boss Encounters'), ('AST-0131.10', 'chapter 15 Boss Encounters'),
    ('AST-0138.1', 'chapter 16 Boss Turns'),
    ('AST-0138.10', 'chapter 17 Boss Special Rules'), ('AST-0138.11', 'chapter 17 Boss Special Rules'),
    ('AST-0134.2', 'chapter 18 Campaign Play'),
    ('AST-0117.1', 'chapter 19 Campaigns'), ('AST-0138.14', 'chapter 19 Campaigns'),
    ('AST-0138.38', 'chapter 20 Player versus Player'), ('AST-0138.37', 'chapter 20 Player versus Player'),
    ('AST-0138.41', 'chapter 20 Player versus Player'),
    ('AST-0132.9', 'chapter 21 Glossary'),
    ('AST-0138.26', 'chapter 22 F.A.Q.'),
    ('AST-0138.27', 'Appendix A'), ('AST-0138.20', 'Appendix A'),
    ('AST-0117.2', 'theme: mega bosses (spare)'),
    ('AST-0138.5', 'theme: enemies (spare)'), ('AST-0138.8', 'theme: enemies (spare)'), ('AST-0138.9', 'theme: enemies (spare)'),
    ('AST-0138.51', 'theme: characters, armour sets (spare)'), ('AST-0138.53', 'theme: characters, armour sets (spare)'),
    ('AST-0138.55', 'theme: characters, armour sets (spare)'), ('AST-0138.56', 'theme: characters, armour sets (spare)'),
    ('AST-0138.58', 'theme: characters, armour sets (spare)'), ('AST-0138.59', 'theme: characters, armour sets (spare)'),
    ('AST-0138.24', 'theme: phantoms, summons (spare)'), ('AST-0138.29', 'theme: phantoms, summons (spare)'),
    ('AST-0138.30', 'theme: phantoms, summons (spare)'), ('AST-0138.31', 'theme: phantoms, summons (spare)'),
    ('AST-0138.28', 'theme: phantoms, summons (spare)'),
    ('AST-0138.34', 'theme: phantoms, invaders (spare)'), ('AST-0138.35', 'theme: phantoms, invaders (spare)'),
    ('AST-0138.36', 'theme: phantoms, invaders (spare)'), ('AST-0138.40', 'theme: phantoms, invaders (spare)'),
    ('AST-0138.42', 'theme: phantoms, invaders (spare)'), ('AST-0138.43', 'theme: phantoms, invaders (spare)'),
]
SUBJECT_TRIM = (' miniature render', ' (2022 core)', ' mini-boss', ' main-boss', ' mega-boss')


def write_heroes():
    def ent(r, sugg=None):
        w, h = [int(v) for v in r['dims'].split(' ')[0].split('×')]
        e = dict(file=r['file'], subject=r['name'], width=w, height=h, has_alpha=r['has_alpha'])
        if sugg:
            e['suggested_for'] = sugg
        return e
    photos = [r for r in RECS.values() if (r.get('file') or '').startswith('assets/photography/')]
    heroes = [ent(RECS[i], s) for i, s in HERO_FOR if i in RECS]
    used = {e['file'] for e in heroes}
    panels = [dict(ent(r), suggested_for='chapter-end panel') for r in sorted(photos, key=lambda r: idkey(r['id'])) if r['file'] not in used]
    notes = HERO_NOTES(photos, heroes)
    os.makedirs('layout', exist_ok=True)
    json.dump(dict(heroes=heroes, panels=panels, notes=notes), open('layout/hero_assets.json', 'w'), indent=1, ensure_ascii=False)
    print('layout/hero_assets.json: heroes', len(heroes), 'panels', len(panels), 'notes', len(notes))


def HERO_NOTES(photos, heroes):
    name = lambda f: os.path.basename(f)
    byfile = {r['file']: r for r in photos}
    comp = {r['file'] for r in photos if (r.get('image_object') or {}).get('upsampled')}
    long_ = lambda e: max(e['width'], e['height'])
    big = [e for e in heroes if long_(e) >= 880 and e['file'] not in comp]
    mid = [e for e in heroes if 700 <= long_(e) < 880 and e['file'] not in comp]
    opaque = [r['file'] for r in photos if not r['has_alpha']]
    clip = [(r['file'], r['image_object']['clipped_edges']) for r in sorted(photos, key=lambda r: idkey(r['id'])) if (r.get('image_object') or {}).get('clipped_edges')]
    return [
        'All files are Steamforged product imagery (miniature renders, boards, tiles, tokens, dice, dashboard section) taken from embedded image objects of the rulebook PDFs; none is a page crop, so none carries parchment, captions or the purchaser watermark. Painted key art was not extracted.',
        "Pixel sizes are the native sizes of the embedded objects (trimmed to their alpha bounds); nothing was upscaled except the composites listed below. The source PDFs are web/low-res exports: miniatures are 150 ppi in the 2022 core, Iron Keep, Explorers and Executioner's Chariot books and 300 ppi in Phantoms, Characters, Darkroot and Black Dragon Kalameet.",
        f'Resolution: only {len(big)} heroes are natively about 900 px or more on the long side (' + ', '.join(name(e['file']) for e in big) + f'); {len(mid)} more are 700 to 880 px (' + ', '.join(name(e['file']) for e in mid) + '). Every other hero is the largest version the sources hold. Size heroes by pixel count: at 150 ppi effective a 450 px image prints 3 in (76 mm) on its long side, at 200 ppi 2.25 in.',
        'Composites (several small embedded token / dice / tile objects re-assembled with their page placement on a transparent ground, upsampled about 4x from 150 ppi objects, therefore soft; their large pixel sizes are not real resolution): ' + ', '.join(name(f) for f in sorted(comp)) + '. Use them small (dice set about 1.7 in, tile fan about 4.4 in, token array and token rows about 6.5 in wide for full sharpness) or as background-weight decoration.',
        'Backgrounds: files with has_alpha=true are cut out on transparency (the soft masks include the sculpt bases). Opaque files (has_alpha=false) are rectangular with their own printed artwork to the edge, not parchment: ' + ', '.join(name(f) for f in opaque) + '.',
        'Subjects cropped by the source image edge (subject runs into the boundary of the embedded object, exactly as in the rulebooks; listed with the cut sides): ' + '; '.join(f"{name(f)} ({', '.join(c)})" for f, c in clip) + '. Most are sculpt bases cut flat at the bottom; set those on a rule or frame edge.',
        'Chapter 14 (Crystal Lizards): the only source image is ast-0138-expansion-miniature-crystal-lizard.png at 149x53 px; it is listed under panels, not heroes. Chapter 13 (Mimics): the Mimic render is 265x381 px (150 ppi), usable up to about 2.5 in tall.',
        'Chapters 03 and 10 share the Characters-expansion class renders; chapter 12 and chapter 20 use the Phantoms summon (white resin) and invader (red resin) renders respectively. Entries marked "theme: ... (spare)" are further hero-grade renders with no chapter of their own.',
        'Character dashboard: only the lower section (ability box, stat grid, slot labels, endurance bar) is provided; the name band of the dashboard carries a painted class portrait and is held for provenance review. The cube slots in ast-0135-character-dashboard-lower-section-a.png are transparent holes.',
        'Card fans (AST-0137) were not extracted: every fan shows card faces with painted illustrations (provenance review). Card backs without illustrations are in assets/frames/ast-0089-card-back-*.png (124x186 to 175x300 px, too small for a hero). No hero-grade match exists for Appendix B (card amendments); use a card back at small size or a generic component image.',
        'The 2017 bonfire tile (ast-0133-game-tile-bonfire-2017.png) and the mega-boss boards have node rings and markers printed in the artwork.',
    ]


def run_photography():
    run_photo(); run_groups(); prune(('assets/photography/',))


def run_all_other():
    run_diagrams(); run_icons(); run_frames(); run_textures(); run_review()
    prune(('assets/diagrams/', 'assets/icons/', 'assets/frames/', 'assets/textures/'))


SECTIONS = {'photo': run_photography, 'other': run_all_other, 'heroes': write_heroes}

# --------------------------------------------------------------------------- page-region renders (watermark-safe)
WM_KEYS = ('TG', 'PH', 'BDK', 'EC', 'DR', 'IK', 'EX', 'CH')   # personalised PDFs


def is_wm(t):
    return 'Generated for' in t or '@' in t


def redacted(key):
    """Working copy with the purchaser line removed (text redaction only; images and line art untouched)."""
    if key not in WM_KEYS:
        return SRC[key][0]
    out = f'{SCRATCH}/_redacted/{key}.pdf'
    if not os.path.exists(out):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        d = fitz.open(SRC[key][0])
        for pg in d:
            for b in pg.get_text('blocks'):
                if b[6] == 0 and is_wm(b[4]):
                    pg.add_redact_annot(fitz.Rect(b[:4]) + (-2, -2, 2, 2))
            pg.apply_redactions(images=0, graphics=0)
        d.save(out)
    assert not any(is_wm(b[4]) for pg in fitz.open(out) for b in pg.get_text('blocks') if b[6] == 0)
    return out


def _ppm(path, page, box, dpi):
    s = dpi / 72; tmp = f'{SCRATCH}/_region'
    os.makedirs(SCRATCH, exist_ok=True)
    subprocess.run(['pdftoppm', '-r', str(dpi), '-f', str(page), '-l', str(page), '-x', str(round(box[0] * s)), '-y', str(round(box[1] * s)),
                    '-W', str(round((box[2] - box[0]) * s)), '-H', str(round((box[3] - box[1]) * s)), '-png', path, tmp], check=True)
    f = glob.glob(tmp + '*.png')[0]
    im = Image.open(f).convert('RGB'); im.load(); os.remove(f)
    return im


def region(key, page, box, dpi):
    """pdftoppm crop of a page region; for personalised PDFs it is rendered from the redacted copy, must stay
    30 pt clear of the head and foot of the page, and must be pixel-identical to the same crop of the unredacted
    page (i.e. no pixel of the purchaser line lies inside it)."""
    ph = doc(key)[page - 1].rect.height
    if key in WM_KEYS:
        assert box[1] >= 30 and box[3] <= ph - 30, 'crop too close to the page head/foot'
    im = _ppm(redacted(key), page, box, dpi)
    if key in WM_KEYS:
        assert np.array_equal(np.asarray(im), np.asarray(_ppm(SRC[key][0], page, box, dpi))), 'purchaser line inside crop'
    return im


def region_asset(rid, parent, name, typ, key, page, box, dpi, folder, slug, subject='', notes=''):
    im = region(key, page, box, dpi)
    path = out_path(folder, parent, slug, subject)
    im = write(im, path)
    wm = ' rendered from a working copy with the purchaser line redacted; crop verified pixel-identical to the unredacted page region and 30 pt clear of page head and foot' if key in WM_KEYS else ''
    return record(rid, parent, name, typ, key, page, path, im, f'pdftoppm {dpi} dpi page-region crop{";" + wm if wm else ""}', bbox=box, notes=notes)


def overlay_diff(key, page, xref):
    """Mean abs difference between an embedded object and the page render of its placement (large = vector overlays on top)."""
    im, _ = emb(key, page, xref)
    r = doc(key)[page - 1].get_image_rects(xref)[0]
    ren = _ppm(redacted(key), page, tuple(r), im.width / (r.width / 72)).resize(im.size)
    return float(np.abs(np.asarray(im.convert('RGB')).astype(int) - np.asarray(ren).astype(int)).mean())


def run_diagrams():
    D = 'Embedded raster with the diagram artwork baked in (no page crop, so no parchment, caption or watermark).'
    for rid, name, key, page, xref, slug in [
        ('AST-0112', 'Node adjacency diagram (tile with the adjacent nodes highlighted in green)', 'TG', 11, 945, 'node-adjacency-diagram'),
        ('AST-0113', 'Range / doorway diagram (two tile edges with an arrow through the doorway)', 'TG', 11, 946, 'range-and-doorway-diagram'),
        ('AST-0115', 'Equipment modifier strip ([0] 1 +1 / [3] 2 +1)', 'TG', 21, 1260, 'equipment-modifier-strip'),
    ]:
        dv = overlay_diff(key, page, xref)
        r = single(rid, rid, name, 'diagram', key, page, xref, 'diagrams', slug, '', do_trim=False, crop=(0, 0, 884, 352) if xref == 1260 else None,
                   notes=D + (' The bottom 8 px of the object (tops of the next row of card icons, clipped away on the page) are cropped off.' if xref == 1260 else '') + f' Mean difference to the page render of the same placement: {dv:.1f}/255' + (' (vector overlays are drawn over it on the page and are not in this file).' if dv > 12 else ' (nothing is drawn over it on the page).'))
        print(r['id'], r['file'], r['dims'], 'overlay diff', round(dv, 1))
    r = region_asset('AST-0116', 'AST-0116', 'Enemy attack resolution strip (attack value 5, dice rolled, damage taken)', 'diagram', 'TG', 25,
                     (309, 417, 523, 479.5), 600, 'diagrams', 'enemy-attack-resolution-strip',
                     notes='Vector attack symbol with small dice and wound-token rasters (about 150 ppi) on the page parchment; strip only, the example-box frame and the italic caption below it are outside the crop.')
    print(r['id'], r['file'], r['dims'])
    r = region_asset('AST-0111', 'AST-0111', 'Encounter setup worked example (The Forgotten): encounter card and tile with placed tokens, framed example box', 'diagram', 'CORE', 18,
                     (66, 336, 558, 756), 400, 'diagrams', 'encounter-setup-example-2017',
                     notes='Whole example box with its compass-corner frame, heading and explanatory text, on the 2017 parchment. 2017 components (Hollow Soldiers, Silver Knight Greatbowman); the 2017 PDF carries no purchaser line.')
    print(r['id'], r['file'], r['dims'])
    status('AST-0114', 'not required', 'The timer track belongs to a rule this ruleset does not use; not extracted.')


# --------------------------------------------------------------------------- icons
def slugify(t):
    import re
    return re.sub(r'[^a-z0-9]+', '-', t.lower().replace("'", '')).strip('-')


def icon(rid, parent, name, key, page, xref, slug, subject, notes=''):
    im, info = emb(key, page, xref)
    bb = im.getchannel('A').point(lambda v: 255 if v > 12 else 0).getbbox()
    im = im.crop(bb) if bb else im
    rects = doc(key)[page - 1].get_image_rects(xref)
    bbox = tuple(rects[0]) if rects else None
    info['ppi_as_placed'] = round(int(info['native'].split('×')[0]) / ((bbox[2] - bbox[0]) / 72)) if bbox else None
    path = out_path('icons', parent, slug, subject)
    im = write(im, path)
    method = (f"pdfimages -png p.{page} image #{info['pdfimages_num']} (object {xref}, {info['native']} {info['colour']}) + soft mask "
              f"#{info.get('smask_pdfimages_num')} composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution")
    return record(rid, parent, name, 'icon', key, page, path, im, method, bbox=bbox, image_object=info, notes=notes)


def key_alpha(im, soft=(14, 60)):
    """Same parchment keying as the Phase 0 icon set (tools/finalise_tg_icons.py)."""
    a = np.asarray(im.convert('RGB')).astype(int)
    border = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]]); bg = np.median(border, axis=0)
    d = np.abs(a - bg).max(axis=2); alpha = np.clip((d - soft[0]) / (soft[1] - soft[0]), 0, 1)
    return Image.fromarray(np.dstack([a, alpha * 255]).astype(np.uint8), 'RGBA'), tuple(int(v) for v in bg)


def keyed_icon(rid, parent, name, key, page, box, slug, subject, notes=''):
    crop = region(key, page, box, 600)
    al, bg = key_alpha(crop); bb = al.getchannel('A').getbbox()
    if bb:
        al = al.crop((max(0, bb[0] - 3), max(0, bb[1] - 3), min(al.width, bb[2] + 3), min(al.height, bb[3] + 3)))
    path = out_path('icons', parent, slug, subject)
    al = write(al, path)
    return record(rid, parent, name, 'icon', key, page, path, al, f'pdftoppm 600 dpi render crop → parchment-key alpha (bg {bg}) → trimmed to inked bounds', bbox=box, notes=notes)


PH_ICONS = [  # (page, xref, kind, name)
    (4, 74, 'summon', 'Ruined Aflis'), (4, 110, 'summon', 'Eygon of Carim'), (4, 106, 'summon', 'Horace the Hushed'),
    (4, 100, 'summon', 'Siegward of Catarina'), (4, 102, 'summon', 'Sword Master'), (4, 72, 'summon', 'Rogue Witch Beatrice'),
    (4, 108, 'summon', 'Lucatiel of Mirrah'), (4, 104, 'summon', 'Sellsword Luet'), (4, 98, 'summon', 'Sirris of the Sunless Realms'),
    (4, 96, 'summon', 'Solaire of Astora'),
    (5, 141, 'invader', 'Kirk, Knight of Thorns'), (5, 149, 'invader', 'Longfinger Kirk'), (5, 119, 'invader', 'Melinda the Butcher'),
    (5, 121, 'invader', 'Maldron the Assassin'), (5, 159, 'invader', 'Maneater Mildred'), (5, 145, 'invader', 'Xanthous King Jeremiah'),
    (5, 155, 'invader', 'Oliver the Collector'), (5, 117, 'invader', 'Armorer Dennis'), (5, 161, 'invader', 'Marvelous Chester'),
    (5, 157, 'invader', 'Invader Brylex'), (5, 153, 'invader', 'Paladin Leeroy'), (5, 151, 'invader', 'Fencer Sharron'),
]
PH_TOKENS = [299, 279, 301, 281, 283, 285, 293, 291, 289, 287, 295, 297]   # p.10 wheel; 275 and 277 carry painted art (review)


def run_icons():
    LOWI = 'Native 64 px (150 ppi at its 15 pt printed size): use at inline size only. No larger copy exists as a separate object in any source PDF (searched by image similarity).'
    icon('AST-0069.1', 'AST-0069', 'Mini-boss (standard) skull icon', 'TG', 5, 339, 'boss-icon', 'mini-boss-standard-skull', LOWI)
    icon('AST-0069.2', 'AST-0069', 'Main-boss (advanced) crowned skull icon', 'TG', 5, 335, 'boss-icon', 'main-boss-advanced-crowned-skull', LOWI)
    icon('AST-0070.1', 'AST-0070', 'Mega-boss icon: Black Dragon Kalameet (dragon head with red glow)', 'BDK', 4, 67, 'mega-boss-icon', 'black-dragon-kalameet',
         'The embedded object beside the Kalameet miniature on the contents page (325 ppi); larger and cleaner than the data-card call-out on p.11.')
    icon('AST-0070.2', 'AST-0070', "Mega-boss icon: Executioner's Chariot (chariot glyph with red glow)", 'EC', 4, 88, 'mega-boss-icon', 'executioners-chariot', '')
    icon('AST-0071.1', 'AST-0071', 'Universal (all-languages) card icon', 'DR', 2, 51, 'set-symbol', 'universal-icon',
         '51 px at 300 ppi (12 pt glyph): inline size only.')
    status('AST-0071', 'BLOCKED', 'Only the universal icon exists as a separate image object (extracted as AST-0071.1). The seven expansion set symbols occur '
           'only inside the low-resolution card rasters (about 12 to 15 px across), so no print-fit source exists: redraw as vectors or obtain card artwork from the owner.')
    k = 0
    for page, xref, kind, name in PH_ICONS:
        k += 1
        icon(f'AST-0072.{k}', 'AST-0072', f'{kind.capitalize()} icon: {name} (portrait glyph in ring{", glowing: advanced tier" if xref in (72, 108, 104, 98, 96, 149, 117, 161, 157, 153, 151) else ""})',
             'PH', page, xref, 'phantom-icon', f'{kind}-{slugify(name)}', 'Named from the miniature caption it sits beside on the contents page.')
    for n, xref in enumerate(PH_TOKENS, 1):
        k += 1
        icon(f'AST-0072.{k}', 'AST-0072', f'Phantom token {n:02d} of the p.10 set-up wheel (dark disc with portrait glyph)', 'PH', 10, xref, 'phantom-token', f'{n:02d}',
             'Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review).')
    for n, (y, name) in enumerate([(90.3, 'Hollow Soldier'), (114.3, 'Crossbow Hollow'), (138.3, 'Large Hollow Soldier'), (162.3, 'Silver Knight Swordsman'),
                                   (186.3, 'Silver Knight Greatbowman'), (210.3, 'Sentinel')], 1):
        keyed_icon(f'AST-0067.{n}', 'AST-0067', f'2017 enemy icon: {name}', 'CORE', 40, (302.5, y - 2, 325, y + 20.5), 'enemy-icon-2017', slugify(name),
                   'Source is a flattened 39 px raster (150 ppi) on parchment: the 600 dpi crop is a ×4 upsample, keyed like the 2022 set. Inline size only.')
    keyed_icon('AST-0068', 'AST-0068', 'Trapped-encounter sword icon (2017 horizontal variant)', 'CORE', 40, (82.7, 184.3, 130, 206.8), 'trapped-encounter-icon-2017', '',
               'Source is a flattened 91×39 px raster on parchment (×4 upsample, keyed). Reference only: the 2022 three-spear trap icon supersedes it.')
    print('icons done:', sum(1 for r in RECS.values() if (r.get('file') or '').startswith('assets/icons/')))


# --------------------------------------------------------------------------- frames, card backs, textures
def run_frames():
    # AST-0085 large art frame (vector)
    svg = f'{SCRATCH}/_redacted/tg_p07.svg'
    subprocess.run(['pdftocairo', '-svg', '-f', '7', '-l', '7', redacted('TG'), svg], check=True)
    out = 'assets/frames/ast-0085-large-art-frame-compass-corners.svg'
    assert out not in TRACKED
    box = (44, 38, 540, 758)   # frame rules at x 56.7/527.2 and y 50.8/747.5 plus the corner ornaments; the folio rule (y 761+) stays outside
    subprocess.run(['python3', 'tools/svg_crop.py', svg, out, *map(str, box)], check=True)
    txt = open(out).read()
    assert '<image' not in txt and '<text' not in txt and 'glyph' not in txt, 'raster/text left in frame SVG'
    RECS['AST-0085'] = dict(id='AST-0085', parent='AST-0085', name='Large art frame: compass corners + hairline rules around full-column illustrations', type='frame',
                            src=SRC['TG'][1], page=7, bbox_pt=list(box), image_object=None,
                            method='pdftocairo -svg p.7 (from a working copy with the purchaser line redacted) → tools/svg_crop.py (raster images and all text glyphs dropped; vector paths inside the bbox kept)',
                            file=out, format='svg', dims=f'{box[2] - box[0]}×{box[3] - box[1]} pt (vector)', has_alpha=True, bytes=os.path.getsize(out),
                            notes=f'{txt.count("<path")} vector paths; the framed painting is a raster and is not in the file. Scale by moving the corners, not the strokes.')
    PRODUCED.append('AST-0085'); save_records()
    # AST-0087 / 0088: illustration-free parts of card faces only
    single('AST-0087.1', 'AST-0087', 'Encounter card frame, upper section: title banner, flavour strip and parchment text box (Grave Matters, card text printed in)', 'frame', 'TG', 16, 1184,
           'frames', 'encounter-card-frame', 'upper-section-banner-and-text-box', do_trim=False, crop=(0, 0, 584, 458),
           notes='Top 458 px of the 584×1000 card raster (300 ppi). The lower right of the card carries a painted scene and is left out (see Provenance Review). Card text is part of the raster.')
    single('AST-0087.2', 'AST-0087', 'Encounter card frame, node-map panel (parchment panel with the node layout diagram)', 'frame', 'TG', 16, 1184,
           'frames', 'encounter-card-frame', 'node-map-panel', do_trim=False, crop=(14, 466, 392, 996),
           notes='Left panel of the lower half of the card raster; the painted scene to its right is left out (see Provenance Review).')
    single('AST-0088.1', 'AST-0088', 'Boss data card frame, lower section: framed parchment text box (Gravelord Nito card, rule text printed in)', 'frame', 'TG', 28, 1442,
           'frames', 'data-card-frame', 'boss-card-text-box', do_trim=False, crop=(0, 515, 653, 912),
           notes='Lower 397 px of the 653×912 card raster (300 ppi). The upper part of every enemy, boss and behaviour card is a character illustration and was not extracted (see Provenance Review).')
    for k, (key, page, xref, subject, name) in enumerate([
            ('TG', 5, 342, 'treasure', 'Treasure card back (gold ring with chest glyph)'),
            ('TG', 5, 348, 'boss-treasure', 'Boss treasure card back (gold ring with glowing skull glyph)'),
            ('TG', 16, 1190, 'encounter-level-1', 'Encounter card back, level 1 (blue flame)'),
            ('TG', 6, 783, 'event', 'Event card back'),
            ('TG', 5, 328, 'mini-boss-black-knight', 'Mini-boss card back (Black Knight glyph on orange lattice)'),
            ('TG', 5, 322, 'main-boss-gravelord-nito', 'Main-boss card back (Gravelord Nito glyph on red lattice)')], 1):
        single(f'AST-0089.{k}', 'AST-0089', name, 'frame', key, page, xref, 'frames', 'card-back', subject, do_trim=False,
               notes='Card back, no illustration. Thumbnail-grade raster (about 130 to 150 ppi at the size printed in the rulebook): decorative use at small size only.')
    status('AST-0137', 'BLOCKED', 'Provenance review: every card fan in the sources shows card faces (encounter, event, treasure and boss cards) that carry painted '
           'illustrations, so no fan was extracted. The card backs, which carry none, are extracted singly as AST-0089.1 to AST-0089.6.')
    print('frames done')


def run_textures():
    single('AST-0145.1', 'AST-0145', 'Card text-box parchment plate: blank worn-cream panel with its hairline frame (Phantoms summon card)', 'texture', 'PH', 6, 207,
           'textures', 'card-textbox-parchment', 'blank-plate',
           notes='Blank plate with soft mask at 445 ppi as placed: the cleanest text-box parchment in the sources (the 2022 encounter card boxes have their text printed in). Crop the centre for a pure fill.')
    single('AST-0145.2', 'AST-0145', 'Card text-box parchment fill: blank area of the Gravelord Nito data card text box', 'texture', 'TG', 28, 1442,
           'textures', 'card-textbox-parchment', 'fill-2022-boss-card', do_trim=False, crop=(45, 662, 608, 878),
           notes='Text-free lower part of the text box of the 653×912 card raster (300 ppi).')
    single('AST-0146', 'AST-0146', 'Dashboard parchment panel texture (blank lower part of the ability box of the character dashboard)', 'texture', 'TG', 8, 809,
           'textures', 'dashboard-parchment-panel-texture', '', do_trim=False, crop=(112, 405, 292, 655),
           notes='180×250 px at 150 ppi: small swatch, tile or stretch with care. The dark stone ground of the dashboard is visible only as narrow margins and gives no usable swatch.')
    status('AST-0147', 'BLOCKED', 'No usable floor texture can be cut from the sources: every tile and board raster is covered with node rings and markers '
           'at 70 to 170 px spacing (rasters are 140 to 300 ppi), and the largest marker-free square found by masking is 44 to 270 px. '
           'Whole tiles and boards are available as tile art (AST-0133, AST-0117); a seamless flagstone, dirt or bone-pit texture needs node-free tile artwork from the owner or a redraw.')
    print('textures done')


# --------------------------------------------------------------------------- statuses and provenance review
def status(rid, st, reason):
    RECS[rid] = dict(id=rid, parent=rid, status=st, reason=reason, file=None)
    PRODUCED.append(rid); save_records()


REVIEW = [  # (parent, source key, page, object, what, reason)
    ('AST-0135', 'TG', 8, '809, 807', 'Whole character dashboard (1019×806 and 1019×685 px)', 'The name band (top 236 px) is a painted class portrait with painted item roundels. Only the portrait-free lower section was extracted (AST-0135.1, AST-0135.2).'),
    ('AST-0137', 'TG', 6, '638, 636, 634, 785', 'Encounter card fan and event card face (Lifegem)', 'Card faces with painted scenes / a painted figure. Not extracted.'),
    ('AST-0137', 'TG', 5, '155, 344, 353, 350, 332, 326', 'Treasure deck fan and boss data cards (Shortbow, Winged Spear, Dark Sword, Gravelord Sword, Black Knight, Gravelord Nito)', 'Card faces with painted item and boss illustrations. Not extracted.'),
    ('AST-0087', 'TG', 16, '1184, 1188', 'Whole encounter card (Grave Matters, 584×1000 px)', 'Lower right of the card is a painted scene. Only the illustration-free parts were extracted (AST-0087.1, AST-0087.2).'),
    ('AST-0088', 'TG', 24, '1288', 'Whole enemy data card (Skeleton Soldier, 372×520 px)', 'The card centre is a coloured character illustration, not the grey miniature render. Not extracted.'),
    ('AST-0088', 'TG', 28, '1442, 1444', 'Whole boss data card (Gravelord Nito) and behaviour card (Death\'s Embrace)', 'Upper half of both cards is a painted boss illustration. Only the text-box section of the data card was extracted (AST-0088.1).'),
    ('AST-0138', 'PH', 6, '187 (also p.12 object 393)', 'Phantom figure artwork, 815×1110 px with soft mask', 'Looks like a painting (dark painted figure fading to black), not a miniature render. Not extracted.'),
    ('AST-0138', 'DR', 7, '378', 'Mushroom Parent and Child artwork, 1258×1576 px with soft mask', 'Coloured character art on a dark ground, not the grey miniature render. Not extracted.'),
    ('AST-0138', 'IK', 6, '338', 'Knight in a burning landscape, 406×605 px with soft mask', 'Painting. Not extracted.'),
    ('AST-0138', 'EC', 16, '2867 (also p.17 object 2886)', "Executioner's Chariot horse artwork, 847×926 px with soft mask", 'Dark rendered creature art on a grey ground, not the miniature render. Not extracted.'),
    ('AST-0138', 'BDK', 11, '1431', 'Kalameet head artwork on the mega-boss data card, 530×721 px', 'Painted boss illustration. Not extracted.'),
    ('AST-0072', 'PH', 10, '275, 277', 'Two tokens of the invader set-up wheel, 201×201 px', 'Token faces filled with painted art (red eye / red figure) instead of a glyph. Not extracted.'),
]


def run_review():
    n = {}
    for parent, key, page, obj, what, reason in REVIEW:
        n[parent] = n.get(parent, 0) + 1
        rid = f'{parent}.R{n[parent]}'
        RECS[rid] = dict(id=rid, parent=parent, status='PROVENANCE REVIEW', name=what, src=SRC[key][1], page=page, image_object=f'object(s) {obj}', reason=reason, file=None)
        PRODUCED.append(rid)
    save_records()
    print('review items:', len(REVIEW))




def prune(prefixes):
    """Drop records (and this tool's own, untracked files) that a re-run no longer produces."""
    live = set(PRODUCED)
    for rid in [i for i, r in RECS.items() if i not in live and ((r.get('file') or '').startswith(prefixes) or (not r.get('file') and 'assets/icons/' in prefixes))]:
        del RECS[rid]
    keep = {r['file'] for r in RECS.values() if r.get('file')}
    for f in PREV_FILES - keep:
        if f not in TRACKED and os.path.exists(f):
            os.remove(f); print('removed superseded file of this tool:', f)
    save_records()


if __name__ == '__main__':
    todo = [a for a in sys.argv[1:] if a in SECTIONS] or list(SECTIONS)
    for s in todo:
        SECTIONS[s]()
    print('records:', len(RECS), '->', RECFILE)
