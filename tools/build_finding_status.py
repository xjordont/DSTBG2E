#!/usr/bin/env python3
"""Give every audit finding a status from the Phase 2A change log (Class A).
resolved  = cited in the Source line (or body) of a change-log entry that applies it
declined  = listed in an entry that records findings skipped, not applied, or owned elsewhere without change
open      = cited nowhere in the change log
Writes 15_finding_status.csv and prints a summary by severity and tag."""
import csv, re, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(ROOT / '02_audit_table.csv', encoding='utf-8')))
log = (ROOT / '11_change_log.md').read_text(encoding='utf-8')
entries = re.split(r'(?m)^### ', log)[1:]
ID = re.compile(r'\b([A-F]-\d{3}|CMP-\d{4})\b')
applied, declined = collections.defaultdict(list), collections.defaultdict(list)
for e in entries:
    head = e.splitlines()[0]
    ch = head.split(' ')[0]
    is_decline = bool(re.search(r'not applied|skipped|declined|owned elsewhere|findings not applied', head, re.I)) or \
        bool(re.search(r'^- (Before|After|Rationale):.*\b(skipped|not applied|declined)\b', e, re.I | re.M) and re.search(r'OPTIONAL', e))
    for i in set(ID.findall(e)):
        (declined if is_decline else applied)[i].append(ch)
out = []
for r in rows:
    i = r['ID']
    if i in applied: status, where = 'resolved', ' '.join(sorted(set(applied[i])))
    elif i in declined: status, where = 'declined', ' '.join(sorted(set(declined[i])))
    else: status, where = 'open', ''
    out.append({'ID': i, 'Severity': r['Severity'], 'Tag': r['Tag'], 'Status': status, 'Change-log entries': where, 'Location': r['Location'][:90]})
with open(ROOT / '15_finding_status.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
c = collections.Counter((o['Status'], o['Severity']) for o in out)
print('status x severity:', {f'{s}/{v}': n for (s, v), n in sorted(c.items())})
print('open by tag:', collections.Counter(o['Tag'] for o in out if o['Status'] == 'open'))
print('open Blocker/Major:', [o['ID'] for o in out if o['Status'] == 'open' and o['Severity'] in ('Blocker', 'Major')])
