#!/usr/bin/env python3
"""Deterministic style enforcement for Class B manuscript files.
Checks: hedge words, Americanisms, second person outside examples, external rulebook
citations / page references, meta tags, and (optionally) undefined keywords vs 12_glossary.md.
Usage: python3 tools/style_check.py 10_manuscript_chapter_*.md 12_glossary.md [--report 13_style_enforcement_report.md]"""
import re, sys, pathlib, datetime
HEDGE = r"\b(should|might|could|reasonably|probably|perhaps|maybe|likely)\b"
AMER = r"\b(armor\w*|behavior\w*|center\w*|favor(?!ite)\w*|color\w*|randomiz\w*|leveling|defense\w*|offense\w*|license(?!d\b)\w*|gray|catalog(?!ue)\w*|analyz\w*|organiz\w*|standardiz\w*|realiz\w*|recogniz\w*|maneuver\w*|jewelry|fulfill\w*|skillful\w*|traveled|canceled|labeled|modeled|plow\w*|practic(e|es)\b(?=\s+(the|a|an)\b)|\w+ization\b|\w+izes?\b|\w+izing\b)\b"
AMER_WHITELIST = {"size","sizes","sized","prize","prizes","seize","seizes","capsize","horizon","citizen","citizens","sizing","seizing"}
EXT = r"(official rule\s?book|original rule\s?book|rule booklet|core rulebook|SFG|Steam ?Forged|Kickstarter|first edition|1E\b|V2\b|see page \d+|p\.\s?\d+|pp\.\s?\d+|google docs|Hollowed Edition|Extended Rules)"
META = r"\[(PROPOSED|HOMEBREW|CLARITY|BALANCE|RULES-BLOAT|ERRATA|MECHANICAL CHANGE|CLEAN-UP|TODO|TBD|ASSET-[^\]]*)\]"
YOU = r"\b(you|your|yours|yourself)\b"
def check(path):
    out = []; in_example = False; in_colophon = False   # the Colophon section may name rights holders
    for n, line in enumerate(pathlib.Path(path).read_text(encoding="utf-8").splitlines(), 1):
        low = line.lower()
        # The second-person exemption covers only a paragraph that opens with "Example"
        # (optionally emphasised) and ends at the first blank line or heading.
        if line.startswith("#"):
            in_colophon = line.lstrip("#").strip().lower() == "colophon"
        if line.strip() == "" or line.startswith("#"):
            in_example = False
        elif re.match(r"^\s*(>\s*)?[*_]*example\b", low):
            in_example = True
        for m in re.finditer(HEDGE, low): out.append((path, n, "hedge", m.group(0), line.strip()))
        for m in re.finditer(AMER, low):
            w = m.group(0)
            if w in AMER_WHITELIST or w.endswith(("size","sizes")): continue
            out.append((path, n, "americanism", w, line.strip()))
        if not in_example and not line.lstrip().startswith(">"):
            for m in re.finditer(YOU, low): out.append((path, n, "second-person", m.group(0), line.strip()))
        if not in_colophon:
            for m in re.finditer(EXT, line, re.IGNORECASE): out.append((path, n, "external-ref", m.group(0), line.strip()))
        for m in re.finditer(META, line): out.append((path, n, "meta-tag", m.group(0), line.strip()))
    return out
def main(argv):
    report = None
    if "--report" in argv:
        i = argv.index("--report"); report = argv[i+1]; argv = argv[:i] + argv[i+2:]
    files = argv[1:]
    viol = []
    for f in files: viol += check(f)
    # keyword coverage: italic terms must have a glossary headword
    gl = [f for f in files if f.endswith("12_glossary.md")]
    if gl:
        heads = set()
        for h in re.findall(r"^\*\*([^*]+)\*\*", pathlib.Path(gl[0]).read_text(encoding="utf-8"), re.M):
            h = h.strip().lower().rstrip(".,;:")          # "**Bonfire.**" -> "bonfire"
            heads.add(h)
            m = re.match(r"^(.*?)\s*\(([^)]+)\)\s*$", h)     # "area-of-effect (aoe)" -> both forms
            if m: heads.add(m.group(1).strip()); heads.add(m.group(2).strip())
        for f in files:
            if f.endswith("12_glossary.md"): continue
            txt = pathlib.Path(f).read_text(encoding="utf-8")
            for n, line in enumerate(txt.splitlines(), 1):
                for m in re.finditer(r"(?<!\*)\*([^*\n]{2,40})\*(?!\*)", line):
                    term = m.group(1).strip().lower().rstrip(".,;:")
                    if term.startswith("example"): continue
                    base = term[:-1] if term.endswith("s") and term[:-1] in heads else term
                    base2 = term[:-2] if term.endswith("ed") and term[:-2] in heads else base
                    if term not in heads and base not in heads and base2 not in heads and term+"d" not in heads and term[:-1]+"e" not in heads:
                        viol.append((f, n, "undefined-keyword", term, line.strip()))
    by = {}
    for v in viol: by.setdefault(v[2], []).append(v)
    lines = [f"# 13 — Style Enforcement Report", "", f"Run: {datetime.datetime.now():%Y-%m-%d %H:%M} — files: {', '.join(files)}", "", f"**Total violations: {len(viol)}**", ""]
    for k in sorted(by):
        lines.append(f"## {k} ({len(by[k])})"); lines.append("")
        lines.append("| File | Line | Match | Context |"); lines.append("|---|---|---|---|")
        for f, n, _, m, ctx in by[k]: lines.append(f"| {f} | {n} | `{m}` | {ctx[:140].replace('|','\\|')} |")
        lines.append("")
    if report: pathlib.Path(report).write_text("\n".join(lines)+"\n", encoding="utf-8")
    print("\n".join(lines[:6]))
    for k in sorted(by): print(f"  {k}: {len(by[k])}")
    return 1 if viol else 0
if __name__ == "__main__": sys.exit(main(sys.argv))
