#!/usr/bin/env python3
"""The print-and-play encounter decks (Tomb of Giants, Painted World of Ariamis): mini cards in the layout of the
printed 2017 encounter cards. Called by build_pnp.py; reads pnp/encounters/<deck>.json."""
import html, json, pathlib
from build_pnp import ROOT, uri, MINI, PAPER, icon, font_face, sheet_css, sheets, back, BASE_CSS, EVENT_CSS, LEVEL_ICON

ENEMY_ICON = {'Skeleton Soldier': 'ast-0008-skeleton-soldier', 'Skeleton Archer': 'ast-0012-skeleton-archer', 'Giant Skeleton Soldier': 'ast-0016-giant-skeleton-soldier',
              'Giant Skeleton Archer': 'ast-0019-giant-skeleton-archer', 'Skeleton Beast': 'ast-0022-skeleton-beast', 'Necromancer': 'ast-0024-necromancer'}
# the Painted World icons are cut from a community sheet of 2017-style encounter cards (pnp/encounters/icons)
PWA_ICON = {'Bonewheel Skeleton': 'pwa-bonewheel-skeleton', 'Crow Demon': 'pwa-crow-demon', 'Engorged Zombie': 'pwa-engorged-zombie', 'Phalanx': 'pwa-phalanx',
            'Phalanx Hollow': 'pwa-phalanx-hollow', 'Snow Rat': 'pwa-snow-rat'}
TERRAIN_ICON = {'barrel': 'ast-0013-barrel', 'chest': 'ast-0009-treasure-chest', 'gravestone': 'ast-0017-gravestone'}

CSS = """
.en { background: #23262b; color: #f1ead9; outline: 0.2mm solid #777; }
.en .name { position: absolute; top: 2.2mm; left: 1mm; right: 1mm; text-align: center; font-size: 7.4pt; line-height: 1.08; letter-spacing: 0.03em; height: 7mm; display: flex; align-items: center; justify-content: center; }
.en .row { position: absolute; left: 2.3mm; display: flex; gap: 1.5mm; align-items: center; }
.en .row .nd { flex: 0 0 8mm; width: 8mm; height: 8mm; border-radius: 50%; overflow: hidden; display: flex; align-items: center; justify-content: center; } .en .row .nd img { height: 9.4mm; }
.en .slot { flex: 0 0 7.6mm; width: 7.6mm; height: 7.6mm; border-radius: 50%; background: #d9d4c6; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.en .slot.empty { background: #8d8a80; opacity: 0.45; } .en .slot img { height: 8.3mm; } .en .slot.t img { height: 8mm; }
.en .slot span { font-family: 'Cinzel', serif; font-weight: 700; font-size: 6.6pt; color: #1b1b1b; letter-spacing: -0.02em; }
.en .slot.pwa img { width: 7.6mm; height: 7.6mm; flex: none; } .lg .slot.pwa img { width: 6mm; height: 6mm; flex: none; }
.en .lv { position: absolute; left: 2mm; bottom: 2.6mm; } .en .lv img { height: 7.2mm; }
.en .trap { position: absolute; left: 11.5mm; right: 11.5mm; bottom: 4.6mm; text-align: center; } .en .trap img { height: 2.4mm; margin: 0 0.3mm; }
.en .set { position: absolute; right: 2.2mm; bottom: 3.1mm; width: 6.6mm; height: 6.6mm; border-radius: 50%; border: 0.3mm solid #b9a36a; display: flex; align-items: center; justify-content: center;
           font-family: 'Cinzel', serif; font-weight: 700; font-size: 4.6pt; color: #e8d9ae; }
.en .id { position: absolute; left: 0; right: 0; bottom: 0.7mm; text-align: center; font-family: 'Cinzel', serif; font-size: 3.4pt; letter-spacing: 0.1em; color: #9a9485; }
.lg { background: #f5f0e6; } .lg .name { text-align: center; font-size: 6.6pt; padding: 2mm 1mm 1mm; } .lg table { width: 37mm; margin: 0 2mm; border-collapse: collapse; font-size: 5.3pt; }
.lg td { padding: 0.35mm 0.5mm; border-top: 0.12mm solid #b8ad98; vertical-align: middle; line-height: 1.1; } .lg td.i { width: 7mm; } .lg .slot { width: 6mm; height: 6mm; border-radius: 50%; background: #d9d4c6; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.lg .slot img { height: 6.6mm; } .lg .slot span { font-family: 'Cinzel', serif; font-weight: 700; font-size: 5.2pt; }
.lg .note { font-size: 4.9pt; line-height: 1.15; padding: 1mm 2.2mm 0; text-align: center; color: #3c372d; }
"""


def slot(name):
    if name is None: return '<div class="slot empty"></div>'
    if name in ENEMY_ICON: return f'<div class="slot">{icon(ENEMY_ICON[name], "")}</div>'
    if name in PWA_ICON: return f'<div class="slot pwa"><img src="{uri(ROOT / "pnp/encounters/icons" / (PWA_ICON[name] + ".png"))}" alt=""></div>'
    return f'<div class="slot t">{icon(TERRAIN_ICON[name], "")}</div>'


def front(c, code):
    def row(y, node, items, n):
        cells = ''.join(slot(x) for x in (list(items) + [None] * n)[:n])
        return f'<div class="row" style="top:{y}mm"><div class="nd">{icon(node, "")}</div>{cells}</div>'
    trap = f'<div class="trap">{icon("ast-0068-trapped-encounter-icon-2017", "") * 2}</div>' if c.get('trap') else ''
    return (f'<div class="card en"><div class="name">{html.escape(c["name"])}</div>'
            + row(10.2, 'ast-0006-primary-spawn-node', c['spawn1'], 3) + row(19.6, 'ast-0010-secondary-spawn-node', c['spawn2'], 3)
            + row(29.0, 'ast-0014-primary-terrain-node', [c.get('terrain1')] if c.get('terrain1') else [], 1)
            + row(38.4, 'ast-0018-secondary-terrain-node', [c.get('terrain2')] if c.get('terrain2') else [], 1)
            + f'<div class="lv">{icon(LEVEL_ICON[c["level"]], "")}</div>{trap}<div class="set">{code}</div><div class="id">{c["id"]} · print and play</div></div>')


def legend(deck):
    rows = ''.join(f'<tr><td class="i">{slot(e["name"])}</td><td><b>{html.escape(e["name"])}</b><br>{e["models"]} · threat {e["threat"]} · health {e["health"]}</td></tr>' for e in deck['enemies'])
    return (f'<div class="card lg"><div class="name">{html.escape(deck["deck"])}<br>encounter deck</div><table>{rows}</table>'
            f'<div class="note">{html.escape(deck["note"])}</div></div>')


def build_encounters(paper):
    from weasyprint import HTML
    outs = []
    for file in sorted((ROOT / 'pnp/encounters').glob('*.json')):
        deck = json.loads(file.read_text(encoding='utf-8'))
        fronts = [(legend(deck), ('lg', 0))] + [(front(c, deck['code']), ('en', c['level'])) for c in sorted(deck['cards'], key=lambda c: c['id'])]
        def back_of(k, deck=deck):
            if k[0] == 'lg': return back(deck['deck'], 'Encounter deck', letter=deck['code'], mini=True)
            return back(deck['deck'], f'Encounter · Level {k[1]}', LEVEL_ICON[k[1]], mini=True)
        css = font_face() + BASE_CSS + EVENT_CSS + CSS + sheet_css(paper, MINI, 4, 4)
        doc = f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(sheets(fronts, back_of, 4, 4))}</body></html>'
        out = file.with_name(f'{file.stem}_{paper}.pdf'); HTML(string=doc, base_url=str(ROOT)).write_pdf(str(out)); outs.append(out)
    return outs
