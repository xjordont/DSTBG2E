#!/usr/bin/env python3
"""Integrate one drafted chapter into the Phase 2A artefacts.
Usage: python3 tools/integrate_chapter.py NN
 - merges work/phase2a/glossary/NN_*.md deltas (ADD/AMEND lines) into 12_glossary.md (alphabetical)
 - replaces/appends the chapter block in 11_change_log.md from work/phase2a/changelog/NN_*.md
 - marks the chapter's rows Drafted in 03_coverage_tracker.md
 - runs tools/style_check.py over every drafted chapter + glossary -> 13_style_enforcement_report.md
 - runs tools/xref_check.py"""
import re, sys, glob, pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
TITLES = {'00': 'Front Matter', '01': 'Introduction', '02': 'Game Components', '03': 'Characters', '04': 'Equipment',
          '05': 'Tiles and Nodes', '06': 'Setup', '07': 'Gameplay', '08': 'Combat Basics', '09': 'Enemy Turn',
          '10': 'Character Turn', '11': 'Returning to the Bonfire', '12': 'Phantoms', '13': 'Mimics', '14': 'Crystal Lizards',
          '15': 'Boss Encounters', '16': 'Boss Turns', '17': 'Boss Special Rules', '18': 'Campaign Play', '19': 'Campaigns',
          '20': 'Player versus Player', '21': 'Glossary', '22': 'F.A.Q.', '23': 'Appendices'}
# tracker chapter heading per output number
TRACKER_CHAPTER = {'00': 'SECOND EDITION NOTES', '01': 'INTRODUCTION', '02': 'GAME COMPONENTS', '03': 'CHARACTERS', '04': 'EQUIPMENT',
                   '05': 'TILES & NODES', '06': 'SETUP', '07': 'GAMEPLAY', '08': 'COMBAT BASICS', '09': 'ENEMY TURN', '10': 'CHARACTER TURN',
                   '11': 'RETURNING TO THE BONFIRE', '12': 'SUMMONS', '13': 'MIMICS', '14': 'CRYSTAL LIZARDS', '15': 'BOSS ENCOUNTERS',
                   '16': 'BOSS TURNS', '17': 'BOSS SPECIAL RULES', '18': 'CAMPAIGN PLAY', '19': 'CAMPAIGNS', '20': 'PLAYER VS PLAYER',
                   '21': 'GLOSSARY', '22': 'F.A.Q.', '23': 'COMMUNITY UPDATE PACK'}

def one(pattern):
    m = sorted(glob.glob(str(ROOT / pattern)))
    return pathlib.Path(m[0]) if m else None

def parse_glossary(text):
    head, entries = [], []
    for para in re.split(r'\n\s*\n', text.strip()):
        m = re.match(r'^\*\*(.+?)\*\*\s*(.*)$', para, re.S)
        if m: entries.append((m.group(1).strip(), para.strip()))
        else: head.append(para.strip())
    return head, entries

def key(h): return re.sub(r'[^a-z0-9 ]', '', h.lower().rstrip('.'))

def merge_glossary(num):
    delta = one(f'work/phase2a/glossary/{num}_*.md')
    gp = ROOT / '12_glossary.md'
    head, entries = parse_glossary(gp.read_text(encoding='utf-8'))
    added = amended = 0
    if delta:
        for ln in delta.read_text(encoding='utf-8').splitlines():
            m = re.match(r'^(ADD|AMEND)\s+(\*\*.+?\*\*.*)$', ln.strip())
            if not m: continue
            hw = re.match(r'^\*\*(.+?)\*\*', m.group(2)).group(1).strip()
            idx = next((i for i, (h, _) in enumerate(entries) if key(h) == key(hw)), None)
            if idx is None: entries.append((hw, m.group(2).strip())); added += 1
            else: entries[idx] = (hw, m.group(2).strip()); amended += 1
    entries.sort(key=lambda e: key(e[0]))
    gp.write_text('\n\n'.join(head + [e[1] for e in entries]) + '\n', encoding='utf-8')
    return added, amended, len(entries)

def merge_changelog(num):
    frag = one(f'work/phase2a/changelog/{num}_*.md')
    cp = ROOT / '11_change_log.md'
    if not cp.exists():
        cp.write_text('# 11 — Change Log (Class A)\n\nEvery substantive change made in Phase 2A between the manuscript (`work/docx/manuscript.md`) and the Class B chapters, one block per chapter, entries `CH-NN-KKK` (NN = chapter). Types: clarification, correction, completion, cut, restructure, style, mechanical change. Mechanical changes cite `Source: Gate 1 — OQ-NN` (see `05_gate1_decisions.md`).\n', encoding='utf-8')
    text = cp.read_text(encoding='utf-8')
    body = frag.read_text(encoding='utf-8').strip() if frag else '_No change-log fragment supplied._'
    body = re.sub(r'^#\s[^\n]*\n', '', body).strip()   # drop a fragment-level H1 if present
    block = f'\n\n## Chapter {num} — {TITLES[num]}\n\n{body}\n'
    pat = re.compile(rf'\n\n## Chapter {num} — .*?(?=\n\n## Chapter \d\d — |\Z)', re.S)
    text = pat.sub(block.rstrip('\n'), text) if pat.search(text) else text.rstrip('\n') + block
    cp.write_text(text.rstrip('\n') + '\n', encoding='utf-8')
    return len(re.findall(r'^### CH-', body, re.M))

def mark_tracker(num):
    tp = ROOT / '03_coverage_tracker.md'; lines = tp.read_text(encoding='utf-8').splitlines(); n = 0
    chap = TRACKER_CHAPTER[num]; sect = int(num) if num not in ('00', '23') else None
    tag = f'yes (§{sect})' if sect and sect <= 22 else ('yes (Foreword)' if num == '00' else 'yes (Appendix A/B)')
    for i, ln in enumerate(lines):
        if ln.startswith(f'| {chap} |'):
            cells = ln.split('|')
            if len(cells) > 6 and cells[6].strip() in ('no', ''):
                cells[6] = f' {tag} '; lines[i] = '|'.join(cells); n += 1
    tp.write_text('\n'.join(lines) + '\n', encoding='utf-8'); return n

def main():
    num = sys.argv[1]
    a, b, total = merge_glossary(num)
    c = merge_changelog(num)
    t = mark_tracker(num)
    print(f'chapter {num}: glossary +{a} / amended {b} (now {total} headwords); change-log entries {c}; tracker rows marked {t}')
    files = sorted(glob.glob(str(ROOT / '10_manuscript_chapter_*.md'))) + [str(ROOT / '12_glossary.md')]
    r = subprocess.run([sys.executable, str(ROOT / 'tools/style_check.py'), *files, '--report', str(ROOT / '13_style_enforcement_report.md')], capture_output=True, text=True)
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr)
    subprocess.run([sys.executable, str(ROOT / 'tools/xref_check.py')])

if __name__ == '__main__': main()
