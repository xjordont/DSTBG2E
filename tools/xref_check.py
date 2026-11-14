#!/usr/bin/env python3
"""Cross-reference check for the Class B chapters.
Validates every "§N", "§N.M" and "Appendix X" reference against the section map in the drafting brief
and against the headings actually present in drafted chapters; checks each drafted chapter's H2 numbering
against the map. Exit 1 on any broken reference."""
import re, glob, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
brief = (ROOT / 'work/phase2a/DRAFTING_BRIEF.md').read_text(encoding='utf-8')
mapblock = brief.split('## 4. Section map')[1].split('## 5.')[0]
valid = {'Appendix A', 'Appendix B'}
mapped = {}   # 'N.M' -> title from the brief
for ln in mapblock.splitlines():
    m = re.match(r'^§(\d+) ([^:(]+?)(?: \(|:|$)', ln.strip())
    if m:
        valid.add(m.group(1)); mapped[m.group(1)] = m.group(2).strip()
        for s, t in re.findall(r'(\d+\.\d+) ([^·()\n]+?)(?= ·| \(|$)', ln):
            valid.add(s); mapped[s] = t.strip()
# Chapters whose H2s the brief leaves to the author ("numbered H2s of your choosing" / "unless needed"):
# their drafted headings extend the map instead of being checked against it.
EXTENSIBLE = {'13', '14', '22'}
bad, warn = [], []
present = {}
if '--files' in sys.argv:   # explicit list (paths relative to the repo root); default: every chapter file on disk
    files = [str(ROOT / f) for f in sys.argv[sys.argv.index('--files') + 1:]]
else:
    files = sorted(glob.glob(str(ROOT / '10_manuscript_chapter_*.md'))) + [str(ROOT / '12_glossary.md')]
for f in files:   # pass 1: collect the headings actually drafted
    txt = pathlib.Path(f).read_text(encoding='utf-8'); name = pathlib.Path(f).name
    for m in re.finditer(r'^## (\d+\.\d+) (.+)$', txt, re.M):
        sec, title = m.group(1), m.group(2).strip()
        present[sec] = title
        if sec.split('.')[0] in EXTENSIBLE: valid.add(sec); mapped.setdefault(sec, title); continue
        if sec not in mapped: warn.append(f'{name}: H2 "{sec} {title}" is not in the section map')
        elif mapped[sec].lower() != title.lower(): warn.append(f'{name}: H2 {sec} titled "{title}" but map says "{mapped[sec]}"')
for f in files:   # pass 2: check every reference against the map plus the extensible chapters' headings
    txt = pathlib.Path(f).read_text(encoding='utf-8'); name = pathlib.Path(f).name
    for n, line in enumerate(txt.splitlines(), 1):
        for m in re.finditer(r'§(\d+(?:\.\d+)?)|Appendix ([AB])\b', line):
            ref = m.group(1) or f'Appendix {m.group(2)}'
            if ref not in valid: bad.append(f'{name}:{n}: §{ref} is not a valid target')
        if re.search(r'\b(see|refer to)\s+(?:the\s+)?["“]', line, re.I): bad.append(f'{name}:{n}: quoted-name cross-reference')
        if re.search(r'\b(described|explained|detailed|discussed|mentioned)\s+(later|earlier|previously|above|below|elsewhere)\b|\baforementioned\b', line, re.I): bad.append(f'{name}:{n}: vague cross-reference')
# a cited sub-section ("see §N.M, Title") must be an H3 of that section
h3 = {}
for f in files:
    cur = None
    for ln in pathlib.Path(f).read_text(encoding='utf-8').splitlines():
        m = re.match(r'^## (\d+\.\d+) ', ln)
        if m: cur = m.group(1); h3.setdefault(cur, set()); continue
        if ln.startswith('# '): cur = None
        m = re.match(r'^### (.+)$', ln)
        if m and cur: h3[cur].add(m.group(1).strip())
for f in files:
    name = pathlib.Path(f).name
    for n, line in enumerate(pathlib.Path(f).read_text(encoding='utf-8').splitlines(), 1):
        for m in re.finditer(r'§(\d+\.\d+), ([A-Z][^);]*)', line):
            sec, rest = m.group(1), m.group(2).strip()
            if sec in h3 and not any(rest == t or rest.startswith(t) for t in h3[sec]):
                bad.append(f'{name}:{n}: §{sec} has no sub-section "{rest[:40]}"')
# chapters drafted so far: do their H2 sets match the map exactly?
drafted = {m.group(1) for m in (re.match(r'10_manuscript_chapter_(\d\d)_', pathlib.Path(f).name) for f in files) if m}
for ch in sorted(drafted):
    if ch in EXTENSIBLE: continue
    want = {s for s in mapped if s.split('.')[0] == str(int(ch)) and '.' in s}
    have = {s for s in present if s.split('.')[0] == str(int(ch))}
    if want and want != have:
        miss = sorted(want - have, key=lambda s: float(s)); extra = sorted(have - want, key=lambda s: float(s))
        if miss: warn.append(f'chapter {ch}: sections in map but not drafted: {", ".join(miss)}')
        if extra: warn.append(f'chapter {ch}: sections drafted but not in map: {", ".join(extra)}')
for w in warn: print('WARN', w)
for b in bad: print('BAD ', b)
print(f'xref: {len(bad)} broken reference(s), {len(warn)} warning(s); map has {len(valid)} valid targets')
sys.exit(1 if bad else 0)
