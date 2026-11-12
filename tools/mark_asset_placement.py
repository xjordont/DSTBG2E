#!/usr/bin/env python3
"""Record where every asset file is used in the assembled book.

Reads build/book_<edition>.html and layout/book.css and writes work/asset_placement.json:
    {"assets/<kind>/<file>": ["banner, chapter 8", "gallery, end of chapter 1", ...], ...}
Files the build derives (trimmed icons in build/icons, figure crops in build/fig, the logo-free cover crop in
build/tex) are recorded under the asset file they are derived from. tools/build_asset_docs.py reads the result
and sets Status = placed and the real placement in 21_asset_manifest.csv and 22_asset_extraction_log.md.

Usage: python3 tools/mark_asset_placement.py [--edition screen]
"""
import argparse, glob, json, pathlib, re
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIGURE_SOURCES = {pathlib.Path(f['file']).name: f['file']
                  for f in json.loads((ROOT / 'layout/tuning.json').read_text(encoding='utf-8')).get('figures', [])}


def source_of(path):
    """Map a path used by the book to the asset file it is, or is derived from."""
    p = path.lstrip('./')
    while p.startswith('../'):
        p = p[3:]
    name = pathlib.Path(p).name
    if p.startswith('assets/'):
        return p
    if p.startswith('build/icons/'):
        return f'assets/icons/{name}'
    if p.startswith('build/fig/'):
        # a figure is a prepared copy of the source file that layout/tuning.json configures for it
        if name in FIGURE_SOURCES:
            return FIGURE_SOURCES[name]
        for folder in ('diagrams', 'photography', 'art', 'frames'):
            if (ROOT / f'assets/{folder}/{name}').exists():
                return f'assets/{folder}/{name}'
        return f'assets/diagrams/{name}'
    if p.startswith('build/tex/lava'):
        hit = sorted(glob.glob(str(ROOT / 'assets/textures/ast-0142-*')))
        return str(pathlib.Path(hit[0]).relative_to(ROOT)) if hit else None
    return None


def chapter_label(sec):
    if sec is None:
        return 'front matter'
    cid = sec.get('id', '')
    if cid.startswith('ch-'):
        return f'chapter {cid[3:]}'
    if cid.startswith('app-'):
        return f'Appendix {cid[4:].upper()}'
    return cid or 'front matter'


def section_label(el):
    sec = el.find_parent('div', class_='sec')
    h2 = sec.find('h2') if sec else None
    num = h2.find('span', class_='secnum') if h2 else None
    return f'§{num.get_text()}' if num else chapter_label(el.find_parent('section'))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--edition', default='screen'); a = ap.parse_args()
    html = (ROOT / f'build/book_{a.edition}.html').read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    use = {}

    def add(path, where):
        src = source_of(path)
        if src and where not in use.setdefault(src, []):
            use[src].append(where)

    for img in soup.find_all('img'):
        cls = img.get('class') or []
        chap = img.find_parent('section')
        if 'hero' in cls:
            add(img['src'], f'banner, {chapter_label(chap)}')
        elif img.find_parent('div', class_='endpanel'):
            add(img['src'], f'gallery, end of {chapter_label(chap)}')
        elif img.find_parent('div', class_='ik'):
            add(img['src'], 'icon reference page')
        elif 'icon' in cls:
            add(img['src'], f'inline icon, {section_label(img)}')
        elif img.find_parent('figure'):
            add(img['src'], f'figure, {section_label(img)}')
        elif img.find_parent('div', class_='endmark'):
            add(img['src'], 'chapter-end ornament')
        elif img.find_parent('div', class_='ftrule'):
            add(img['src'], 'front-matter rule')
        else:
            add(img['src'], chapter_label(chap))
    # pictures set as backgrounds in inline styles (the painting behind each chapter title)
    for el in soup.find_all(style=True):
        for u in re.findall(r"url\(['\"]?([^'\")]+)['\"]?\)", el['style']):
            sec = el if el.name == 'section' else el.find_parent('section')
            where = 'chapter header' if 'banner' in (el.get('class') or []) else 'background'
            add(u, f'{where}, {chapter_label(sec)}')
    css = (ROOT / 'layout/book.css').read_text(encoding='utf-8')
    role = {'ast-0075': 'folio ornament, every page', 'ast-0143': 'back cover ground', 'lava': 'cover field and chapter banner ground (logo-free crop)'}
    for m in re.finditer(r'url\("?([^")]+)"?\)', css):
        u = m.group(1)
        if '/fonts/' in u:
            continue
        add(u, next((v for k, v in role.items() if k in u), 'stylesheet'))
    # inline icons are used in many sections: keep the first three and count the rest
    out = {}
    for f, w in sorted(use.items()):
        inline = [x for x in w if x.startswith('inline icon')]
        other = [x for x in w if not x.startswith('inline icon')]
        if len(inline) > 3:
            inline = inline[:3] + [f'and {len(inline) - 3} more sections']
        out[f] = other + inline
    missing = [f for f in out if not (ROOT / f).exists()]
    (ROOT / 'work/asset_placement.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{len(out)} asset files placed; {len(missing)} not found on disk {missing[:5]}')


if __name__ == '__main__':
    main()
