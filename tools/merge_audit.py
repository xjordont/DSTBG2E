#!/usr/bin/env python3
"""Merge the per-agent audit CSVs (work/audit/*_rows.csv) into 02_audit_table.csv.
Validates the 11-column schema, de-duplicates IDs, normalises severity/tag vocab,
and prints summary counts. Usage: python3 tools/merge_audit.py"""
import csv, glob, sys, collections, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
HEADER = ["ID","Location","Issue type","Severity","Evidence","Current text","Proposed fix","Rationale","Gameplay impact","Tag","Decision needed"]
SEV = {"blocker":"Blocker","major":"Major","minor":"Minor","note":"Note"}
TAG = {"required":"REQUIRED","optional":"OPTIONAL","proposed":"PROPOSED","clean-up":"CLEAN-UP","cleanup":"CLEAN-UP","proposed-systemic":"PROPOSED"}
rows, seen, problems = [], set(), []
for f in sorted(glob.glob(str(ROOT/"work/audit/*_rows.csv"))):
    with open(f, newline="", encoding="utf-8") as fh:
        r = csv.reader(fh); hdr = next(r)
        if [h.strip() for h in hdr] != HEADER:
            problems.append(f"{f}: header mismatch: {hdr}"); 
        for row in r:
            if not any(row): continue
            if len(row) != 11:
                problems.append(f"{f}: {row[0] if row else '?'} has {len(row)} columns"); continue
            row = [c.strip() for c in row]
            if row[0] in seen: problems.append(f"duplicate ID {row[0]} in {f}"); continue
            seen.add(row[0])
            row[3] = SEV.get(row[3].lower(), row[3]); row[9] = TAG.get(row[9].lower(), row[9])
            row[10] = "Y" if row[10].strip().upper().startswith("Y") else "N"
            rows.append(row)
def key(r):
    order = {"Blocker":0,"Major":1,"Minor":2,"Note":3}
    return (r[0][0], order.get(r[3],9), r[0])
rows.sort(key=lambda r: (r[0].split("-")[0], int(''.join(ch for ch in r[0].split("-")[-1] if ch.isdigit()) or 0)))
with open(ROOT/"02_audit_table.csv","w",newline="",encoding="utf-8") as fh:
    w = csv.writer(fh, quoting=csv.QUOTE_ALL); w.writerow(HEADER); w.writerows(rows)
c = collections.Counter(r[3] for r in rows); t = collections.Counter(r[9] for r in rows); a = collections.Counter(r[0].split("-")[0] for r in rows)
print(f"rows={len(rows)} severity={dict(c)} tags={dict(t)} agents={dict(a)} decisions={sum(1 for r in rows if r[10]=='Y')}")
for p in problems: print("PROBLEM:", p)
