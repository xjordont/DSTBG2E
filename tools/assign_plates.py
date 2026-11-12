#!/usr/bin/env python3
"""Fill the illustration pools of layout/tuning.json from the art list (layout/art_candidates.json).

The build sets an illustration in the room a section break leaves at the foot of a column (see choose_plates in
tools/build_pdf.py). It picks from `plates.by_chapter[NN]` first and then from `plates.pool`. This tool writes
both lists and the captions:

  - a picture goes to the chapter the art list suggests for it (`suggested_for`), largest first;
  - pictures with a title or logo baked in, pictures already used as a chapter header, in a closing gallery or as
    a figure, pictures listed in `plates.never`, and pictures too small to print at column width are left out;
  - paintings carry no caption; a card, dashboard or card fan is captioned with what it is (from `subject`);
  - the general pool is every remaining painting; miniatures are left to the galleries and the boss headings.

Run it again whenever the art list or the chapter headers change:  python3 tools/assign_plates.py
"""
import glob, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
tp = ROOT / 'layout/tuning.json'
tun = json.loads(tp.read_text(encoding='utf-8'))
cands = json.loads((ROOT / 'layout/art_candidates.json').read_text(encoding='utf-8'))['candidates']
headers = {h['header']['file'] for h in tun.get('heroes', {}).values() if h.get('header')}
skip = set(tun.get('plates', {}).get('never', []))
# a picture already shown in a chapter's closing gallery or as a figure is not set again as an illustration
shown = {f for h in tun.get('heroes', {}).values() for f in h.get('end', [])} | {f.get('file') for f in tun.get('figures', [])}


def chapter_key(s):
    s = str(s or '')
    m = re.match(r'\s*(\d+)\b', s)
    if m:
        return '%02d' % int(m.group(1))
    m = re.search(r'Appendix ([AB])', s)
    return f'app-{m.group(1).lower()}' if m else None


def caption(c):
    if c['file'].startswith('assets/art/'):
        return ''
    s = re.split(r'[,;(]', c.get('subject', ''))[0].strip()
    s = re.sub(r'^(The|A|An) ', '', s)
    return s[:1].upper() + s[1:]


by, pool, caps = {}, [], dict(tun.get('captions', {}))
for c in sorted(cands, key=lambda c: -(c['width'] * c['height'])):
    f = c['file']
    if f in headers or f in skip or c.get('baked_text') or not (ROOT / f).exists():
        continue
    if max(c['width'], c['height']) < 260 or c['height'] < 150:
        continue
    if c.get('kind') == 'token':
        continue
    if re.search(r'-(expansion-)?miniature-', f):
        continue
    key = chapter_key(c.get('suggested_for'))
    (by.setdefault(key, []) if key else pool).append(f)
    stem = re.sub(r'^ast-\d+-', '', pathlib.Path(f).stem)
    caps[stem] = caption(c)
    if key and f.startswith('assets/art/'):
        pool.append(f)                      # a painting not needed by its own chapter may serve another
# miniatures are shown in the closing galleries and under the boss headings, never as column illustrations
pool = [f for f in pool if f not in skip and f not in shown]
by = {k: [f for f in v if f not in shown] for k, v in by.items()}
old = tun.get('plates', {})
tun['plates'] = {'min_gap': old.get('min_gap', 104), 'min_h': old.get('min_h', 70), 'max_stack': old.get('max_stack', 2), 'enlarge': old.get('enlarge', 1.0),
                 'never': sorted(skip), 'by_chapter': {k: v for k, v in sorted(by.items())}, 'pool': list(dict.fromkeys(pool))}
caps.update(tun.get('captions_fixed', {}))      # captions written by hand are never recomputed
tun['captions'] = caps
tp.write_text(json.dumps(tun, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('chapters with their own pictures:', {k: len(v) for k, v in sorted(by.items())}, '· general pool:', len(tun['plates']['pool']))
