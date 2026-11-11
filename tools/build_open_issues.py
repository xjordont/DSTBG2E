#!/usr/bin/env python3
"""Build 14_open_issues.md (Class A) from the per-chapter issue lists written during Phase 2A.
§1 is the lead editor's short list (work/phase2a/issues/_lead.md); §2 reproduces every chapter's list."""
import glob, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
out = ['# 14 — Open Issues for the Author (Class A)', '',
       'Questions that Phase 2A could not settle from the manuscript, the approved completions or the Gate 1 answers. None blocks the book: every rule in the Class B chapters is definite. Each item names the section that would change.', '',
       '## 1. Decisions the author may wish to revisit', '',
       (ROOT / 'work/phase2a/issues/_lead.md').read_text(encoding='utf-8').strip(), '',
       '## 2. Per-chapter lists', '']
total = 0
for f in sorted(glob.glob(str(ROOT / 'work/phase2a/issues/[0-9][0-9]_*.md'))):
    p = pathlib.Path(f); body = p.read_text(encoding='utf-8').strip()
    body = re.sub(r'^#\s[^\n]*\n', '', body).strip()
    if not body or body == 'None.':
        continue
    num, slug = p.stem.split('_', 1)
    n = len(re.findall(r'^- ', body, re.M)); total += n
    out += [f'### Chapter {num} — {slug.replace("_", " ")} ({n})', '', body, '']
out.insert(4, f'Items in the per-chapter lists: {total}.'); out.insert(5, '')
(ROOT / '14_open_issues.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('14_open_issues.md:', total, 'items')
