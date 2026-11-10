#!/usr/bin/env python3
"""Fill the Audit IDs / Completion ID columns of 03_coverage_tracker.md from
02_audit_table.csv and work/audit/E_rows.csv, by mapping each finding's manuscript
line number (any 'L123' / 'line 123' / 'lines 123-130' token in Location or Evidence)
to the enclosing chapter/section of work/docx/manuscript.md. Usage: python3 tools/update_tracker.py"""
import csv, re, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parent.parent
lines = (ROOT/"work/docx/manuscript.md").read_text(encoding="utf-8").split("\n")
# heading index: list of (line, level, text)
heads=[]; started=False
for i,l in enumerate(lines,1):
    m=re.match(r'^(#{1,3})\s*(.*?)\s*$', l)
    if m:
        txt=m.group(2).replace('*','').strip()
        if txt.upper()=='INTRODUCTION': started=True
        if started and txt: heads.append((i,len(m.group(1)),txt))
def locate(n):
    ch=sec=None
    for (ln,lvl,txt) in heads:
        if ln>n: break
        if lvl==1: ch, sec = txt, None
        else: sec = txt
    return ch, sec
def linenums(s):
    out=[]
    for m in re.finditer(r'(?:\bL|\bline[s]?\s*|:)(\d{3,4})', s):
        v=int(m.group(1))
        if 361<=v<=len(lines): out.append(v)
    return out
audit=collections.defaultdict(set); comp=collections.defaultdict(set)
def ingest(path, bucket):
    p=ROOT/path
    if not p.exists(): return 0
    n=0
    for row in csv.DictReader(open(p,newline='',encoding='utf-8')):
        nums=linenums(row.get('Location','')+' '+row.get('Evidence',''))
        keys=set()
        for v in nums:
            ch,sec=locate(v)
            if ch: keys.add((ch,sec)); keys.add((ch,None))
        if not keys:
            # fall back to chapter-name match in Location
            loc=row.get('Location','').lower()
            for (ln,lvl,txt) in heads:
                if lvl==1 and txt.lower() in loc: keys.add((txt,None))
        for k in keys: bucket[k].add(row['ID'])
        n+=1
    return n
na=ingest("02_audit_table.csv", audit); ne=ingest("work/audit/E_rows.csv", comp)
tr=(ROOT/"03_coverage_tracker.md").read_text(encoding="utf-8").split("\n")
out=[]; filled=0
for l in tr:
    if l.startswith('| ') and l.count('|')>=8 and not l.startswith('| Chapter'):
        cells=[c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells)==7:
            ch,sec=cells[0],cells[1]
            key=(ch,None) if sec in ('(chapter)','(empty heading)') else (ch,sec)
            ids=sorted(audit.get(key,set()), key=lambda s:(s.split('-')[0], int(re.sub(r'\D','',s.split('-')[-1]) or 0)))
            cids=sorted(comp.get(key,set()))
            if sec=='(empty heading)': ids=[]
            cells[3]=', '.join(ids); cells[4]=', '.join(cids)
            if ids or cids: filled+=1
            l='| '+' | '.join(cells)+' |'
    out.append(l)
(ROOT/"03_coverage_tracker.md").write_text('\n'.join(out), encoding="utf-8")
print(f"audit rows={na} completion rows={ne} tracker rows annotated={filled}")
