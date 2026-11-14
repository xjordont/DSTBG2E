#!/usr/bin/env python3
"""Instantiate static weights from the OFL variable fonts in assets/fonts (Cinzel, Libre Caslon Text),
so that the PDF build embeds true regular and bold cuts rather than synthesised ones."""
import pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'assets/fonts'; OUT = SRC / 'static'; OUT.mkdir(exist_ok=True)
JOBS = [('Cinzel-VF.ttf', 'Cinzel', [(400, 'Regular'), (600, 'SemiBold'), (700, 'Bold')]),
        ('LibreCaslonText-VF.ttf', 'LibreCaslonText', [(400, 'Regular'), (700, 'Bold')]),
        ('LibreCaslonText-Italic-VF.ttf', 'LibreCaslonText', [(400, 'Italic'), (700, 'BoldItalic')])]
def drop_features(path, tags):
    """Remove discretionary and historical ligatures (the st, ct and sp forms) from the cut: the renderer applies
    them in running italic text, which makes keywords such as 'stamina' and 'catalyst' hard to read."""
    from fontTools import subset
    f = TTFont(path)
    keep = sorted({fr.FeatureTag for tbl in ('GSUB', 'GPOS') if tbl in f for fr in f[tbl].table.FeatureList.FeatureRecord} - set(tags))
    opts = subset.Options(); opts.layout_features = keep; opts.glyph_names = True; opts.notdef_outline = True
    opts.name_IDs = ['*']; opts.name_languages = ['*']; opts.hinting = True; opts.legacy_kern = True
    sub = subset.Subsetter(opts); sub.populate(glyphs=f.getGlyphOrder()); sub.subset(f)
    # The italic also files st, ct and sp under standard ligatures: keep only the f-ligatures.
    removed = []
    for lk in f['GSUB'].table.LookupList.Lookup:
        for st in lk.SubTable:
            st = getattr(st, 'ExtSubTable', st)
            if hasattr(st, 'ligatures'):
                for first in list(st.ligatures):
                    kept = [l for l in st.ligatures[first] if first.startswith('f') or len(l.Component) == 0]
                    removed += [l.LigGlyph for l in st.ligatures[first] if l not in kept and '_' in l.LigGlyph]
                    kept += [l for l in st.ligatures[first] if l not in kept and '_' not in l.LigGlyph]
                    if kept: st.ligatures[first] = kept
                    else: del st.ligatures[first]
    f.save(path)
    if removed: print('   ligatures removed:', ', '.join(sorted(set(removed))))


for src, fam, cuts in JOBS:
    for wght, name in cuts:
        f = TTFont(SRC / src)
        axes = {a.axisTag: (a.minValue, a.maxValue) for a in f['fvar'].axes}
        lo, hi = axes['wght']
        inst = instancer.instantiateVariableFont(f, {'wght': max(lo, min(hi, wght))}, inplace=False)
        out = OUT / f'{fam}-{name}.ttf'; inst.save(out)
        drop_features(out, {'dlig', 'hlig'})
        print(out.relative_to(ROOT), out.stat().st_size, f'wght axis {lo:g}-{hi:g}')
