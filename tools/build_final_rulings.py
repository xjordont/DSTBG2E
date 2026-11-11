#!/usr/bin/env python3
"""Write 06_final_rulings.md (the decision record of the final rulings) and the closing 14_open_issues.md.

Sources: the five rulings memos in work/phase3/rulings_<area>.md (one entry per question, with evidence), the
proposed text changes in work/phase3/edits_<area>.json, the lead editor's decisions in
work/phase3/lead_overrides.json and work/phase3/edits_lead.json, and the record of what was applied
(work/phase3/applied.json). Run after tools/apply_rulings.py.
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
P3 = ROOT / 'work/phase3'
AREAS = [('core', 'Core loop and economy (chapters 3, 4, 6, 7, 11, appendices)'), ('combat', 'Movement and combat (chapters 5, 8, 9, 10)'),
         ('boss', 'Bosses (chapters 15, 16, 17)'), ('campaign', 'Campaign play and components (chapters 2, 18, 19)'),
         ('phantom', 'Phantoms, mimics, crystal lizards, player versus player, F.A.Q. (chapters 12, 13, 14, 20, 22)')]
LEAD_Q = {1: 'Campaign soul rewards against doubled stat costs', 2: "When an invader's encounter is cleared", 3: 'What marks hollowing', 4: 'Bosses whose rules were placeholders',
          5: 'Ornstein & Smough', 6: 'Player-versus-player stalemate', 7: 'Player-versus-player dodge difficulty', 8: 'Traps and models other than characters',
          9: 'Shop stocking', 10: 'Shop sales', 11: 'Joining or leaving a game', 12: 'Luck', 13: 'Boss encounter details (shortcut, facing, turn order)',
          14: "The mimic's reward", 15: 'Appendix A and the Butcher Knife', 16: 'Frostbite duration', 17: 'The dropped Firekeeper luck purchase',
          18: 'Component counts and campaigns from booklets not first supplied', 19: 'Level 4 treasure', 20: 'Layout of the first leg',
          21: 'Painted illustrations', 22: 'Shortage of blank invader tokens'}

applied = json.loads((P3 / 'applied.json').read_text(encoding='utf-8')) if (P3 / 'applied.json').exists() else {}
over = json.loads((P3 / 'lead_overrides.json').read_text(encoding='utf-8')) if (P3 / 'lead_overrides.json').exists() else {}


def entries(area):
    t = (P3 / f'rulings_{area}.md').read_text(encoding='utf-8')
    out = []
    for m in re.finditer(r'^### (\S+) · ([^\n]+)\n(.*?)(?=^### |^## |\Z)', t, re.S | re.M):
        body = m.group(3)
        f = lambda k: (re.search(rf'^- {k}:\s*(.+?)(?=\n- [A-Z][a-z ]+:|\Z)', body, re.S | re.M) or [None, ''])[1].strip().replace('\n', ' ')
        out.append({'id': m.group(1), 'title': m.group(2).strip(), 'question': f('Question'), 'ruling': f('Ruling'), 'why': f('Why'), 'mech': f('Mechanical'), 'edits': f('Edits')})
    return out, t


def short(s, n):
    s = re.sub(r'\s+', ' ', s.split('|')[0])          # a table inside an entry is left to the memo
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' …'


def kind(r):
    m = re.match(r'\s*(CONFIRM|CHANGE|ADD|DELETE|NOT A RULES QUESTION)', r.upper())
    return m.group(1) if m else 'OTHER'


ALL = {a: entries(a) for a, _ in AREAS if (P3 / f'rulings_{a}.md').exists()}
EDITS = {a: json.loads((P3 / f'edits_{a}.json').read_text(encoding='utf-8')) for a, _ in AREAS if (P3 / f'edits_{a}.json').exists()}
lead_edits = json.loads((P3 / 'edits_lead.json').read_text(encoding='utf-8')) if (P3 / 'edits_lead.json').exists() else []
verify_edits = [e for v in ('verify_a', 'verify_b') if (P3 / f'edits_{v}.json').exists()
                for e in json.loads((P3 / f'edits_{v}.json').read_text(encoding='utf-8'))]
n_items = sum(len(v[0]) for v in ALL.values())
counts = {}
for a, (es, _) in ALL.items():
    for e in es:
        counts[kind(e['ruling'])] = counts.get(kind(e['ruling']), 0) + 1
n_applied = len(applied)
n_mech = (sum(1 for a in EDITS for e in EDITS[a] if e.get('mechanical') and e['id'] in applied)
          + sum(1 for e in lead_edits + verify_edits if e.get('mechanical') and e['id'] in applied))

L = []
A = L.append
A('# 06 — Final Rulings (Class A)')
A('')
A('Date: 2026-11-11. Authority: the author delegated every open rules question to the lead editor ("use your best judgement as a pro boardgame designer"), '
  'asked that the official rulesets, the two community rulesets, and online discussion inform each ruling, and set the standard: clear, intuitive, simple, '
  'mechanically consistent, well written, tactically interesting, and free of bloat. On the same date the author confirmed ownership of the rights in all source '
  'artwork and supplied eight further expansion booklets. This file records what was decided. It supersedes `05_gate1_decisions.md` wherever the two differ, '
  'and each such place is named below.')
A('')
A('## 1. Method')
A('')
A('1. Every item in `14_open_issues.md` (22 lead items and the per-chapter lists) was assigned to one of five rules areas.')
A('2. For each area a researcher read the chapters, the author\'s source manuscript, the official 2017 and 2022 rulebooks, the official F.A.Q., the official expansion booklets, '
  'the two community rulesets (Extended Rules, Hollowed Edition), and what online discussion could be reached, and wrote one entry per question with the evidence and a recommendation. '
  'The memos are `work/phase3/rulings_<area>.md`; the proposed text changes are `work/phase3/edits_<area>.json`.')
A('3. The lead editor read every ruling that changes play, settled the places where two areas met, withdrew what the evidence did not support, and added the follow-up changes the researchers flagged for other areas '
  '(`work/phase3/lead_overrides.json`, `work/phase3/edits_lead.json`).')
A('4. `tools/apply_rulings.py` applied the accepted changes; each is an entry in `11_change_log.md` that cites its ruling, marked `[MECHANICAL CHANGE]` where play changes.')
A('5. Online evidence was thin: several forums refuse automated reading. No ruling rests on an online source alone; the memos say which sources were reached.')
A('')
A(f'Totals: {n_items} questions answered ({", ".join(f"{k.lower()} {v}" for k, v in sorted(counts.items()))}); {n_applied} text changes applied, {n_mech} of them changes to play.')
A('')
A('## 2. The 22 lead questions')
A('')
A('| # | Question | Ruling | Entry |')
A('|---|---|---|---|')
for n in range(1, 23):
    hits = [(a, e) for a, (es, _) in ALL.items() for e in es if re.search(rf'\blead(?: item)?s? {n}\b', e['title'], re.I)]
    if n == 21:
        A(f"| 21 | {LEAD_Q[21]} | Closed by the author: the rights in all source artwork are confirmed, so the paintings are placed and the anatomy plates are shown whole. | author, 2026-11-11 |")
        continue
    if not hits:
        A(f'| {n} | {LEAD_Q[n]} | see the area tables below | |'); continue
    a, e = hits[0]
    A(f"| {n} | {LEAD_Q[n]} | {short(kind(e['ruling']).capitalize() + ': ' + e['why'], 330)} | {', '.join(h[1]['id'] for h in hits[:3])} |")
A('')
A('## 3. Rulings that change play')
A('')
A('| Edit | Where | What changes |')
A('|---|---|---|')
seen = set()
for a in list(EDITS) + ['lead', 'verify']:
    for e in (EDITS.get(a, []) if a not in ('lead', 'verify') else lead_edits if a == 'lead' else verify_edits):
        if e.get('mechanical') and e['id'] in applied and e.get('rationale') not in seen:
            seen.add(e.get('rationale'))
            A(f"| {e['id']} | {e.get('section', '')} | {short(e.get('rationale', ''), 260)} |")
A('')
A('## 4. Where a Gate 1 answer is revised')
A('')
revised = [(a, e) for a, (es, _) in ALL.items() for e in es if re.search(r'Gate 1|OQ-\d+', e['ruling'] + ' ' + e['why']) and kind(e['ruling']) in ('CHANGE', 'ADD', 'DELETE') and re.search(r'revers|revis|replac|supersed|restor', e['ruling'] + ' ' + e['why'], re.I)]
if revised:
    for a, e in revised:
        A(f"- {e['id']} ({e['title']}): {short(e['why'], 300)}")
else:
    A('None recorded by the researchers.')
A('')
A('## 5. The lead editor\'s own decisions')
A('')
A('Recommendations not adopted, or adjusted:')
A('')
for eid, o in over.items():
    A(f"- {eid}: {'not applied' if o.get('skip') else 'applied with adjusted text'}. {o.get('why', '')}")
A('')
A('Follow-up changes across areas:')
A('')
for e in lead_edits:
    A(f"- {e['id']} ({e.get('section', '')}): {e.get('rationale', '')}")
A('')
A('## 6. Every question, by area')
A('')
A('The full entry for each row (question, what the book said, evidence from each source, reasoning) is in the area\'s memo.')
for a, label in AREAS:
    if a not in ALL:
        continue
    es, _ = ALL[a]
    A('')
    A(f'### {label}')
    A('')
    A(f'Memo: `work/phase3/rulings_{a}.md`. {len(es)} questions.')
    A('')
    A('| Entry | Question | Ruling | Changes play |')
    A('|---|---|---|---|')
    for e in es:
        A(f"| {e['id']} | {short(e['title'], 90)} | {short(e['ruling'], 120)} | {'yes' if e['mech'].lower().startswith('yes') else 'no'} |")
A('')
A('## 7. What could not be settled from the materials')
A('')
A('These are facts about printed components, not rules decisions. Each is stated in the book in the safest form the evidence allows.')
A('')
for a, label in AREAS:
    if a not in ALL:
        continue
    t = ALL[a][1]
    m = re.search(r'^## [^\n]*\(b\)[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
    if m:
        A(f'**{label.split(" (")[0]}.**')
        A('')
        A(m.group(1).strip())
        A('')
A('## 8. Verification after the rulings')
A('')
va = [e for e in verify_edits if e['id'] in applied]
A(f'Once the rulings were applied, two independent readers checked the whole book against itself: every worked example recomputed from the rules as they now stand, '
  f'every table against its text, every statement of a rule against every other statement of the same rule, and the eight added booklets against the entries drawn from them. '
  f'Their reports are `work/phase3/verify_a.md` (chapters 1 to 11, glossary A to M) and `work/phase3/verify_b.md` (chapters 12 to 23, glossary N to Z). '
  f'{len(va)} corrections followed, each an entry in `11_change_log.md` that cites its `VA-` or `VB-` number; '
  f'{sum(1 for e in va if e.get("mechanical"))} of them settle a point the rules had left open and are listed in section 3. The readers\' judgement calls were decided by the lead editor:')
A('')
for e in va:
    if 'judgement call' in e.get('evidence', ''):
        A(f"- {e['id']} ({e.get('section', '')}): {e.get('rationale', '')}")
A('')
(ROOT / '06_final_rulings.md').write_text('\n'.join(L).rstrip('\n') + '\n', encoding='utf-8')

O = []
B = O.append
B('# 14 — Open Issues (Class A)')
B('')
B('Status on 2026-11-11: **no rules question is open.** The 22 lead questions and every item of the per-chapter lists that stood in this file were answered under the author\'s delegation; '
  'the answers, the evidence, and the changes made are in `06_final_rulings.md`, and each change is an entry in `11_change_log.md`. The earlier form of this file is in the repository history, '
  'and the per-chapter lists it was built from remain in `work/phase2a/issues/`.')
B('')
B('What remains are facts about printed components that the supplied files cannot confirm. None blocks play; each is stated in the book in the safest form the evidence allows. They are listed in '
  '`06_final_rulings.md`, section 7. The chief ones:')
B('')
B('- **The Painted World of Ariamis rulebook was not supplied.** Crossbreed Priscilla keeps a short entry that plays her from her cards, and that set\'s share of the card totals rests on a community guide.')
B('- **Printed card values** used in a few worked examples, and whether any enemy data card prints a repeat icon, could not be checked against the cards themselves.')
B('- **Image resolution.** The sources are web exports; see `30_pdf_production_notes.md`.')
(ROOT / '14_open_issues.md').write_text('\n'.join(O) + '\n', encoding='utf-8')
print(f'06_final_rulings.md: {len(L)} lines; {n_items} questions; {n_applied} changes applied ({n_mech} mechanical)')
