#!/usr/bin/env python3
"""Word budget per manuscript file, against work/phase12/REWRITE_BRIEF.md.
A file more than 15% over its budget is reported and the script exits 1.
Usage: python3 tools/word_budget.py"""
import pathlib, re, sys, glob
ROOT = pathlib.Path(__file__).resolve().parent.parent
BUDGET = {'00': 250, '01': 140, '02': 1300, '03': 965, '04': 880, '05': 955, '06': 1715, '07': 1680, '08': 1260,
          '09': 1450, '10': 1130, '11': 830, '12': 845, '13': 520, '14': 260, '15': 1615, '16': 915, '17': 3950,
          '18': 1415, '19': 1930, '20': 500, '22': 400, '23': 1800, 'glossary': 2200}
def words(p): return len(re.sub(r'\{\{[^}]*\}\}', '', p.read_text(encoding='utf-8')).split())
total = over = 0
for f in sorted(glob.glob(str(ROOT / '10_manuscript_chapter_*.md'))) + [str(ROOT / '12_glossary.md')]:
    p = pathlib.Path(f); m = re.match(r'10_manuscript_chapter_(\d\d)_', p.name)
    key = m.group(1) if m else 'glossary'; n = words(p); b = BUDGET[key]; total += n
    flag = ''
    if n > b * 1.15: flag = '  OVER'; over += 1
    print(f'{p.name:55s} {n:6d} / {b:5d}{flag}')
print(f'total {total} / {sum(BUDGET.values())}')
sys.exit(1 if over else 0)
