#!/usr/bin/env python3
"""Phase 3 asset extraction: the painted art released from the Provenance Review (2026-11-11).

The author confirmed ownership of the painted illustrations on 2026-11-11, so the items that Phase 0 and
Phase 2B held back are extracted here: the paintings AST-0119 to AST-0130, the other painted illustrations
of the official books, whole card faces, whole character dashboards and the card fans. The two community
PDFs are not read.

Method (same as Phase 2B, whose helpers are imported): every file comes from embedded image objects decoded
with `pdfimages -png` (soft mask composited when present) at native resolution, never from a page render, so
no page text of any kind (captions, the personalisation line of the purchased PDFs) can be in a file.
Composites re-join image objects exactly as placed on the page. Large opaque paintings are saved as JPEG
(quality 92, 4:4:4), everything else as PNG.

Writes work/extraction_records_phase3.json (one record per file, schema of the Phase 2B records plus
`phase` and, where a record answers a held review item, `resolves`), layout/art_candidates.json and the
contact sheets build/art_contact*.jpg.

usage: extract_phase3.py [extract] [megaboss] [candidates] [sheets]   (default: all four, in that order)
  extract  = the art, card faces, dashboards and fans of the books catalogued in Phases 0 to 2
  megaboss = the eight mega-boss expansion booklets supplied on 2026-11-11 (parents AST-0156 to AST-0163), essentials only:
             logo-free cover art, one boss painting or concept, the miniature render, both sides of the game board
  megaboss-full = the wider set for those booklets (all paintings, covers with logo, page-region crops of the card faces and
             special-rule plates). NOT part of the default run and not completed or checked in this pass: the lead asked
             for the essentials only. Every page-region crop it makes must be looked at before use (purchaser-line rule).
"""
import os, sys, json, warnings
warnings.simplefilter('ignore')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract_phase2b as P            # also changes to the repository root
import numpy as np
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
P.SCRATCH = 'work/pdfimages/phase3'
RECFILE = 'work/extraction_records_phase3.json'
CANDFILE = 'layout/art_candidates.json'
P2B = json.load(open(P.RECFILE))
RECS, NEXT = {}, {}
# files this tool wrote on an earlier run (they may be committed since): only these may be written again
OWN = {r['file'] for r in json.load(open(RECFILE))} if os.path.exists(RECFILE) else set()
JPG_MIN_PIXELS = 500_000               # opaque paintings at or above this size are stored as JPEG


def next_id(parent):
    if parent not in NEXT:
        ks = [int(r['id'].split('.')[1]) for r in P2B if r['parent'] == parent and '.' in r['id'] and r['id'].split('.')[1].isdigit()]
        NEXT[parent] = max(ks, default=0) + 1
    NEXT[parent] += 1
    return f'{parent}.{NEXT[parent] - 1}'


def save_records():
    for r in RECS.values():            # the purchaser line must never reach a record
        s = json.dumps(r)
        assert '@' not in s and 'Generated for' not in s, r['id']
    txt = json.dumps([RECS[k] for k in sorted(RECS, key=P.idkey)], indent=1, ensure_ascii=False)
    with open(RECFILE + '.tmp', 'w') as f:
        f.write(txt)
    os.replace(RECFILE + '.tmp', RECFILE)


def flatten(im, info):
    """Drop an alpha channel that is opaque everywhere (min alpha >= 240: mask noise only)."""
    if im.mode == 'RGBA':
        lo = im.getchannel('A').getextrema()[0]
        if lo >= 240:
            if info is not None and info.get('has_mask'):
                info['mask_opaque'] = True
            return im.convert('RGB')
    return im


def store(im, parent, folder, slug, art):
    opaque = im.mode != 'RGBA'
    jpg = art and opaque and im.width * im.height >= JPG_MIN_PIXELS
    path = f"assets/{folder}/{parent.lower()}-{slug}.{'jpg' if jpg else 'png'}"
    assert path not in P.TRACKED or path in OWN, 'refusing to overwrite a tracked asset of another phase: ' + path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if jpg:
        im.convert('RGB').save(path, quality=92, subsampling=0, optimize=True)
    else:
        im.save(path, optimize=True)
    return path, ('jpg' if jpg else 'png')


def record(parent, name, typ, key, page, path, fmt, im, method, bbox, image_object, notes, meta, resolves=None):
    rid = next_id(parent)
    r = dict(id=rid, parent=parent, name=name, type=typ, src=P.SRC[key][1], page=page,
             bbox_pt=[round(v, 1) for v in bbox] if bbox else None, image_object=image_object, method=method,
             file=path, format=fmt, dims=f'{im.width}×{im.height} px', has_alpha=im.mode == 'RGBA',
             bytes=os.path.getsize(path), notes=notes, phase=3)
    if resolves:
        r['resolves'] = resolves
    r['design'] = dict(meta)
    RECS[rid] = r
    OWN.add(path)
    save_records()
    print(rid, path, r['dims'], 'alpha' if r['has_alpha'] else 'opaque')
    return r


def single(parent, folder, slug, name, typ, key, page, xref, meta, notes='', crop_frac=None, resolves=None, art=False):
    """One embedded image object -> one file at native resolution (optionally a crop given as fractions l, t, r, b)."""
    im, info = P.emb(key, page, xref)
    native = im.size
    im = flatten(im, info)
    if crop_frac:
        box = (round(crop_frac[0] * im.width), round(crop_frac[1] * im.height), round(crop_frac[2] * im.width), round(crop_frac[3] * im.height))
        im = im.crop(box); info['crop_px'] = list(box)
    if im.mode == 'RGBA':
        im = P.trim(im)
    rects = P.doc(key)[page - 1].get_image_rects(xref)
    bbox = tuple(rects[0]) if rects else None
    info['ppi_as_placed'] = round(native[0] / ((bbox[2] - bbox[0]) / 72)) if bbox else None
    path, fmt = store(im, parent, folder, slug, art)
    mask = ''
    if info['has_mask']:
        mask = (f" + soft mask #{info['smask_pdfimages_num']} (opaque everywhere, dropped)" if info.get('mask_opaque')
                else f" + soft mask #{info['smask_pdfimages_num']} composited to RGBA")
    else:
        mask = ', no soft mask'
    method = (f"pdfimages -png p.{page} image #{info['pdfimages_num']} (object {xref}, {info['native']} {info['colour']}{mask})"
              f"{'; cropped to px box ' + str(tuple(info['crop_px'])) + ' of the object' if crop_frac else ''}"
              f"{'; trimmed to alpha bounds' if im.mode == 'RGBA' else ''}; native resolution, no resampling"
              f"{'; saved as JPEG quality 92 (4:4:4)' if fmt == 'jpg' else ''}")
    return record(parent, name, typ, key, page, path, fmt, im, method, bbox, info, notes, meta, resolves)


def tiles(parent, folder, slug, name, key, page, grid, meta, notes='', resolves=None):
    """Image objects that the source splits into abutting tiles, re-joined edge to edge at native resolution."""
    W = max(ox + P.emb(key, page, x)[0].width for x, ox, oy in grid)
    H = max(oy + P.emb(key, page, x)[0].height for x, ox, oy in grid)
    canvas = Image.new('RGB', (W, H))
    rects = []
    for x, ox, oy in grid:
        canvas.paste(P.emb(key, page, x)[0].convert('RGB'), (ox, oy))
        rects.append(P.doc(key)[page - 1].get_image_rects(x)[0])
    bbox = (min(r.x0 for r in rects), min(r.y0 for r in rects), max(r.x1 for r in rects), max(r.y1 for r in rects))
    path, fmt = store(canvas, parent, folder, slug, True)
    xs = [x for x, _, _ in grid]
    method = (f"pdfimages -png p.{page}: {len(xs)} abutting image tiles (objects {xs[0]} to {xs[-1]}) re-joined edge to edge exactly as "
              f"placed on the page; native resolution, no resampling{'; saved as JPEG quality 92 (4:4:4)' if fmt == 'jpg' else ''}")
    io = dict(xrefs=xs, native=f'{W}×{H}', has_mask=False, ppi_as_placed=round(W / ((bbox[2] - bbox[0]) / 72)))
    return record(parent, name, 'art', key, page, path, fmt, canvas, method, bbox, io, notes, meta, resolves)


def compose(parent, folder, slug, name, key, page, xrefs, meta, notes='', resolves=None, pad=2):
    """A group of embedded objects (a card fan) re-assembled exactly as placed on the page, on a transparent ground.
    Canvas resolution = the highest native resolution among the objects, so nothing is enlarged beyond its source."""
    pg = P.doc(key)[page - 1]
    infos = [i for i in pg.get_image_info(xrefs=True) if i['xref'] in xrefs]
    assert infos, slug
    x0 = min(i['bbox'][0] for i in infos) - pad; y0 = min(i['bbox'][1] for i in infos) - pad
    x1 = max(i['bbox'][2] for i in infos) + pad; y1 = max(i['bbox'][3] for i in infos) + pad
    ppi = round(max(i['width'] / ((i['transform'][0] ** 2 + i['transform'][1] ** 2) ** 0.5 / 72) for i in infos))
    s = ppi / 72
    W, H = round((x1 - x0) * s), round((y1 - y0) * s)
    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cache = {}
    for i in infos:
        xr = i['xref']
        if xr not in cache:
            cache[xr] = P.emb(key, page, xr)[0]
        im = cache[xr]
        a, b, c, d, e, f = i['transform']
        F = np.array([[a / im.width * s, c / im.height * s, (e - x0) * s],
                      [b / im.width * s, d / im.height * s, (f - y0) * s], [0, 0, 1]])
        inv = np.linalg.inv(F)
        canvas.alpha_composite(im.transform((W, H), Image.AFFINE, tuple(inv[:2].flatten()), resample=Image.BICUBIC))
    canvas = P.trim(canvas)
    path, fmt = store(canvas, parent, folder, slug, False)
    order = list(dict.fromkeys(i['xref'] for i in infos))
    method = (f"pdfimages -png p.{page}: {len(infos)} placements of {len(order)} embedded objects ({', '.join(str(x) for x in order)}), each decoded "
              f"natively with its soft mask and re-assembled with its placement matrix in page draw order on a transparent ground at {ppi} ppi "
              f"(the highest native resolution in the group); drop shadows, captions and every other page element are left out")
    io = dict(xrefs=order, ppi=ppi, has_mask=True)
    return record(parent, name, 'photography', key, page, path, fmt, canvas, method, (x0, y0, x1, y1), io, notes, meta, resolves)


# --------------------------------------------------------------------------- the item tables
CH = {n: s for n, s in [(1, '1 Introduction'), (2, '2 Game Components'), (3, '3 Characters'), (4, '4 Equipment'), (5, '5 Tiles and Nodes'),
                        (6, '6 Setup'), (7, '7 Gameplay'), (8, '8 Combat Basics'), (9, '9 Enemy Turn'), (10, '10 Character Turn'),
                        (11, '11 Returning to the Bonfire'), (12, '12 Phantoms'), (13, '13 Mimics'), (14, '14 Crystal Lizards'),
                        (15, '15 Boss Encounters'), (16, '16 Boss Turns'), (17, '17 Boss Special Rules'), (18, '18 Campaign Play'),
                        (19, '19 Campaigns'), (20, '20 Player versus Player'), (21, '21 Glossary'), (22, '22 F.A.Q.'),
                        ('A', 'Appendix A Weapon Stat Revisions'), ('B', 'Appendix B Card Amendments')]}
COVER, BACK, FULL, HDR, COL, SPOT = 'cover', 'back cover', 'full-page plate', 'chapter header strip', 'column plate', 'spot'
NOPARENT = 'No catalogue entry of its own: attached to {} as the closest existing entry.'
LOGO = 'The white "DARK SOULS / THE BOARD GAME" logo lock-up is baked into the image (lower third).'
SHOT = 'In-game render rather than a painting.'


def m(subject, mood, use, ch, also=(), hdr=None, baked=None, kind='painting'):
    return dict(subject=subject, mood=mood, suggested_use=use, also_suits=list(also), suggested_for=CH[ch], hdr=hdr, baked=baked, kind=kind)


# (parent, slug, record name, key, page, xref or tile grid, meta, notes, crop fractions, resolves)
ART = [
    # ---- the held catalogue paintings, AST-0120 to AST-0128
    ('AST-0120', 'knight-resting-at-bonfire', 'Knight resting at a bonfire among ruins (2022 core p.14, 300 ppi)', 'TG', 14, 1152,
     m('A knight rests before a bonfire among broken walls, sparks streaming from the coiled sword', 'warm, weary, quiet', COL, 11, (HDR, SPOT), hdr=0.42),
     'The 2017 book prints a wider framing of the same painting: see the next file of AST-0121.', None, None),
    ('AST-0121', 'tomb-cavern-with-skull-pillar', 'Cavern tomb with a skull-studded pillar (2022 core p.31, 300 ppi)', 'TG', 31, 1488,
     m('A cavern tomb: a pillar studded with skulls, a great trunk of stone beyond, bones across the floor', 'subterranean, ochre, grim', FULL, 5, (HDR, COL), hdr=0.47),
     'The catalogue entry cites p.31 of the 2022 book for "knight resting at bonfire"; the image object on that page is this cavern painting. The bonfire painting named by the entry is the next file (2017 p.31) and AST-0120.', None, None),
    ('AST-0121', 'knight-resting-at-bonfire-wide-2017', 'Knight resting at a bonfire among ruins, wider framing (2017 core p.31)', 'CORE', 31,
     [(1476, 0, 0), (1477, 491, 0), (1478, 0, 428), (1479, 491, 428), (1480, 0, 856), (1481, 701, 856)],
     m('A knight rests before a bonfire among broken arches, wider view with the ruined wall at left', 'warm, weary, quiet', COL, 11, (HDR,), hdr=0.50),
     'Stored in the 2017 PDF as six abutting tiles at 150 ppi. Shows more of the scene than AST-0120 (which is sharper where they overlap).', None, None),
    ('AST-0122', 'ruined-keep-over-graveyard-portrait', 'Ruined keep above a misty graveyard under a storm sky, portrait framing (2022 core p.7, 300 ppi)', 'TG', 7, 793,
     m('A ruined keep on a crag above a mist-filled graveyard, bare branches against a storm sky', 'bleak, stormy, cold', FULL, 1, (COVER, HDR, COL), hdr=0.27),
     'Largest version in the sources. The catalogue entry cites p.32; the painting is on p.7 of the 2022 book and p.32 of the 2017 book.', None, None),
    ('AST-0122', 'ruined-keep-over-graveyard-wide-2017', 'Ruined keep above a misty graveyard, wide framing (2017 core p.32)', 'CORE', 32, 1484,
     m('A ruined keep on a crag above a misty graveyard, wide view with dead trees at both sides', 'bleak, stormy, cold', HDR, 6, (COL,), hdr=0.36),
     'Wider field of view than the portrait framing of the 2022 book, at 150 ppi.', None, None),
    ('AST-0123', 'anor-londo-spires-at-sunset', 'Cathedral spires stacked up a cliff in red evening light (2022 core p.23, 300 ppi)', 'TG', 23, 1278,
     m('Gothic spires and buttresses piled up a cliff face in deep red evening light', 'majestic, red, towering', FULL, 19, (COVER, HDR, COL), hdr=0.20), '', None, None),
    ('AST-0124', 'black-knight-in-flames', 'Black Knight with greatsword, wreathed in flame (2022 core p.19, 300 ppi)', 'TG', 19, 1231,
     m('The Black Knight, horned helm and greatsword, wreathed in flame', 'menacing, fiery, dark', COL, 15, (HDR, SPOT), hdr=0.24),
     'Also in the 2017 book (p.26) at half the resolution; not extracted twice.', None, None),
    ('AST-0125', 'ruined-cathedral-interior', 'Ruined cathedral interior with light through the broken apse (2022 core p.9, 300 ppi)', 'TG', 9, 885,
     m('A ruined cathedral nave, daylight falling through the broken apse onto an overgrown floor', 'solemn, golden, still', COL, 7, (HDR,), hdr=0.30),
     'Also in the 2017 book (p.19) at half the resolution; not extracted twice.', None, None),
    ('AST-0126', 'tomb-colossus-and-lone-knight', 'Monochrome concept painting of a blade-crowned colossus with a lone knight at its foot (2022 core p.15, 300 ppi)', 'TG', 15, 1158,
     m('A towering engine of wheels, coffins and scythe blades looms over a lone knight, in grey monochrome', 'ominous, monochrome, vast', FULL, 16, (HDR, COL), hdr=0.22), '', None, None),
    ('AST-0127', 'knight-kneeling-in-dark-forest', 'Armoured knight kneeling in a moonlit forest (2017 core p.38)', 'CORE', 38, 1505,
     m('An armoured knight kneels in a moonlit forest, a pale light held at the chest', 'nocturnal, blue, lonely', COL, 10, (BACK, HDR), hdr=0.50),
     '150 ppi: about 120 ppi if run across a full page.', None, None),
    ('AST-0128', 'ashen-one-key-art', 'Ember-scarred knight striding forward on a yellow ground (2017 core p.36)', 'CORE', 36, 1497,
     m('An ember-scarred knight strides forward, sword held low, against a sulphur-yellow sky', 'fierce, smouldering, yellow', COL, 8, (SPOT,)), '640 px wide: column width at most.', None, None),
    # ---- AST-0129: environment concept art and campaign-page thumbnails
    ('AST-0129', 'env-gate-tower-2017', 'Environment sketch: gate tower at the end of a walled road (2017 core p.35)', 'CORE', 35, 1492,
     m('Sepia sketch of a square gate tower closing a walled road', 'austere, sepia, quiet', SPOT, 19, (COL,)), '', None, None),
    ('AST-0129', 'env-fortress-boulder-engine-2017', 'Environment sketch: boulder engine in a dark fortress (2017 core p.35)', 'CORE', 35, 1493,
     m('A great stone ball in the machinery of a dark fortress, steam rising', 'mechanical, dark, oppressive', SPOT, 19, (COL,)), '', None, None),
    ('AST-0129', 'env-white-city-spires-2017', 'Environment sketch: white cathedral city (2017 core p.35)', 'CORE', 35, 1494,
     m('Pale cathedral spires of a city in the clouds, loosely painted', 'pale, lofty, serene', SPOT, 19, (COL,)), '', None, None),
    ('AST-0129', 'env-burning-town-below-castle', 'Key art: knight before a burning town and castle (2017 core p.37)', 'CORE', 37, 1500,
     m('A knight stands before a burning town with a castle rising behind it', 'embattled, smoky, dusk', SPOT, 18, (COL,)), '', None, None),
    ('AST-0129', 'env-frost-knight', 'Key art: armoured figure trailing frost, sword drawn (2017 core p.37)', 'CORE', 37, 1501,
     m('An armoured figure lunges with a long sword, trailing pale frost', 'cold, swift, spectral', SPOT, 16, (COL,)), '', None, None),
    ('AST-0129', 'env-dancer-flaming-blade', 'Key art: veiled figure with a flaming curved blade (2017 core p.37)', 'CORE', 37, 1502,
     m('A veiled figure sweeps a flaming curved blade through the dark', 'fiery, sinuous, dark', SPOT, 17, (COL,)), '', None, None),
    ('AST-0129', 'env-fortress-boulder-engine-phantoms', 'Environment sketch: boulder engine in a dark fortress, squarer framing (Phantoms p.17, 300 ppi)', 'PH', 17, 470,
     m('A great stone ball in the machinery of a dark fortress, steam rising (squarer framing)', 'mechanical, dark, oppressive', SPOT, 19, (COL,)), '', None, None),
    ('AST-0129', 'env-gate-tower-phantoms', 'Environment sketch: gate tower, upright framing (Phantoms p.17, 300 ppi)', 'PH', 17, 469,
     m('Sepia sketch of a square gate tower, upright framing', 'austere, sepia, quiet', SPOT, 19, (COL,)), '', None, None),
    ('AST-0129', 'env-white-city-spires-phantoms', 'Environment sketch: white cathedral city, close framing (Phantoms p.17, 300 ppi)', 'PH', 17, 471,
     m('Pale cathedral spires with dark roofs, close framing', 'pale, lofty, serene', SPOT, 19, (COL,)), '', None, None),
    ('AST-0129', 'env-sealed-door-of-light', 'Campaign art: sealed stone door split by white light (Darkroot p.11)', 'DR', 11, 438,
     m('A sealed stone door split by a blade of white light, blue night around mossy ruins', 'mysterious, blue, hushed', COL, 18, (SPOT,)), SHOT, None, None),
    ('AST-0129', 'env-knight-wading-forest-lake', 'Campaign art: knight wading a forest lake at night (Darkroot p.11)', 'DR', 11, 437,
     m('A knight wades through a shallow forest lake at night', 'nocturnal, misty, lonely', SPOT, 7, (COL,)), SHOT + ' Same scene as the Darkroot cover, without the logo.', None, None),
    ('AST-0129', 'env-artorias-crouched', 'Campaign art: Artorias crouched with greatsword (Darkroot p.11)', 'DR', 11, 439,
     m('Knight Artorias crouches low, greatsword trailing, in a blue-lit arena', 'feral, blue, tense', SPOT, 17, (COL,)), '', None, None),
    ('AST-0129', 'env-kalameet-breath-and-knight', 'Campaign art: knight facing the black dragon (Kalameet p.15)', 'BDK', 15, 2025,
     m('A knight with shield raised faces the black dragon under an orange sky', 'heroic, orange, perilous', SPOT, 16, (COL,)), SHOT, None, None),
    ('AST-0129', 'env-iron-keep-forecourt', 'Campaign thumbnail: iron keep forecourt lit by braziers (Iron Keep p.7)', 'IK', 7, 359,
     m('A red-lit iron keep forecourt with burning braziers', 'hot, red, forbidding', SPOT, 19), SHOT + ' 291 px: thumbnail size only.', None, None),
    ('AST-0129', 'env-throne-hall-arches', 'Campaign thumbnail: figure silhouetted in a hall of tall arches (Iron Keep p.7)', 'IK', 7, 360,
     m('A lone figure silhouetted beneath tall pointed arches', 'grand, pale, still', SPOT, 19), SHOT + ' 290 px: thumbnail size only.', None, None),
    ('AST-0129', 'env-windmill-tower', 'Campaign thumbnail: tower hung with windmill sails (Explorers p.15)', 'EX', 15, 1031,
     m('A leaning stone tower hung with windmill sails under a green-grey sky', 'eerie, green, decayed', SPOT, 19), '292 px: thumbnail size only.', None, None),
    ('AST-0129', 'env-bonfire-in-autumn-leaves', 'Campaign thumbnail: bonfire in fallen leaves (Explorers p.15)', 'EX', 15, 1030,
     m('A bonfire burning among fallen autumn leaves', 'warm, restful, autumnal', SPOT, 11), SHOT + ' 292 px: thumbnail size only.', None, None),
    ('AST-0129', 'env-torchlit-arena-tunnel', "Campaign thumbnail: torch-lit arena tunnel (Executioner's Chariot p.19)", 'EC', 19, 2927,
     m('A torch-lit circular tunnel of stone ribs', 'claustrophobic, amber, dark', SPOT, 5), SHOT + ' 290 px: thumbnail size only.', None, None),
    ('AST-0129', 'env-greatsword-bearer-above-forest', "Campaign thumbnail: warrior with a great blade above a dusk forest (Executioner's Chariot p.19)", 'EC', 19, 2926,
     m('A warrior shoulders a huge blade above a pine forest at dusk', 'brooding, green, windswept', SPOT, 20), SHOT + ' 288 px: thumbnail size only.', None, None),
    ('AST-0129', 'concept-blood-stained-roots', 'Concept painting: mass of twisted roots stained dark red (2022 core p.12, 300 ppi)', 'TG', 12, 1052,
     m('A mass of twisted roots stained dark red against a pale wall', 'organic, unsettling, pale', COL, 9, (HDR,), hdr=0.50), NOPARENT.format('AST-0129'), None, None),
    ('AST-0129', 'concept-stone-bridge-and-city', 'Concept painting: great stone bridge with a city beyond (2022 core p.13, 300 ppi)', 'TG', 13, 1089,
     m('A great stone bridge arches over dark water, a towered city rising behind it', 'gloomy, monumental, grey', COL, 18, (HDR,), hdr=0.33), NOPARENT.format('AST-0129'), None, None),
    ('AST-0129', 'concept-flooded-cavern-light-shaft', 'Concept painting: shaft of light into a flooded cavern (2022 core p.22, 300 ppi)', 'TG', 22, 1272,
     m('A shaft of amber light falls into a flooded cavern of roots and pale water', 'deep, amber, silent', COL, 10, (HDR,), hdr=0.70), NOPARENT.format('AST-0129') + ' Very tall (1:1.93): suits a full column height.', None, None),
    ('AST-0129', 'concept-hooded-figure-and-light-pillars', 'Concept painting: hooded figure seated before pillars of light (2022 core p.26, 300 ppi)', 'TG', 26, 1384,
     m('A hooded figure sits by a small fire before towering pillars of light', 'contemplative, golden, hazy', COL, 21, (HDR,), hdr=0.60),
     NOPARENT.format('AST-0129') + ' Also in the 2017 book (p.14) at half the resolution; not extracted twice.', None, None),
    ('AST-0129', 'concept-ruined-parish-green-ink', 'Concept sketch in green ink: ruined tower and courtyard with a crow (2017 core p.15)', 'CORE', 15, 1224,
     m('Green-ink sketch of a ruined tower above a walled courtyard, a crow perched at left', 'sketchy, green, desolate', SPOT, 5, (COL,)), NOPARENT.format('AST-0129') + ' 465 px wide.', None, None),
    ('AST-0129', 'concept-ruined-gate-with-roots-wide', 'Concept painting: ruined gate overgrown with roots, wide framing (2017 core p.16)', 'CORE', 16, 1235,
     m('A ruined gatehouse choked with roots on a mossy rise, a red figure at its door', 'overgrown, grey-green, lonely', HDR, 6, (COL,), hdr=0.45),
     NOPARENT.format('AST-0129') + ' The Darkroot book prints an upright framing at 300 ppi (AST-0130).', None, None),
    ('AST-0129', 'concept-misty-ruins-panorama', 'Concept painting: panorama of ruins in mist (2017 core p.23)', 'CORE', 23, 1333,
     m('A panorama of drowned ruins and leaning spars fading into mist', 'misty, grey, desolate', HDR, 7, (COL,), hdr=0.50), NOPARENT.format('AST-0129') + ' Already about 2:1.', None, None),
    ('AST-0129', 'concept-rose-marble-hall-2017', 'Concept painting: rose marble cathedral hall with a small red figure (2017 core p.34)', 'CORE', 34, 1489,
     m('A vast rose-marble cathedral hall of statues and galleries, one small red figure on the floor', 'opulent, rose, hushed', COL, 19, (SPOT,)), NOPARENT.format('AST-0129'), None, None),
    ('AST-0129', 'concept-rose-marble-hall-phantoms', 'Concept painting: rose marble hall, lower part at 300 ppi (Phantoms p.16)', 'PH', 16, 452,
     m('The statue wall of a rose-marble hall, one small red figure on the dark floor', 'opulent, rose, hushed', COL, 12, (SPOT,)), NOPARENT.format('AST-0129') + ' Sharper crop of the lower half of the 2017 p.34 painting.', None, None),
    # ---- AST-0130: expansion cover key art and expansion interior art
    ('AST-0130', 'cover-phantoms', 'Phantoms expansion front cover: white phantom duellist on black, logo baked in', 'PH', 1, 24,
     m('A white phantom duellist in a wide-brimmed hat on black, with the game logo', 'spectral, stark, elegant', COVER, 12, baked=LOGO), LOGO + ' The same figure without the logo is AST-0138 (phantom figure with soft mask).', None, None),
    ('AST-0130', 'cover-phantoms-art-only', 'Phantoms front cover, art above the logo', 'PH', 1, 24,
     m('A white phantom duellist in a wide-brimmed hat on black', 'spectral, stark, elegant', COL, 12, (COVER,)), 'Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish.', (0, 0, 1, 0.615), None),
    ('AST-0130', 'cover-kalameet', 'Black Dragon Kalameet expansion front cover, logo baked in', 'BDK', 1, 22,
     m('The black dragon hangs in a sulphur sky above a tiny knight, with the game logo', 'awe, sulphur, looming', COVER, 15, baked=LOGO), LOGO + ' The same painting without the logo, and larger, is the next file.', None, None),
    ('AST-0130', 'kalameet-over-lone-knight', 'Black Dragon Kalameet hanging in a sulphur sky above a lone knight, no logo (Kalameet p.6, largest version)', 'BDK', 6, 693,
     m('The black dragon hangs in a sulphur-yellow sky above a tiny lone knight', 'awe, sulphur, looming', FULL, 15, (COVER, HDR, COL), hdr=0.17), 'Text-free and larger than the cover image. A third, smaller copy on p.14 was not extracted.', None, None),
    ('AST-0130', 'cover-executioners-chariot', "Executioner's Chariot expansion front cover, logo baked in", 'EC', 1, 21,
     m('A skeletal chariot horse rears out of the dark, with the game logo', 'dread, black, feral', COVER, 15, baked=LOGO), LOGO + ' 846 px wide (150 ppi).', None, None),
    ('AST-0130', 'cover-executioners-chariot-art-only', "Executioner's Chariot front cover, art above the logo", 'EC', 1, 21,
     m('A skeletal chariot horse rears out of the dark', 'dread, black, feral', COL, 16, (SPOT,)), 'Text-free crop: the top 61.5 % of the cover image.', (0, 0, 1, 0.615), None),
    ('AST-0130', 'cover-darkroot', 'Darkroot expansion front cover, logo baked in', 'DR', 1, 22,
     m('A knight wades a moonlit forest lake, with the game logo', 'nocturnal, blue, misty', COVER, 19, baked=LOGO), LOGO, None, None),
    ('AST-0130', 'cover-darkroot-art-only', 'Darkroot front cover, art above the logo', 'DR', 1, 22,
     m('A knight wades a moonlit forest lake beneath dark trees', 'nocturnal, blue, misty', COL, 7, (HDR, FULL), hdr=0.70), 'Text-free crop: the top 61.5 % of the cover image.', (0, 0, 1, 0.615), None),
    ('AST-0130', 'cover-iron-keep', 'Iron Keep expansion front cover, logo baked in', 'IK', 1, 20,
     m('Knights stand before a dark keep split by a seam of molten light, with the game logo', 'ominous, ember, smoky', COVER, 19, baked=LOGO), LOGO + ' 850 px wide (150 ppi).', None, None),
    ('AST-0130', 'cover-iron-keep-art-only', 'Iron Keep front cover, art above the logo', 'IK', 1, 20,
     m('Knights stand before a dark keep split by a seam of molten light', 'ominous, ember, smoky', COL, 18, (SPOT,)), 'Text-free crop: the top 61.5 % of the cover image.', (0, 0, 1, 0.615), None),
    ('AST-0130', 'cover-explorers', 'Explorers expansion front cover, logo baked in', 'EX', 1, 21,
     m('An armoured pursuer with a great blade stands in a shaft of light, with the game logo', 'cold, steel, dramatic', COVER, 13, baked=LOGO), LOGO + ' 849 px wide (150 ppi).', None, None),
    ('AST-0130', 'cover-explorers-art-only', 'Explorers front cover, art above the logo', 'EX', 1, 21,
     m('An armoured pursuer with a great blade stands in a shaft of light', 'cold, steel, dramatic', COL, 9, (SPOT,)), 'Text-free crop: the top 61.5 % of the cover image.', (0, 0, 1, 0.615), None),
    ('AST-0130', 'cover-characters', 'Characters expansion front cover, logo baked in', 'CH', 1, 21,
     m('A hooded adventurer in dark leather on black, with the game logo', 'shadowed, leather, resolute', COVER, 3, baked=LOGO), LOGO, None, None),
    ('AST-0130', 'cover-characters-art-only', 'Characters front cover, art above the logo', 'CH', 1, 21,
     m('A hooded adventurer in dark leather on black', 'shadowed, leather, resolute', COL, 3, (SPOT,)), 'Text-free crop: the top 61.5 % of the cover image; the figure is cut at the knee by the crop.', (0, 0, 1, 0.615), None),
    ('AST-0130', 'backcover-phantoms-red-invader', 'Phantoms back cover: red phantom knight on black', 'PH', 20, 507,
     m('A red phantom knight stands on black', 'hostile, crimson, stark', BACK, 20, (FULL, COL)), '', None, None),
    ('AST-0130', 'backcover-kalameet-close', 'Black Dragon Kalameet back cover: the dragon close, fading to black', 'BDK', 16, 2040,
     m('The black dragon seen close from below, one red eye burning, fading to black at the foot', 'menacing, red-eyed, dark', BACK, 17, (FULL, COL)), 'The lower third is black (room for back-cover text).', None, None),
    ('AST-0130', 'backcover-chariot-rope-bridge', "Executioner's Chariot back cover: torch-bearer on a rope bridge, fading to black", 'EC', 20, 2937,
     m('A torch-bearer crosses a rope bridge toward a dark fortress, fading to black at the foot', 'tense, torchlit, dark', BACK, 18, (COL,)), SHOT + ' 846 px wide (150 ppi). The lower third is black.', None, None),
    ('AST-0130', 'backcover-darkroot-artorias', 'Darkroot back cover: Artorias on black', 'DR', 12, 453,
     m('Knight Artorias, cloak streaming, on black', 'tragic, blue-steel, stark', BACK, 15, (FULL, COL)), '', None, None),
    ('AST-0130', 'backcover-iron-keep-tower', 'Iron Keep back cover: crumbling tower in a lake of fire', 'IK', 8, 373,
     m('A crumbling tower rises from a lake of fire under ash clouds', 'infernal, ashen, towering', BACK, 19, (COL,)), '850 px wide (150 ppi).', None, None),
    ('AST-0130', 'backcover-explorers-stone-arch', 'Explorers back cover: ruined stone arch on a mountain path', 'EX', 16, 1046,
     m('A ruined stone arch on a mountain path, bare trees and pale cliffs', 'quiet, grey, wintry', BACK, 22, (COL,)), '849 px wide (150 ppi).', None, None),
    ('AST-0130', 'backcover-characters-armour', 'Characters back cover: suit of dark plate armour on black', 'CH', 8, 200,
     m('A suit of dark, ragged plate armour on black', 'sombre, steel, still', BACK, 4, (FULL, COL)), '', None, None),
    ('AST-0130', 'phantoms-red-phantom-smear', 'Phantoms p.3: red phantom figure on black', 'PH', 3, 62,
     m('A red phantom, half figure and half blood-smear, on black', 'violent, crimson, abstract', COL, 12, (FULL, HDR), hdr=0.36), NOPARENT.format('AST-0130'), None, None),
    ('AST-0130', 'phantoms-knight-among-blue-spirits', 'Phantoms p.9: armoured knight silhouetted against blue spirits', 'PH', 9, 265,
     m('An armoured knight silhouetted against swirling blue spirits', 'electric, blue, embattled', HDR, 20, (COL,), hdr=0.50), NOPARENT.format('AST-0130'), None, None),
    ('AST-0130', 'phantoms-procession-sketch', 'Phantoms p.12: monochrome sketch of warriors on a great stair', 'PH', 12, 386,
     m('Monochrome sketch of a band of warriors climbing a great stair toward a giant figure', 'monochrome, rain-streaked, epic', HDR, 12, (COL,), hdr=0.55), NOPARENT.format('AST-0130'), None, None),
    ('AST-0130', 'phantoms-ruined-castle-on-cliff', 'Phantoms p.13: ruined castle of spires on a cliff', 'PH', 13, 419,
     m('A ruined castle of spires and buttresses on a cliff under a pale sky', 'lofty, weathered, pale', FULL, 19, (HDR, COL), hdr=0.30), NOPARENT.format('AST-0130'), None, None),
    ('AST-0130', 'phantoms-shanty-town-in-the-murk', 'Phantoms p.15: shanty town on stilts in a murky cavern', 'PH', 15, 440,
     m('A shanty town on stilts in a murky yellow-green cavern, fires burning below', 'murky, sickly, sprawling', FULL, 19, (HDR, COL), hdr=0.33),
     NOPARENT.format('AST-0130') + ' The 2017 book (p.21) carries a smaller copy inside a photographed art-book spread with caption text; that object was not extracted.', None, None),
    ('AST-0130', 'kalameet-close-from-below', 'Kalameet p.3: the black dragon close from below', 'BDK', 3, 56,
     m('The black dragon seen close from below against a pale green sky', 'menacing, red-eyed, close', COL, 17, (SPOT,)), SHOT + ' Uncropped frame of the back-cover image, 640 px wide.', None, None),
    ('AST-0130', 'kalameet-overgrown-forest-gate', 'Kalameet p.10: overgrown temple gate in a red-gold forest', 'BDK', 10, 1348,
     m('An overgrown temple gate in a red-gold forest, a small red figure in the doorway', 'lush, amber, secretive', FULL, 19, (HDR, COL), hdr=0.45), NOPARENT.format('AST-0130'), None, None),
    ('AST-0130', 'chariot-knight-by-bonfire', "Executioner's Chariot p.3: knight seated by a bonfire below a cliff fortress", 'EC', 3, 55,
     m('A knight sits by a bonfire below a cliff-top fortress at night', 'restful, firelit, blue-dark', COL, 11, (SPOT,)), SHOT + ' 626 px wide.', None, None),
    ('AST-0130', 'chariot-rope-bridge-at-dusk', "Executioner's Chariot p.6: rope bridge under a green dusk sky", 'EC', 6, 1151,
     m('A rope bridge sags between cliffs under a green dusk sky', 'eerie, green, empty', COL, 5, (SPOT,)), SHOT + ' 626 px wide.', None, None),
    ('AST-0130', 'chariot-horse-in-the-arena', "Executioner's Chariot p.10: the chariot horse breathing mist in the arena", 'EC', 10, 1858,
     m('The skeletal chariot horse breathes mist in a torch-lit arena, a fallen figure before it', 'brutal, torchlit, smoky', COL, 16, (SPOT,)), SHOT + ' 626 px wide.', None, None),
    ('AST-0130', 'chariot-torch-bearer-in-corridor', "Executioner's Chariot p.13: torch-bearer in a fire-lit corridor", 'EC', 13, 2731,
     m('A hooded torch-bearer advances down a fire-lit stone corridor', 'tense, amber, enclosed', COL, 9, (SPOT,)), SHOT + ' 626 px wide.', None, None),
    ('AST-0130', 'chariot-warrior-against-skeletons', "Executioner's Chariot p.15: red-armoured warrior fighting shield-bearing skeletons", 'EC', 15, 2845,
     m('A red-armoured warrior fights shield-bearing skeletons by firelight', 'frantic, firelit, red', COL, 8, (SPOT,)), SHOT + ' 626 px wide.', None, None),
    ('AST-0130', 'darkroot-grave-with-planted-swords', 'Darkroot p.3: ink sketch of a great gravestone ringed by planted swords', 'DR', 3, 74,
     m('Ink sketch on tan paper of a great gravestone ringed by swords planted in the earth', 'elegiac, sepia, still', FULL, 21, (HDR, COL), hdr=0.62), NOPARENT.format('AST-0130'), None, None),
    ('AST-0130', 'darkroot-ruined-gate-with-roots-upright', 'Darkroot p.8: ruined gate overgrown with roots, upright framing (300 ppi)', 'DR', 8, 388,
     m('A ruined gatehouse choked with roots, a dead tree and a tall sword-like spire beside it', 'overgrown, grey-green, lonely', FULL, 6, (HDR, COL), hdr=0.55), NOPARENT.format('AST-0130') + ' Upright, sharper framing of the 2017 p.16 painting.', None, None),
    ('AST-0130', 'darkroot-artorias-concept-front-and-back', 'Darkroot p.9: Artorias concept art, front and back views', 'DR', 9, 409,
     m('Concept art of Knight Artorias in tattered blue, front and back views', 'tragic, dark-blue, studied', COL, 15, (FULL,)), NOPARENT.format('AST-0130'), None, None),
    ('AST-0130', 'darkroot-overgrown-stone-doorway', 'Darkroot p.10: sketch of an overgrown arched stone doorway', 'DR', 10, 420,
     m('Sketch of a heavy arched stone doorway overgrown with moss and leaves', 'ancient, mossy, closed', COL, 5, (SPOT,)), NOPARENT.format('AST-0130'), None, None),
    ('AST-0130', 'iron-keep-throne-in-fire-clouds', 'Iron Keep p.4: iron throne-keep in clouds of fire, wide', 'IK', 4, 319,
     m('An iron throne-keep stands in a sea of fire-lit cloud', 'infernal, red, brooding', COL, 19, (SPOT,)), NOPARENT.format('AST-0130') + ' 628 px wide (about 2:1): too small for a full-width strip.', None, None),
    ('AST-0130', 'explorers-castle-at-dusk', 'Explorers p.3: gothic castle over water in red dusk', 'EX', 3, 55,
     m('A gothic castle of spires stands over water in red dusk light', 'grand, red, fading', COL, 19, (SPOT,)), NOPARENT.format('AST-0130') + ' 630 px wide.', None, None),
    ('AST-0130', 'explorers-shrine-mirrored-in-water', 'Explorers p.7: shrine mirrored in still water under a column of light', 'EX', 7, 797,
     m('A shrine and its reflection in still blue water, joined by a column of light', 'serene, blue, luminous', COL, 14, (SPOT,)), NOPARENT.format('AST-0130') + ' 632 px wide.', None, None),
    ('AST-0130', 'explorers-rain-lashed-ruined-stair', 'Explorers p.8: rain-lashed ruined stair lined with statues', 'EX', 8, 806,
     m('A rain-lashed ruined stair climbs between broken walls and spear-bearing statues', 'drenched, blue-grey, ruined', COL, 5, (SPOT,)), NOPARENT.format('AST-0130') + ' 628 px wide.', None, None),
    ('AST-0130', 'explorers-chapel-with-stained-glass', 'Explorers p.9: chapel interior with a great stained-glass window', 'EX', 9, 815,
     m('A dark chapel lit by a great stained-glass window above an altar', 'reverent, dim, jewelled', COL, 4, (SPOT,)), NOPARENT.format('AST-0130') + ' 632 px wide.', None, None),
    ('AST-0130', 'explorers-wanderer-before-buried-door', 'Explorers p.13: lone wanderer before a great buried doorway', 'EX', 13, 1001,
     m('A lone wanderer crosses drifted sand toward a great half-buried doorway', 'desolate, dun, windblown', COL, 18, (SPOT,)), NOPARENT.format('AST-0130') + ' 632 px wide.', None, None),
    ('AST-0130', 'explorers-knight-in-golden-hall', 'Explorers p.14: knight on a fallen column in a golden hall', 'EX', 14, 1012,
     m('A knight stands on a fallen column in a hall of gold light and gnarled pillars', 'radiant, golden, ruined', SPOT, 10, (COL,)), NOPARENT.format('AST-0130') + ' 406 px wide.', None, None),
    ('AST-0130', 'characters-pilgrim-before-golden-city', 'Characters p.3: lone pilgrim before a golden city of spires (largest painting with a figure)', 'CH', 3, 55,
     m('A lone pilgrim looks out over a golden city of spires under a heavy sky', 'golden, vast, wistful', FULL, 3, (COVER, HDR, COL), hdr=0.48), NOPARENT.format('AST-0130'), None, None),
    # ---- AST-0138: the art held in Phase 2B beside the expansion miniature renders
    ('AST-0138', 'art-phantom-duellist-white', 'White phantom duellist, cut out by its soft mask (Phantoms p.6)', 'PH', 6, 187,
     m('A white phantom duellist in a wide-brimmed hat, fading out below the knee', 'spectral, stark, elegant', COL, 12, (SPOT,)), 'Soft mask fades the figure into transparency at the foot: place on a dark ground.', None, 'AST-0138.R1'),
    ('AST-0138', 'art-phantom-red-smear', 'Red phantom figure, cut out by its soft mask (Phantoms p.12)', 'PH', 12, 393,
     m('A red phantom figure on black, fading out at the foot', 'violent, crimson, abstract', SPOT, 20, (COL,)), 'Soft mask fades the image into transparency at the foot: place on a dark ground. Named as a second object of the same review item, but it is a different image.', None, 'AST-0138.R1'),
    ('AST-0138', 'art-mushroom-parent-and-child', 'Mushroom Parent and Child artwork (Darkroot p.7, 300 ppi)', 'DR', 7, 378,
     m('A Mushroom Parent holding the hand of a Mushroom Child, on a dark ground', 'odd, gentle, dark', COL, 9, (SPOT,)), 'The soft mask is opaque apart from noise (min alpha 243), so the dark ground is part of the image.', None, 'AST-0138.R2'),
    ('AST-0138', 'art-knight-in-burning-waste', 'Knight pierced by arrows in a burning waste (Iron Keep p.6)', 'IK', 6, 338,
     m('A knight, arrows in his back, stands in a burning waste under a red sun', 'defiant, red, scorched', SPOT, 8, (COL,)), '406 px wide.', None, 'AST-0138.R3'),
    ('AST-0138', 'art-chariot-horse', "Executioner's Chariot horse artwork (p.16)", 'EC', 16, 2867,
     m('The skeletal, ragged horse of the Executioner\'s Chariot on a grey ground', 'gaunt, grey, feral', COL, 15, (SPOT,)), '', None, 'AST-0138.R4'),
    ('AST-0138', 'art-chariot-and-rider', "Executioner's Chariot and rider artwork (p.17)", 'EC', 17, 2886,
     m('The spiked chariot and its armoured rider on a grey ground', 'cruel, grey, iron', COL, 17, (SPOT,)), 'Named as a second object of the same review item, but it is a different image.', None, 'AST-0138.R4'),
    ('AST-0138', 'art-kalameet-head', 'Black Dragon Kalameet head artwork from the mega-boss data card, cut out by its soft mask (Kalameet p.11)', 'BDK', 11, 1431,
     m('The horned head and neck of the black dragon, fading out below', 'menacing, dark, golden-horned', SPOT, 17, (COL,)), 'Soft mask fades the image into transparency below: place on a dark ground.', None, 'AST-0138.R5'),
    ('AST-0138', 'art-treasure-chest-closed', 'Painted treasure chest, closed (Explorers p.10)', 'EX', 10, 841,
     m('A closed wooden treasure chest', 'plain, wooden, expectant', SPOT, 13), 'Below the 400 px rule (201 px): kept because the Mimic and Crystal Lizard chapters have no other art. Thumbnail size only.', None, None),
    ('AST-0138', 'art-treasure-chest-crystal-glow', 'Painted treasure chest, open with a crystal glow (Explorers p.10)', 'EX', 10, 843,
     m('An open treasure chest with a pale crystal glow inside', 'luminous, cool, lucky', SPOT, 14), 'Below the 400 px rule (201 px): kept for the Crystal Lizard chapter. Thumbnail size only.', None, None),
    ('AST-0138', 'art-mimic-chest-open', 'Painted Mimic: chest open, lined with teeth (Explorers p.10)', 'EX', 10, 844,
     m('A Mimic: a treasure chest gaping open, lined with teeth', 'grotesque, toothy, sudden', SPOT, 13), 'Below the 400 px rule (201 px): kept for the Mimic chapter. Thumbnail size only.', None, None),
    ('AST-0138', 'art-mimic-walking', 'Mimic walking on long limbs, cut out by its soft mask (Explorers p.11)', 'EX', 11, 879,
     m('A Mimic risen on long thin limbs, chest for a head', 'grotesque, gangling, dark', SPOT, 13), 'Below the 400 px rule (275 px wide): kept for the Mimic chapter. Soft mask fades it out below: place on a dark ground.', None, None),
]

CARDTXT = 'Card face: the title, icons and rules text are part of the card image.'


def card(parent, slug, name, key, page, xref, ch, small=False, resolves=None, extra=''):
    note = (extra + ' ' if extra else '') + ('Under 200 px on the long side (about 135 ppi as printed): thumbnail size only.' if small else '')
    return (parent, slug, name, key, page, xref,
            m(name.split(' (')[0], 'card face', SPOT, ch, baked=CARDTXT, kind='card face'), note.strip(), None, resolves)


EV = NOPARENT.format('AST-0086 (the card frame family it shares)')
CARDS = [
    # equipment, treasure and event cards -> AST-0086
    card('AST-0086', 'equipment-card-shortbow', 'Shortbow equipment card (2022 core p.10)', 'TG', 10, 929, 4),
    card('AST-0086', 'equipment-card-ember', 'Ember treasure card (2022 core p.10)', 'TG', 10, 931, 4),
    card('AST-0086', 'equipment-card-carthus-flame-arc', 'Carthus Flame Arc upgrade card (2022 core p.10)', 'TG', 10, 933, 4),
    card('AST-0086', 'equipment-card-obscuring-ring', 'Obscuring Ring upgrade card (2022 core p.10)', 'TG', 10, 935, 4),
    card('AST-0086', 'equipment-card-dragonslayer-spear', 'Dragonslayer Spear equipment card (2022 core p.22)', 'TG', 22, 1271, 'A'),
    card('AST-0086', 'equipment-card-titanite-shard', 'Titanite Shard upgrade card (2022 core p.27)', 'TG', 27, 1417, 4),
    card('AST-0086', 'equipment-card-morning-star', 'Morning Star equipment card (2022 core p.27)', 'TG', 27, 1419, 'A'),
    card('AST-0086', 'equipment-card-chloranthy-ring', 'Chloranthy Ring upgrade card (2022 core p.27)', 'TG', 27, 1421, 4),
    card('AST-0086', 'equipment-card-sunless-armour', 'Sunless Armour equipment card (2022 core p.27)', 'TG', 27, 1423, 4),
    card('AST-0086', 'equipment-card-mace', 'Mace starting equipment card (2022 core p.4)', 'TG', 4, 187, 'A', small=True),
    card('AST-0086', 'equipment-card-hand-axe', 'Hand Axe starting equipment card (2022 core p.4)', 'TG', 4, 159, 'A', small=True),
    card('AST-0086', 'equipment-card-winged-spear', 'Winged Spear treasure card (2022 core p.5)', 'TG', 5, 344, 'A', small=True),
    card('AST-0086', 'equipment-card-dark-sword', 'Dark Sword treasure card (2022 core p.5)', 'TG', 5, 353, 'A', small=True),
    card('AST-0086', 'equipment-card-gravelord-sword', 'Gravelord Sword boss treasure card (2022 core p.5)', 'TG', 5, 350, 'A', small=True),
    card('AST-0086', 'event-card-green-blossom', 'Green Blossom event card (2022 core p.19)', 'TG', 19, 1230, 7, extra=EV),
    card('AST-0086', 'event-card-lifegem', 'Lifegem event card (2022 core p.6)', 'TG', 6, 785, 7, small=True, resolves='AST-0137.R1', extra=EV),
    card('AST-0086', 'equipment-card-greataxe-2017', 'Greataxe equipment card (2017 core p.12)', 'CORE', 12, 1189, 'A'),
    card('AST-0086', 'equipment-card-titanite-shard-2017', 'Titanite Shard upgrade card (2017 core p.12)', 'CORE', 12, 1188, 'B'),
    card('AST-0086', 'equipment-card-sunless-armour-2017', 'Sunless Armour equipment card (2017 core p.14)', 'CORE', 14, 1210, 'B'),
    card('AST-0086', 'equipment-card-morning-star-2017', 'Morning Star equipment card (2017 core p.14)', 'CORE', 14, 1216, 'B'),
    card('AST-0086', 'equipment-card-shortsword-2017', 'Shortsword equipment card (2017 core p.22)', 'CORE', 22, 1328, 'A'),
    card('AST-0086', 'equipment-card-dragonslayer-spear-2017', 'Dragonslayer Spear equipment card (2017 core p.23)', 'CORE', 23, 1332, 'B'),
    card('AST-0086', 'equipment-card-abyss-greatsword', 'Abyss Greatsword boss treasure card (Darkroot p.5)', 'DR', 5, 362, 'A'),
    card('AST-0086', 'equipment-card-greatsword-of-artorias', 'Greatsword of Artorias boss treasure card (Darkroot p.5)', 'DR', 5, 363, 'A'),
    # encounter cards -> AST-0087
    card('AST-0087', 'encounter-card-grave-matters', 'Grave Matters encounter card, whole (2022 core p.16, 300 ppi)', 'TG', 16, 1184, 6, resolves='AST-0087.R1',
         extra='Largest card image in the sources. The smaller copies on p.16 (350×600) and p.6 were not extracted.'),
    card('AST-0087', 'encounter-card-lakeview-refuge', 'Lakeview Refuge encounter card (2022 core p.6)', 'TG', 6, 634, 6, resolves='AST-0137.R1'),
    card('AST-0087', 'encounter-card-the-abandoned-chest', 'The Abandoned Chest encounter card (2022 core p.6)', 'TG', 6, 636, 6, resolves='AST-0137.R1'),
    card('AST-0087', 'encounter-card-demon-ruins-2017', 'Demon Ruins encounter card (2017 core p.17)', 'CORE', 17, 1240, 'B'),
    card('AST-0087', 'encounter-card-the-forgotten-2017', 'The Forgotten encounter card (2017 core p.18)', 'CORE', 18, 1278, 'B'),
    card('AST-0087', 'encounter-card-ghostly-keep-2017', 'Ghostly Keep encounter card (2017 core p.6)', 'CORE', 6, 898, 'B', small=True),
    card('AST-0087', 'encounter-card-prison-tower-2017', 'Prison Tower encounter card (2017 core p.6)', 'CORE', 6, 892, 'B', small=True),
    card('AST-0087', 'encounter-card-pit-of-the-dead-2017', 'Pit of the Dead encounter card (2017 core p.6)', 'CORE', 6, 885, 'B', small=True),
    # enemy data, boss data and behaviour cards -> AST-0088
    card('AST-0088', 'enemy-card-skeleton-soldier', 'Skeleton Soldier enemy data card (2022 core p.24)', 'TG', 24, 1288, 9, resolves='AST-0088.R1'),
    card('AST-0088', 'boss-card-gravelord-nito', 'Gravelord Nito boss data card, whole (2022 core p.28, 300 ppi)', 'TG', 28, 1442, 15, resolves='AST-0088.R2'),
    card('AST-0088', 'behaviour-card-deaths-embrace', "Death's Embrace boss behaviour card (2022 core p.28)", 'TG', 28, 1444, 16, resolves='AST-0088.R2'),
    card('AST-0088', 'enemy-card-giant-skeleton-archer', 'Giant Skeleton Archer enemy data card (2022 core p.4)', 'TG', 4, 167, 9, small=True),
    card('AST-0088', 'enemy-card-necromancer', 'Necromancer enemy data card (2022 core p.4)', 'TG', 4, 179, 9, small=True),
    card('AST-0088', 'enemy-card-giant-skeleton-soldier', 'Giant Skeleton Soldier enemy data card (2022 core p.4)', 'TG', 4, 183, 9, small=True),
    card('AST-0088', 'enemy-card-skeleton-archer', 'Skeleton Archer enemy data card (2022 core p.4)', 'TG', 4, 171, 9, small=True),
    card('AST-0088', 'enemy-card-skeleton-beast', 'Skeleton Beast enemy data card (2022 core p.4)', 'TG', 4, 175, 9, small=True),
    card('AST-0088', 'boss-card-black-knight', 'Black Knight mini-boss data card (2022 core p.5)', 'TG', 5, 332, 15, small=True, resolves='AST-0137.R2'),
    card('AST-0088', 'behaviour-card-overhead-swing', 'Overhead Swing boss behaviour card (2022 core p.5)', 'TG', 5, 330, 16, small=True),
    card('AST-0088', 'behaviour-card-lunging-cleave', 'Lunging Cleave boss behaviour card (2022 core p.5)', 'TG', 5, 324, 16, small=True),
    card('AST-0088', 'enemy-card-hollow-soldier-2017', 'Hollow Soldier enemy data card (2017 core p.24)', 'CORE', 24, 1336, 'B', extra='A smaller copy on p.20 was not extracted.'),
    card('AST-0088', 'enemy-card-large-hollow-soldier-2017', 'Large Hollow Soldier enemy data card (2017 core p.4)', 'CORE', 4, 252, 'B', small=True),
    card('AST-0088', 'enemy-card-crossbow-hollow-2017', 'Crossbow Hollow enemy data card (2017 core p.4)', 'CORE', 4, 238, 'B', small=True),
    card('AST-0088', 'boss-card-dancer-of-the-boreal-valley-2017', 'Dancer of the Boreal Valley boss data card (2017 core p.26)', 'CORE', 26, 1349, 17),
    card('AST-0088', 'behaviour-card-blade-dance-2017', 'Blade Dance boss behaviour card (2017 core p.27)', 'CORE', 27, 1371, 16, extra='A smaller copy on p.29 was not extracted.'),
    card('AST-0088', 'enemy-card-mushroom-parent', 'Mushroom Parent enemy data card (Darkroot p.4)', 'DR', 4, 168, 9),
    card('AST-0088', 'enemy-card-plow-scarecrow', 'Plow Scarecrow enemy data card (Darkroot p.4)', 'DR', 4, 170, 9),
    card('AST-0088', 'enemy-card-shears-scarecrow', 'Shears Scarecrow enemy data card (Darkroot p.4)', 'DR', 4, 172, 9),
    card('AST-0088', 'enemy-card-demonic-foliage', 'Demonic Foliage enemy data card (Darkroot p.4)', 'DR', 4, 190, 9),
    card('AST-0088', 'enemy-card-mushroom-child', 'Mushroom Child enemy data card (Darkroot p.4)', 'DR', 4, 192, 9),
    card('AST-0088', 'enemy-card-stone-knight', 'Stone Knight enemy data card (Darkroot p.5)', 'DR', 5, 345, 9),
    card('AST-0088', 'enemy-card-stone-guardian', 'Stone Guardian enemy data card (Darkroot p.5)', 'DR', 5, 352, 9),
    card('AST-0088', 'boss-card-knight-artorias', 'Knight Artorias boss data card (Darkroot p.5)', 'DR', 5, 358, 17),
    card('AST-0088', 'boss-card-great-grey-wolf-sif', 'Great Grey Wolf Sif boss data card (Darkroot p.5)', 'DR', 5, 359, 17),
    card('AST-0088', 'behaviour-card-overhead-cleave', 'Overhead Cleave boss behaviour card (Darkroot p.5)', 'DR', 5, 326, 16),
    card('AST-0088', 'behaviour-card-sword-slam', 'Sword Slam boss behaviour card (Darkroot p.5)', 'DR', 5, 327, 16),
    card('AST-0088', 'enemy-card-alonne-bow-knight', 'Alonne Bow Knight enemy data card (Iron Keep p.2)', 'IK', 2, 136, 9, small=True),
    card('AST-0088', 'enemy-card-alonne-knight-captain', 'Alonne Knight Captain enemy data card (Iron Keep p.2)', 'IK', 2, 134, 9, small=True),
    card('AST-0088', 'enemy-card-alonne-sword-knight', 'Alonne Sword Knight enemy data card (Iron Keep p.2)', 'IK', 2, 138, 9, small=True),
    card('AST-0088', 'enemy-card-ironclad-soldier', 'Ironclad Soldier enemy data card (Iron Keep p.3)', 'IK', 3, 301, 9, small=True),
    card('AST-0088', 'enemy-card-crystal-lizard', 'Crystal Lizard data card (Iron Keep p.3)', 'IK', 3, 288, 14, small=True),
    card('AST-0088', 'boss-card-sir-alonne', 'Sir Alonne boss data card (Iron Keep p.3)', 'IK', 3, 306, 17, small=True),
    card('AST-0088', 'boss-card-smelter-demon', 'Smelter Demon boss data card (Iron Keep p.3)', 'IK', 3, 305, 17, small=True),
    card('AST-0088', 'behaviour-card-charging-katana-slash', 'Charging Katana Slash boss behaviour card (Iron Keep p.3)', 'IK', 3, 274, 16, small=True),
    card('AST-0088', 'behaviour-card-overhead-chop', 'Overhead Chop boss behaviour card (Iron Keep p.3)', 'IK', 3, 273, 16, small=True),
]

DASHTXT = 'Dashboard: class name, slot labels and printed stat values are part of the image.'


def dash(slug, name, key, page, xref, subject, notes='', resolves=None):
    return ('AST-0135', slug, name, key, page, xref, m(subject, 'component, painted portrait', COL, 3, (SPOT,), baked=DASHTXT, kind='dashboard'), notes, None, resolves)


DASH = [
    dash('character-dashboard-whole-cleric-large', 'Character dashboard, whole, Cleric with class portrait (2022 core p.8, largest clean copy)', 'TG', 8, 807,
         'The Cleric character dashboard, whole, with the class portrait and starting-item roundels', 'Phase 2B stored only the lower section of this object (AST-0135.2).', 'AST-0135.R1'),
    dash('character-dashboard-whole-cleric-with-ability', 'Character dashboard, whole, Cleric with ability text and empty cube slots (2022 core p.8)', 'TG', 8, 809,
         'The Cleric character dashboard with its ability text; the cube slots are transparent holes', 'The cube slots of the stat grid and endurance bar are transparent in the source mask. Phase 2B stored only the lower section (AST-0135.1).', 'AST-0135.R1'),
    dash('character-dashboard-whole-pyromancer', 'Character dashboard, whole, Pyromancer with class portrait (2022 core p.4)', 'TG', 4, 147,
         'The Pyromancer character dashboard, whole, with the class portrait'),
    dash('character-dashboard-whole-thief', 'Character dashboard, whole, Thief with class portrait (2022 core p.4)', 'TG', 4, 151,
         'The Thief character dashboard, whole, with the class portrait'),
    dash('character-dashboard-whole-cleric', 'Character dashboard, whole, Cleric with class portrait (2022 core p.4)', 'TG', 4, 145,
         'The Cleric character dashboard, whole (smaller copy with the endurance bar printed red)'),
    dash('character-board-2017-warrior', 'Character board, 2017 edition, Warrior with class portrait (2017 core p.9)', 'CORE', 9, 1061,
         'The 2017 Warrior character board with its painted class portrait', 'A smaller copy on p.4 was not extracted.'),
    dash('character-board-2017-herald', 'Character board, 2017 edition, Herald with class portrait (2017 core p.11)', 'CORE', 11, 1171,
         'The 2017 Herald character board with its painted class portrait'),
    dash('character-board-2017-knight', 'Character board, 2017 edition, Knight with class portrait, partly shaded (2017 core p.4)', 'CORE', 4, 310,
         'The 2017 Knight character board with its painted class portrait (shaded where another board overlapped it)', 'The source image is darkened where the next board of the fan lay over it.'),
]

FANTXT = 'Card faces and backs: their titles and text are part of the image.'


def fan(slug, name, page, xrefs, subject, resolves=None, notes=''):
    return ('AST-0137', slug, name, 'TG', page, xrefs, m(subject, 'component, fanned cards', SPOT, 2, (COL,), baked=FANTXT, kind='card fan'), notes, resolves)


FANS = [
    fan('card-fan-encounter-cards', 'Encounter card fan: Grave Matters, The Abandoned Chest, Lakeview Refuge (2022 core p.6)', 6, [638, 636, 634],
        'A fan of three encounter cards: Grave Matters, The Abandoned Chest and Lakeview Refuge', 'AST-0137.R1'),
    fan('card-fan-event-deck', 'Event deck: card back and the Lifegem card (2022 core p.6)', 6, [783, 785],
        'The event deck: a card back with the Lifegem card fanned over it', 'AST-0137.R1'),
    fan('card-fan-treasure-decks', 'Treasure deck row: class, common, legendary and boss treasure, each a card back and a face (2022 core p.5)', 5, [342, 155, 344, 353, 348, 350],
        'The four treasure decks in a row, each a card back with a face card: Shortbow, Winged Spear, Dark Sword, Gravelord Sword', 'AST-0137.R2'),
    fan('card-spread-black-knight', 'Black Knight boss cards: card back, data card and Overhead Swing behaviour card (2022 core p.5)', 5, [328, 332, 330],
        'The Black Knight boss cards: card back, data card and a behaviour card', 'AST-0137.R2', 'On the page the miniature stands in front of this group; it is left out here.'),
    fan('card-spread-gravelord-nito', 'Gravelord Nito boss cards: card back, data card and Lunging Cleave behaviour card (2022 core p.5)', 5, [322, 326, 324],
        'The Gravelord Nito boss cards: card back, data card and a behaviour card', 'AST-0137.R2', 'On the page the miniature stands in front of this group; it is left out here.'),
    fan('character-set-cleric', 'Cleric set: dashboard, class token and starting equipment cards as fanned on p.4 (2022 core)', 4, [145, 185, 187, 192],
        'The Cleric set: dashboard, class token and starting equipment cards', None, 'On the page the miniature stands in front of this group; it is left out here.'),
    fan('character-set-pyromancer', 'Pyromancer set: dashboard, class token and starting equipment cards as fanned on p.4 (2022 core)', 4, [147, 157, 159, 188],
        'The Pyromancer set: dashboard, class token and starting equipment cards', None, 'On the page the miniature stands in front of this group; it is left out here.'),
    fan('character-set-thief', 'Thief set: dashboard, class token and starting equipment cards as fanned on p.4 (2022 core)', 4, [151, 153, 155, 190],
        'The Thief set: dashboard, class token and starting equipment cards', None, 'On the page the miniature stands in front of this group; it is left out here.'),
]

TOKENS = [
    ('AST-0072', 'phantom-token-red-eye-orb', 'Invader set-up token with painted red eye orb (Phantoms p.10)', 'PH', 10, 275,
     m('A round black token bearing a painted red eye orb', 'token, crimson', SPOT, 12, kind='token'), '201 px: inline or thumbnail size only.', None, 'AST-0072.R1'),
    ('AST-0072', 'phantom-token-cracked-red-eye-orb', 'Invader set-up token with painted cracked red eye orb (Phantoms p.10)', 'PH', 10, 277,
     m('A round black token bearing a painted cracked red eye orb', 'token, crimson', SPOT, 12, kind='token'), '201 px: inline or thumbnail size only.', None, 'AST-0072.R1'),
]

# Phase 0 file that the review had blocked: no new record, but it belongs on the designer's list.
EXISTING = [dict(id='AST-0119', file='assets/art/ast-0119-tg-2022-cover-art-gravelord-nito.png',
                 meta=m('Gravelord Nito, a mound of skeletons under a black shroud, on black (2022 cover art, no logo)', 'macabre, black, still', COVER, 15, (FULL, COL, HDR), hdr=0.36),
                 note='Extracted in Phase 0 and held until 2026-11-11; no logo or text in the image.')]


def run_extract():
    RECS.clear(); NEXT.clear()
    for parent, slug, name, key, page, xref, meta, notes, crop, resolves in ART:
        if isinstance(xref, list):
            tiles(parent, 'art', slug, name, key, page, xref, meta, notes, resolves)
        else:
            single(parent, 'art', slug, name, 'art', key, page, xref, meta, notes, crop, resolves, art=True)
    for parent, slug, name, key, page, xref, meta, notes, crop, resolves in DASH:
        single(parent, 'photography', slug, name, 'photography', key, page, xref, meta, notes, crop, resolves)
    for parent, slug, name, key, page, xrefs, meta, notes, resolves in FANS:
        compose(parent, 'photography', slug, name, key, page, xrefs, meta, notes, resolves)
    for parent, slug, name, key, page, xref, meta, notes, crop, resolves in CARDS:
        single(parent, 'frames', slug, name, 'frame', key, page, xref, meta, notes, crop, resolves)
    for parent, slug, name, key, page, xref, meta, notes, crop, resolves in TOKENS:
        single(parent, 'icons', slug, name, 'icon', key, page, xref, meta, notes, crop, resolves)
    print('records:', len(RECS), '->', RECFILE)



# --------------------------------------------------------------------------- the eight mega-boss expansion booklets
# Supplied by the author on 2026-11-11. Catalogue parents AST-0156 to AST-0163 are appended to the catalogue by
# tools/build_asset_docs.py (AST-0148 to AST-0155 were already taken by the typographic specimens).
MB_FIRST = 'AST-0156'
MB = [  # key, parent, file, slug, boss name
    ('FK', 'AST-0156', 'DS-Four-Kings-Rules-web.pdf', 'four-kings', 'The Four Kings'),
    ('GAD', 'AST-0157', 'DS-GaD-Rules-web.pdf', 'gaping-dragon', 'Gaping Dragon'),
    ('GD', 'AST-0158', 'DS-GD-Rules-web.pdf', 'guardian-dragon', 'Guardian Dragon'),
    ('TLG', 'AST-0159', 'DS-TLG-Rules.pdf', 'last-giant', 'The Last Giant'),
    ('MFA', 'AST-0160', 'DS-MFA-Rules.pdf', 'manus', 'Manus, Father of the Abyss'),
    ('OIK', 'AST-0161', 'DS-OIK-Rules-web.pdf', 'old-iron-king', 'Old Iron King'),
    ('VOT', 'AST-0162', 'DS-VotBV-Rules-web.pdf', 'vordt', 'Vordt of the Boreal Valley'),
    ('AD', 'AST-0163', 'DS-AD-Rules-web-EN.pdf', 'asylum-demon', 'Asylum Demon'),
]
for _k, _p, _f, _s, _b in MB:          # register the sources with the Phase 2B helpers (personalised PDFs)
    P.SRC[_k] = (P.DEC + _f, _f)
P.WM_KEYS = tuple(P.WM_KEYS) + tuple(k for k, *_ in MB)

# per booklet: cover (page, xref, subject), back cover, interior art, miniature renders, boards, special-rule extras
# art rows: (slug, record name, page, xref, subject, mood, use, chapter, also, header focus, notes)
MB_ART = {
    'FK': dict(
        cover=(1, 20, 'The Four Kings, a crowned wraith of trailing dark limbs, on black', 'abyssal, spectral, black'),
        back=(16, 2539, 'Drowned ruins in deep blue gloom, fading to black at the foot', 'sunken, blue, silent'),
        art=[('art-knight-in-dark-ruins', 'p.3: armoured figure in dark ruins', 3, 54, 'An armoured figure moves through dark ruins toward a lit doorway', 'furtive, dark, teal', COL, 19, (SPOT,), None, SHOT),
             ('art-drowned-city', 'p.6: drowned city of towers in blue gloom', 6, 668, 'A drowned city of towers looms through deep blue gloom', 'sunken, blue, silent', COL, 19, (FULL,), None, ''),
             ('concept-king-on-white', 'p.10: ink concept of one of the Four Kings, on white', 10, 1334, 'Ink concept of one of the Four Kings, a wraith of ragged black limbs, on white', 'spidery, black, stark', COL, 17, (SPOT,), None, 'White ground is part of the image.'),
             ('art-sunken-ruins-blue', 'p.15: sunken ruins in blue haze', 15, 2523, 'Sunken ruins in blue haze', 'sunken, blue, silent', SPOT, 19, (), None, '')],
        minis=[(4, 65, 'miniature', 'The Four Kings miniature render (one king, full figure)'), (4, 81, 'miniature-second-pose', 'The Four Kings miniature render (second copy as placed behind the first)')],
        boards=(626, 1299)),
    'GAD': dict(
        cover=(1, 20, 'The Gaping Dragon rears in blue gloom, its ribcage a maw of teeth', 'monstrous, blue, gaping'),
        back=(16, 2482, 'The Gaping Dragon, pale wings spread, small on black', 'pale, distant, black'),
        art=[('art-vaulted-corridor-sketch', 'p.3: sepia sketch of a long vaulted corridor', 3, 54, 'Sepia sketch of a long vaulted corridor receding into the dark', 'sepia, receding, quiet', FULL, 19, (HDR, COL), 0.45, ''),
             ('art-maw-study-tall', 'p.6: monochrome study of the Gaping Dragon maw', 6, 820, "Monochrome study of the Gaping Dragon's maw of ribs and tendrils", 'monochrome, writhing, close', COL, 17, (SPOT,), None, '530 px wide.'),
             ('concept-sheet-on-white', 'p.10: pencil concept sheet of the Gaping Dragon, on white', 10, 1545, 'Pencil concept sheet of the Gaping Dragon in several views, on white', 'studied, pencil, anatomical', COL, 17, (SPOT,), None, 'White ground is part of the image.'),
             ('art-mossy-depths', 'p.14: mossy ruins dropping into green-black depths', 14, 2443, 'Mossy ruins drop away into green-black depths', 'dank, green, deep', SPOT, 19, (COL,), None, ''),
             ('art-maw-study-wide', 'p.15: monochrome study of the Gaping Dragon maw, wide', 15, 2465, "Monochrome study of the Gaping Dragon's maw, wide framing", 'monochrome, writhing, close', SPOT, 16, (COL,), None, ''),
             ('art-golden-buttresses', 'p.15: pale golden buttresses and spires from above', 15, 2467, 'Pale golden buttresses and spires seen from above', 'lofty, golden, pale', SPOT, 19, (), None, ''),
             ('art-stair-and-arch-sketch', 'p.15: sepia sketch of a stair past a stone arch', 15, 2468, 'Sepia sketch of a stair climbing past a stone arch', 'sepia, quiet, worn', SPOT, 19, (), None, '')],
        minis=[(4, 79, 'miniature', 'Gaping Dragon mega-boss miniature render')],
        boards=(795, 1506), extra_objects=[(5, 801, 'corrosion-token', 'Corrosion condition token (Gaping Dragon special rule)', 'A green corrosion condition token', 'token, acid green')]),
    'GD': dict(
        cover=(1, 20, 'The Guardian Dragon, red-winged, coiled on black', 'coiled, crimson, black'),
        back=(16, 2260, 'A dark hall of tall shelves under hanging lamps, fading to black', 'dim, amber, hushed'),
        art=[('art-ruined-castle-on-cliff-tall', 'p.3: ruined castle of spires on a cliff, tall framing', 3, 54, 'A ruined castle of spires and buttresses on a cliff under a pale sky, tall framing', 'lofty, weathered, pale', FULL, 19, (HDR, COL), 0.22, 'Taller framing of the painting stored as AST-0130 (Phantoms p.13), same width.'),
             ('art-dark-library-hall', 'p.6: dark library hall under hanging lamps', 6, 778, 'A vast dark library hall recedes under hanging lamps', 'dim, amber, hushed', FULL, 19, (HDR, COL), 0.62, ''),
             ('concept-sketches-on-grey', 'p.10: Guardian Dragon concept sketches on grey', 10, 1496, 'Concept sketches of the Guardian Dragon: a line drawing above, a red-winged colour study below', 'studied, grey, crimson', COL, 17, (SPOT,), None, 'Grey ground is part of the image.')],
        minis=[(4, 79, 'miniature', 'Guardian Dragon mega-boss miniature render')],
        boards=(748, 1457)),
    'TLG': dict(
        cover=(1, 20, 'The Last Giant, hollow-faced and bound in roots, on black', 'hulking, hollow, black'),
        back=(16, 2601, 'A shrine mirrored in still blue water under a column of light, fading to black', 'serene, blue, luminous'),
        art=[('art-giant-turned-to-tree', 'p.3: colossal giant turned to a dead tree', 3, 54, 'A colossal giant turned to a dead tree stands in a grey wood', 'petrified, grey, mournful', FULL, 17, (HDR, COL), 0.25, ''),
             ('art-knight-in-golden-hall-tall', 'p.6: knight on a fallen column in a golden hall, large', 6, 862, 'A knight stands on a fallen column in a hall of gold light and gnarled pillars', 'radiant, golden, ruined', FULL, 19, (HDR, COL), 0.52, 'Largest version of the painting stored small as AST-0130 (Explorers p.14, 406 px).'),
             ('concept-front-and-back', 'p.10: Last Giant concept art, front and back views', 10, 1582, 'Concept art of the Last Giant, front and back views', 'gaunt, dark, studied', COL, 17, (SPOT,), None, ''),
             ('art-mossy-cave-mouth', 'p.15: lone figure before a moss-green cave mouth', 15, 2586, 'A lone figure stands before a moss-green cave mouth', 'damp, green, hushed', SPOT, 19, (), None, ''),
             ('art-forest-ruin-with-light', 'p.15: overgrown forest ruin with pale light', 15, 2587, 'An overgrown forest ruin with pale light falling through an arch', 'overgrown, green, hazy', SPOT, 19, (), None, '')],
        minis=[(4, 77, 'miniature', 'The Last Giant mega-boss miniature render')],
        boards=(842, 1540)),
    'MFA': dict(
        cover=(1, 20, 'Manus, Father of the Abyss: antlers, a mass of red eyes and a great clawed hand', 'abyssal, red-eyed, looming'),
        back=(16, 2008, 'An armoured knight silhouetted against swirling blue spirits, fading to black', 'electric, blue, embattled'),
        art=[('art-figure-in-light-beam', 'p.3: figure with a glowing charm under a beam of light', 3, 54, 'A dark figure holds a glowing charm beneath a slanting beam of light', 'mystic, dark, glinting', FULL, 19, (COL,), None, ''),
             ('art-knight-resting-at-bonfire-tall', 'p.6: knight resting at a bonfire among ruins, large tall framing', 6, 616, 'A knight rests before a bonfire among broken walls, sparks streaming from the coiled sword', 'warm, weary, quiet', FULL, 19, (HDR, COL), 0.47, 'Largest version of the bonfire painting (AST-0120 is 934 px wide).'),
             ('art-knight-in-shaft-of-light', 'p.10: armoured knight in a shaft of light', 10, 1262, 'An armoured knight stands in a shaft of light, sword and shield lowered', 'solemn, dark, spotlit', COL, 15, (FULL,), None, ''),
             ('art-blood-red-hall', 'p.15: blood-red ruined hall', 15, 1996, 'A ruined hall drenched in blood-red light', 'bloody, red, ruined', SPOT, 19, (), None, ''),
             ('art-manus-over-small-figure', 'p.15: Manus looming over a small blue figure', 15, 1997, 'Manus looms, antlered and red-eyed, over a small figure in blue', 'abyssal, red-eyed, looming', SPOT, 17, (COL,), None, '')],
        minis=[(4, 67, 'miniature', 'Manus, Father of the Abyss mega-boss miniature render')],
        boards=(592, 1227)),
    'OIK': dict(
        cover=(1, 22, 'The Old Iron King, a horned demon of molten iron, wreathed in flame', 'molten, infernal, roaring'),
        back=(16, 2428, 'An iron keep in clouds of fire, fading to black', 'infernal, red, brooding'),
        art=[('art-knights-before-fiery-gate', 'p.3: knights before a keep split by a seam of fire', 3, 58, 'Knights stand before a dark keep split by a seam of molten light', 'ominous, ember, smoky', COL, 19, (SPOT,), None, '630 px wide. A larger copy of this painting is in the Vordt booklet (AST-0162).'),
             ('art-bull-headed-iron-idol', 'p.10: bull-headed iron idol holding a candle', 10, 1587, 'A bull-headed iron idol holds out a lit candle', 'brazen, dark, candlelit', COL, 17, (SPOT,), None, '627 px wide.')],
        minis=[(4, 80, 'miniature', 'Old Iron King mega-boss miniature render')],
        boards=(815, 1548)),
    'VOT': dict(
        cover=(1, 20, 'Vordt of the Boreal Valley, a hunched beast in frost-rimed armour, on black', 'frozen, bestial, silver'),
        back=(16, 2627, 'A moonlit gothic city of spires, fading to black', 'moonlit, blue, cold'),
        art=[('art-moonlit-gothic-city', 'p.3: moonlit gothic city of spires', 3, 54, 'A moonlit gothic city of spires and bridges in blue night', 'moonlit, blue, cold', FULL, 19, (HDR, COL), 0.30, ''),
             ('art-knight-before-fire-seam-gate', 'p.6: knight before a towering gate split by a seam of fire', 6, 1032, 'A knight faces a towering gate split by a seam of fire', 'ominous, ember, towering', FULL, 19, (HDR, COL), 0.62, 'Text-free and larger than the Iron Keep cover (AST-0130), which uses this painting.'),
             ('art-vordt-on-black', 'p.10: Vordt of the Boreal Valley on black', 10, 1750, 'Vordt of the Boreal Valley, silver-armoured and hunched, on black', 'frozen, bestial, silver', COL, 17, (FULL,), None, ''),
             ('art-snowbound-ruined-street', 'p.14: snow-bound ruined city street', 14, 2594, 'A snow-bound street of ruined towers', 'frozen, pale, ruined', SPOT, 19, (COL,), None, ''),
             ('art-cathedral-rose-window', 'p.15: cathedral front with a great rose window', 15, 2612, 'A cathedral front with a great rose window in blue light', 'cold, blue, ornate', SPOT, 19, (), None, ''),
             ('art-path-through-teal-ruins', 'p.15: path through dark teal ruins', 15, 2613, 'A path winds through dark teal ruins', 'murky, teal, deserted', SPOT, 19, (), None, ''),
             ('art-cliff-city-in-mist', 'p.15: city on a cliff in teal mist', 15, 2614, 'A city clings to a cliff in teal mist', 'murky, teal, lofty', SPOT, 19, (), None, '')],
        minis=[(4, 79, 'miniature', 'Vordt of the Boreal Valley mega-boss miniature render')],
        boards=(899, 1419)),
    'AD': dict(
        cover=(1, 20, 'The Asylum Demon, horned and bloated, great hammer in hand, on black', 'brutish, dark, heavy'),
        back=(16, 1844, 'A ruined cathedral nave, fading to black at the foot', 'solemn, golden, still'),
        art=[('art-ruined-cathedral-interior-large', 'p.3: ruined cathedral interior, largest copy', 3, 54, 'A ruined cathedral nave, daylight falling through the broken apse onto an overgrown floor', 'solemn, golden, still', COL, 19, (HDR,), 0.30, 'Slightly larger copy of AST-0125 (934 px wide).'),
             ('art-asylum-cell', 'p.10: stone cell lit from a grate above', 10, 1585, 'A stone cell lit from a grate above, a huddled figure by the wall', 'confined, grey, forlorn', COL, 19, (SPOT,), None, ''),
             ('concept-stray-demon-on-white', 'p.12: demon concept art on white', 12, 1786, 'Concept art of the demon, horned, winged and bloated, on white', 'brutish, dark, studied', COL, 17, (SPOT,), None, 'White ground is part of the image.'),
             ('art-ruined-parish-green-ink-large', 'p.13: green-ink sketch of a ruined tower and courtyard, large', 13, 1795, 'Green-ink sketch of a ruined tower above a walled courtyard, a crow perched at left', 'sketchy, green, desolate', FULL, 19, (HDR, COL), 0.35, 'Largest version of the sketch stored small as AST-0129 (2017 core p.15, 465 px).')],
        minis=[(4, 65, 'miniature', 'Asylum Demon / Stray Demon mega-boss miniature render')],
        boards=(864, 1545), extra_objects=[(5, 873, 'pillar-token', 'Pillar token (Asylum Demon special rule: Pillar Smasher)', 'A round pillar token: a broken stone pillar seen from above', 'token, stone')]),
}
# special-rule plates cut from the page (no single image object exists): page 13 card, with room for its key where it has one
MB_SPECIAL = {'GAD': (13, 3, 3, 3, 3, 'Crawling Charge behaviour card (Custom Game Elements)'),
              'GD': (13, 80, 3, 3, 8, 'Fiery Breath card with its key: the indicated cage node and the nodes the breath strikes'),
              'MFA': (13, 3, 3, 3, 3, 'Ground Slam behaviour card (the Shaft rule)'),
              'OIK': (13, 34, 3, 3, 26, 'Beam card with its key: the nodes the beam strikes and the movement node')}
MB_STRIP_TOP = {'FK': 46, 'TLG': 46}    # page 12 strips whose deck icons sit above the card fans
PAGECROP = 'Cut from a page render because the card is built on the page from a texture, an art layer and live text (no single image object): the parchment page shows at the rounded corners.'


# the one logo-free painting or concept of the boss that the essentials run takes from each booklet (None: the booklet has none)
MB_MAIN = {'FK': 'concept-king-on-white', 'GAD': 'concept-sheet-on-white', 'GD': 'concept-sketches-on-grey', 'TLG': 'concept-front-and-back',
           'MFA': 'art-manus-over-small-figure', 'OIK': None, 'VOT': 'art-vordt-on-black', 'AD': 'concept-stray-demon-on-white'}


def _card_boxes(key, page, wmin=38, wmax=210):
    out = []
    for i in P.doc(key)[page - 1].get_image_info(xrefs=True):
        b = i['bbox']
        if i['xref'] and 0.68 <= i['width'] / i['height'] <= 0.79 and wmin <= b[2] - b[0] <= wmax and b[3] - b[1] > 0.9 * (b[2] - b[0]):
            out.append(tuple(b))
    return out


def _clusters(boxes, gap=0.0):
    groups = []
    for b in boxes:
        hit = [g for g in groups if any(not (b[2] + gap < c[0] or c[2] + gap < b[0] or b[3] + gap < c[1] or c[3] + gap < b[1]) for c in g)]
        groups = [g for g in groups if not any(g is h for h in hit)] + [[b] + [c for g in hit for c in g]]
    out = [(min(c[0] for c in g), min(c[1] for c in g), max(c[2] for c in g), max(c[3] for c in g)) for g in groups]
    return sorted(out, key=lambda r: (round(r[1] / 40), r[0]))


def _text(key, page, rect):
    """Live page text inside a rectangle (never the head strip of the page), as one cleaned line."""
    assert rect[1] >= 30
    words = P.doc(key)[page - 1].get_text('words', clip=P.fitz.Rect(rect))
    words = sorted(words, key=lambda w: (round(w[1] / 4), w[0]))
    t = ' '.join(w[4] for w in words if not w[4].strip('0123456789.,x') == '')
    assert '@' not in t and 'Generated' not in t
    return ' '.join(t.split())


def _slug(t, n=48):
    s = ''.join(ch.lower() if ch.isalnum() else '-' for ch in t)
    while '--' in s:
        s = s.replace('--', '-')
    return s.strip('-')[:n].strip('-')


def region(key, page, box, dpi):
    """Page-region render for the personalised booklets, from the working copy in which the purchaser line is redacted.
    Guards: every purchaser-line text block of the page lies in the head strip (above 24 pt) and none is left in the
    working copy; the crop stays 30 pt clear of head and foot; and the crop is compared with the same crop of the
    unredacted page. Phase 2B asked for pixel identity; these booklets re-render fanned (rotated) card images with a
    few stray pixels of resampling noise after the redaction rewrite, so a difference is tolerated only if it is that
    small: under 0.3 % of pixels touched at all and next to none (at most 40, or 0.002 %) by more than 16 levels.
    A removed line of text would change tens of thousands of pixels. Returns the image and the two counts."""
    pg = P.doc(key)[page - 1]
    assert box[1] >= 30 and box[3] <= pg.rect.height - 30, 'crop too close to the page head/foot'
    assert all(b[3] < 24 for b in pg.get_text('blocks') if b[6] == 0 and P.is_wm(b[4])), 'purchaser line outside the head strip'
    im = P._ppm(P.redacted(key), page, box, dpi)
    d = np.abs(np.asarray(im).astype(int) - np.asarray(P._ppm(P.SRC[key][0], page, box, dpi)).astype(int)).max(axis=2)
    touched, strong = int((d > 0).sum()), int((d > 16).sum())
    assert touched <= 0.003 * d.size and strong <= max(40, 2e-5 * d.size), ('redaction changed the crop', key, page, touched, strong)
    return im, touched, strong


def page_crop(parent, folder, slug, name, typ, key, page, box, dpi, meta, notes=''):
    pg = P.doc(key)[page - 1]
    box = (max(box[0], 0), max(box[1], 30), min(box[2], pg.rect.width), min(box[3], pg.rect.height - 30))
    im, touched, strong = region(key, page, box, dpi)
    path, fmt = store(im, parent, folder, slug, False)
    same = ('pixel-identical to' if not touched else f'compared with (identical but for {touched} px of resampling noise, {strong} of them above 16 levels, out of {im.width * im.height})')
    method = (f'pdftoppm {dpi} dpi page-region crop; rendered from a working copy with the purchaser line redacted; crop {same} '
              f'the unredacted page region and 30 pt clear of page head and foot')
    return record(parent, name, typ, key, page, path, fmt, im, method, box, None, notes, meta)


def run_megaboss(full=False):
    if not RECS:
        for r in json.load(open(RECFILE)):
            if r['parent'] < MB_FIRST:
                RECS[r['id']] = r
    for rid in [i for i, r in RECS.items() if r['parent'] >= MB_FIRST]:
        del RECS[rid]
    for key, parent, _f, sl, boss in MB:
        NEXT.pop(parent, None)
        T = MB_ART[key]
        # cover, text-free crop of it, back cover
        p, x, subj, mood = T['cover']
        if full:
            single(parent, 'art', f'{sl}-cover', f'{boss} expansion front cover, logo baked in', 'art', key, p, x,
               m(subj + ', with the game logo', mood, COVER, 17, baked=LOGO), LOGO, None, None, art=True)
        single(parent, 'art', f'{sl}-cover-art-only', f'{boss} front cover, art above the logo', 'art', key, p, x,
               m(subj, mood, COL, 17, (SPOT, COVER)), 'Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. The lower third of the cover carries the baked-in game logo.', (0, 0, 1, 0.615), None, art=True)
        p, x, subj, mood = T['back']
        if full:
            single(parent, 'art', f'{sl}-backcover', f'{boss} expansion back cover', 'art', key, p, x,
               m(subj, mood, BACK, 19, (FULL, COL)), 'The lower part is black (room for back-cover text).', None, None, art=True)
        for slug, name, p, x, subj, mood, use, ch, also, hdr, notes in T['art']:
            if not full and slug != MB_MAIN.get(key):
                continue
            single(parent, 'art', f'{sl}-{slug}', f'{boss} booklet {name}', 'art', key, p, x, m(subj, mood, use, ch if full else 17, also, hdr=hdr), notes, None, None, art=True)
        for p, x, slug, name in (T['minis'] if full else T['minis'][:1]):
            single(parent, 'photography', f'{sl}-{slug}', name, 'photography', key, p, x,
                   m(name.replace(' render', '') + ', grey resin render cut out by its own mask', 'miniature, grey, imposing', COL, 17, (SPOT, FULL), kind='miniature render'),
                   'SFG miniature render, cut out by its own soft mask. Largest copy in the booklet.')
        bx, ex = T['boards']
        single(parent, 'photography', f'{sl}-game-board-boss-side', f'{boss} mega-boss game board, boss side (p.5)', 'photography', key, 5, bx,
               m(f'The {boss.replace("The ", "")} mega-boss game board, boss side, with its node markings', 'component, top-down, arena', COL, 16, (FULL, SPOT), kind='game board'),
               'Node markers are printed on the board. Use this side to show where the special rule plays out.')
        single(parent, 'photography', f'{sl}-game-board-encounter-side', f'{boss} mega-boss game board, encounter side (p.9, larger of the two copies)', 'photography', key, 9, ex,
               m(f'The {boss.replace("The ", "")} game board, level 4 encounter side', 'component, top-down, tile', COL, 15, (SPOT,), kind='game board'),
               'The tokens and the card that lie on it on p.9 are separate objects and are not in this image.')
        if not full:      # essentials only: cover art, boss painting, miniature render, both sides of the board
            continue
        for p, x, slug, name, subj, mood in T.get('extra_objects', []):
            single(parent, 'photography', f'{sl}-{slug}', name, 'photography', key, p, x, m(subj, mood, SPOT, 17, kind='token'), 'Small: inline or thumbnail size only.')
        # ---- card faces: page-region crops
        for n, box in enumerate(_clusters(_card_boxes(key, 5), gap=3.0), 1):          # contents-page fans
            cap = _text(key, 5, (box[0] - 14, box[3] + 1, box[2] + 14, box[3] + 24)) or f'card group {n}'
            low = cap.lower()
            ch = 19 if 'level 4' in low and 'data' not in low else 15 if ('data' in low or 'treasure' in low) else 17
            page_crop(parent, 'frames', f'{sl}-cards-p05-{_slug(cap, 40)}', f'{boss} booklet p.5 card fan: {cap}', 'frame', key, 5,
                      (box[0] - 3, box[1] - 3, box[2] + 3, box[3] + 3), 600,
                      m(f'{boss}: {cap} as fanned on the contents page', 'component, fanned cards', SPOT, ch, baked=FANTXT, kind='card fan'), PAGECROP + ' Small on the page (about 57 pt wide per card).')
        for box in _clusters(_card_boxes(key, 8, wmin=80)):                           # level 4 encounter card with its call-outs
            t = _text(key, 8, (box[0] + 22, box[1] + 4, box[2] - 22, box[1] + 0.2 * (box[3] - box[1]))).title()
            page_crop(parent, 'frames', f'{sl}-level4-encounter-card-{_slug(t, 30)}', f'{boss} booklet p.8: level 4 encounter card "{t}" with its numbered call-outs', 'frame', key, 8,
                      (box[0] - 10, box[1] - 10, box[2] + 10, box[3] + 10), 450,
                      m(f'Level 4 encounter card "{t}" with numbered call-outs 1 to 7', 'card face, annotated', SPOT, 19, (COL,), baked=CARDTXT + ' Gold call-out numbers 1 to 7 from the anatomy figure sit on its edges.', kind='card face'), PAGECROP)
        cards11 = sorted(_clusters(_card_boxes(key, 11, wmin=80)), key=lambda r: r[1])
        for j, box in enumerate(cards11):                                              # data card (call-outs) and behaviour card
            t = _text(key, 11, (box[0] + 20, box[1] + 4, box[2] - 20, box[1] + 0.2 * (box[3] - box[1]))).title()
            if j == 0:
                page_crop(parent, 'frames', f'{sl}-data-card', f'{boss} booklet p.11: mega-boss data card "{t}" with its numbered call-outs', 'frame', key, 11,
                          (box[0] - 10, box[1] - 10, box[2] + 10, box[3] + 10), 450,
                          m(f'Mega-boss data card "{t}" with numbered call-outs 1 to 8', 'card face, annotated', COL, 15, (SPOT,), baked=CARDTXT + ' Gold call-out numbers 1 to 8 from the anatomy figure sit on its edges.', kind='card face'), PAGECROP)
            else:
                page_crop(parent, 'frames', f'{sl}-behaviour-card-{_slug(t, 30)}', f'{boss} booklet p.11: behaviour card "{t}"', 'frame', key, 11,
                          (box[0] - 3, box[1] - 3, box[2] + 3, box[3] + 3), 450,
                          m(f'Mega-boss behaviour card "{t}"', 'card face', SPOT, 16, (COL,), baked=CARDTXT, kind='card face'), PAGECROP)
        b12 = _card_boxes(key, 12)
        if b12:                                                                        # behaviour-deck fans of the encounter set-up page
            x0, y0, x1, y1 = min(b[0] for b in b12), min(b[1] for b in b12), max(b[2] for b in b12), max(b[3] for b in b12)
            cap = _text(key, 12, (x0 - 10, y1 + 1, x1 + 10, y1 + 14))
            special = key in MB_STRIP_TOP or key == 'VOT'
            page_crop(parent, 'frames' if not special else 'diagrams', f'{sl}-behaviour-decks-p12', f'{boss} booklet p.12: behaviour decks as laid out for the encounter ({cap})', 'frame' if not special else 'diagram', key, 12,
                      (x0 - 4, y0 - 4 - MB_STRIP_TOP.get(key, 0), x1 + 4, y1 + 4), 450,
                      m(f'{boss}: the behaviour decks of the encounter ({cap})', 'component, fanned cards', SPOT if not special else COL, 17 if special else 16, baked=FANTXT, kind='diagram' if special else 'card fan'),
                      PAGECROP + (' This is the plate that shows the special rule: the decks the boss draws from.' if special else ''))
        if key in MB_SPECIAL:
            p, l, t_, r_, b_, what = MB_SPECIAL[key]
            for box in _clusters(_card_boxes(key, p, wmin=60))[:1]:
                page_crop(parent, 'diagrams', f'{sl}-special-rule-p13', f'{boss} booklet p.13: {what}', 'diagram', key, p,
                          (box[0] - l, box[1] - t_, box[2] + r_, box[3] + b_), 450,
                          m(f'{boss} special rule: {what}', 'card face, rule example', COL, 17, (SPOT,), baked=CARDTXT, kind='diagram'), PAGECROP)
    print('records:', len(RECS), '->', RECFILE)


def header_box(w, h, hdr, aspect=3.0):
    """Crop box (fractions left, top, right, bottom) for a 520 pt wide strip about 173 pt high."""
    if hdr is None:
        return None
    if isinstance(hdr, (tuple, list)):
        return [round(v, 3) for v in hdr]
    hf = min(1.0, w / (aspect * h))
    t = min(max(hdr - hf / 2, 0.0), 1.0 - hf)
    return [0.0, round(t, 3), 1.0, round(t + hf, 3)]


def run_candidates():
    recs = json.load(open(RECFILE))
    rows = []
    for e in EXISTING:
        im = Image.open(e['file'])
        rows.append((e['id'], e['file'], dict(e['meta'], width=im.width, height=im.height, has_alpha=im.mode == 'RGBA'), 'Phase 0', e['note'], None, 1))
    order = {'painting': 0, 'dashboard': 1, 'card fan': 2, 'card face': 3, 'token': 4}
    mb = lambda r: r['parent'] >= MB_FIRST

    def key(r):
        return (1, 0, P.idkey(r['id'])) if mb(r) else (0, order[r['design']['kind']], P.idkey(r['id']))
    for r in sorted(recs, key=key):
        w, h = (int(v) for v in r['dims'].split(' ')[0].split('×'))
        rows.append((r['id'], r['file'], dict(r['design'], width=w, height=h, has_alpha=r['has_alpha']), 'Phase 3', r['notes'], r, None))
    out = []
    for n, (rid, f, mt, phase, note, r, _) in enumerate(rows, 1):
        w, h = mt['width'], mt['height']
        d = dict(n=n, file=f, id=rid, kind=mt['kind'], subject=mt['subject'], width=w, height=h, has_alpha=mt['has_alpha'],
                 orientation='portrait' if h > 1.1 * w else 'landscape' if w > 1.1 * h else 'square', mood=mt['mood'],
                 baked_text=bool(mt['baked']), baked_text_note=mt['baked'] or 'none: no text, title or logo in the image',
                 suggested_use=mt['suggested_use'], also_suits=mt['also_suits'], suggested_for=mt['suggested_for'])
        box = header_box(w, h, mt['hdr'])
        if box:
            px = round((box[2] - box[0]) * w)
            d['header_crop'] = box
            d['header_crop_note'] = f"fractions left, top, right, bottom; {px}×{round((box[3] - box[1]) * h)} px, about {round(px / (520 / 72))} ppi at 520 pt wide"
        d['ppi_at_column_250pt'] = round(w / (250 / 72))
        d['ppi_at_full_width_520pt'] = round(w / (520 / 72))
        d['source'] = f"{r['src']}, p.{r['page']}" if r else 'DS-TG-Rulebook-Compressed_compressed.pdf, p.1'
        if r and r['method'].startswith('pdftoppm'):
            d['page_render_crop'] = True
        d['extracted_in'] = phase
        if note:
            d['notes'] = note
        out.append(d)
    doc = dict(about=('Painted art, card faces, dashboards and card fans cleared for use on 2026-11-11 (provenance confirmed by the author). '
                      'One entry per file; n is the index printed on the contact sheets build/art_contact*.jpg (48 per sheet, 6 per row). '
                      'suggested_use is one of: cover, back cover, full-page plate, chapter header strip, column plate, spot; also_suits lists other workable uses. '
                      'header_crop, where given, is a crop box as fractions (left, top, right, bottom) that reads well at 520 pt wide by about 173 pt high.'),
               generated_by='tools/extract_phase3.py', count=len(out), candidates=out)
    s = json.dumps(doc, indent=1, ensure_ascii=False)
    assert '@' not in s and 'Generated for' not in s
    with open(CANDFILE, 'w') as f:
        f.write(s + '\n')
    print('candidates:', len(out), '->', CANDFILE)


def run_sheets(per=48, cols=6, T=260):
    cand = json.load(open(CANDFILE))['candidates']
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
    cw, ch = T + 10, T + 38
    os.makedirs('build', exist_ok=True)
    for s in range(0, len(cand), per):
        chunk = cand[s:s + per]
        rows = (len(chunk) + cols - 1) // cols
        sheet = Image.new('RGB', (cols * cw, rows * ch), (24, 22, 20))
        dr = ImageDraw.Draw(sheet)
        for j, c in enumerate(chunk):
            im = Image.open(c['file'])
            im.thumbnail((T, T), Image.LANCZOS)
            if im.mode == 'RGBA':
                bg = Image.new('RGB', im.size, (96, 96, 96)); bg.paste(im, mask=im.getchannel('A')); im = bg
            x, y = (j % cols) * cw, (j // cols) * ch
            sheet.paste(im.convert('RGB'), (x + 5 + (T - im.width) // 2, y + 4 + (T - im.height) // 2))
            dr.text((x + 6, y + T + 6), str(c['n']), fill=(255, 220, 120), font=font)
            dr.text((x + 44, y + T + 5), f"{c['width']}×{c['height']}  {c['suggested_use']}", fill=(225, 225, 225), font=small)
            dr.text((x + 44, y + T + 19), os.path.basename(c['file'])[9:46], fill=(160, 160, 160), font=small)
        name = 'build/art_contact.jpg' if s == 0 else f'build/art_contact_{s // per + 1}.jpg'
        sheet.save(name, quality=88)
        print(name, sheet.size, f"n {chunk[0]['n']}–{chunk[-1]['n']}")


SECTIONS = {'extract': run_extract, 'megaboss': run_megaboss, 'megaboss-full': lambda: run_megaboss(True), 'candidates': run_candidates, 'sheets': run_sheets}
if __name__ == '__main__':
    for s in ([a for a in sys.argv[1:] if a in SECTIONS] or ['extract', 'megaboss', 'candidates', 'sheets']):
        SECTIONS[s]()
