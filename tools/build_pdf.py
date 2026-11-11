#!/usr/bin/env python3
"""Build the rulebook PDF from the Class B chapter files (Phase 2C).

Usage:
  python3 tools/build_pdf.py [--edition screen|print] [--only NN[,NN...]] [--out PATH] [--html-only]

Pipeline: chapter Markdown -> pandoc (commonmark_x) -> structured HTML (one continuous two-column flow per
chapter; banner; sections; examples; tables; icons; cross-reference links; glossary keyword links) ->
WeasyPrint. Layout decisions made by eye live in layout/tuning.json so that the build is repeatable.
Outputs: build/book_<edition>.html, the PDF, and build/pagemap_<edition>.json (element positions per page).
A chapter file that does not exist yet is skipped with a warning, so partial builds are possible."""
import argparse, glob, json, pathlib, re, subprocess, sys
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
ORDER = ['00'] + [f'{i:02d}' for i in range(1, 24)]
TUNING = json.loads((ROOT / 'layout/tuning.json').read_text(encoding='utf-8')) if (ROOT / 'layout/tuning.json').exists() else {}
TITLE = 'Dark Souls: The Board Game — Second Edition Rulebook'


def chapter_file(num):
    if num == '21':
        p = ROOT / '12_glossary.md'
        return p if p.exists() else None
    m = sorted(glob.glob(str(ROOT / f'10_manuscript_chapter_{num}_*.md')))
    return pathlib.Path(m[0]) if m else None


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def norm_term(s):
    return s.strip().lower().rstrip('.,;:')


def glossary_heads():
    """Map every accepted spelling of a glossary headword to its anchor slug."""
    gp = ROOT / '12_glossary.md'
    heads = {}
    if not gp.exists():
        return heads
    for h in re.findall(r'^\*\*([^*]+)\*\*', gp.read_text(encoding='utf-8'), re.M):
        key = norm_term(h); slug = 'g-' + slugify(key)
        heads[key] = slug
        m = re.match(r'^(.*?)\s*\(([^)]+)\)\s*$', key)
        if m:
            heads[m.group(1).strip()] = slug; heads[m.group(2).strip()] = slug
    return heads


def lookup_term(term, heads):
    t = norm_term(term)
    for cand in (t, t[:-1] if t.endswith('s') else None, t[:-2] if t.endswith('ed') else None, t + 'd',
                 (t[:-1] + 'e') if t else None, t[:-3] if t.endswith('ing') else None, (t[:-3] + 'e') if t.endswith('ing') else None,
                 t[:-2] if t.endswith('es') else None):
        if cand and cand in heads:
            return heads[cand]
    return None


def preprocess(md):
    """Markdown fixes before pandoc: numbered sub-steps (4.1.) become their own paragraph inside the list item."""
    out = []
    for line in md.splitlines():
        m = re.match(r'^(\s{2,})(\d+\.\d+)\.?\s+(.*)$', line)
        if m:
            out += ['', f'    @@SUB:{m.group(2)}@@ {m.group(3)}', '']
        else:
            out.append(line)
    return '\n'.join(out) + '\n'


def pandoc(md):
    r = subprocess.run(['pandoc', '-f', 'commonmark_x', '-t', 'html5', '--wrap=none'], input=md, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit('pandoc failed: ' + r.stderr)
    html = r.stdout
    html = re.sub(r'\{\{icon:([a-z0-9-]+)\}\}', lambda m: icon_tag(m.group(1)), html)
    html = re.sub(r'(<p>)?@@SUB:([\d.]+)@@ ', lambda m: f'<p class="substep"><span class="sn">{m.group(2)}</span> ', html)
    html = html.replace('\u221e', '<span class="sym">\u221e</span>')   # the body face has no infinity sign
    return html


MISSING_ICONS = set()
NO_ENDMARK = set()   # chapters whose closing ornament would otherwise sit alone on a new page
END_FREE = {}         # chapter id -> points of empty page under its closing ornament (measured on the first pass)
NO_PANEL = set()      # chapters whose gallery did not fit after all (verified on the second pass)
PAGE_FOOT = 742.0     # y of the foot of the text block, in points (792 - 50)
SEC_BREAK = {}        # section id -> 'page' | 'column': numbered sections that start a new page or column
SEC_FIXED = set()     # section ids already weighed and left where they fall
PLATES = {}           # section id -> art plate set in the room left before that section's break
NO_PLATE = set()      # section ids whose plate did not fit after all
_SS = TUNING.get('section_starts') if isinstance(TUNING.get('section_starts'), dict) else {}
T_PAGE = float(_SS.get('page', 600))     # a section in the right column with this much column left, or less, starts a new page
T_COL = float(_SS.get('column', 345))    # a section in the left column with this much column left, or less, starts the next column
COL_W = 252.0
PT_PER_PX = 72 / 150  # no image is set larger than 150 ppi allows
_SIZES = {}


def img_size(file):
    if file not in _SIZES:
        from PIL import Image
        with Image.open(ROOT / file) as im:
            _SIZES[file] = im.size
    return _SIZES[file]


def hero_caption(file):
    stem = re.sub(r'^ast-\d+-', '', pathlib.Path(file).stem)
    caps = TUNING.get('captions', {})
    if '/art/' in file or stem in caps:        # paintings carry no caption unless one is given for the file
        return caps.get(stem, '')
    for prefix in ('', 'expansion-miniature-', 'miniature-', 'token-', 'game-tile-'):
        if stem.startswith(prefix) and stem[len(prefix):] in caps:
            return caps[stem[len(prefix):]]
    stem = re.sub(r'^(expansion-)?(miniature-)?(character-)?', '', stem)
    return ' '.join(w.capitalize() for w in stem.split('-'))


def cap_width(file):
    """Width a gallery caption needs on one line (6.1 pt capitals with tracking), up to 104 pt; longer captions wrap."""
    return min(104.0, len(hero_caption(file) or '') * 4.75 + 4)


def end_panel(soup, cid, key):
    """A gallery of product images that fills the empty foot of a chapter's last page. Its rows are sized from
    the room measured on the first pass (END_FREE), and it is anchored to the foot of the text block."""
    spec = TUNING.get('heroes', {}).get(key, {})
    pool = spec.get('end') or []
    free = END_FREE.get(cid, 0)
    avail = free - 22
    if not pool or cid in NO_PANEL or avail < 92:
        return None
    width, pad, cap_h, gap = 520.0, 18.0, 19.0, 12.0
    nrows = spec.get('rows') or (1 if avail < 250 else 2 if avail < 470 else 3)
    if spec.get('caption'):
        avail -= cap_h
    row_h = min((avail - nrows * cap_h - (nrows - 1) * gap) / nrows, float(spec.get('max_row', 178.0)))
    rows, cur, curw = [], [], 0.0
    for f in pool:
        pw, ph = img_size(f)
        dh = min(row_h, ph * PT_PER_PX); dw = pw * dh / ph
        if dw > width - pad:
            dw = width - pad; dh = ph * dw / pw
        cw = max(dw, cap_width(f))        # a cell is as wide as its image or its caption, whichever is wider
        if cur and curw + cw + pad > width:
            rows.append(cur); cur, curw = [], 0.0
            if len(rows) == nrows:
                break
        cur.append((f, dw, dh, cw)); curw += cw + pad
    if cur and len(rows) < nrows:
        rows.append(cur)
    if not rows:
        return None
    if len(rows) > 1:   # share the images evenly between the rows when the even split also fits the measure
        flat = [d for r in rows for d in r]; n = len(rows); q, rem = divmod(len(flat), n)
        even, i = [], 0
        for k in range(n):
            size = q + (1 if k < rem else 0); even.append(flat[i:i + size]); i += size
        if all(r and sum(d[3] + pad for d in r) <= width for r in even):
            rows = even
    total = sum(max(d[2] for d in r) + (cap_h if any(hero_caption(d[0]) for d in r) else 0) for r in rows) + gap * (len(rows) - 1)
    if spec.get('caption'):
        total += cap_h
    panel = soup.new_tag('div', id=f'panel-{cid}'); panel['class'] = 'endpanel'
    spare = free - total - 6
    # a gallery that nearly fills the room stands on the foot of the text block; a smaller one is centred in the room
    panel['style'] = f'margin-top:{max(12.0, spare if spare < 70 else spare * 0.5):.1f}pt'
    for i, r in enumerate(rows):
        row = soup.new_tag('div'); row['class'] = 'prow'
        if i: row['style'] = f'margin-top:{gap}pt'
        caps = any(hero_caption(d[0]) for d in r)
        for f, dw, dh, cw in r:
            cell = soup.new_tag('div'); cell['class'] = 'pf'
            im = soup.new_tag('img', src=f, alt=hero_caption(f) or ''); im['style'] = f'width:{dw:.1f}pt;height:{dh:.1f}pt'
            cell.append(im)
            if caps:
                c = soup.new_tag('div'); c['class'] = 'pc'; c['style'] = f'width:{cw:.0f}pt'; c.string = hero_caption(f) or '\u00a0'
                cell.append(c)
            row.append(cell)
        panel.append(row)
    if spec.get('caption'):
        c = soup.new_tag('div'); c['class'] = ['pc', 'pcall']; c.string = spec['caption']; panel.append(c)
    return panel


def icon_tag(slug):
    p = ROOT / 'assets/icons' / f'{slug}.png'
    if not p.exists():
        MISSING_ICONS.add(slug); return ''
    alt = slug.split('-', 2)[2].replace('-', ' ') if slug.count('-') >= 2 else slug
    return f'<img class="icon" src="build/icons/{slug}.png" alt="{alt} icon">'


def split_h1(md):
    """A file may hold several chapters (the appendices): split before each level-one heading."""
    parts, cur = [], []
    for line in md.splitlines():
        if line.startswith('# ') and cur and any(l.strip() for l in cur):
            parts.append('\n'.join(cur)); cur = []
        cur.append(line)
    parts.append('\n'.join(cur))
    return [p for p in parts if p.strip()]


class Chapter:
    def __init__(self, num, md):
        self.num = num
        self.soup = BeautifulSoup(pandoc(preprocess(md)), 'html.parser')
        h1 = self.soup.find('h1')
        self.h1_text = h1.get_text(' ', strip=True) if h1 else ''
        m = re.match(r'^(\d+)\.\s+(.*)$', self.h1_text)
        a = re.match(r'^Appendix ([A-Z])\.\s+(.*)$', self.h1_text)
        if m:
            self.kind, self.label, self.title = 'chapter', m.group(1), m.group(2); self.id = f'ch-{self.label}'; self.kicker = f'Chapter {self.label}'
        elif a:
            self.kind, self.label, self.title = 'appendix', a.group(1), a.group(2); self.id = f'app-{self.label.lower()}'; self.kicker = f'Appendix {self.label}'
        else:
            self.kind, self.label, self.title = 'front', '', self.h1_text; self.id = 'front'; self.kicker = ''
        self.sections = []   # (id, number, title)
        self.ids = {self.id}

    def structure(self, heads):
        soup = self.soup
        h1 = soup.find('h1')
        if h1:
            h1.extract()
        nodes = [n for n in list(soup.contents) if not (isinstance(n, NavigableString) and not n.strip())]
        lead, secs, cur = [], [], None
        for n in nodes:
            n.extract()
            if isinstance(n, Tag) and n.name == 'h2':
                cur = [n]; secs.append(cur)
            elif cur is None:
                lead.append(n)
            else:
                cur.append(n)
        key = self.num if self.kind != 'appendix' else f'app-{self.label.lower()}'
        flow_cls = ['flow']
        if key in TUNING.get('single_column', []): flow_cls.append('single')
        if key in TUNING.get('ref_chapters', []): flow_cls.append('ref')
        if key in TUNING.get('small_type', []): flow_cls.append('small')
        sec = soup.new_tag('section', id=self.id); sec['class'] = ['chapter', f'ch{key}']
        banner = soup.new_tag('header'); banner['class'] = 'banner'
        badge = soup.new_tag('div'); badge['class'] = ['badge'] + (['letter'] if self.kind == 'appendix' else []); badge.string = self.label
        kt = soup.new_tag('div'); kt['class'] = 'ktitle'
        kick = soup.new_tag('div'); kick['class'] = 'kicker'; kick.string = self.kicker
        nh1 = soup.new_tag('h1'); nh1.string = self.title
        nh1['data-running'] = f'{self.label}  ·  {self.title}' if self.kind == 'chapter' else f'{self.kicker}  ·  {self.title}'
        nh1['data-bookmark'] = f'{self.label}. {self.title}' if self.kind == 'chapter' else f'{self.kicker}. {self.title}'
        kt.append(kick); kt.append(nh1); banner.append(badge); banner.append(kt); sec.append(banner)
        hdr = TUNING.get('heroes', {}).get(key, {}).get('header')
        if hdr:
            # a painting behind the chapter title: the band of the picture is chosen by `pos`, and a dark
            # gradient rises from the foot so that the badge and the title stay legible
            banner['class'] = ['banner', 'art']
            banner['style'] = (f"min-height:{hdr.get('h', 150)}pt;background-image:linear-gradient(to top, rgba(9,8,7,0.94) 0%, rgba(9,8,7,0.66) 30%, "
                               f"rgba(9,8,7,0.12) 68%, rgba(9,8,7,0) 100%), url('{hdr['file']}');background-position:center, {hdr.get('pos', 'center 40%')};"
                               f"background-size:cover, {hdr.get('size', 'cover')};background-repeat:no-repeat, no-repeat")
        hb = None if hdr else TUNING.get('heroes', {}).get(key, {}).get('banner')
        if hb:
            pw, ph = img_size(hb['file']); hw = hb['h'] * pw / ph
            him = soup.new_tag('img', src=hb['file'], alt=''); him['class'] = 'hero'
            him['style'] = f"height:{hb['h']}pt;width:{hw:.1f}pt;right:{hb.get('right', 16)}pt;bottom:{hb.get('bottom', 0)}pt"
            banner['class'] = ['banner', 'has-hero']; banner['style'] = f"padding-right:{hw + hb.get('right', 16) + 12:.0f}pt"
            banner.append(him)
        # a short lead of plain paragraphs sits under the banner, before the flow; anything else joins the flow
        lead_text = ''.join(n.get_text() for n in lead if isinstance(n, Tag))
        # the chapter's in-voice opening (its first plain paragraph) is set as a centred lead under the banner;
        # definitions and rules that precede the first section join the two-column flow
        tags = [n for n in lead if isinstance(n, Tag)]
        first = tags[0] if tags else None
        is_intro = (self.kind == 'chapter' and (secs or key not in TUNING.get('single_column', [])) and first is not None and first.name == 'p' and len(first.get_text()) <= 560
                    and not (first.contents and isinstance(first.contents[0], Tag) and first.contents[0].name == 'strong'))
        if is_intro:
            intro = soup.new_tag('div'); intro['class'] = 'intro'
            intro.append(first.extract())
            sec.append(intro); lead = [n for n in lead if n is not first and not (isinstance(n, NavigableString) and not n.strip())]
        for fig in figures_for(soup, key, 'top'):
            sec.append(fig)
        flow = soup.new_tag('div', id='flow-' + self.id); flow['class'] = flow_cls
        if lead:
            d = soup.new_tag('div'); d['class'] = ['sec', 'lead']
            for n in lead: d.append(n)
            flow.append(d)
        for group in secs:
            h2 = group[0]
            text = h2.get_text(' ', strip=True)
            m = re.match(r'^(\d+\.\d+)\s+(.*)$', text)
            if m:
                sid = 'sec-' + m.group(1).replace('.', '-'); num, title = m.group(1), m.group(2)
                h2.clear(); sp = soup.new_tag('span'); sp['class'] = 'secnum'; sp.string = num; h2.append(sp); h2.append(' ' + title)
            else:
                sid = f'{self.id}-{slugify(text)}'; num, title = '', text
            h2['id'] = sid; self.ids.add(sid); self.sections.append((sid, num, title))
            d = soup.new_tag('div', id='box-' + sid); d['class'] = ['sec'] + ({'page': ['newpage'], 'column': ['newcol']}.get(SEC_BREAK.get(sid), []))
            for n in group: d.append(n)
            plate = PLATES.get(sid)
            if plate and sid not in NO_PLATE and flow.contents:
                flow.contents[-1].append(plate_tag(soup, sid, plate))    # stands at the foot of the section before the break
            for h3 in d.find_all('h3'):
                h3['id'] = f'{sid}-{slugify(h3.get_text(" ", strip=True))}'; self.ids.add(h3['id'])
            flow.append(d)
            for fig in figures_for(soup, sid, 'in'):
                place_in_section(d, fig)
        sec.append(flow)
        for fig in figures_for(soup, key, 'end'):
            sec.append(fig)
        if self.id not in NO_ENDMARK:
            end = soup.new_tag('div', id=f'end-{self.id}'); end['class'] = 'endmark'
            end.append(soup.new_tag('img', src='assets/ornaments/ast-0082-section-divider-knot-rule-knot.png', alt=''))
            sec.append(end)
            panel = end_panel(soup, self.id, key)
            if panel is not None:
                sec.append(panel)
        soup.append(sec)
        self.decorate(heads)
        self.keep_headings()

    def keep_headings(self):
        """A heading and a short block that follows it travel together (WeasyPrint does not always honour
        break-after: avoid at a column foot)."""
        soup = self.soup
        for h in soup.find_all(['h3', 'h4']):
            nxt = h.find_next_sibling()
            if nxt is None or nxt.name in ('h2', 'h3', 'h4') or (h.parent and 'keep' in (h.parent.get('class') or [])):
                continue
            short = len(nxt.get_text()) < 260 and nxt.name in ('p', 'ol', 'ul', 'div')
            if short:
                w = soup.new_tag('div'); w['class'] = 'keep'; h.wrap(w); w.append(nxt.extract())

    def decorate(self, heads):
        soup = self.soup
        # every table row carries an id, so that the page map shows where each row fell (QA: widow and orphan rows)
        for ti, tb in enumerate(soup.find_all('table'), 1):
            for ri, tr in enumerate(tb.find_all('tr')):
                tr['id'] = f'{self.id}-t{ti}-r{ri}'
        is_gloss = self.num == '21'; is_faq = self.num == '22'
        for p in soup.find_all('p'):
            first = next((c for c in p.contents if not (isinstance(c, NavigableString) and not c.strip())), None)
            if isinstance(first, Tag) and first.name == 'em' and first.get_text().strip().lower().startswith('example'):
                box = soup.new_tag('div'); box['class'] = ['example'] + (['short'] if len(p.get_text()) < 430 else [])
                lab = soup.new_tag('span'); lab['class'] = 'exlabel'; lab.string = 'Example'
                first.replace_with(lab); p.wrap(box)
            elif isinstance(first, Tag) and first.name == 'strong':
                label = first.get_text().strip()
                if is_faq and label in ('Q.', 'A.'):
                    p['class'] = 'faq-q' if label == 'Q.' else 'faq-a'
                    lab = soup.new_tag('span'); lab['class'] = 'ql'; lab.string = label[0]; first.replace_with(lab)
                elif is_gloss and label.endswith('.'):
                    p['class'] = 'gloss'; gid = heads.get(norm_term(label))
                    if gid: p['id'] = gid; self.ids.add(gid)
                elif label.endswith('.') and 'substep' not in (p.get('class') or []):
                    p['class'] = (p.get('class') or []) + ['defn']
        for t in soup.find_all('table'):
            rows = t.find_all('tr')
            if len(rows) <= 10: t['class'] = 'nobreak'
            for cell in t.find_all(['td', 'th']):
                cell.attrs.pop('style', None)
                if re.fullmatch(r'[+−\-]?\d+([./:–]\d+)*( → \d+)?|—|-|∞', cell.get_text(strip=True) or ''):
                    cell['class'] = 'num'
            # a header cell above an all-numeric column is centred too
            body = [r.find_all('td') for r in rows if r.find('td')]
            for i in range(max((len(r) for r in body), default=0)):
                col = [r[i] for r in body if i < len(r)]
                if len(col) > 2 and sum('num' in (c.get('class') or []) for c in col) >= 0.6 * len(col):
                    for c in col: c['class'] = 'num'
            for i, th in enumerate(t.find_all('th')):
                col = [r[i] for r in body if i < len(r)]
                if col and all('num' in (c.get('class') or []) for c in col): th['class'] = 'num'
            w = soup.new_tag('div'); w['class'] = 'tablewrap'; t.wrap(w)

    def link(self, all_ids, heads, missing):
        soup = self.soup
        ref = re.compile(r'§(\d+)(?:\.(\d+))?|Appendix ([A-Z])\b')
        for node in list(soup.find_all(string=True)):
            if not isinstance(node, NavigableString) or node.find_parent(['a', 'h1', 'h2', 'h3', 'h4', 'header']):
                continue
            s = str(node)
            if '§' not in s and 'Appendix' not in s:
                continue
            parts, last = [], 0
            for m in ref.finditer(s):
                if m.group(3):
                    target = f'app-{m.group(3).lower()}'
                else:
                    target = f'sec-{m.group(1)}-{m.group(2)}' if m.group(2) else f'ch-{m.group(1)}'
                if target not in all_ids:
                    missing.add((self.h1_text, m.group(0))); continue
                if target == self.id and m.group(3):
                    continue
                parts.append(s[last:m.start()])
                a = soup.new_tag('a', href='#' + target); a['class'] = 'xref'; a.string = m.group(0)
                parts.append(a); last = m.end()
            if parts:
                parts.append(s[last:])
                # two short references side by side ("§16.5, §18.3") stay on one line
                merged, i = [], 0
                while i < len(parts):
                    if (i + 2 < len(parts) and isinstance(parts[i], Tag) and parts[i + 1] in (', ', '; ') and isinstance(parts[i + 2], Tag)
                            and len(parts[i].get_text()) + len(parts[i + 2].get_text()) <= 12):
                        sp = soup.new_tag('span'); sp['class'] = 'xl'
                        sp.append(parts[i]); sp.append(parts[i + 1]); sp.append(parts[i + 2]); merged.append(sp); i += 3
                    else:
                        merged.append(parts[i]); i += 1
                node.replace_with(*[p for p in merged if p != ''])
        for em in soup.find_all('em'):
            if em.find_parent(['a', 'h1', 'h2', 'h3', 'h4', 'header', 'figcaption']):
                continue
            gid = lookup_term(em.get_text(), heads)
            if gid and gid in all_ids:
                par = em.find_parent('p')
                if par is not None and par.get('id') == gid:
                    continue
                a = soup.new_tag('a', href='#' + gid); a['class'] = 'kw'; em.wrap(a)


def figures_for(soup, key, where):
    """Figures placed by layout/tuning.json: {"figures": [{"file":…, "at":"top|end|in", "chapter"/"section":…, "caption":…, "width":…}]}"""
    out = []
    for f in TUNING.get('figures', []):
        if f.get('at') != where:
            continue
        if (where == 'in' and f.get('section') != key) or (where != 'in' and f.get('chapter') != key):
            continue
        fig = soup.new_tag('figure'); fig['id'] = 'fig-' + slugify(pathlib.Path(f['file']).stem)
        if f.get('legend'): fig['class'] = 'legend'
        img = soup.new_tag('img', src='build/fig/' + pathlib.Path(f['file']).name, alt=re.sub(r'<[^>]+>', '', f.get('caption', ''))[:120])
        if f.get('width'): img['style'] = f'width: {f["width"]}'
        fig.append(img)
        if f.get('caption'):
            ctext = re.sub(r'(?<![\w.])(\d{1,2}) (?=[A-Z])', '\\1\u00a0', f['caption'])
            cap = soup.new_tag('figcaption'); cap.append(BeautifulSoup(ctext, 'html.parser')); fig.append(cap)
        if where == 'in':
            fig['data-after'] = str(f.get('after', 1))
            out.append(fig)
        else:
            w = soup.new_tag('div'); w['class'] = 'topfig' if where == 'top' else 'endfig'; w.append(fig); out.append(w)
    return out


def place_in_section(div, fig):
    """Put a column-width figure after the n-th block of its section (never past the section's end)."""
    n = int(fig.attrs.pop('data-after', 1))
    blocks = [c for c in div.children if isinstance(c, Tag) and c.name != 'h2']
    if not blocks or n <= 0:
        div.find('h2').insert_after(fig)
    else:
        blocks[min(n, len(blocks)) - 1].insert_after(fig)


def front_matter(md):
    soup = BeautifulSoup(pandoc(preprocess(md)), 'html.parser')
    parts, cur = {}, None
    title = soup.find('h1').get_text(' ', strip=True)
    for n in soup.contents:
        if isinstance(n, Tag) and n.name == 'h2':
            cur = n.get_text(' ', strip=True); parts[cur] = []
        elif isinstance(n, Tag) and cur:
            parts[cur].append(str(n))
    subtitle = next((k for k in parts if not parts[k]), 'Second Edition Rulebook')
    main, _, rest = title.partition(':')
    cover = f'''<section class="cover"><div class="cscales"></div><div class="ctitle"><div class="c1">{main.strip()}</div><div class="c2">{rest.strip()}</div>
<div class="crule"></div><div class="c3">{subtitle}</div></div><div class="cfoot">An unofficial, non-commercial fan work</div></section>'''
    rule = '<div class="ftrule"><img src="assets/ornaments/ast-0082-section-divider-knot-rule-knot.png" alt=""></div>'
    fore = f'''<section class="front" id="foreword"><div class="foreword"><h1 class="ft">Foreword</h1>{rule}{"".join(parts.get("Foreword", []))}</div>
<div class="colophon">{"".join(parts.get("Colophon", []))}</div></section>'''
    return cover, fore


def contents(chapters):
    rule = '<div class="ftrule"><img src="assets/ornaments/ast-0082-section-divider-knot-rule-knot.png" alt=""></div>'
    rows = []
    for c in chapters:
        label = c.label if c.kind == 'chapter' else c.label
        head = f'<a class="tch" href="#{c.id}"><span class="tn">{label}</span>{c.title}</a>'
        subs = ''.join(f'<a class="ts" href="#{sid}">{(num + " ") if num else ""}{title}</a>' for sid, num, title in c.sections) \
            if c.num not in TUNING.get('toc_no_sections', []) else ''
        rows.append(f'<div class="tc">{head}{subs}</div>')
    return f'<section class="front" id="contents"><h1 class="ft">Contents</h1>{rule}<div class="toc">{"".join(rows)}</div></section>'


ICON_NAMES = {
    'primary-spawn-node': 'Spawn node', 'encounter-level-1': 'Level 1 encounter', 'encounter-level-2': 'Level 2 encounter',
    'encounter-level-3': 'Level 3 encounter', 'skeleton-soldier': 'Skeleton Soldier', 'skeleton-archer': 'Skeleton Archer',
    'giant-skeleton-soldier': 'Giant Skeleton Soldier', 'giant-skeleton-archer': 'Giant Skeleton Archer', 'skeleton-beast': 'Skeleton Beast',
    'necromancer': 'Necromancer', 'treasure-chest': 'Chest', 'barrel': 'Barrel', 'gravestone': 'Gravestone', 'primary-terrain-node': 'Terrain node',
    'trapped-encounter': 'Trapped encounter', 'threat-level': 'Threat', 'taunt': 'Threat (dashboard)', 'behaviour-deck-size': 'Behaviour deck size',
    'block-resist-shield': 'Block and resist values', 'starting-health': 'Health', 'heat-up-point': 'Heat-up point',
    'push-with-damage-satellite-glyph': 'Push with a damage value', 'target-nearest-character': 'Nearest character',
    'enemy-movement-composite-symbol': 'Movement icon', 'turn-90-right': 'Turn 90\u00b0 right', 'turn-90-left': 'Turn 90\u00b0 left', 'turn-around': 'Turn around',
    'enemy-attack-composite-symbol': 'Attack icon', 'area-attack-icon': 'Area attack', 'neutral-boss-arc': 'Neutral arc', 'attack-boss-arc': 'Attack arc',
    'weak-boss-arc': 'Weak arc', 'deal-magical-damage': 'Magical damage', 'one-handed-weapon': 'One-handed weapon', 'weapon-upgrade': 'Weapon upgrade',
    'two-handed-weapon': 'Two-handed weapon', 'armour-upgrade': 'Armour upgrade', 'armour': 'Armour', 'block': 'Block', 'upgrade-slots': 'Upgrade slots',
    'resist': 'Resist', 'black-dice': 'Black die', 'blue-dice': 'Blue die', 'node-attack': 'Node attack and area-of-effect', 'orange-dice': 'Orange die',
    'shaft': 'Shaft', 'shift': 'Shift', 'push-affected-enemies': 'Push', 'attack-range': 'Range', 'repeat-behaviour-or-attack': 'Repeat', 'dodge': 'Dodge',
    'bleed': 'Bleed', 'frostbite': 'Frostbite', 'poison': 'Poison', 'stagger': 'Stagger'}


def icon_reference(chapters):
    """Back-matter page: every icon used in the rules, with its name and the first section that uses it."""
    first = {}
    for c in chapters:
        for img in c.soup.find_all('img', class_='icon'):
            slug = pathlib.Path(img['src']).stem
            sec = img.find_parent('div', class_='sec')
            h2 = sec.find('h2') if sec else None
            first.setdefault(slug, (h2.get('id') if h2 else c.id, (h2.find('span', class_='secnum').get_text() if h2 and h2.find('span', class_='secnum') else '')))
    cells = []
    for slug in sorted(first, key=lambda s: ICON_NAMES.get(s.split('-', 2)[2], s).lower()):
        name = ICON_NAMES.get(slug.split('-', 2)[2])
        if not name: continue
        tid, num = first[slug]
        ref = f' <a class="xref" href="#{tid}">\u00a7{num}</a>' if num else ''
        cells.append(f'<div class="ik"><img src="build/icons/{slug}.png" alt="{name} icon"><span>{name}{ref}</span></div>')
    rule = '<div class="ftrule"><img src="assets/ornaments/ast-0082-section-divider-knot-rule-knot.png" alt=""></div>'
    return f'<section class="front" id="icon-reference"><h1 class="ft">Icon Reference</h1>{rule}<div class="ikgrid">{"".join(cells)}</div></section>'


def back_cover(intro_md):
    """Closing page: the Introduction's opening and closing lines on the dark back-cover ground."""
    paras = [p.strip() for p in re.split(r'\n\s*\n', intro_md) if p.strip() and not p.startswith('#')]
    strip = lambda t: re.sub(r'\(see [^)]*\)', '', re.sub(r'[*_]', '', t)).replace('  ', ' ').replace(' .', '.').strip()
    lead = strip(paras[0]) if paras else ''
    last = strip(paras[-1]) if len(paras) > 1 else ''
    return f'<section class="backcover"><div class="bc"><p class="bc1">{lead}</p><p class="bc2">{last}</p></div></section>'


def plate_tag(soup, sid, plate):
    """Illustrations set in the room a section break leaves at the foot of a column."""
    div = soup.new_tag('div', id='plate-' + sid); div['class'] = 'plate'; div['style'] = f"margin-top:{plate['mt']:.1f}pt"
    for k, it in enumerate(plate['items']):
        im = soup.new_tag('img', src=it['file'], alt=it.get('caption') or '')
        im['style'] = f"width:{it['w']:.1f}pt;height:{it['h']:.1f}pt" + (';margin-top:12pt' if k else '')
        div.append(im)
        if it.get('caption'):
            c = soup.new_tag('div'); c['class'] = 'pc'; c.string = it['caption']; div.append(c)
    return div


def decide_breaks(pm):
    """Weigh, chapter by chapter, the first numbered section not yet weighed. A section that would start part
    way down the right column starts a new page instead, and one that would start low in the left column starts
    the right column, when the room given up is no more than T_PAGE or T_COL. A section already at the head of
    a page or column, or close under it, stays. One new break per chapter per pass, since a break moves
    everything after it. Returns True if a break was added."""
    by_ch = {}; col_top = {}
    for e in pm:
        if e['tag'] == 'h2' and re.match(r'sec-\d+-\d+$', e['id']):
            hs = by_ch.setdefault(e['id'].split('-')[1], [])
            if not hs or hs[-1]['id'] != e['id']:
                hs.append(e)
        elif e['tag'] == 'div' and e['id'].startswith('flow-'):
            col_top.setdefault(e['page'], e['y'])          # where the columns begin on that page
    added = False
    for ch, hs in by_ch.items():
        for i, h in enumerate(hs):
            sid = h['id']
            if i == 0 or sid in SEC_BREAK or sid in SEC_FIXED:
                continue
            left = h['x'] < 300; room = PAGE_FOOT - h['y']
            down = h['y'] - col_top.get(h['page'], 52.0)       # distance below the head of the column
            if down < 90:
                SEC_FIXED.add(sid); continue                    # heads a page or a column already, or nearly
            if not left and room <= T_PAGE:
                SEC_BREAK[sid] = 'page'; added = True; break
            if left and room <= T_COL:
                SEC_BREAK[sid] = 'column'; added = True; break
            SEC_FIXED.add(sid)
    return added


def choose_plates(pm):
    """After the breaks are settled: measure the room left before each break and pick an illustration for it."""
    spec = TUNING.get('plates', {})
    if not spec:
        return False
    last = {}                                # sec box id -> its last fragment
    order = []
    for e in pm:
        if e['tag'] == 'div' and e['id'].startswith('box-'):
            if e['id'] not in last: order.append(e['id'])
            last[e['id']] = e
    used = set(it['file'] for p in PLATES.values() for it in p['items'])
    changed = False
    for sid, kind in SEC_BREAK.items():
        if sid in PLATES or sid in NO_PLATE or 'box-' + sid not in last:
            continue
        i = order.index('box-' + sid)
        if i == 0 or order[i - 1].split('-')[2] != sid.split('-')[1]:      # the section before it, in the same chapter
            continue
        prev = last[order[i - 1]]
        gap = PAGE_FOOT - (prev['y'] + prev['h'])
        if gap < spec.get('min_gap', 104):
            NO_PLATE.add(sid); continue
        ch = '%02d' % int(sid.split('-')[1])
        pool = [(f, 1.25) for f in spec.get('by_chapter', {}).get(ch, [])] + [(f, 1.0) for f in spec.get('pool', [])]
        items, room = [], gap - 10
        while len(items) < spec.get('max_stack', 3):
            best = None
            for f, weight in pool:
                if f in used or not (ROOT / f).exists():
                    continue
                cap = hero_caption(f); avail = room - (13 if cap else 0)
                pw, ph = img_size(f)
                s = min(COL_W / pw, avail / ph, PT_PER_PX * spec.get('enlarge', 1.0))
                dw, dh = pw * s, ph * s
                if dh < spec.get('min_h', 70):
                    continue
                score = dw * dh * weight
                if best is None or score > best[0]:
                    best = (score, f, dw, dh, cap)
            if best is None:
                break
            _, f, dw, dh, cap = best
            items.append({'file': f, 'w': dw, 'h': dh, 'caption': cap}); used.add(f)
            room -= dh + (13 if cap else 0) + 12
            if room < spec.get('min_h', 70) + 30:
                break
        if not items:
            NO_PLATE.add(sid); continue
        total = sum(it['h'] + (13 if it['caption'] else 0) for it in items) + 12 * (len(items) - 1)
        spare = gap - total - 3
        PLATES[sid] = {'items': items, 'mt': max(8.0, spare if spare < 60 else spare * 0.5), 'page': prev['page'], 'left': prev['x'] < 300}
        changed = True
    return changed


_PLAN = {}


def _plan_one(job):
    """Settle the section starts of one chapter by rendering it alone until no break is added (worker process)."""
    num, idx = job
    import wp_patch  # noqa: F401
    from weasyprint import HTML
    part = split_h1(chapter_file(num).read_text(encoding='utf-8'))[idx]
    cid = None
    for _ in range(40):
        ch = Chapter(num, part); ch.structure(_PLAN['heads']); ch.link(_PLAN['all_ids'], _PLAN['heads'], set()); cid = ch.id
        html = ('<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><link rel="stylesheet" href="layout/book.css"></head>'
                f'<body class="screen">{ch.soup}</body></html>')
        doc = HTML(string=html, base_url=str(ROOT) + '/').render()
        if not decide_breaks(pagemap(doc)):
            break
    mine = lambda s: cid and cid.startswith('ch-') and s.split('-')[1] == cid[3:]
    return {k: v for k, v in SEC_BREAK.items() if mine(k)}, {k for k in SEC_FIXED if mine(k)}


def plan_breaks(jobs, heads, all_ids):
    import multiprocessing as mp, logging
    logging.getLogger('weasyprint').setLevel(logging.ERROR)
    _PLAN.update(heads=heads, all_ids=all_ids)
    with mp.get_context('fork').Pool(min(len(jobs), mp.cpu_count() or 1)) as pool:
        for br, fx in pool.map(_plan_one, jobs, chunksize=1):
            SEC_BREAK.update(br); SEC_FIXED.update(fx)


def build(edition='screen', only=None, out=None, html_only=False, _phase='plan', _n=0, reuse=False):
    import make_layout_assets
    if not (ROOT / 'build/tex/lava_scales_clean.jpg').exists() or not (ROOT / 'build/icons').exists():
        make_layout_assets.lava(); make_layout_assets.icons()
    make_layout_assets.figures()
    heads = glossary_heads()
    chapters, cover, fore, jobs = [], '', '', []
    for num in ORDER:
        if only and num not in only:
            continue
        f = chapter_file(num)
        if f is None:
            print(f'  (chapter {num} not drafted yet: skipped)'); continue
        md = f.read_text(encoding='utf-8')
        if num == '00':
            cover, fore = front_matter(md); continue
        for idx, part in enumerate(split_h1(md)):
            ch = Chapter(num, part); ch.structure(heads); chapters.append(ch); jobs.append((num, idx))
    all_ids = set().union(*[c.ids for c in chapters]) if chapters else set()
    state = ROOT / 'build/layout_plan.json'
    if _phase == 'plan' and not html_only:
        if reuse and state.exists():
            # the plan of an earlier build of the same text (the two editions paginate alike)
            st = json.loads(state.read_text(encoding='utf-8'))
            SEC_BREAK.update(st['breaks']); SEC_FIXED.update(st['fixed']); PLATES.update(st['plates']); NO_PLATE.update(st['no_plate'])
            END_FREE.update(st['end_free']); NO_ENDMARK.update(st['no_endmark']); NO_PANEL.update(st['no_panel'])
            return build(edition, only, out, html_only, _phase='verify', _n=_n + 1)
        if TUNING.get('section_starts', True):
            plan_breaks(jobs, heads, all_ids)
        return build(edition, only, out, html_only, _phase='breaks', _n=_n + 1)
    missing = set()
    for c in chapters:
        c.link(all_ids, heads, missing)
    # the Foreword is not a chapter object: its section references are linked here
    def _fore_ref(m):
        target = f'sec-{m.group(1)}-{m.group(2)}' if m.group(2) else f'ch-{m.group(1)}'
        if target in all_ids:
            return f'<a class="xref" href="#{target}">{m.group(0)}</a>'
        if not only:
            missing.add(('Foreword', m.group(0)))
        return m.group(0)
    fore = re.sub(r'§(\d+)(?:\.(\d+))?', _fore_ref, fore)
    intro = chapter_file('01')
    tail = (icon_reference(chapters) + (back_cover(intro.read_text(encoding='utf-8')) if intro else '')) if not only else ''
    body = cover + fore + (contents(chapters) if not only else '') + ''.join(str(c.soup) for c in chapters) + tail
    html = f'''<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><title>{TITLE}</title>
<link rel="stylesheet" href="layout/book.css"></head><body class="{edition}">{body}</body></html>'''
    (ROOT / 'build').mkdir(exist_ok=True)
    # The saved copy sits in build/, one level below the repository root that every asset URL is relative to.
    # Asset URLs are rewritten for it (fragment-only links are left alone, so the contents, cross-references
    # and glossary links still work in a browser). WeasyPrint is given the root as base_url instead.
    saved = re.sub(r'\b(src|href)="(?!#|[a-z]+:|/|\.\./)([^"]+)"', r'\1="../\2"', html)
    saved = re.sub(r"url\('(assets/[^']+)'\)", r"url('../\1')", saved)
    hp = ROOT / f'build/book_{edition}.html'; hp.write_text(saved, encoding='utf-8')
    report = {'edition': edition, 'chapters': len(chapters), 'unresolved_refs': sorted(missing), 'missing_icons': sorted(MISSING_ICONS)}
    if html_only:
        print(json.dumps(report, ensure_ascii=False)); return report
    import wp_patch  # noqa: F401  (column-balancing patch; must precede rendering)
    from weasyprint import HTML
    # Images are embedded at no more than the edition's resolution at their placed size (none is enlarged).
    img_opts = dict(optimize_images=True, dpi=300 if edition == 'print' else 200, jpeg_quality=88)
    doc = HTML(string=html, base_url=str(ROOT) + '/').render(**img_opts)
    pm = pagemap(doc)
    ends = {e['id'][4:]: e for e in pm if e['id'].startswith('end-') and e['tag'] == 'div'}
    again = lambda phase: build(edition, only, out, html_only, _phase=phase, _n=_n + 1)
    if _n < 24 and _phase == 'breaks':
        # Passes 1..k: settle where numbered sections start (one new break per chapter per pass).
        if TUNING.get('section_starts', True) and decide_breaks(pm):
            return again('breaks')
        # Breaks settled: this render is the measuring pass. A closing ornament stranded at a page top is
        # dropped; the room under the others is measured for the galleries, and the room before each break
        # for an illustration.
        stranded = {cid for cid, e in ends.items() if e['y'] < 70}
        NO_ENDMARK.update(stranded)
        END_FREE.clear()
        END_FREE.update({cid: PAGE_FOOT - (e['y'] + e['h']) for cid, e in ends.items() if cid not in stranded})
        plates = choose_plates(pm)
        if stranded or plates or (any(v >= 114 for v in END_FREE.values()) and TUNING.get('heroes')):
            return again('verify')
    elif _n < 24:
        # Verifying passes: a gallery or a plate that slipped to another page or column is withdrawn.
        moved = {e['id'][6:] for e in pm if e['id'].startswith('panel-') and e['id'][6:] in ends and e['page'] != ends[e['id'][6:]]['page']}
        seen = {e['id'][6:]: e for e in pm if e['id'].startswith('plate-')}
        slipped = {sid for sid, pl in PLATES.items() if sid not in NO_PLATE and (sid not in seen or seen[sid]['page'] != pl['page'] or (seen[sid]['x'] < 300) != pl['left'])}
        heads_ = {e['id']: e for e in pm if e['tag'] == 'h2'}
        # a break that no longer does its job (the section would now head a page anyway) is harmless; one that
        # strands a plate alone on a page is caught above
        if (moved - NO_PANEL) or slipped:
            NO_PANEL.update(moved); NO_PLATE.update(slipped)
            return again('verify')
    if not only:
        state.write_text(json.dumps({'breaks': SEC_BREAK, 'fixed': sorted(SEC_FIXED), 'plates': PLATES, 'no_plate': sorted(NO_PLATE),
                                     'end_free': END_FREE, 'no_endmark': sorted(NO_ENDMARK), 'no_panel': sorted(NO_PANEL)}, indent=1), encoding='utf-8')
    doc.metadata.title = TITLE; doc.metadata.authors = ['PittedPanda']; doc.metadata.lang = 'en-GB'
    out = pathlib.Path(out) if out else ROOT / f'build/book_{edition}.pdf'
    doc.write_pdf(str(out), **img_opts)
    report.update(passes=_n + 1, section_breaks={k: sum(1 for v in SEC_BREAK.values() if v == k) for k in ('page', 'column')}, plates=len([s for s in PLATES if s not in NO_PLATE]), no_endmark=sorted(NO_ENDMARK), galleries=sorted(e['id'][6:] for e in pm if e['id'].startswith('panel-')), no_gallery=sorted(NO_PANEL), pages=len(doc.pages), out=str(out.relative_to(ROOT)) if out.is_relative_to(ROOT) else str(out), patch=wp_patch.PATCH_APPLIED)
    (ROOT / f'build/pagemap_{edition}.json').write_text(json.dumps(pagemap(doc), indent=0), encoding='utf-8')
    if not only:
        (ROOT / f'build/report_{edition}.json').write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))
    return report


def pagemap(doc):
    """For every element with an id: page number and box position in points (CSS px x 0.75)."""
    out = []
    def walk(box, pno):
        el = getattr(box, 'element', None)
        if el is not None and el.get('id') and getattr(box, 'element_tag', '').split('::')[0] == el.tag:
            out.append({'id': el.get('id'), 'tag': el.tag, 'page': pno, 'x': round(box.position_x * .75, 1), 'y': round(box.position_y * .75, 1),
                        'h': round(box.margin_height() * .75, 1) if hasattr(box, 'margin_height') else 0})
        for c in getattr(box, 'children', []) or []:
            walk(c, pno)
    for i, page in enumerate(doc.pages, 1):
        walk(page._page_box, i)
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--edition', default='screen', choices=['screen', 'print'])
    ap.add_argument('--only'); ap.add_argument('--out'); ap.add_argument('--html-only', action='store_true')
    ap.add_argument('--reuse', action='store_true', help='reuse the layout plan of the last full build (build/layout_plan.json)')
    a = ap.parse_args()
    r = build(a.edition, set(a.only.split(',')) if a.only else None, a.out, a.html_only, reuse=a.reuse)
    # A full build with an unresolved cross-reference or a missing icon is a failed build: the reference would
    # print as plain text and the icon would be left out. (A partial build cannot resolve other chapters.)
    if not a.only and (r.get('unresolved_refs') or r.get('missing_icons')):
        print('BUILD FAILED: unresolved references or missing icons (see the report above)', file=sys.stderr)
        sys.exit(1)
