#!/usr/bin/env python3
"""Automated QA for the built rulebook PDF (Phase 2C).
Usage: python3 tools/qa_pdf.py [build/book_screen.pdf] [--edition screen] [--target-pages N] [--report FILE]
Checks: placeholders; external citations and purchaser watermarks in the PDF text; fonts embedded and no fallback
face; internal links resolve; every manuscript passage present; text inside the margins; headings stranded at a
column foot; short columns mid-chapter; page count against the target; every asset marked 'placed' in the manifest
referenced by the assembled HTML; measured characters per line. Exit 1 if any FAIL."""
import csv, glob, json, pathlib, re, subprocess, sys, statistics
import fitz
ROOT = pathlib.Path(__file__).resolve().parent.parent
args = sys.argv[1:]
def opt(name, default):
    return args[args.index(name) + 1] if name in args else default
edition = opt('--edition', 'screen')
pdf_path = pathlib.Path(next((a for a in args if a.endswith('.pdf')), ROOT / f'build/book_{edition}.pdf'))
target = int(opt('--target-pages', json.loads((ROOT / 'layout/tuning.json').read_text()).get('target_pages', 0)) or 0)
report_path = opt('--report', None)
doc = fitz.open(pdf_path)
W, H = doc[0].rect.width, doc[0].rect.height
ML, MR, MT, MB = 46, 46, 52, 50
results = []   # (status, name, detail)
def add(ok, name, detail=''):
    results.append(('PASS' if ok else 'FAIL', name, detail))
def note(name, detail):
    results.append(('INFO', name, detail))

pages_text = [p.get_text() for p in doc]
alltext = '\n'.join(pages_text)
norm = lambda s: re.sub(r'[^a-z0-9]+', '', s.lower())
flat = norm(re.sub(r'-\n', '', alltext))

# 1 placeholders
ph = re.findall(r'\{\{[^}]*\}\}|\[ASSET-[^\]]*\]|@@SUB|\[(?:PROPOSED|TODO|TBD|MECHANICAL CHANGE)[^\]]*\]', alltext)
add(not ph, 'No unresolved placeholders or tags', f'{len(ph)} found: {ph[:5]}' if ph else '')

# 2 external citations (colophon page excepted) and purchaser watermarks
EXT = re.compile(r'(official rule\s?book|original rule\s?book|rule booklet|core rulebook|\bSFG\b|Steam ?Forged|Kickstarter|first edition|\b1E\b|\bV2\b|see page \d+|\bp\.\s?\d+|\bpp\.\s?\d+|google docs|Hollowed Edition|Extended Rules)', re.I)
hits = []
for i, t in enumerate(pages_text, 1):
    if i <= 4:   # the colophon names the rights holders: that one statement is exempt
        t = re.sub(r'Based on Dark Souls: The Board Game by.*?fan work\.', '', t, flags=re.S)
    for m in EXT.finditer(t): hits.append((i, m.group(0)))
add(not hits, 'No external rulebook citation in the PDF text', f'{hits[:6]}' if hits else '')
wm = re.findall(r'Generated for|#SFU|[\w.]+@[\w.]+\.\w+', alltext)
add(not wm, 'No purchaser watermark or e-mail address in the PDF text', f'{wm[:3]}' if wm else '')

# 3 fonts
out = subprocess.run(['pdffonts', str(pdf_path)], capture_output=True, text=True).stdout.splitlines()[2:]
fonts = [(l.split()[0], l.split()[-5]) for l in out if l.strip()]
not_emb = [f for f, emb in fonts if emb != 'yes']
fallback = [f for f, _ in fonts if not re.search(r'Cinzel|Libre-?Caslon', f, re.I)]
synth = [f for f, _ in fonts if re.search(r'Cinzel.*(Oblique|Italic)', f)]
add(not not_emb, 'All fonts embedded', ', '.join(not_emb))
add(not fallback, 'No fallback typeface', ', '.join(fallback))
add(not synth, 'No synthesised italic of the display face', ', '.join(synth))

# 4 internal links
bad_links = n_links = 0
for p in doc:
    for l in p.get_links():
        if l.get('kind') in (fitz.LINK_GOTO, fitz.LINK_NAMED):
            n_links += 1
            if l.get('page', -1) is None or not (0 <= l.get('page', -1) < len(doc)): bad_links += 1
hp = ROOT / f'build/book_{edition}.html'
html = hp.read_text(encoding='utf-8') if hp.exists() else ''
ids = set(re.findall(r'\bid="([^"]+)"', html))
dangling = sorted({h for h in re.findall(r'href="#([^"]+)"', html) if h not in ids})
add(bad_links == 0 and not dangling, 'All internal links resolve', f'{n_links} link annotations; bad {bad_links}; dangling hrefs {dangling[:5]}')

# 5 every manuscript passage present
files = sorted(glob.glob(str(ROOT / '10_manuscript_chapter_*.md'))) + [str(ROOT / '12_glossary.md')]
missing, total = [], 0
def units(text):
    """Probe units: each list item on its own, every other paragraph whole."""
    for para in re.split(r'\n\s*\n', text):
        p = para.strip()
        if not p or p.startswith('|') or p.startswith('#'): continue
        if re.match(r'^\s*(\d+\.|-)\s+', p):
            for item in re.split(r'\n\s*(?=(?:\d+(?:\.\d+)?\.|-)\s+)', p): yield item
        else:
            yield p
for f in files:
    for p in units(pathlib.Path(f).read_text(encoding='utf-8')):
        p = re.sub(r'\{\{icon:[^}]+\}\}', '', p); p = re.sub(r'^\s*(\d+(\.\d+)?\.|-)\s+', '', p)
        p = re.sub(r'[*_`]', '', p)
        words = p.split()
        if len(words) < 5: continue
        total += 1
        probes = [norm(' '.join(words[:9]))[:42], norm(' '.join(words[len(words)//2:len(words)//2 + 9]))[:42]]
        if not any(pr and pr in flat for pr in probes): missing.append((pathlib.Path(f).name, ' '.join(words[:10])))
add(not missing, 'Every manuscript passage is present in the PDF', f'{total} passages checked; missing {len(missing)}: {missing[:4]}')

# 6 geometry: text inside the margins (cover and full-bleed pages excepted)
outside = []
for i, p in enumerate(doc, 1):
    if i == 1: continue
    for b in p.get_text('blocks'):
        x0, y0, x1, y1, txt = b[0], b[1], b[2], b[3], b[4]
        if not str(txt).strip() or b[6] != 0: continue
        if MT - 2 <= y0 and y1 <= H - MB + 2 and (x0 < ML - 3 or x1 > W - MR + 3):
            outside.append((i, round(x0), round(x1), str(txt).strip()[:30]))
add(not outside, 'No text outside the side margins', f'{len(outside)}: {outside[:4]}')

# 7 headings stranded at a column foot; chapter page spans
pm = json.loads((ROOT / f'build/pagemap_{edition}.json').read_text()) if (ROOT / f'build/pagemap_{edition}.json').exists() else []
stranded = [(e['id'], e['page']) for e in pm if e['tag'] in ('h2', 'h3') and e['y'] > H - MB - 34]
add(not stranded, 'No heading within 34 pt of a column foot', f'{stranded[:6]}')
chap_pages = {}
for e in pm:
    if e['tag'] == 'section' and (e['id'].startswith('ch-') or e['id'].startswith('app-')):
        chap_pages.setdefault(e['id'], set()).add(e['page'])

# 8 short columns mid-chapter (not on a chapter's last page)
last_pages = {max(v) for v in chap_pages.values()}
short = []
mid = W / 2
for i, p in enumerate(doc, 1):
    if i <= 4 or i in last_pages: continue
    feet = {'L': 0, 'R': 0}
    for b in p.get_text('blocks') + [(r.x0, r.y0, r.x1, r.y1, 'img', 0, 1) for r in [fitz.Rect(im['bbox']) for im in p.get_image_info()]]:
        x0, y0, x1, y1 = b[0], b[1], b[2], b[3]
        if y1 > H - MB + 2 or y0 < MT - 2: continue
        side = 'L' if x1 <= mid + 4 else ('R' if x0 >= mid - 4 else 'LR')
        for s in side:
            feet[s] = max(feet[s], y1)
    for s in 'LR':
        gap = (H - MB) - feet[s]
        if feet[s] and gap > 60: short.append((i, s, round(gap)))
note('Columns ending more than 60 pt short mid-chapter', f'{len(short)}: {short[:12]}')

# 9 page count
if target:
    lo, hi = round(target * 0.9), round(target * 1.1)
    add(lo <= len(doc) <= hi, f'Page count within 10% of the target ({target})', f'{len(doc)} pages; allowed {lo}-{hi}')
else:
    note('Page count', f'{len(doc)} pages (no target set)')

# 10 manifest against the assembled book: every asset marked placed is really used, and every extracted file
#    that is not used says why (a file under Provenance Review must not be used at all)
man = list(csv.DictReader(open(ROOT / '21_asset_manifest.csv', encoding='utf-8')))
css = (ROOT / 'layout/book.css').read_text(encoding='utf-8')
used_text = html + css
def file_of(r):
    m = re.search(r'\bfile: (assets/\S+?)\.? ', r['Notes'] + ' ')
    return m.group(1) if m else None
def in_book(path):
    name = path.rsplit('/', 1)[-1]
    if path in used_text or f'build/icons/{name}' in used_text or f'build/fig/{name}' in used_text:
        return True
    return 'ast-0142' in name and 'lava_scales_clean' in used_text      # the cover field is a logo-free crop of AST-0142
placed = [r for r in man if r['Status'].strip().lower() == 'placed']
single = [r for r in placed if file_of(r)]
absent = [r['Asset ID'] for r in single if not in_book(file_of(r))]
parents = [r for r in placed if not file_of(r)]
orphan = [r['Asset ID'] for r in parents if not any(s['Asset ID'].startswith(r['Asset ID'] + '.') and s['Status'] == 'placed' for s in man)]
add(not absent and not orphan, 'Every asset marked placed in the manifest is present in the book', f'{len(placed)} placed ({len(single)} files); absent {(absent + orphan)[:8]}')
unplaced = [r for r in man if file_of(r) and r['Status'].strip().lower() != 'placed']
no_reason = [r['Asset ID'] for r in unplaced if not r['Placement (page/chapter)'].startswith('not placed:')]
leaked = [r['Asset ID'] for r in unplaced if in_book(file_of(r))]
held = [r['Asset ID'] for r in man if 'provenance' in r['Licensing'].lower() and file_of(r) and in_book(file_of(r))]
add(not no_reason and not leaked and not held, 'Every extracted file that is not placed states why, and none held for provenance is used',
    f'{len(unplaced)} files not placed; without a reason {no_reason[:6]}; used but not marked {leaked[:6]}; held but used {held[:6]}')

# 11 measured characters per line (body columns)
lens = []
for i, p in enumerate(doc, 1):
    if i < 6 or i % 5: continue
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            x0, x1 = l['bbox'][0], l['bbox'][2]
            if 200 < x1 - x0 < 262:
                lens.append(len(''.join(s['text'] for s in l['spans'])))
if lens: note('Measured line length (full body lines)', f'median {statistics.median(lens):.0f} characters, mean {statistics.mean(lens):.1f}, n={len(lens)}')

fails = [r for r in results if r[0] == 'FAIL']
lines = [f'# PDF QA — {pdf_path.name}', '', f'Pages: {len(doc)} · size {W:.0f} x {H:.0f} pt · links {n_links} · passages {total}', '',
         '| Result | Check | Detail |', '|---|---|---|'] + [f'| {s} | {n} | {str(d).replace("|", "/")[:400]} |' for s, n, d in results]
lines += ['', f'**{"QA PASSED" if not fails else f"QA FAILED ({len(fails)} checks)"}**', '']
txt = '\n'.join(lines)
if report_path: pathlib.Path(report_path).write_text(txt, encoding='utf-8')
print(txt)
sys.exit(1 if fails else 0)
