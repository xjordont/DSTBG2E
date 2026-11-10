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
    """Return (chapter, [enclosing H2, enclosing H3]) for manuscript line n, so a finding
    rolls up to every heading level that contains it."""
    ch=h2=h3=None
    for (ln,lvl,txt) in heads:
        if ln>n: break
        if lvl==1: ch, h2, h3 = txt, None, None
        elif lvl==2: h2, h3 = txt, None
        else: h3 = txt
    return ch, [x for x in (h2,h3) if x]
def linenums(s):
    """Line references in any of the agents' formats: 'L945', 'line 945', 'lines 945-950',
    'manuscript.md:945', 'manuscript.md 945 (Gravestones)', 'manuscript.md:1203–1223'."""
    out=[]
    prefixed = re.compile(r'(?:\bL|\bline[s]?\s*|manuscript\.md\s*:?\s*|:)(\d{3,4})(?:\s*[–-]\s*(\d{3,4}))?')
    for m in prefixed.finditer(s):
        for g in (m.group(1), m.group(2)):
            if g:
                v=int(g)
                if 361<=v<=len(lines): out.append(v)
    if out:
        # A reference list such as "manuscript.md 661–667 (components), 1133, 1161 (setup), 939 (scrying)"
        # continues with bare numbers after commas; take those too (years excluded).
        for m in re.finditer(r'(?:,|;)\s*(?:L)?(\d{3,4})(?:\s*[–-]\s*(\d{3,4}))?', s):
            for g in (m.group(1), m.group(2)):
                if g and g not in ('2017','2022'):
                    v=int(g)
                    if 361<=v<=len(lines) and v not in out: out.append(v)
    return out
audit=collections.defaultdict(set); comp=collections.defaultdict(set)
def ingest(path, bucket):
    """Return the number of rows ingested, or None when the source file is absent
    (the corresponding tracker column is then preserved, not blanked)."""
    p=ROOT/path
    if not p.exists(): return None
    n=0
    for row in csv.DictReader(open(p,newline='',encoding='utf-8')):
        nums=linenums(row.get('Location','')+' '+row.get('Evidence',''))
        keys=set()
        for v in nums:
            ch,secs=locate(v)
            if ch:
                keys.add((ch,None))
                for sec in secs: keys.add((ch,sec))
        if not keys:
            # fall back to section-name, then chapter-name, match in Location
            loc=row.get('Location','').lower()
            ch=None
            for (ln,lvl,txt) in heads:
                if lvl==1: ch=txt
                elif len(txt)>3 and txt.lower() in loc: keys.add((ch,txt)); keys.add((ch,None))
            for (ln,lvl,txt) in heads:
                if lvl==1 and txt.lower() in loc: keys.add((txt,None))
        for k in keys: bucket[k].add(row['ID'])
        n+=1
    return n
na=ingest("02_audit_table.csv", audit); ne=ingest("work/audit/E_rows.csv", comp)
if na is None and ne is None:
    print("ABORT: neither 02_audit_table.csv nor work/audit/E_rows.csv exists; tracker left untouched.")
    raise SystemExit(1)
VIRTUAL = {("CHARACTERS","Estus Flask"): (["A-012"], ["CMP-0001"]),
           ("GLOSSARY","(chapter)"): ([], ["CMP-0002"]),
           ("—","Combat Cards"): (["OQ-04 (not in this revision)"], [])}
for k,(a,c) in VIRTUAL.items():
    audit[k].update(a); comp[k].update(c)
tr=(ROOT/"03_coverage_tracker.md").read_text(encoding="utf-8").split("\n")
out=[]; filled=0
for l in tr:
    if l.startswith('| ') and l.count('|')>=8 and not l.startswith('| Chapter'):
        cells=[c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells)==7:
            ch,sec=cells[0],cells[1]
            key=(ch,None) if sec in ('(chapter)','(empty heading)') else (ch,sec)
            if (ch,sec) in VIRTUAL: key=(ch,sec)
            ids=sorted(audit.get(key,set()), key=lambda s:(s.split('-')[0], int(re.sub(r'\D','',s.split('-')[-1]) or 0)))
            cids=sorted(comp.get(key,set()))
            if sec=='(empty heading)': ids=[]
            if na is not None: cells[3]=', '.join(ids)   # preserve column when source absent
            if ne is not None: cells[4]=', '.join(cids)
            if ids or cids: filled+=1
            l='| '+' | '.join(cells)+' |'
    out.append(l)
(ROOT/"03_coverage_tracker.md").write_text('\n'.join(out), encoding="utf-8")
print(f"audit rows={na if na is not None else '(absent, column preserved)'} completion rows={ne if ne is not None else '(absent, column preserved)'} tracker rows annotated={filled}")
