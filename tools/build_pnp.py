#!/usr/bin/env python3
"""Build the print-and-play modules: the Events Expansion and the two encounter decks.

Usage: python3 tools/build_pnp.py [events] [encounters] [--paper letter|a4|both]

events: tools/build_pnp_events.py lays out the Events Expansion II cards from their maker's files, with the text
changes of pnp/events/edits.json. encounters: tools/build_pnp_encounters.py builds pnp/encounters/<deck>.json.
Card fronts are laid out on a grid; each sheet of fronts is followed by a sheet of backs, so a file prints
double-sided (flip on the long edge). This module holds the layout helpers the encounter decks use."""
import argparse, base64, html, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ICONS = ROOT / 'assets/icons'
FONTS = ROOT / 'assets/fonts/static'
PAPER = {'letter': (215.9, 279.4), 'a4': (210.0, 297.0)}
POKER = (63.5, 88.9); MINI = (41.0, 63.0)


def uri(path):
    return 'data:image/png;base64,' + base64.b64encode(pathlib.Path(path).read_bytes()).decode()


_cache = {}
def icon(slug, cls='ic'):
    if slug not in _cache: _cache[slug] = uri(ICONS / (slug + '.png'))
    return f'<img class="{cls}" src="{_cache[slug]}" alt="">'


def font_face():
    out = []
    for fam, file, weight, style in (('Cinzel', 'Cinzel-Regular.ttf', 400, 'normal'), ('Cinzel', 'Cinzel-Bold.ttf', 700, 'normal'),
                                     ('Caslon', 'LibreCaslonText-Regular.ttf', 400, 'normal'), ('Caslon', 'LibreCaslonText-Bold.ttf', 700, 'normal'),
                                     ('Caslon', 'LibreCaslonText-Italic.ttf', 400, 'italic')):
        out.append(f"@font-face {{ font-family: '{fam}'; src: url('file://{FONTS / file}'); font-weight: {weight}; font-style: {style}; }}")
    return '\n'.join(out)


BASE_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Caslon', serif; color: #1a1a1a; }
.sheet { page-break-after: always; display: grid; justify-content: center; align-content: center; width: 100%; height: 100%; }
.card { position: relative; overflow: hidden; outline: 0.2mm solid #9a9a9a; background: #f5f0e6; }
.ic { height: 1em; vertical-align: -0.15em; }
.name { font-family: 'Cinzel', serif; font-weight: 700; letter-spacing: 0.02em; }
.foot { position: absolute; left: 0; right: 0; bottom: 1.6mm; text-align: center; font-family: 'Cinzel', serif; font-size: 5.2pt; letter-spacing: 0.08em; color: #6b6253; text-transform: uppercase; }
"""

EVENT_CSS = """
.ev .head { background: #1c1b20; color: #f3ead6; height: 17mm; padding: 2.4mm 3mm 0 3mm; text-align: center; }
.ev .head .name { font-size: 10.5pt; line-height: 1.12; }
.ev .lvl { position: absolute; top: 1.6mm; left: 2mm; } .ev .lvl img { height: 6.4mm; }
.ev .tag { position: absolute; top: 15mm; left: 50%; transform: translateX(-50%); font-family: 'Cinzel', serif; font-weight: 700; font-size: 6.2pt; letter-spacing: 0.14em;
           color: #fff; padding: 0.7mm 3mm 0.5mm; border-radius: 1.2mm; text-transform: uppercase; white-space: nowrap; }
.ev .tag.lingering { background: #7a2318; } .ev .tag.once { background: #2f4a63; }
.ev .kind { margin-top: 5.2mm; text-align: center; font-family: 'Cinzel', serif; font-size: 5.6pt; letter-spacing: 0.16em; color: #7b715f; text-transform: uppercase; }
.ev .text { position: absolute; top: 26mm; bottom: 7mm; left: 4.2mm; right: 4.2mm; display: flex; align-items: center; }
.ev .text p { font-size: 8.3pt; line-height: 1.24; text-align: center; width: 100%; hyphens: auto; }
.ev.long .text p { font-size: 7.5pt; line-height: 1.2; }
.back { background: #1c1b20; color: #e9dfc8; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
.back .ring { width: 30mm; height: 30mm; border-radius: 50%; border: 0.5mm solid #b9975a; display: flex; align-items: center; justify-content: center; margin-bottom: 4mm; }
.back .ring img { height: 15mm; } .back .ring span { font-family: 'Cinzel', serif; font-weight: 700; font-size: 20pt; color: #b9975a; }
.back .t1 { font-family: 'Cinzel', serif; font-weight: 700; font-size: 11pt; letter-spacing: 0.12em; text-transform: uppercase; }
.back .t2 { font-family: 'Cinzel', serif; font-size: 7pt; letter-spacing: 0.2em; margin-top: 1.5mm; color: #b9975a; text-transform: uppercase; }
.back.mini .ring { width: 20mm; height: 20mm; margin-bottom: 3mm; } .back.mini .ring img { height: 10mm; } .back.mini .ring span { font-size: 13pt; }
.back.mini .t1 { font-size: 7.5pt; } .back.mini .t2 { font-size: 5pt; }
.tr .head { background: #3a2a14; color: #f3ead6; height: 13mm; padding: 2.2mm 3mm 0; text-align: center; }
.tr .head .name { font-size: 10.5pt; } .tr .sub { font-family: 'Cinzel', serif; font-size: 5.6pt; letter-spacing: 0.18em; color: #d9c28f; text-transform: uppercase; }
.tr svg { position: absolute; top: 15.5mm; left: 50%; transform: translateX(-50%); width: 42mm; height: 42mm; }
.tr .entry { position: absolute; top: 57.2mm; left: 0; right: 0; text-align: center; font-family: 'Cinzel', serif; font-size: 5.4pt; letter-spacing: 0.2em; color: #7b715f; }
.tr table { position: absolute; left: 3mm; right: 3mm; bottom: 6.6mm; width: 57.5mm; border-collapse: collapse; font-size: 7pt; }
.tr td { text-align: center; padding: 0.5mm 0.3mm; border-top: 0.15mm solid #b8ad98; line-height: 1.15; } .tr td.l img { height: 5mm; } .tr td.l { width: 8mm; }
.tr td b { font-size: 9pt; }
.it .head { background: #20303a; color: #f3ead6; padding: 1.6mm 1.5mm 1.2mm; text-align: center; min-height: 9.5mm; }
.it .head .name { font-size: 7.2pt; line-height: 1.1; } .it .slot { font-family: 'Cinzel', serif; font-size: 4.6pt; letter-spacing: 0.12em; color: #c9d6dd; text-transform: uppercase; }
.it .req { display: flex; justify-content: space-around; font-family: 'Cinzel', serif; font-size: 5.2pt; padding: 1mm 1.5mm; border-bottom: 0.15mm solid #b8ad98; }
.it .req b { font-size: 7pt; } .it .atk { font-size: 6.2pt; padding: 0.8mm 2mm 0; line-height: 1.2; } .it .atk b { font-family: 'Cinzel', serif; }
.it .text { position: absolute; left: 2.2mm; right: 2.2mm; bottom: 9.5mm; font-size: 6pt; line-height: 1.18; text-align: center; }
.it .stats { position: absolute; left: 0; right: 0; bottom: 4.2mm; text-align: center; font-size: 5.2pt; color: #4b4538; }
.it .foot { bottom: 1.2mm; font-size: 4.2pt; }
"""


def sheet_css(paper, card, cols, rows):
    w, h = PAPER[paper]
    return (f"@page {{ size: {w}mm {h}mm; margin: 0; }}\nhtml, body {{ width: {w}mm; height: {h}mm; }}\n"
            f".sheet {{ grid-template-columns: repeat({cols}, {card[0]}mm); grid-auto-rows: {card[1]}mm; width: {w}mm; height: {h}mm; }}\n"
            f".card {{ width: {card[0]}mm; height: {card[1]}mm; }}\n")


def sheets(fronts, back_of, cols, rows, mirror=True):
    """Lay cards out, each sheet of fronts followed by its sheet of backs (columns mirrored for long-edge duplex)."""
    per = cols * rows; out = []
    for i in range(0, len(fronts), per):
        chunk = fronts[i:i + per]
        out.append('<div class="sheet">' + ''.join(c for c, _ in chunk) + '</div>')
        cells = [back_of(k) for _, k in chunk] + [''] * (per - len(chunk))
        grid = [cells[r * cols:(r + 1) * cols] for r in range(rows)]
        if mirror: grid = [list(reversed(r)) for r in grid]
        out.append('<div class="sheet">' + ''.join(c or '<div class="card" style="outline:none;background:none"></div>' for r in grid for c in r) + '</div>')
    return out


def esc(s): return html.escape(s)


# ---------------------------------------------------------------- the events deck
LEVEL_ICON = {1: 'ast-0007-encounter-level-1', 2: 'ast-0011-encounter-level-2', 3: 'ast-0015-encounter-level-3'}
EFFECT_ICON = {'poison': 'ast-0065-poison', 'bleed': 'ast-0063-bleed', 'frostbite': 'ast-0064-frostbite', 'stagger': 'ast-0066-stagger', 'push': 'ast-0058-push-affected-enemies'}


def back(title, sub, glyph=None, letter=None, mini=False):
    inner = icon(glyph, '') if glyph else f'<span>{letter}</span>'
    return f'<div class="card back{" mini" if mini else ""}"><div class="ring">{inner}</div><div class="t1">{title}</div><div class="t2">{sub}</div></div>'


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('what', nargs='*', default=['events', 'encounters']); ap.add_argument('--paper', default='both')
    a = ap.parse_args(); papers = ['letter', 'a4'] if a.paper == 'both' else [a.paper]
    if 'events' in a.what:
        import build_pnp_events
        prepared = build_pnp_events.prepare()
        for p in papers: print(build_pnp_events.build_events(p, prepared))
    for p in papers:
        if 'encounters' in a.what:
            try:
                from build_pnp_encounters import build_encounters
            except ImportError:
                continue
            for o in build_encounters(p): print(o)
