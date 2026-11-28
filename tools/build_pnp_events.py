#!/usr/bin/env python3
"""Build the print-and-play Events Expansion II from its maker's own card files.

Every card is reproduced as printed. The cards listed in pnp/events/edits.json, and only those, have the text in
their text box set again: the box is cleaned with a background taken from all the cards together (the box is the same
artwork on every card and its text is darker than its parchment, so a high percentile of the 49 at each pixel is
the box without any text), and the new text is set in Alegreya,
the face the cards use.

Sources (not committed; see .gitignore): sources/events_expansion/EventsExpansion_EventsCards_V2-2.pdf (114 pages:
49 event cards and 8 trap cards, each face followed by its back) and EventsExpansion-Treasures.pdf (28 pages: 14
treasure cards, each face followed by its back).

Output: pnp/events/events_expansion_<paper>.pdf. Each sheet of fronts is followed by its sheet of backs."""
import json, pathlib, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'sources/events_expansion'
CACHE = ROOT / 'work/scratch/pnp_events'
FONT = ROOT / 'assets/fonts/alegreya/Alegreya-wght.ttf'
PAPER = {'letter': (215.9, 279.4), 'a4': (210.0, 297.0)}
DPI = 300
MM = DPI / 25.4
# event and trap cards: a poker card with 12.72 pt of bleed on every side
EV_TRIM = (63.5, 88.9)
# treasure cards: the trim their maker's crop marks show on the card backs (x 31 to 566, y 20 to 802 at 300 dpi)
TR_BOX = (31, 20, 566, 802)
TR_TRIM = ((TR_BOX[2] - TR_BOX[0]) / MM, (TR_BOX[3] - TR_BOX[1]) / MM)
# the text box of an event card at 300 dpi: the parchment inside its frame
BOX = (117, 909, 739, 1005)             # where text is set
PARCH = (112, 906, 745, 1014)           # all of the parchment, out to the inner edge of the frame
REGION = (96, 890, 776, 1040)          # the box with its frame and the maker's emblem
EMBLEM = (748, 1012, 40)               # centre and clear radius of the emblem at the box's lower right corner
INK = (24, 20, 18)
WEIGHT = 540                           # between Alegreya Medium and Bold: the cards' text prints heavy


def render(pdf, prefix):
    out = CACHE / prefix; out.mkdir(parents=True, exist_ok=True)
    if not any(out.glob('p-*.png')):
        subprocess.run(['pdftoppm', '-r', str(DPI), '-png', str(pdf), str(out / 'p')], check=True)
    return sorted(out.glob('p-*.png'))


def clean_box(faces):
    """The text box without text, from the box of every event card."""
    stack = np.stack([np.asarray(Image.open(p).convert('RGB').crop(REGION)) for p in faces])
    # text is darker than the parchment, so a high percentile at each pixel is the parchment with no text on it
    return Image.fromarray(np.percentile(stack, 80, axis=0).astype(np.uint8))


def wrap(draw, words, font, width):
    lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=font) <= width or not cur: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]


def balance(draw, words, font, width, n):
    """Break into n lines of nearly equal width (least sum of squared widths), none wider than width."""
    W = [draw.textlength(w, font=font) for w in words]; sp = draw.textlength(' ', font=font); m = len(words)
    def span(i, j): return sum(W[i:j]) + sp * (j - i - 1)
    best = {(m, 0): (0.0, [])}
    def go(i, k):
        if (i, k) in best: return best[(i, k)]
        res = None
        if k > 0:
            for j in range(i + 1, m - (k - 1) + 1):
                w = span(i, j)
                if w > width: break
                rest = go(j, k - 1)
                if rest is None: continue
                c = w * w + rest[0]
                if res is None or c > res[0]: pass
                if res is None or c < res[0]: res = (c, [j] + rest[1])
        best[(i, k)] = res; return res
    r = go(0, n)
    if r is None: return None
    cuts = [0] + r[1]; return [' '.join(words[a:b]) for a, b in zip(cuts, cuts[1:])]


def set_text(card, text, clean):
    """Paste the clean box over the card's text box and set text in it, as large as fits."""
    card = card.copy(); rx, ry = REGION[:2]; px0, py0, px1, py1 = PARCH
    inner = clean.crop((px0 - rx, py0 - ry, px1 - rx, py1 - ry))
    mask = Image.new('L', inner.size, 0); ImageDraw.Draw(mask).rectangle((2, 2, inner.width - 3, inner.height - 3), fill=255)
    card.paste(inner, (px0, py0), mask.filter(ImageFilter.GaussianBlur(1.0)))
    x0, y0, x1, y1 = BOX
    K = 4                                                    # set the text at four times the size and scale it down
    W, H = (x1 - x0) * K, (y1 - y0) * K
    layer = Image.new('L', (W, H), 0); d = ImageDraw.Draw(layer); words = text.split()
    for size in range(33, 13, -1):
        f = ImageFont.truetype(str(FONT), size * K, layout_engine=ImageFont.Layout.RAQM)
        f.set_variation_by_axes([WEIGHT])
        lead = round(size * 0.98) * K; width = W - 2 * 16 * K
        n = len(wrap(d, words, f, width))
        if n * lead > H - 2 * K * 3: continue
        lines = balance(d, words, f, width, n) or wrap(d, words, f, width)
        # the last line must stay clear of the emblem at the lower right
        top = (H - len(lines) * lead) / 2
        last_w = d.textlength(lines[-1], font=f); right = (W + last_w) / 2
        bottom = top + len(lines) * lead
        ex, ey, er = (EMBLEM[0] - x0) * K, (EMBLEM[1] - y0) * K, EMBLEM[2] * K
        if right > ex - er and bottom > ey - er: continue
        asc, desc = f.getmetrics()
        for i, ln in enumerate(lines):
            w = d.textlength(ln, font=f)
            d.text(((W - w) / 2, top + i * lead + (lead - (asc + desc)) / 2), ln, font=f, fill=255)
        break
    else:
        raise SystemExit('text does not fit the box: ' + text[:40])
    layer = layer.resize((x1 - x0, y1 - y0), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.35))
    ink = Image.new('RGB', layer.size, INK)
    card.paste(ink, (x0, y0), layer)
    return card, size, lines


def trim(img, box):
    return img.crop(tuple(int(round(v)) for v in box))


def prepare():
    """Every card face and back as a trimmed JPEG in the cache; returns (poker, mini), lists of (front, back) paths."""
    for f in (SRC / 'EventsExpansion_EventsCards_V2-2.pdf', SRC / 'EventsExpansion-Treasures.pdf', FONT):
        if not f.exists(): raise SystemExit(f'missing {f.relative_to(ROOT)}')
    ev = render(SRC / 'EventsExpansion_EventsCards_V2-2.pdf', 'ev'); tr = render(SRC / 'EventsExpansion-Treasures.pdf', 'tr')
    assert len(ev) == 114 and len(tr) == 28, (len(ev), len(tr))
    edits = {e['page']: e for e in json.loads((ROOT / 'pnp/events/edits.json').read_text(encoding='utf-8'))['edits']}
    clean = clean_box(ev[0:98:2])
    out = CACHE / 'cards'; out.mkdir(parents=True, exist_ok=True)
    w, h = Image.open(ev[0]).size; tw, th = EV_TRIM[0] * MM, EV_TRIM[1] * MM
    ebox = ((w - tw) / 2, (h - th) / 2, (w + tw) / 2, (h + th) / 2)
    def save(img, name):
        p = out / name; img.convert('RGB').save(p, 'JPEG', quality=90, subsampling=0); return p
    backs = {}
    def back(path, box, key):
        sig = (key, hash(Image.open(path).convert('RGB').resize((32, 32)).tobytes()))
        if sig not in backs: backs[sig] = save(trim(Image.open(path), box), f'back_{key}_{len(backs)}.jpg')
        return backs[sig]
    poker = []
    for i in range(0, 114, 2):
        page = i + 1; img = Image.open(ev[i]).convert('RGB')
        if page in edits:
            img, size, lines = set_text(img, edits[page]['text'], clean)
            print(f"  page {page} {edits[page]['name']}: {size} px, {len(lines)} lines")
        poker.append((save(trim(img, ebox), f'ev_{page:03d}.jpg'), back(ev[i + 1], ebox, 'ev')))
    assert not set(edits) - set(range(1, 98, 2)), 'an edit names a page that is not an event card face'
    mini = [(save(trim(Image.open(tr[i]), TR_BOX), f'tr_{i + 1:02d}.jpg'), back(tr[i + 1], TR_BOX, 'tr')) for i in range(0, 28, 2)]
    return poker, mini


def sheet_html(cards, size, cols, rows, paper):
    w, h = PAPER[paper]; per = cols * rows; out = []
    def cell(p): return f'<div class="c"><img src="file://{p}"></div>' if p else '<div class="c e"></div>'
    for i in range(0, len(cards), per):
        chunk = cards[i:i + per]
        out.append('<div class="s">' + ''.join(cell(f) for f, _ in chunk) + '</div>')
        cells = [b for _, b in chunk] + [None] * (per - len(chunk))
        grid = [list(reversed(cells[r * cols:(r + 1) * cols])) for r in range(rows)]       # mirrored for a flip on the long edge
        out.append('<div class="s">' + ''.join(cell(b) for r in grid for b in r) + '</div>')
    css = (f"@page {{ size: {w}mm {h}mm; margin: 0; }} * {{ margin: 0; padding: 0; box-sizing: border-box; }}"
           f"html, body {{ width: {w}mm; height: {h}mm; }}"
           f".s {{ page-break-after: always; display: grid; justify-content: center; align-content: center; width: {w}mm; height: {h}mm;"
           f" grid-template-columns: repeat({cols}, {size[0]:.3f}mm); grid-auto-rows: {size[1]:.3f}mm; }}"
           f".c {{ width: {size[0]:.3f}mm; height: {size[1]:.3f}mm; outline: 0.15mm solid #8c8c8c; overflow: hidden; }} .c.e {{ outline: none; }}"
           f".c img {{ width: 100%; height: 100%; display: block; }}")
    return f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(out)}</body></html>'


def build_events(paper, prepared=None):
    from weasyprint import HTML
    poker, mini = prepared or prepare()
    a = HTML(string=sheet_html(poker, EV_TRIM, 3, 3, paper)).render()
    b = HTML(string=sheet_html(mini, TR_TRIM, 4, 4, paper)).render()
    out = ROOT / f'pnp/events/events_expansion_{paper}.pdf'
    a.copy(a.pages + b.pages).write_pdf(str(out))
    return out


if __name__ == '__main__':
    papers = [p for p in sys.argv[1:] if p in PAPER] or ['letter', 'a4']
    prepared = prepare()
    for p in papers: print(build_events(p, prepared))
