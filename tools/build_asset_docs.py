#!/usr/bin/env python3
"""Renumber assets sequentially, rename files, and build 22_asset_extraction_log.md,
21_asset_manifest.csv and work/asset_recon_summary.md from the extraction records.

Record files: work/extraction_records_batch1.json and work/extraction_records_icons_final.json (Phase 0;
these define the catalogue order and are renumbered here) and work/extraction_records_phase2b.json
(Phase 2B, written by tools/extract_phase2b.py). Phase 2B records carry the final catalogue Asset ID
of the entry they belong to (`parent`), are attached after the renumbering and never change it: one
record per file (`AST-NNNN` for a single-file asset, `AST-NNNN.k` for one file of a multi-file asset),
file-less records that set a status (`not required`, `BLOCKED`) and `AST-NNNN.Rk` provenance-review items."""
import os, json, csv, re, shutil
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # repo root, checkout-independent
B1=json.load(open('work/extraction_records_batch1.json')); IC=json.load(open('work/extraction_records_icons_final.json'))
P2B_FILE='work/extraction_records_phase2b.json'
P2B=json.load(open(P2B_FILE)) if os.path.exists(P2B_FILE) else []
PAL=json.load(open('work/palette.json'))
AUTH='authorised under owner\'s rights assertion'; PROV='PROVENANCE REVIEW'
TG='DS-TG-Rulebook-Compressed_compressed.pdf'; CORE='DS-Core-Rules-lores.pdf'
def by(pref): return [r for r in B1 if r['id'].startswith(pref)]
def ids(lo,hi): return [r for r in B1 if lo<=int(r['id'][4:])<=hi]
def bbox_s(b): return 'bbox (pt) %s' % ('–'.join([]) if not b else f'x {b[0]}–{b[2]}, y {b[1]}–{b[3]}')
entries=[]
def add(r,placement,notes='',lic=AUTH,status='extracted',region=None):
    e=dict(r); e['placement']=placement; e['notes']=notes; e['lic']=lic; e['status']=status
    if region: e['region']=region
    entries.append(e)
def todo(name,typ,src,page,region,placement,notes,lic=AUTH,fmt='png',dims='—',method='TO EXTRACT',status='TO EXTRACT',designated=True):
    entries.append(dict(id=None,name=name,type=typ,src=src,page=page,region=region,dims=dims,format=fmt,method=method,file=None,placement=placement,notes=notes,lic=lic,status=status,designated=designated))
# ---- G1 logos
L={r['id']:r for r in ids(1,5)}
add(L['AST-0001'],'cover, title page, running footer wordmark (vector master)','Single compound path; the ™ glyph is live text in the PDF and was deliberately excluded. The DARK SOULS wordmark itself is a Bandai Namco trade mark (see Provenance Review); "THE BOARD GAME" line and the circular flourish are SFG lock-up elements.')
add(L['AST-0002'],'cover / title page raster fallback','Alpha keyed from parchment; edge pixels carry a faint parchment fringe — prefer AST-0001 for print.')
add(L['AST-0003'],'cover on dark ground','Derived from AST-0002 by forcing RGB to white; alpha identical.')
add(L['AST-0004'],'front cover (white, vector)','White fill (CMYK 0/0/0/0 in source). Identical outline to AST-0001.')
add(L['AST-0005'],'behind the cover logo as a soft glow layer','Greyscale 1276×629 image placed as a luminosity glow behind the white logo on every cover; use as a mask (screen/add blend).')
# ---- G2 icons
SEC_PLACE={'Encounter Cards':'icon set — encounter card legend / Encounters chapter','Enemy Statistics':'icon set — enemy data card anatomy','Enemy Movement':'icon set — Enemy Turns chapter (movement)','Enemy Attacks':'icon set — Enemy Turns chapter (attacks) and Boss arcs','Equipment Icons':'icon set — Treasure / Equipment chapter','Character Attacks':'icon set — Character Turns chapter','Other Icons':'icon set — inline symbols throughout','Conditions':'icon set — Conditions section'}
for r in IC:
    n=''
    if r['kind']=='vector': n='Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox. '
    else: n='Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead. '
    if 'Block (vs physical)' in r['name'] or 'Resist (vs magic)' in r['name']: n+='Light-grey/cream glyph on parchment: keyed alpha is weak at the shield interior — re-cut from a dark-ground source or vectorise.'
    if 'composite' in r['name']: n+='Whole anatomy diagram kept as one unit; the satellite glyphs are also available separately.'
    if r.get('note'): n+=r['note']
    add(r,SEC_PLACE[r['section']],n.strip(),region=f"back-cover key panel, section “{r['section']}”, {bbox_s(r['bbox_pt'])}")
todo('2017-edition enemy icons: Hollow Soldier, Crossbow Hollow, Large Hollow Soldier, Silver Knight Swordsman, Silver Knight Greatbowman, Sentinel','icon',CORE,40,'back-cover key, “Encounter cards” column 3 (39×39 px rasters, pre-composited onto parchment, no soft mask)','icon set — core-set enemies (needed if the 2E book keeps the 2017 roster)','Only sources are flattened 39 px rasters (work/pdfimages/Core_p40_rgba/005–010) or the 400 dpi render (assets/diagrams/… -2017.png). Re-cut from the 400/600 dpi render with parchment keying as done for the 2022 set.')
todo('Trapped-encounter sword icon (2017 horizontal variant)','icon',CORE,40,'key panel, 91×39 px raster #032','icon set — alternative trap glyph','2022 edition replaced it with the three-spear trap icon (extracted). Keep for reference only.')
todo('Mini-boss (standard) and Main-boss (advanced) skull icons','icon',TG,5,'“Bosses” heads: skull-in-ring icons above Black Knight / Gravelord Nito (rasters with masks, p.5 #150 region)','icon set — Boss Encounters chapter','Also on Phantoms p.6 (Summon icons) and Explorers p.4; cut from a 600 dpi render of TG p.5.')
todo('Mega-boss icon (dragon silhouette in flame ring)','icon','DS-BDK-Rules-web.pdf',11,'Mega Boss Data Cards call-out 8; also on p.4 beside the Kalameet miniature','icon set — Mega Boss chapter','Render BDK p.11 at 600 dpi and key against parchment; also present on EC p.11 (chariot variant).')
todo('Expansion set symbols (Darkroot wolf, Iron Keep helm, Explorers chest, BDK dragon, EC chariot, Phantoms, Characters) and the “universal” DS globe icon','icon','DS-Darkroot-Rules-web.pdf',2,'Introduction paragraphs (universal icon inline, ~9 pt) and card corner set symbols on contents pages','icon set — set-symbol legend in the components appendix','Inline glyphs are tiny in the rulebooks; cards on the contents pages show them at ~12 pt. Needs 1200 dpi render crops or redraw as vectors.')
todo('Invader and Summon token icons (Phantoms): 14 invader portraits + 10 summon portraits in rings','icon','DS-Phantoms-Rules-lores.pdf',10,'“Game Setup with Invader Encounters” token wheel (12 tokens) and p.4–5 miniature call-outs','icon set — Phantoms module (if included)','Crop from 600 dpi render of Phantoms p.10; tokens are dark discs with white glyphs.')
todo('Language flag icons (EN/FR/DE/IT/ES)','icon','DS-Darkroot-Rules-web.pdf',2,'Introduction, inline','not needed','Not designated — listed for completeness.',designated=False,status='TO EXTRACT')
# ---- G3 ornaments
O={r['id']:r for r in ids(10,18)}
add(O['AST-0010'],'rule terminals on chapter titles, folios, table corners','12 paths; renders cleanly at any size.')
add(O['AST-0011'],'raster fallback for the knot','Keyed from parchment at 2400 dpi; black only.')
add(O['AST-0012'],'corners of example boxes, caption frames and art frames','12 paths. In the 2022 book this diamond replaces the knot on example boxes; the 2017 book uses it on art frames too.')
add(O['AST-0013'],'raster fallback for the compass corner','')
add(O['AST-0014'],'chapter-opener title treatment (place title text in the gap)','Rules are 0.5 pt hairlines; knots 11.8 pt square; gap for a title of ~180 pt. Title text itself removed by the crop tool.')
add(O['AST-0015'],'raster version of the left half of the title rule (mirror for right)','')
add(O['AST-0016'],'running footer / folio treatment','Gap in the rule is where the page number sits (OptimusPrinceps ~9 pt).')
add(O['AST-0017'],'section break inside a chapter (between lore and rules text)','From p.3 introduction: separates the italic lore block from the rules intro.')
add(O['AST-0018'],'raster fallback of AST-0017','')
# ---- G4 frames
F={r['id']:r for r in ids(20,21)}
add(F['AST-0020'],'example / sidebar box frame (scale to fit)','Vector template: four compass corners, four 0.5 pt rules inset 6 pt from the corners; the raster icons that sat inside were dropped by the tool. Resize by moving corners, not scaling strokes.')
add(F['AST-0021'],'tables (cost tables, turn-order tables)','Vector template with knot corners; the 2022 book uses this for all small tables. Text removed; row rules kept.')
todo('Large art frame: compass corners + hairline rules around full-column illustrations','frame',TG,7,'vector frame around the p.7 full-page illustration (corners at ~(63,42) (587,42) (63,775) (587,775) pt)','illustration frames / chapter-opener art','Cut with tools/svg_crop.py from a pdftocairo SVG of TG p.7 (bbox 55,35,595,785); all art frames in both books use this construction.',fmt='svg')
todo('Equipment card frame (charcoal ground, gold corner ornament, parchment text box, stat column)','frame',TG,10,'Shortbow card, 248×372 px raster at 150 ppi (p.10 image #454)','card-style callouts; appendix card anatomy','Embedded card images are ≤372 px — too small for print reuse. Request original card artwork from the owner or rebuild the frame as vector from the anatomy diagram AST-? (equipment card anatomy).',status='BLOCKED')
todo('Encounter card frame (parchment card with dark banner, node map area)','frame',TG,16,'Grave Matters card, 584×1000 px raster at 300 ppi (p.16 image #624)','encounter-card style callouts','Best-resolution card raster in the set (1000 px tall); crop via pdfimages -png -f 16 -l 16 and composite with its soft mask.')
todo('Enemy / boss data card frame and behaviour card frame','frame',TG,24,'Skeleton Soldier data card (p.24 image #689/690), Gravelord Nito data card (p.28 #782 653×912), Death\'s Embrace behaviour card (p.28 #781 483×656)','enemy chapter card callouts','Composite from pdfimages output (image + smask) — 300 ppi sources exist for the two p.28 cards.')
todo('Card backs: treasure (orange ring), encounter level 1/2/3 (blue/purple ring), event card back, mini/main boss summon backs','frame',TG,6,'“Cards” section of Game Contents (p.6) and core p.6/p.9','appendix component list','Small rasters (~130–300 px); photography-grade only. Extract via pdfimages p.6.')
# ---- G5 diagrams
D={r['id']:r for r in ids(40,60)}
dp={'AST-0040':('Characters chapter — dashboard anatomy','Includes raster dashboard (1019×685 + 1019×806 px in PDF) and vector numbered call-outs (gold circles). Text labels sit outside the crop.'),
 'AST-0041':('Treasure chapter — equipment card anatomy','Card raster is only 248×372 px in the PDF; call-outs are vector. For a 2E card anatomy, rebuild the card and reuse the call-out style.'),
 'AST-0042':('Campaign Dashboard chapter','Two 979×250 px rasters at 150 ppi plus vector call-outs.'),
 'AST-0043':('Encounters chapter — encounter card anatomy','Card raster 584×1000 px at 300 ppi — reusable.'),
 'AST-0044':('Enemy Turns chapter — enemy data card anatomy','Card raster 372×520 px at 150 ppi.'),
 'AST-0045':('Enemy Turns chapter — movement symbol legend','Fully vector in the PDF; SVG available via svg_crop of tg_p24.svg with the same bbox.'),
 'AST-0046':('Enemy Turns chapter — attack symbol legend','Fully vector; SVG available via svg_crop of tg_p25.svg.'),
 'AST-0047':('Boss Encounters chapter — boss data card anatomy','Card raster 653×912 px at 300 ppi.'),
 'AST-0048':('Boss Encounters chapter — behaviour card anatomy','Card raster 483×656 px.'),
 'AST-0049':('Boss Encounters chapter — arcs','875×811 px raster at 300 ppi: boss base with X-arcs over tile with node colour overlay.'),
 'AST-0050':('Boss Encounters chapter — arcs','875×834 px raster at 300 ppi.'),
 'AST-0051':('Boss Encounters chapter — base markings','Photo of a boss model base (275×182 px raster).'),
 'AST-0052':('Boss Activations chapter — worked example','Six tile panels with behaviour-card icons; whole-page specimen at 300 dpi (also usable as a layout model for worked examples).'),
 'AST-0053':('Character Turns chapter — movement example','Tile raster with vector arrows; 884×360 px source.'),
 'AST-0054':('Campaign Dashboard chapter — getting underway','Composite of encounter track strip, party token and card.'),
 'AST-0055':('Characters chapter (2017 variant, reference)','2017 board layout; superseded by AST-0040 but useful for comparison.'),
 'AST-0056':('Bonfire chapter (2017 only — tile not in 2022 set)','788×788 px tile raster with vector call-outs 1–6.'),
 'AST-0057':('Treasure chapter (2017 variant, reference)','Fallback bbox used (image object not isolated by pdfplumber); verify crop before use.'),
 'AST-0058':('Boss Encounters chapter (2017 variant)','2017 arc diagram with coloured node highlights.'),
 'AST-0059':('reference appendix / back cover','Full legend panel; individual icons extracted as the icon set above. Panel bbox auto-detected from the bright region.'),
 'AST-0060':('reference appendix (2017 variant)','2017 legend including 2017-only enemy icons; see icon TO EXTRACT entries.')}
for k in sorted(D): add(D[k],*dp[k])
todo('Encounter setup worked example (The Forgotten) — card + tile with placed tokens','diagram',CORE,18,'framed example box, right-hand page (~x 40–585, y 395–830 pt)','Encounters chapter — setup example','Crop from a 400 dpi render of core p.18; frame uses compass corners.')
todo('Node adjacency diagram (green highlighted nodes)','diagram',TG,11,'“Movement” example box lower-left (~x 60–300, y 560–780 pt); 875×875 px tile raster','Tiles and Nodes chapter','Render TG p.11 at 400 dpi and crop.')
todo('Range / doorway diagram (tile with arrow through door)','diagram',TG,11,'right column box (~x 311–521, y 183–285 pt), 438×213 px raster','Tiles and Nodes chapter','')
todo('Timer track diagram (0–8 track with hourglass marker)','diagram',TG,18,'top of page (~x 55–585, y 95–230 pt)','Encounters chapter — timer track','')
todo('Equipment modifier strip ([0] 1 +1 / [3] 2 +1)','diagram',TG,21,'example box top-left (~x 60–305, y 92–175 pt), 884×360 px raster','Character Turns chapter — modifiers','')
todo('Enemy attack dice resolution strip (attack 5 → dice → damage cubes)','diagram',TG,25,'example box left column (~x 60–305, y 455–545 pt)','Enemy Turns chapter','Vector + small rasters.')
todo('Mega-boss game board (round Chariot arena; Kalameet forest board)','diagram','DS-EC-Rules-Web.pdf',5,'p.5 top (board raster 846×1245 region) and BDK p.5','Mega Boss chapter (if included)','SFG tile art; crop via pdfimages.')
# ---- G6 art
A={r['id']:r for r in ids(80,81)}
add(A['AST-0080'],'cover concept reference (texture + logo); 2E cover to be re-composed','Composition only: texture (AST-0033) + logo (AST-0004).')
add(A['AST-0081'],'HOLD — not to be placed until provenance is cleared','Gravelord Nito artwork is FromSoftware/Bandai Namco licensed art reproduced on the SFG cover; the owner\'s assertion covers the SFG PDF but the lead must decide whether licensed third-party key art is in scope.',lic=PROV,status='BLOCKED')
for name,src,page,region in [
 ('Firelink-style bonfire with seated knight (full-page painting)',TG,14,'right column illustration, ~x 385–585, y 470–790 pt'),
 ('Knight resting at bonfire among ruins (full-page painting)',TG,31,'~x 55–585, y 150–790 pt (also core p.31)'),
 ('Graveyard and ruined tower under storm sky (full-page painting)',TG,32,'~x 55–585, y 270–790 pt (also core p.32)'),
 ('Anor Londo spires at sunset (full-page painting)',TG,23,'full page'),
 ('Black Knight with greatsword in flame light (character key art)',TG,19,'~x 60–300, y 450–790 pt (also core p.26)'),
 ('Cathedral interior with light shafts (concept painting)',TG,9,'~x 330–585, y 300–790 pt (also core p.19)'),
 ('Gravelord Nito on his throne / Tomb of Giants (concept painting)',TG,15,'~x 55–585, y 150–790 pt'),
 ('Chosen Undead knight in dark forest (2017 cover-style key art)',CORE,38,'full page'),
 ('Ashen One with coiled sword (Dark Souls III key art)',CORE,36,'~x 150–445, y 360–790 pt'),
 ('Environment concept sketches: Undead Burg, Sen\'s Fortress, Anor Londo, Lothric, Darkroot, Iron Keep, Lost Bastille etc.',CORE,35,'section thumbnails on p.35/37 and on every expansion campaign page'),
 ('Expansion cover key art (Phantoms knight, Darkroot Artorias/Hydra lake, Iron Keep gate, Explorers Pursuer, Kalameet, Executioner\'s Chariot)','DS-*-Rules-*.pdf',1,'cover art rasters 1754×2551 (300 ppi) or ~850×1245 (150 ppi)')]:
    todo(name,'art',src,page,region,'none until cleared','FromSoftware / Bandai Namco concept or key art reproduced under SFG\'s licence. Not extracted.',lic=PROV,status='BLOCKED',method='NOT EXTRACTED — provenance',designated=False)
# ---- G7 photography
for name,src,page,region,place,notes in [
 ('Miniature renders, 2022 core: Cleric, Pyromancer, Thief; Giant Skeleton Archer/Soldier, Necromancer, Skeleton Archer/Beast/Soldier; Black Knight; Gravelord Nito',TG,4,'Game Contents pp.4–5: grey resin renders with drop shadows (CMYK rasters 457–666 px with soft masks)','Components appendix / chapter openers','pdfimages -png -f 4 -l 5 then composite with masks (tools/composite_pdfimages.py already produced 216 composites for p.6 as a test). SFG sculpts — clean.'),
 ('Token and terrain photography set (wound/soul tokens, luck, heroic action, estus, ember, aggro, party, condition tokens, spark dial, chest, gravestone, barrel, shrine, lever, torch, trap, skeleton ball, Patches, enemy tokens)',TG,6,'“Tokens and Terrain Elements” rows (146 masked rasters, 93–284 px)','Components appendix; inline token references','Already split to RGBA in work/pdfimages/TG_p06_rgba/ (unlabelled); needs naming pass using the p.6 captions.'),
 ('Game tile photography (4 double-sided tiles; 2017: 6 exploration + bonfire + boss tiles)',TG,6,'p.6 tile fan (1389×271 + 1004×166 px); core p.7 tile grid','Tiles chapter','SFG tile art; low-res in PDF (≤1389 px). Larger single-tile rasters exist on TG p.11 (875×875) and core p.13 (788×788).'),
 ('Campaign board photograph (full strip)',TG,6,'bottom of p.6, 1x Campaign board (1389×271 px)','Campaign Dashboard chapter','Higher-res halves on p.13 (979×250 each).'),
 ('Character dashboard photograph (clean, no call-outs)',TG,8,'1019×685 and 1019×806 px rasters at 150 ppi','Characters chapter','pdfimages -png -f 8 -l 8 → images #380/#382 + masks #379/#381.'),
 ('Dice photography (black, blue, orange, green)',TG,6,'“Dice” group (4 masked rasters ~452×452 px)','Combat chapter','Also core p.7 (2017 set with green dodge dice).'),
 ('Card fan photographs (encounter cards, event cards, treasure decks)',TG,6,'“Cards” and “Treasure Deck” groups','Components appendix','Low-res; decorative only.'),
 ('Expansion miniature renders (Sif, Artorias, Mushroom Parent/Child, Smelter Demon, Sir Alonne, Pursuer, Mimic, Kalameet, Executioner\'s Chariot, invaders, summons)','DS-*-Rules-*.pdf',4,'Contents pages of each expansion (CMYK 300 ppi rasters up to 1776×3000 px in Phantoms/BDK)','Expansion module openers','Phantoms p.4–5 and BDK p.4 have the largest renders.')]:
    todo(name,'photography',src,page,region,place,notes)
# ---- G8 textures
T={r['id']:r for r in ids(30,35)}
add(T['AST-0030'],'master page background (place as a spread, 629×811 pt per page)','5174×3378 px = 2 × 629.3 pt at 300 ppi exactly; CMYK (U.S. Web Coated SWOP) in source, converted to sRGB by pdfimages. Left page carries the dark leather gutter; right page the page-block edge. Also present on p.1 (cover) as 1312×1690 for the dark cover.')
add(T['AST-0031'],'right-hand (recto) page background','')
add(T['AST-0032'],'left-hand (verso) page background','')
add(T['AST-0033'],'cover ground, chapter-opener backdrops','Credited "Texture Design: Alex Cairns" in the 2017 credits block — SFG-originated, not FromSoftware art. 150 ppi: at A4 it prints at ~106 ppi; upscale or re-texture for print.')
add(T['AST-0034'],'back-cover ground / dark sidebar ground','Panel is baked in (centre luminance ≫ edges); crop the dark border strips for a seamless dark stone texture.')
add(T['AST-0035'],'low-res alternative background (2017 RGB export)','Keep only as colour reference; AST-0030 supersedes.')
todo('Card text-box parchment fill (worn cream paper)','texture',TG,16,'inside the encounter card raster (p.16 #624, 584×1000 px) and equipment cards','card-style callout fills','Crop a text-box area from the composited encounter card raster.')
todo('Dashboard stone/parchment panel texture','texture',TG,8,'dashboard raster 1019×685 px','sidebar fills','')
todo('Tile floor textures (flagstone, dirt, bone pit)','texture',TG,11,'875×875 px tile raster','backgrounds for example diagrams','')
# ---- G9 specimens
S={r['id']:r for r in ids(70,77)}
sp={'AST-0070':('style guide — table styling','Caslon regular at ~8.5 pt in cells, hairline rules, knot corners.'),
 'AST-0071':('style guide — chapter title','Title size recorded in method; OptimusPrinceps caps, letter-spaced, centred between rules.'),
 'AST-0072':('style guide — body text','Adobe Caslon Pro Regular with Bold run-in heads; sizes recorded in method (8.5–9 pt range).'),
 'AST-0073':('style guide — sub-heads','OptimusPrinceps small caps ~13 pt, centred.'),
 'AST-0074':('style guide — captions','Caslon Italic ~8 pt, set as a hanging caption beside diagrams.'),
 'AST-0075':('style guide — folio','Page number in OptimusPrinceps ~9 pt within the footer rule gap.'),
 'AST-0076':('style guide — cover subtitle','OptimusPrinceps SemiBold, white, tracked; used for every expansion title on covers.'),
 'AST-0077':('style guide — lore block','Italic lore paragraphs open each chapter/expansion; measure ~330 pt, ragged right.')}
for k in sorted(S): add(S[k],*sp[k])
# ---- renumber & rename
n=0
for e in entries:
    n+=1; new=f'AST-{n:04d}'
    if e.get('file'):
        d,fn=os.path.split(e['file']); fn2=re.sub(r'^(ast-\d{4}|ico-\d{3})-',new.lower()+'-',fn)
        dst=os.path.join(d,fn2)
        if fn2!=fn:
            if os.path.exists(e['file']):
                os.rename(e['file'],dst)          # first run: rename the extracted file
            # already renamed by a previous run: record the destination; the existence
            # check below still fails loudly if neither path exists
            e['file']=dst
    e['old_id']=e.get('id'); e['id']=new
missing=[e['file'] for e in entries if e.get('file') and not os.path.exists(e['file'])]
assert not missing, missing
# ---- rewrite embedded cross-references (notes, placement, method…) from the pre-renumber IDs
idmap={e['old_id']:e['id'] for e in entries if e.get('old_id')}
def remap(s): return re.sub(r'AST-\d{4}', lambda m: idmap.get(m.group(0), m.group(0)), s) if isinstance(s,str) else s
for e in entries:
    for f in ('notes','placement','method','region','name','note'):
        if e.get(f): e[f]=remap(e[f])
TG_COVER=next((e['id'] for e in entries if str(e.get('name','')).startswith('2022 Tomb of Giants cover art')),'(see catalogue)')
# ---- Phase 2B: attach the later extraction records to their catalogue entries by final Asset ID
def _long(d):
    m=re.match(r'(\d+)×(\d+)',d or ''); return max(int(m.group(1)),int(m.group(2))) if m else None
def _subkey(r):
    k=r['id'].partition('.')[2]; return (1,int(k[1:])) if k.startswith('R') else (0,int(k or 0))
byid={e['id']:e for e in entries}
for e in entries: e['sub']=[]; e['review']=[]; e['p2b']=None
for r in sorted(P2B,key=lambda r:(r['parent'],_subkey(r))):
    e=byid[r['parent']]
    if r.get('file'):
        assert os.path.exists(r['file']), r['file']
        e['sub'].append(r)
    elif r.get('status')=='PROVENANCE REVIEW': e['review'].append(r)
    else: e['p2b']=r                       # status-only record (not required / BLOCKED) with its reason
for e in entries:
    sub,ov=e['sub'],e['p2b']
    if not sub and not ov: continue
    e['p0_notes']=e['notes']               # Phase 0 note is kept verbatim after the Phase 2B note
    new=[]
    if len(sub)==1 and sub[0]['id']==e['id']:
        r=sub[0]; e.update(file=r['file'],dims=r['dims'],format=r['format'],method=r['method'],status='extracted')
        e['p0_region']=e.get('region')
        if r.get('bbox_pt'): e['bbox_pt']=r['bbox_pt']
        if r.get('notes'): new.append(r['notes'])
        e['sub']=[]; e['single']=r
    elif sub:
        ls=[_long(r['dims']) for r in sub if _long(r['dims'])]
        e['status']='extracted'
        e['dims']=f"{len(sub)} file{'s' if len(sub)>1 else ''}; "+((f"{min(ls)}–{max(ls)}" if min(ls)!=max(ls) else f"{ls[0]}")+" px on the long side" if ls else 'vector')
        d,_=os.path.split(sub[0]['file']); stem=re.match(r'(ast-\d{4})-',os.path.basename(sub[0]['file'])).group(1)
        e['files_note']=(f"{d}/{stem}-*.{sub[0]['format']} ({len(sub)} files, listed as sub-entries {sub[0]['id']} to {sub[-1]['id']})" if len(sub)>1 else f"{sub[0]['file']} (sub-entry {sub[0]['id']})")
        e['method']='Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file'
        pages=sorted({(r['src'],r['page']) for r in sub})
        new.append('Phase 2B extraction, one file per subject from '+'; '.join(f"{s} p.{p}" for s,p in pages[:12])+('.' if len(pages)<=12 else ' and others.'))
    if ov:
        e['status']=ov['status']; new.insert(0,ov['reason'])
        if not sub: e['method']=f"{ov['status']} (Phase 2B decision)"
    if e['review']: new.append(f"{len(e['review'])} related candidate(s) held for provenance review: see Provenance Review, section F.")
    e['p2b_note']=' '.join(new)
    e['notes']=(e['p2b_note']+(' Phase 0 note: '+e['p0_notes'] if e['p0_notes'] else '')).strip()
json.dump(entries,open('work/asset_catalogue_final.json','w'),indent=1,default=str)
# ---- final usage: where each file is placed in the assembled book (work/asset_placement.json is written by
# tools/mark_asset_placement.py from the built HTML and the stylesheet; absent before the first build)
PLACED=json.load(open('work/asset_placement.json')) if os.path.exists('work/asset_placement.json') else {}
WHY_NOT={'logo':'the wordmark is used nominatively only and the title is set in the display face (Gate 1 OQ-33)',
 'icon':'no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)',
 'diagram':'reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate',
 'ornament':'reserve ornament; the book uses the knot square and the knot rule',
 'texture':'reserve texture','photography':'reserve image, or a component these rules do not use',
 'frame':'reference for the stylesheet; boxes and tables are drawn in CSS','typographic specimen':'reference for the type scale',
 'art':'held under Provenance Review (Gate 1 OQ-33)'}
def why_not(e): return 'held under Provenance Review (Gate 1 OQ-33)' if e['lic']==PROV else WHY_NOT.get(e['type'],'held in reserve')
def usage(e):
    """(status, placement text) for a catalogue entry, from the files it owns."""
    if e.get('file') and not e.get('sub'):
        w=PLACED.get(e['file'])
        return ('placed','; '.join(w)) if w else (e['status'],'not placed: '+why_not(e))
    if e.get('sub'):
        n=sum(1 for r in e['sub'] if r['file'] in PLACED)
        return ('placed',f"{n} of {len(e['sub'])} files placed (see the sub-entries)") if n else (e['status'],'not placed: '+why_not(e))
    return (e['status'],e['placement'])
def sub_usage(e,r):
    w=PLACED.get(r['file'])
    return ('placed','; '.join(w)) if w else ('extracted','not placed: '+why_not(e))
# ---- write log
head=open('22_asset_extraction_log.md').read().split('## Colour Palette (sampled)')[0]
out=[head.rstrip()+'\n\n## Colour Palette (sampled)\n\nSampled with PIL/numpy from 400–600 dpi `pdftoppm` renders (sRGB) and from the extracted icon crops (median of saturated pixels in the named hue band). CMYK is a naive RGB→CMYK conversion for orientation only — the source PDFs are U.S. Web Coated (SWOP) CMYK; re-pick in the layout application against that profile.\n\n| Swatch | Hex (sRGB) | Approx. CMYK | Used for | Sampled from |\n|---|---|---|---|---|\n']
for k,v in PAL.items(): out.append(f"| {k.replace('_',' ')} | `{v['hex']}` | {v['cmyk']} | {v['use']} | {v.get('src','—')} |\n")
out.append('\nReading of the palette: the books are essentially two-tone — warm parchment (`#f4f2ea`) with charcoal ink (`#231f20`, i.e. rich black ≈ C0 M11 Y9 K86 in the CMYK source) — with gold (`#9c8141`/`#b77e2e`) as the single decorative accent and a small functional colour code borrowed from the components: red = enemy/spawn/weak, magenta = terrain, blue/purple = encounter level, green = attack arc/adjacency, orange/blue/black = dice. Covers and the back cover use a warm near-black (`#110f0e`).\n\n## Asset Catalogue\n\nGroups: logos (AST-0001–0005), icon set from the 2022 reference page (AST-0006 onward), ornaments, frames, diagrams, art, photography, textures, typographic specimens. Entries whose Method is `TO EXTRACT` have no file yet; entries marked `NOT EXTRACTED — provenance` are catalogued for the lead\'s decision only.\n\n'
 +('Phase 2B extractions (2026-11-11, `tools/extract_phase2b.py`, records in `work/extraction_records_phase2b.json`) are shown on the catalogue entry they belong to. An asset extracted as several files lists one sub-entry `AST-NNNN.k` per file in a table under its entry; Asset IDs of the catalogue are unchanged. Component imagery was taken from embedded image objects (`pdfimages -png` with soft masks composited to RGBA) at native resolution, so it carries no parchment, caption or watermark; the few page-region crops were rendered from a working copy with the personalisation line redacted and verified clear of it.\n\n' if P2B else ''))
def fmt_entry(e):
    src=e['src']; page=e.get('page'); 
    region=e.get('region') or (bbox_s(e.get('bbox_pt')) if e.get('bbox_pt') else 'whole embedded image (see Method)')
    dims=e.get('dims') or '—'
    if e.get('format')=='svg' and (not e.get('dims') or e['dims']=='—') and e.get('bbox_pt'):
        b=e['bbox_pt']; dims=f'{round(b[2]-b[0],1)}×{round(b[3]-b[1],1)} pt (vector)'
    typ=e['type'] if e['type']!='typographic specimen' else 'typographic specimen'
    cf=e['file'] if e.get('file') else 'not yet extracted'
    if e.get('files_note'): cf=e['files_note']
    elif e.get('p2b') and not e.get('file'): cf='none ('+e['p2b']['status']+')'
    if e.get('single') and e.get('p0_region') and e['single'].get('image_object'):
        io=e['single']['image_object']; region=f"embedded image object {io.get('xref')} (pdfimages #{io.get('pdfimages_num')}), placed at {bbox_s(e.get('bbox_pt'))}; catalogued as: {e['p0_region']}"
    elif e.get('single') and e.get('p0_region'): region=f"{bbox_s(e.get('bbox_pt'))}; catalogued as: {e['p0_region']}"
    out=(f"### [{e['id']}] {e['name']}\n- Source: {src}, p.{page}\n- Type: {typ}\n- Region: {region}\n- Dimensions: {dims}\n- Format: {e.get('format','png')}\n- Method: {e['method']}\n- Cleaned file: {cf}\n- Proposed placement: {e['placement']}\n- Final usage: {usage(e)[1] if (e.get('file') or e.get('sub')) else 'none ('+e['status']+')'}\n- Licensing: {e['lic']}\n- Notes: {e['notes'] or '—'}\n\n")
    if e.get('sub'):
        out+='| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |\n|---|---|---|---|---|---|---|---|\n'
        for r in e['sub']:
            io=r.get('image_object') or {}
            if io.get('xref'): reg=f"object {io['xref']} (pdfimages #{io.get('pdfimages_num')})"+(f", crop px {tuple(io['crop_px'])}" if io.get('crop_px') else '')
            elif io.get('xrefs'): reg=f"objects {', '.join(str(x) for x in io['xrefs'])}; {bbox_s(r.get('bbox_pt'))}"
            else: reg=bbox_s(r.get('bbox_pt')) if r.get('bbox_pt') else '—'
            out+=f"| {r['id']} | {r['name']} | `{r['file']}` | {r['dims']} | {r['src']}, p.{r['page']} | {reg} | {r['method']} | {(r.get('notes') or '—')+' Final usage: '+sub_usage(e,r)[1]+'.'} |\n"
        out+='\n'
    return out
cur=None
for e in entries:
    g=e['type']
    if g!=cur:
        cur=g; out.append(f"\n#### Group: {g}s\n\n" if not g.endswith('s') else f"\n#### Group: {g}\n\n")
    out.append(fmt_entry(e))
# provenance review
REVIEW_F=''
if any(e['review'] for e in entries):
    REVIEW_F=('\n### F. Phase 2B: candidates seen during extraction and not extracted\nRule applied in Phase 2B: Steamforged product imagery (miniature renders, tiles, boards, tokens, dice, card backs, layout ornaments, icons) is extracted; anything that looks like a painting, and any card or dashboard face whose painted illustration cannot be left out, is listed here instead. Where an illustration-free part could be had, that part was extracted and is named in the reason.\n\nPhase 2C decision: the anatomy plates extracted in Phase 0 that show the same painted card and dashboard illustrations (AST-0105, AST-0091, AST-0094, AST-0097) and the printed model discs of the arcs diagram (AST-0099) are placed in the book with those areas blanked (`masks` in `layout/tuning.json`); the stored plates are unchanged. The project lead is asked to rule (`14_open_issues.md`, item 21).\n\n'
              '| Review ID | Asset | Where | What | Reason / what was done |\n|---|---|---|---|---|\n'
              +''.join(f"| {r['id']} | {e['id']} | {r['src']}, p.{r['page']}, {r['image_object']} | {r['name']} | {r['reason']} |\n" for e in entries for r in e['review']))
out.append('''## Provenance Review

Items below are **not** designated for reuse until the project lead rules on them. Nothing in this section has been extracted into `assets/` except '''+TG_COVER+''' (TG cover art), which was pulled because the brief asked for one cover art and is held as `BLOCKED`.

### A. Third-party (FromSoftware / Bandai Namco) artwork inside the SFG PDFs
The owner's rights assertion covers the SFG publications. The paintings, screenshots and key art below are, however, FromSoftware/Bandai Namco intellectual property that SFG reproduced under licence (every credits block reads "Dark Souls™ & ©BANDAI NAMCO Entertainment Inc. / ©FromSoftware, Inc."). The lead must decide whether the assertion extends to this licensed art.

| Where | What | Notes |
|---|---|---|
| TG pp.1, 7, 9, 12, 14, 15, 19, 22, 23, 26, 31, 32, 34–38 | Full-page/column concept paintings and key art (Nito, Tomb of Giants, cathedral, bonfire knights, Black Knight, Anor Londo, Firekeeper, graveyard, Ashen One, Lothric, Dancer, Boreal knight) | Embedded at 150–300 ppi (up to 1970×2905 px) |
| Core 2017 pp.14–16, 19, 21, 23, 26, 31–38 | Same family of paintings plus environment sketches (Undead Burg, Sen's Fortress, Anor Londo, Lothric) | 150 ppi |
| Expansion covers p.1 and interior pp.3, 6–16 | Cover key art and in-game screenshots (Artorias, Sif, Mushroom Parent, Iron Keep tower, Smelter Demon gate, Pursuer, Lost Bastille, Kalameet, Executioner's Chariot, Hydra lake etc.) | Phantoms/Darkroot/BDK/Characters at 300 ppi (1754×2551 covers) |
| All books | Character/enemy portraits inside card rasters (treasure and enemy card illustrations) | Part of SFG card layouts but the illustration content is licensed art |

### B. Trade marks
- The **DARK SOULS™** wordmark (AST-0001–0004 contain it) is a Bandai Namco trade mark; "THE BOARD GAME" line and the circular flourish are SFG lock-up elements. A homebrew second edition should expect to use the wordmark nominatively (e.g. "a fan expansion for Dark Souls™: The Board Game") rather than as its own title — lead decision.
- SFG logo / Steamforged Games name appears only in credits text (no graphic logo found in these PDFs).

### C. Miniature renders and photography
Sculpts are SFG-owned works (credited sculptors) but depict licensed characters. Catalogued as photography above under the owner's assertion, flagged here so the lead is aware of the likeness issue.

### D. Community homebrews (reference only — nothing designated)
- **Hollowed Edition v1.3** (Serif Affinity Publisher, 10 pp, 620×842 pt): dark full-bleed textured backgrounds (ICC RGB rasters at 144 ppi, one per page), OptimusPrinceps heads with **Bookman Old Style** body (Monotype, commercial), rules in two columns with coloured keyword highlights. Artwork is downloaded fan/concept art with inline credits ("By u/tettix", "Concept art", "By OneSpeechless", "Unknown") — provenance unknown; **not for reuse**.
- **DS Extended Rules V45** (Word → Quartz PDF, 27 pp, A4): Times New Roman/Arial body with ACaslonPro/OptimusPrinceps used only for a title block, SFG parchment page background reused as a 147 ppi raster on every page (1216×1719), miniature photographs at 300 ppi (2113×1492). Layout language: Word two-column text, no ornaments. **Not for reuse**; the SFG background it embeds is already catalogued from the primary source (AST-0030/0035).

### E. Fonts
- **OptimusPrinceps / OptimusPrinceps SemiBold** (Manfred Klein): distributed as freeware; the font files are not in the project and the licence text should be retrieved before embedding. Substitute proposed below in any case.
- **Adobe Caslon Pro** (Regular/Italic/Bold/Semibold/BoldItalic) and **Helvetica**: commercial; the owner's rights assertion over the PDFs does not convey a font licence. Substitution required.
'''+REVIEW_F+'''
## Font Substitution

| Official font | Role | Can it be reproduced locally? | Proposed substitute (open) | Fallback installed now | Notes |
|---|---|---|---|---|---|
| OptimusPrinceps | display / chapter titles / sub-heads / folios / card titles | No — freeware file not present | **Cinzel** (Google Fonts, SIL OFL) Regular | — (none installed; Liberation Serif caps as placeholder) | Both are Trajan-type inscriptional capitals; Cinzel is slightly wider — track −10. Alternatively obtain OptimusPrinceps itself (freeware, check licence). |
| OptimusPrincepsSemiBold | cover subtitles, heavy heads | No | **Cinzel Bold** / **Cinzel Decorative** for display | — | |
| ACaslonPro-Regular | body text, tables | No — commercial | **Libre Caslon Text** Regular (Google Fonts, SIL OFL) | Liberation Serif / DejaVu Serif | Libre Caslon Text is the direct open Caslon; set at 9/11.5 pt to match colour. **EB Garamond** is a lighter alternative if Libre Caslon reads too heavy. |
| ACaslonPro-Italic | lore blocks, captions | No | Libre Caslon Text Italic | Liberation Serif Italic | |
| ACaslonPro-Bold | run-in heads, emphasis | No | Libre Caslon Text Bold | Liberation Serif Bold | |
| ACaslonPro-Semibold | sidebar sub-heads, table heads | No | EB Garamond SemiBold (Libre Caslon has no semibold) | — | |
| ACaslonPro-BoldItalic | rare emphasis | No | Libre Caslon Text Bold + italic synthesis, or EB Garamond Bold Italic | — | |
| Helvetica | small print (TG credits) | No — commercial | **Liberation Sans** (installed) / Inter (installed) / Arimo | Liberation Sans | Only a few strings. |
| Arimo-Regular | watermark / utility text | Yes — open (Apache 2.0); metric clone Liberation Sans installed | — | Liberation Sans | No action. |
| Symbol | bullets | n/a | use body font bullet | — | |

Installed now (`fc-list`): Bitstream Charter, Caladea, Carlito, DejaVu, FreeSerif/Sans, Inter, JetBrains Mono, Liberation, Loma, Unifont, WenQuanYi — none of the proposed substitutes (Cinzel, Libre Caslon Text, EB Garamond) is installed yet; they are all on Google Fonts under the SIL Open Font Licence and need to be fetched before layout starts.
''')
open('22_asset_extraction_log.md','w').write(''.join(out))
# ---- manifest
with open('21_asset_manifest.csv','w',newline='') as f:
    w=csv.writer(f,quoting=csv.QUOTE_MINIMAL)
    w.writerow(['Asset ID','Description','Placement (page/chapter)','Dimensions','Format','Source file','Source page','Licensing','Status','Notes'])
    for e in entries:
        if e.get('designated') is False: continue
        dims=e.get('dims') or '—'
        if e.get('format')=='svg' and (not e.get('dims') or dims=='—') and e.get('bbox_pt'):
            b=e['bbox_pt']; dims=f'{round(b[2]-b[0],1)}x{round(b[3]-b[1],1)} pt (vector)'
        note=(e['notes'] or '')
        if e.get('file'): note=(f"file: {e['file']}. "+note).strip()
        elif e.get('files_note'): note=(f"files: {e['files_note']}. "+note).strip()
        p2=bool(e.get('p2b_note') is not None and (e.get('single') or e['sub'] or e['p2b']))   # Phase 2B rows keep their whole note
        st,pl=usage(e)
        w.writerow([e['id'],e['name'],pl,dims,e.get('format','png'),e['src'],e.get('page',''),e['lic'],st,note if p2 else note[:400]])
        for r in e['sub']:
            st,pl=sub_usage(e,r)
            w.writerow([r['id'],r['name'],pl,r['dims'],r['format'],r['src'],r['page'],e['lic'],st,(f"file: {r['file']}. "+(r.get('notes') or '')).strip()])
    w.writerow(['FONT-01','Display face substitution: OptimusPrinceps → Cinzel (Google Fonts, SIL OFL)','all headings, titles, folios','—','ttf','pdffonts inventory','—','OFL substitute for freeware original','substitution','files: assets/fonts/static/Cinzel-Regular.ttf, Cinzel-SemiBold.ttf, Cinzel-Bold.ttf (cut from the OFL variable font by tools/make_fonts.py); embedded in the PDF'])
    w.writerow(['FONT-02','Body face substitution: Adobe Caslon Pro → Libre Caslon Text (Google Fonts, SIL OFL)','all body text, tables, captions','—','ttf','pdffonts inventory','—','OFL substitute for commercial original','substitution','files: assets/fonts/static/LibreCaslonText-Regular.ttf, -Italic.ttf, -Bold.ttf, -BoldItalic.ttf (cut by tools/make_fonts.py); embedded in the PDF. No semibold is used'])
    w.writerow(['FONT-03','Utility sans: Helvetica → Liberation Sans (installed)','small print','—','ttf','pdffonts inventory','—','open (OFL/Liberation licence)','substitution','not used: the book sets its small print in the body face'])
# ---- summary
ext=[e for e in entries if e.get('file') and not e.get('single')]; todo_n=[e for e in entries if e['status']=='TO EXTRACT']; prov=[e for e in entries if e['lic']==PROV]
p2f=[r for r in P2B if r.get('file')]; p2n=lambda pre: sum(1 for r in p2f if r['file'].startswith('assets/'+pre))
P2B_SUMM=(f" **Phase 2B added:** {len(p2f)} files for {len({r['parent'] for r in p2f})} catalogue assets ({p2n('photography')} component images incl. composites, {p2n('diagrams')} diagrams, {p2n('icons')} icons, {p2n('frames')} frames and card backs, {p2n('textures')} textures); {sum(1 for e in entries if e.get('p2b') and e['p2b']['status']=='not required')} marked not required, {sum(1 for e in entries if e.get('p2b') and e['p2b']['status']=='BLOCKED')} BLOCKED, {sum(len(e['review']) for e in entries)} candidates listed for provenance review (log, Provenance Review F). Hero list for the layout: `layout/hero_assets.json`." if P2B else '')
icons=[e for e in ext if e['type']=='icon']
summ=f"""# Asset reconnaissance — summary

**Scanned:** 12 PDFs (10 official SFG, 2 community) — every page rendered at 80 dpi and inspected; `pdffonts` and `pdfimages -list` run on all; 9 encrypted files re-saved with pypdf.

**Catalogued:** {len(entries)} assets in `22_asset_extraction_log.md` (AST-0001–AST-{len(entries):04d}). **Extracted {'in Phase 0' if P2B else 'now'}:** {len(ext)} files in `assets/` ({len(icons)} icons from the 2022 reference page, {sum(1 for e in ext if e['type']=='logo')} logo files incl. vector SVG, {sum(1 for e in ext if e['type'] in ('ornament','frame'))} ornaments/frames (SVG + PNG), {sum(1 for e in ext if e['type']=='texture')} textures incl. the 5174×3378 px print-master page background, {sum(1 for e in ext if e['type']=='diagram')} anatomy/worked-example diagrams, {sum(1 for e in ext if e['type']=='typographic specimen')} type specimens, 2 cover items). **Still to extract:** {len(todo_n)}{' (card frames, token/miniature photography, expansion set symbols, 2017-only enemy icons)' if not P2B else ' (not designated)'}.{P2B_SUMM} **Provenance review:** {len(prov)} catalogue entries plus the tables in the log.

**Fonts:** display OptimusPrinceps (+SemiBold, freeware); body Adobe Caslon Pro Regular/Italic/Bold/Semibold (commercial); Arimo (open) for utility text; Helvetica in one credits block. None installed locally. Proposed: Cinzel for display, Libre Caslon Text (or EB Garamond) for body, Liberation Sans for utility.

**Palette:** parchment `#f4f2ea`, ink `#231f20`, gold accent `#9c8141`/`#b77e2e`, cover black `#110f0e`; functional colours red `#ce4c4a`, magenta `#b556a7`, blue `#3ca2e0`, orange `#f89a0f`, green `#36b876`.

**Decisions needed from the lead**
1. Scope of the rights assertion over FromSoftware/Bandai Namco key art reproduced in the SFG books (all paintings, cover art) — currently BLOCKED; only SFG-originated layout, icons, textures, diagrams and sculpt photography are designated.
2. Use of the DARK SOULS™ wordmark in the 2E title versus a nominative mention.
3. Whether to request original card/dashboard artwork from the owner — embedded card rasters are ≤372–1000 px, too small for print.
4. Approve the font substitutions (Cinzel / Libre Caslon Text) so they can be installed.

Manifest: `21_asset_manifest.csv` ({sum(1 for e in entries if e.get('designated') is not False)+3+sum(len(e['sub']) for e in entries if e.get('designated') is not False)} rows). Catalogue data: `work/asset_catalogue_final.json`. Icon label check sheet: `work/icons_contact.png`.
"""
open('work/asset_recon_summary.md','w').write(summ)
print('entries',len(entries),'extracted',len(ext),'todo',len(todo_n),'prov',len(prov),'icons',len(icons),'phase2b files',len(p2f))
print('summary words:',len(summ.split()))
