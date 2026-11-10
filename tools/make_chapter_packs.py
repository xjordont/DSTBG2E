#!/usr/bin/env python3
"""Build per-chapter drafting packs for Phase 2A.
For each manuscript chapter: the source text (from work/docx/manuscript.md), every audit finding
mapped to the chapter by 03_coverage_tracker.md, and the completion entries that apply.
Writes work/phase2a/source/NN_slug.md and work/phase2a/packs/NN_slug.md."""
import csv, re, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parent.parent
MS = (ROOT / 'work/docx/manuscript.md').read_text(encoding='utf-8').splitlines()
TRACKER = (ROOT / '03_coverage_tracker.md').read_text(encoding='utf-8').splitlines()
ROWS = {r['ID']: r for r in csv.DictReader(open(ROOT / '02_audit_table.csv', encoding='utf-8'))}
BACKLOG = (ROOT / '04_completion_backlog.md').read_text(encoding='utf-8')

# Final book order → (manuscript chapter heading in tracker, output number, slug)
ORDER = [
    ('INTRODUCTION', '01', 'introduction'),
    ('SECOND EDITION NOTES', '00', 'front_matter'),
    ('GAME COMPONENTS', '02', 'game_components'),
    ('CHARACTERS', '03', 'characters'),
    ('EQUIPMENT', '04', 'equipment'),
    ('TILES & NODES', '05', 'tiles_and_nodes'),
    ('SETUP', '06', 'setup'),
    ('GAMEPLAY', '07', 'gameplay'),
    ('COMBAT BASICS', '08', 'combat_basics'),
    ('ENEMY TURN', '09', 'enemy_turn'),
    ('CHARACTER TURN', '10', 'character_turn'),
    ('RETURNING TO THE BONFIRE', '11', 'returning_to_the_bonfire'),
    ('SUMMONS', '12', 'phantoms'),
    ('MIMICS', '13', 'mimics'),
    ('CRYSTAL LIZARDS', '14', 'crystal_lizards'),
    ('BOSS ENCOUNTERS', '15', 'boss_encounters'),
    ('BOSS TURNS', '16', 'boss_turns'),
    ('BOSS SPECIAL RULES', '17', 'boss_special_rules'),
    ('CAMPAIGN PLAY', '18', 'campaign_play'),
    ('CAMPAIGNS', '19', 'campaigns'),
    ('PLAYER VS PLAYER', '20', 'player_versus_player'),
    ('GLOSSARY', '21', 'glossary'),
    ('F.A.Q.', '22', 'faq'),
    ('COMMUNITY UPDATE PACK', '23', 'appendices'),
]

# Parse tracker rows: chapter, section, status, audit ids, completion ids, notes, line
chap_rows = collections.OrderedDict()
for ln in TRACKER:
    if not ln.startswith('| ') or ln.startswith('| Chapter') or ln.startswith('|---'): continue
    cells = [c.strip() for c in ln.strip().strip('|').split('|')]
    if len(cells) < 7: continue
    chap, sec, status, aud, cmp_, drafted, notes = cells[:7]
    m = re.search(r'line (\d+)', notes)
    chap_rows.setdefault(chap, []).append(dict(section=sec, status=status, audit=aud, cmp=cmp_, notes=notes,
                                               line=int(m.group(1)) if m else None))

# Chapter line spans from the (chapter) rows, in manuscript order
starts = []
for chap, rows in chap_rows.items():
    for r in rows:
        if r['section'] == '(chapter)' and r['line']:
            starts.append((r['line'], chap)); break
starts.sort()
spans = {}
for i, (ln, chap) in enumerate(starts):
    end = starts[i + 1][0] - 1 if i + 1 < len(starts) else len(MS)
    spans[chap] = (ln, end)

def cmp_entry(cid):
    m = re.search(r'^### \[%s\].*?(?=^### \[CMP-|\Z)' % re.escape(cid), BACKLOG, re.S | re.M)
    return m.group(0).rstrip() if m else f'(entry {cid} not found)'

def ids_in(s):
    return [x.strip() for x in re.split(r'[,;]\s*', s) if x.strip()]

for chap, num, slug in ORDER:
    rows = chap_rows.get(chap, [])
    aud, cmps = [], []
    for r in rows:
        for i in ids_in(r['audit']):
            if i.startswith('CMP-'): cmps.append(i)
            else: aud.append(i)
        cmps += ids_in(r['cmp'])
    aud = sorted(set(a for a in aud if a in ROWS), key=lambda s: (s[0], int(s.split('-')[1])))
    cmps = sorted(set(cmps))
    # source
    src = ''
    if chap in spans:
        a, b = spans[chap]
        src = '\n'.join(MS[a - 1:b])
    (ROOT / f'work/phase2a/source/{num}_{slug}.md').write_text(
        f'<!-- manuscript.md lines {spans.get(chap, ("—","—"))[0]}–{spans.get(chap, ("—","—"))[1]} ; chapter "{chap}" -->\n{src}\n', encoding='utf-8')
    # pack
    out = [f'# Drafting pack — chapter {num} ({slug}) — manuscript chapter "{chap}"', '',
           f'Source text: `work/phase2a/source/{num}_{slug}.md` (manuscript.md lines {spans.get(chap, ("—","—"))[0]}–{spans.get(chap, ("—","—"))[1]}).', '',
           '## Tracker rows (section · status · notes)', '']
    for r in rows:
        out.append(f"- **{r['section']}** · {r['status']} · {r['notes']}")
    out += ['', f'## Audit findings mapped to this chapter ({len(aud)})', '',
            'Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).', '']
    sev_order = {'Blocker': 0, 'Major': 1, 'Minor': 2, 'Note': 3}
    for i in sorted(aud, key=lambda i: (sev_order.get(ROWS[i]['Severity'], 9), i)):
        r = ROWS[i]
        out.append(f"### {i} · {r['Issue type']} · {r['Severity']} · {r['Tag']}")
        out.append(f"- Location: {r['Location']}")
        if r['Evidence'].strip(): out.append(f"- Evidence: {r['Evidence']}")
        if r['Current text'].strip(): out.append(f"- Current text: {r['Current text']}")
        out.append(f"- Proposed fix: {r['Proposed fix']}")
        if r['Rationale'].strip(): out.append(f"- Rationale: {r['Rationale']}")
        if r['Gameplay impact'].strip(): out.append(f"- Gameplay impact: {r['Gameplay impact']}")
        if r['Decision needed'].strip(): out.append(f"- Decision needed: {r['Decision needed']}")
        out.append('')
    out += [f'## Completion entries that apply ({len(cmps)}) — approved at Gate 1', '']
    for c in cmps:
        out.append(cmp_entry(c)); out.append(''); out.append('---'); out.append('')
    (ROOT / f'work/phase2a/packs/{num}_{slug}.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(f'{num} {slug:28s} src L{spans.get(chap, ("—","—"))[0]}-{spans.get(chap, ("—","—"))[1]}  findings={len(aud):3d}  cmps={cmps}')
