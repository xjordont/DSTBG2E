#!/usr/bin/env python3
"""Apply the final rulings to the manuscript.

Reads work/phase3/edits_<cluster>.json (one list of text changes per rulings cluster) and the lead editor's
decisions in work/phase3/lead_overrides.json, applies each accepted change to its chapter file, and records it:

  - chapters: the change is made in 10_manuscript_chapter_NN_*.md and an entry is appended to the chapter's
    change-log fragment (work/phase2a/changelog/NN_*.md), marked [MECHANICAL CHANGE] where play changes;
  - glossary: every entry line the changes alter is appended whole as an AMEND to
    work/phase2a/glossary/21_glossary.md (the lead editor's reconciliation fragment), whether a change replaces
    the entry or a few words of it, and the change is logged in the glossary's change-log fragment; run
    `python3 tools/integrate_chapter.py 21` afterwards.

lead_overrides.json: {"<edit id>": {"skip": true, "why": "..."} | {"new": "replacement text", "why": "..."}
                                 | {"old": "...", "new": "...", "why": "..."}}

Usage: python3 tools/apply_rulings.py [--dry-run] [cluster ...]      (default clusters: core combat campaign phantom boss)
Exit status 1 if any accepted change cannot be applied (its `old` text is not found exactly once).
A state file (work/phase3/applied.json) records what has been applied, so the tool can be run again.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
P3 = ROOT / 'work/phase3'
args = [a for a in sys.argv[1:] if not a.startswith('--')]
dry = '--dry-run' in sys.argv
clusters = args or ['core', 'combat', 'campaign', 'phantom', 'boss']
over = json.loads((P3 / 'lead_overrides.json').read_text(encoding='utf-8')) if (P3 / 'lead_overrides.json').exists() else {}
state_p = P3 / 'applied.json'
done = json.loads(state_p.read_text(encoding='utf-8')) if state_p.exists() else {}

texts, problems, applied, skipped, touched = {}, [], [], [], set()


def text_of(name):
    if name not in texts:
        texts[name] = (ROOT / name).read_text(encoding='utf-8')
    return texts[name]


def fragment_for(name):
    m = re.match(r'10_manuscript_chapter_(\d\d)_(.+)\.md$', name)
    if m:
        return m.group(1), ROOT / f'work/phase2a/changelog/{m.group(1)}_{m.group(2)}.md'
    if name == '12_glossary.md':
        return '21', ROOT / 'work/phase2a/changelog/21_glossary.md'
    return None, None


logs, amends = {}, []
for c in clusters:
    fp = P3 / f'edits_{c}.json'
    if not fp.exists():
        print(f'({c}: no edits file)'); continue
    for e in json.loads(fp.read_text(encoding='utf-8')):
        eid = e['id']; o = over.get(eid, {})
        if eid in done:
            continue
        if o.get('skip'):
            skipped.append((eid, o.get('why', ''))); continue
        old = o.get('old', e['old']); new = o.get('new', e['new']); name = e['file']
        if not (ROOT / name).exists():
            problems.append((eid, name, 'no such file')); continue
        t = text_of(name); n = t.count(old)
        if n != 1:
            problems.append((eid, name, f'old text found {n} times: {old[:70]!r}')); continue
        if old == new:
            skipped.append((eid, 'no change')); continue
        texts[name] = t.replace(old, new)
        num, frag = fragment_for(name)
        why = e.get('rationale', '').strip()
        if o.get('why'):
            why = (why + ' Lead editor: ' + o['why']).strip()
        if e.get('mechanical'):
            why = '[MECHANICAL CHANGE] ' + why
        logs.setdefault((num, frag), []).append((e.get('section', ''), e.get('type', 'ruling'), old, new, why, eid, e.get('evidence', '')))
        applied.append(eid); touched.add(name)

# a glossary change may replace a whole entry or a few words of one: either way the amended entry is the whole line
if '12_glossary.md' in touched:
    before = set((ROOT / '12_glossary.md').read_text(encoding='utf-8').splitlines())
    amends = ['AMEND ' + ln for ln in texts['12_glossary.md'].splitlines() if ln.startswith('**') and ln not in before]

print(f'accepted and applicable: {len(applied)}; skipped by decision: {len(skipped)}; cannot be applied: {len(problems)}')
for p in problems:
    print('  PROBLEM', *p)
if dry or problems:
    sys.exit(1 if problems else 0)

for name in touched:
    if name != '12_glossary.md':              # the glossary itself is rewritten by integrate_chapter.py 21
        (ROOT / name).write_text(texts[name], encoding='utf-8')
for (num, frag), items in logs.items():
    t = frag.read_text(encoding='utf-8').rstrip('\n')
    k = max([int(m) for m in re.findall(rf'CH-{num}-(\d+)', t)] or [0])
    for sec, typ, old, new, why, eid, ev in items:
        k += 1
        clip = lambda s: s if len(s) <= 900 else s[:880].rstrip() + ' […]'
        t += (f'\n\n### CH-{num}-{k:03d} · {sec or "(section)"}\n- Type: {typ}\n- Before: "{clip(old)}"\n- After: "{clip(new)}"\n'
              f'- Rationale: {why}\n- Source: final rulings, {eid} (`06_final_rulings.md`)' + (f'; {ev}' if ev else ''))
    frag.write_text(t + '\n', encoding='utf-8')
if amends:
    gf = ROOT / 'work/phase2a/glossary/21_glossary.md'
    gf.write_text(gf.read_text(encoding='utf-8').rstrip('\n') + '\n' + '\n'.join(amends) + '\n', encoding='utf-8')
for eid in applied:
    done[eid] = True
state_p.write_text(json.dumps(done, indent=0), encoding='utf-8')
chs = sorted({fragment_for(n)[0] for n in touched if fragment_for(n)[0]})
print('applied. Re-integrate chapters:', ' '.join(chs))
