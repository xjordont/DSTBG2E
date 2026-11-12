# 22 — Asset Extraction Log

**Project:** Dark Souls: The Board Game — homebrew "Second Edition" rulebook (DSTBG2E)
**Phase:** Reconnaissance, cataloguing and initial extraction of reusable design assets
**Date:** 2026-11-09 / 2026-11-10; Phase 2B and Phase 3 extraction 2026-11-11

## Introduction

**Later additions (2026-11-11).** On this date the author confirmed ownership of the rights in all source artwork, which closed the Provenance Review, and supplied eight further official booklets (The Four Kings, Gaping Dragon, Guardian Dragon, The Last Giant, Manus Father of the Abyss, Old Iron King, Vordt of the Boreal Valley, Asylum Demon; catalogue AST-0156 to AST-0163). The paintings, whole card faces, and dashboards that had been held were then extracted from embedded image objects (Phase 3; records in `work/extraction_records_phase3.json`, tool `tools/extract_phase3.py`). The paragraphs below describe the first reconnaissance pass and are kept as written.

This log records the reconnaissance pass over the reference PDFs in `sources/`. Twelve PDFs were scanned: ten official Steamforged Games (SFG) publications — the 2017 core rulebook (`DS-Core-Rules-lores.pdf`, 40 pp, 595×808 pt), the 2022 *Tomb of Giants* / V2 core rulebook (`DS-TG-Rulebook-Compressed_compressed.pdf`, 32 pp, 629×811 pt, InDesign 17.2 export re-compressed by iLovePDF), the one-page FAQ, and the seven expansion rulebooks (Characters, Phantoms, Darkroot, Iron Keep, Explorers, Black Dragon Kalameet, Executioner's Chariot) — plus two community homebrews (`Hollowed_Edition_v1.3.pdf`, Affinity Publisher; `DS-Extended-Rules-V45.pdf`, Word/Quartz) which were surveyed for layout language only and whose art is **not** designated for reuse.

Methods: `pdfinfo` and `pdffonts` for metadata and font inventory; `pdfimages -list` for the embedded raster inventory (CSV consolidated at `work/imglist/_all_images.csv`); nine encrypted PDFs (empty user password, `copy:no`) were re-saved unencrypted with pypdf into `work/pdf_decrypted/` so that `pdfimages` and `pdftoppm` run without restriction; every page of every PDF was rendered at 80 dpi (`work/renders/<pdf>/p-NN.png`) and assembled into 2×2 contact sheets (`work/renders/<pdf>/sheets/`) which were then inspected visually page by page; key pages were re-rendered at 400–600 dpi (`work/renders/hires/`) for pixel-exact cropping with PIL; palette samples were taken with PIL/numpy from representative renders; vector-only elements were tested with `pdftocairo -svg`. All extracted assets live under `assets/<type>/` with the asset-ID prefix in the filename. Every "Cleaned file" path listed below exists on disk at the time of writing; anything not yet extracted is marked `not yet extracted` / `TO EXTRACT`.

Note on the purchaser watermark ("Generated for …"): the 2022 rulebook and all seven expansion PDFs carry a per-download personalisation line at the top of every page (text object, not part of the artwork). It is a text layer and does not appear in the embedded images; crops from the high-dpi renders avoid the top ~22 pt of the page.

## Font Inventory

Source: `pdffonts` on every PDF (raw output in `work/fonts/<pdf>.txt`). All fonts are embedded subsets (except *Hollowed Edition*'s OptimusPrinceps, which is embedded in full). Locally installed fonts (`fc-list`): Bitstream Charter, Caladea, Carlito, DejaVu Sans/Serif/Mono, FreeSans/Serif/Mono, Inter, Inter Display, JetBrains Mono, Liberation Sans/Serif/Mono, Loma, Noto Color Emoji, Unifont, WenQuanYi — **none** of the SFG fonts are installed.

| Family (as embedded) | Role in SFG layout | Type | Embedded | Found in | Licensing status |
|---|---|---|---|---|---|
| **OptimusPrinceps** (Regular) | Display/heading face: logo lock-up "THE BOARD GAME", chapter titles, section heads, run-in small-caps heads, card titles, page folios | TrueType (CID TrueType in Hollowed) | yes (subset) | all 12 PDFs | Freeware by Manfred Klein (free for personal and commercial use, no redistribution restriction stated beyond "do not sell"). Not installed locally → needs substitution or the font file obtained from dafont/1001fonts. Closest open equivalent: **Cinzel** (Google Fonts, SIL OFL) — both are Trajan-style inscriptional capitals. |
| **OptimusPrincepsSemiBold** | Heavier display weight: expansion sub-titles on covers, large running heads | TrueType | yes (subset) | TG rulebook, FAQ, Phantoms, Explorers, BDK, EC | As above → **Cinzel Bold / Cinzel Decorative** |
| **ACaslonPro-Regular** (Adobe Caslon Pro) | Body text face throughout; also table body | Type 1C (CFF) | yes (subset) | all 11 SFG PDFs + Extended Rules | **Commercial (Adobe Originals / Adobe Fonts)** → needs substitute: **Libre Caslon Text** (Google Fonts, SIL OFL) — direct open Caslon; alternatives **EB Garamond** or **Cormorant Garamond** for a lighter colour. |
| ACaslonPro-Italic | Flavour text, captions, example-box captions | Type 1C | yes | all SFG + Extended | Commercial → Libre Caslon Text Italic |
| ACaslonPro-Bold | Bold run-ins, keyword emphasis | Type 1C | yes | 10 PDFs | Commercial → Libre Caslon Text Bold |
| ACaslonPro-Semibold | Sub-heads inside sidebars, table heads | Type 1C | yes | Core, Phantoms, Explorers, BDK, EC | Commercial → Libre Caslon Text Bold (Libre Caslon has no semibold; use EB Garamond Medium/SemiBold if a middle weight is needed) |
| ACaslonPro-BoldItalic | Rare emphasis | Type 1C | yes | Core, Phantoms | Commercial → Libre Caslon Text Bold Italic (synthesised; Libre Caslon Text ships Regular/Italic/Bold only) |
| **Arimo-Regular** | Hidden/utility text: the personalisation watermark line, QR/URL strings, symbol fallback | CID TrueType | yes | TG rulebook, FAQ, all 7 expansions | Open (Apache 2.0, Google/Ascender). Metrically identical **Liberation Sans** is installed. No substitution needed. |
| **Helvetica** | A handful of strings in TG rulebook (likely the credits block / small print) | TrueType | yes | TG rulebook only | **Commercial (Linotype/Monotype)** → Liberation Sans / Arimo / Inter (installed) |
| Symbol | Bullet glyphs (•) in 2017 core | CID TrueType | yes | Core 2017 | System font; bullets reproducible with any body face |
| ArialMT, SymbolMT, TimesNewRomanPSMT, TimesNewRomanPS-ItalicMT, Times-Roman | Word defaults | TrueType | yes | Extended Rules (community) | Not relevant — community document |
| BookmanOldStyle (Regular/Bold/Italic/BoldItalic) | Body face of *Hollowed Edition* | CID TrueType | yes | Hollowed Edition (community) | Commercial (Monotype); community document, not for reuse |

**Summary of roles:** Display/heading = OptimusPrinceps (+SemiBold); Body = Adobe Caslon Pro Regular/Italic/Bold; Table = Adobe Caslon Pro Regular (table heads in OptimusPrinceps small caps on the 2022 book, e.g. "BASE / TIER 1 / TIER 2 / TIER 3" on the dashboard; Caslon Semibold in the 2017 book). Captions/flavour = Adobe Caslon Pro Italic. Icon-key labels on the back-cover reference page = Adobe Caslon Pro Regular at ~7 pt.

## Embedded Image Inventory

Source: `pdfimages -list` (raw per-PDF output in `work/imglist/<pdf>.txt`; consolidated CSV `work/imglist/_all_images.csv`). Counts below are per PDF; "Entries" includes soft masks, "Images" are colour/grey image XObjects.

| PDF | Entries | Images | Soft masks | Colour spaces (images) | Encodings | Images ≥800×800 | Largest image |
|---|---|---|---|---|---|---|---|
| DS-Core-Rules-lores | 1518 | 1518 | 0 | icc 1180, rgb 202, index 136 | jpeg 1142, image 376 | 45 | 2516×1719 rgb jpeg @150 ppi |
| DS-TG-Rulebook-Compressed_compressed | 1008 | 667 | 340 | cmyk 435, gray 190, index 42 | jpeg 613, image 54 | 51 | 5174×3378 cmyk jpeg @300 ppi |
| Dark_Souls_The_Board_Game_FAQ | 1 | 1 | 0 | rgb 1 | jpeg 1 | 1 | 2516×1719 rgb jpeg @150 ppi |
| DS-Characters-Rules-lores | 96 | 54 | 42 | cmyk 51, gray 3 | jpeg 54 | 11 | 3437×2551 cmyk jpeg @300 ppi |
| DS-Phantoms-Rules-lores | 283 | 167 | 116 | cmyk 159, gray 5, index 3 | jpeg 164, jpx 3 | 36 | 3437×2551 cmyk jpeg @300 ppi |
| DS-Darkroot-Rules-web | 136 | 104 | 32 | cmyk 74, gray 28, index 2 | jpeg 97, image 7 | 23 | 3437×2551 cmyk jpeg @300 ppi |
| DS-IronKeep-Rules-Web | 113 | 84 | 29 | rgb 54, gray 22, index 8 | jpeg 76, image 8 | 10 | 1725×1276 rgb jpeg @150 ppi |
| DS-Explorers-Rules-Web | 615 | 358 | 257 | rgb 235, index 91, gray 32 | jpeg 266, image 92 | 20 | 1725×1276 rgb jpeg @150 ppi |
| DS-BDK-Rules-web | 916 | 598 | 318 | cmyk 323, gray 235, index 40 | jpeg 486, image 112 | 27 | 3437×2551 cmyk jpeg @300 ppi |
| DS-EC-Rules-Web | 1150 | 768 | 382 | gray 327, rgb 284, index 157 | jpeg 544, image 224 | 25 | 1719×1272 rgb jpeg @150 ppi |
| Hollowed_Edition_v1.3 | 150 | 82 | 68 | icc 82 | image 65, jpeg 17 | 14 | 1245×1688 icc image @144 ppi |
| DS-Extended-Rules-V45 | 150 | 89 | 61 | icc 45, rgb 44 | image 45, jpeg 44 | 38 | 2113×1492 rgb jpeg @300 ppi |

Observations:

- **Every page of every SFG PDF carries a full-page background raster** — the aged-parchment "open book" page texture (dark leather gutter at left, yellowed page-block edges at right). It is one JPEG per page: 2516×1719 RGB @150 ppi in the 2017 core/FAQ/EC/Explorers/Iron Keep (web-res exports), 3437×2551 CMYK @300 ppi in Characters/Phantoms/Darkroot/BDK, and 5174×3378 CMYK @300 ppi in the 2022 TG rulebook (print-res). The 2022 version is the highest-quality source for the page texture (see AST-0060 ff.).
- Very high per-page counts (e.g. core p.4–6: 302/424/168 images; TG p.6: 146; BDK p.5: 162; EC p.5: 241) are **component photographs and icon sprites**: the "Game Contents" spreads place each token, die, card and miniature as its own small image with a soft mask, so individual icons/tokens can be pulled cleanly with `pdfimages -png` + mask compositing.
- Full-page/half-page **key art** is embedded at 150 ppi in the web exports (≈1245×1685 for a full-bleed page) and 300 ppi in the lo-res-named expansion PDFs (1754×2551, i.e. a full A5-ish page at 300 ppi) — ironically the "-lores" expansions are the sharper source.
- The 2017 core rulebook has **no soft masks** (flattened), so its small icons are pre-composited onto parchment; prefer the 2022 book or the expansions for transparent icon pulls.
- 2017 core uses ICC-tagged RGB; 2022 TG and the 2018-era expansions are CMYK (U.S. Web Coated SWOP) — colour conversion needed on extraction (`pdfimages -png` converts to RGB; renders via `pdftoppm` are already sRGB).
- `jpx` (JPEG 2000) appears only in Phantoms (cover art and p.3 key art, indexed colour) — `pdfimages -png` handles it.
- Community PDFs: *Hollowed Edition* art is ICC RGB at 143–144 ppi (screen-res, downloaded concept art/fan art with credits such as "By u/tettix", "By OneSpeechless", "By Unknown", "Concept art"); *Extended Rules* uses miniature photography at 300 ppi and 147 ppi page backgrounds copied from the SFG template. All listed under Provenance Review only.

## Colour Palette (sampled)

Sampled with PIL/numpy from 400–600 dpi `pdftoppm` renders (sRGB) and from the extracted icon crops (median of saturated pixels in the named hue band). CMYK is a naive RGB→CMYK conversion for orientation only — the source PDFs are U.S. Web Coated (SWOP) CMYK; re-pick in the layout application against that profile.

| Swatch | Hex (sRGB) | Approx. CMYK | Used for | Sampled from |
|---|---|---|---|---|
| parchment page 2022 | `#f4f2ea` | C0 M1 Y4 K4 | page background, 2022 book (text-free parchment, p.13 right column) | TG p.13 render 400 dpi |
| parchment page 2017 | `#f5f2ed` | C0 M1 Y3 K4 | page background, 2017 book (brightest 60% of token column) | Core p.7 render 400 dpi |
| parchment panel backcover | `#f5f3ed` | C0 M1 Y3 K4 | reference-panel fill on back cover (brightest parchment) | TG p.32 render 600 dpi |
| page edge shadow | `#141312` | C0 M5 Y10 K92 | outer page-edge / gutter shadow of the open-book background | TG p.13 render |
| heading ink | `#231f20` | C0 M11 Y9 K86 | chapter-title ink (darkest 3 % of title zone) — effectively rich black/charcoal | TG p.13 render |
| body ink | `#231f20` | C0 M11 Y9 K86 | body-text ink (darkest 2 % of body zone) | TG p.13 render |
| cover black | `#110f0e` | C0 M12 Y18 K93 | cover and back-cover ground (warm near-black) | TG p.1 render |
| node gold | `#9c8141` | C0 M17 Y58 K39 | gold rings on icons, node outlines on tiles, dashboard lettering | icon crop: Taunt |
| spawn node red | `#ce4c4a` | C0 M63 Y64 K19 | enemy spawn nodes, Weak boss arc, Bleed | icon crop: Primary spawn node |
| terrain node magenta | `#b556a7` | C0 M52 Y8 K29 | terrain nodes | icon crop: Primary terrain node |
| encounter level1 blue | `#7a9ab7` | C33 M16 Y0 K28 | Encounter level 1 orb | icon crop |
| encounter level3 purple | `#6a59ab` | C38 M48 Y0 K33 | Encounter level 3 orb | icon crop |
| dice blue | `#3ca2e0` | C73 M28 Y0 K12 | blue die icon | icon crop |
| dice orange | `#f89a0f` | C0 M38 Y94 K3 | orange die icon | icon crop |
| attack arc green | `#36b876` | C71 M0 Y36 K28 | Attack boss arc, adjacency highlight | icon crop |
| weak arc red | `#f14e1e` | C0 M68 Y88 K5 | Weak boss arc | icon crop |
| poison green | `#3d9750` | C60 M0 Y47 K41 | Poison condition | icon crop |
| frostbite blue | `#74a3c1` | C40 M16 Y0 K24 | Frostbite condition | icon crop |
| endurance bar red | `#682b35` | C0 M59 Y49 K59 | character dashboard endurance bar (deep red) | TG p.8 render |
| dashboard gold | `#b77e2e` | C0 M31 Y75 K28 | dashboard slot lettering (ARMOUR / BACKUP / LEFT HAND) gold | TG p.8 render |
| card frame charcoal | `#1b1c1c` | C4 M0 Y0 K89 | card frame ground (equipment / enemy / behaviour cards) | TG p.10 render |
| card textbox parchment | `#e1ddc5` | C0 M2 Y12 K12 | card text-box parchment fill | TG p.10 render |

Reading of the palette: the books are essentially two-tone — warm parchment (`#f4f2ea`) with charcoal ink (`#231f20`, i.e. rich black ≈ C0 M11 Y9 K86 in the CMYK source) — with gold (`#9c8141`/`#b77e2e`) as the single decorative accent and a small functional colour code borrowed from the components: red = enemy/spawn/weak, magenta = terrain, blue/purple = encounter level, green = attack arc/adjacency, orange/blue/black = dice. Covers and the back cover use a warm near-black (`#110f0e`).

## Asset Catalogue

Groups: logos (AST-0001–0005), icon set from the 2022 reference page (AST-0006 onward), ornaments, frames, diagrams, art, photography, textures, typographic specimens. Entries whose Method is `TO EXTRACT` have no file yet; entries marked `NOT EXTRACTED — provenance` are catalogued for the lead's decision only.

Phase 2B extractions (2026-11-11, `tools/extract_phase2b.py`, records in `work/extraction_records_phase2b.json`) are shown on the catalogue entry they belong to. An asset extracted as several files lists one sub-entry `AST-NNNN.k` per file in a table under its entry; Asset IDs of the catalogue are unchanged. Component imagery was taken from embedded image objects (`pdfimages -png` with soft masks composited to RGBA) at native resolution, so it carries no parchment, caption or watermark; the few page-region crops were rendered from a working copy with the personalisation line redacted and verified clear of it.

Phase 3 extractions (2026-11-11, `tools/extract_phase3.py`, records in `work/extraction_records_phase3.json`) are attached in the same way. The author confirmed provenance of the painted art on 2026-11-11, so the paintings, whole card faces, whole dashboards and card fans that had been held are now extracted, and the entries that were marked `NOT EXTRACTED — provenance` or `BLOCKED` for that reason are shown as cleared. Painted art for which the catalogue had no entry is attached to the closest entry and says so in its note. Eight mega-boss expansion booklets supplied the same day have one entry each at the end of the catalogue (group "mega-boss expansion sets"). Only the essentials were taken from them (logo-free cover art, one boss painting, the miniature render, both sides of the game board), all from embedded image objects; no Phase 3 file is a page render. The designer's list of all Phase 3 files is `layout/art_candidates.json`; contact sheets are `build/art_contact*.jpg`.


#### Group: logos

### [AST-0001] Dark Souls: The Board Game logo lock-up (vector, black)
- Source: Dark_Souls_The_Board_Game_FAQ.pdf, p.1
- Type: logo
- Region: bbox (pt) x 176–392, y 41–134
- Dimensions: 216×93 pt (vector)
- Format: svg
- Method: pdftocairo -svg p.1 → tools/svg_crop.py (image/text removed, 1 compound path kept)
- Cleaned file: assets/logos/ast-0001-ds-tbg-logo-black.svg
- Proposed placement: cover, title page, running footer wordmark (vector master)
- Final usage: not placed: the wordmark is used nominatively only and the title is set in the display face (Gate 1 OQ-33)
- Licensing: authorised under owner's rights assertion
- Notes: Single compound path; the ™ glyph is live text in the PDF and was deliberately excluded. The DARK SOULS wordmark itself is a Bandai Namco trade mark (see Provenance Review); "THE BOARD GAME" line and the circular flourish are SFG lock-up elements.

### [AST-0002] Dark Souls: The Board Game logo lock-up (raster, black on transparent)
- Source: Dark_Souls_The_Board_Game_FAQ.pdf, p.1
- Type: logo
- Region: bbox (pt) x 176–392, y 41–134
- Dimensions: 3585×1517 px
- Format: png
- Method: pdftoppm 1200 dpi crop → parchment-key alpha (bg (244, 241, 236)) → trim
- Cleaned file: assets/logos/ast-0002-ds-tbg-logo-black.png
- Proposed placement: cover / title page raster fallback
- Final usage: not placed: the wordmark is used nominatively only and the title is set in the display face (Gate 1 OQ-33)
- Licensing: authorised under owner's rights assertion
- Notes: Alpha keyed from parchment; edge pixels carry a faint parchment fringe — prefer AST-0001 for print.

### [AST-0003] Dark Souls: The Board Game logo lock-up (raster, white on transparent)
- Source: Dark_Souls_The_Board_Game_FAQ.pdf, p.1
- Type: logo
- Region: bbox (pt) x 176–392, y 41–134
- Dimensions: 3585×1517 px
- Format: png
- Method: AST-0002 alpha with RGB forced to white (matches cover usage)
- Cleaned file: assets/logos/ast-0003-ds-tbg-logo-white.png
- Proposed placement: cover on dark ground
- Final usage: not placed: the wordmark is used nominatively only and the title is set in the display face (Gate 1 OQ-33)
- Licensing: authorised under owner's rights assertion
- Notes: Derived from AST-0002 by forcing RGB to white; alpha identical.

### [AST-0004] Logo lock-up as used on covers (vector, white fill)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.1
- Type: logo
- Region: bbox (pt) x 113–518, y 475–647
- Dimensions: 405×172 pt (vector)
- Format: svg
- Method: pdftocairo -svg p.1 → svg_crop (cover raster removed)
- Cleaned file: assets/logos/ast-0004-ds-tbg-logo-white-cover.svg
- Proposed placement: front cover (white, vector)
- Final usage: not placed: the wordmark is used nominatively only and the title is set in the display face (Gate 1 OQ-33)
- Licensing: authorised under owner's rights assertion
- Notes: White fill (CMYK 0/0/0/0 in source). Identical outline to AST-0001.

### [AST-0005] Logo glow (soft white halo raster placed behind cover logo)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.1
- Type: logo
- Region: whole embedded image (see Method)
- Dimensions: 1276×629 px
- Format: png
- Method: pdfimages -png p.1 image #1 (1276×629 grey, 200 ppi)
- Cleaned file: assets/logos/ast-0005-logo-glow-mask.png
- Proposed placement: behind the cover logo as a soft glow layer
- Final usage: not placed: the wordmark is used nominatively only and the title is set in the display face (Gate 1 OQ-33)
- Licensing: authorised under owner's rights assertion
- Notes: Greyscale 1276×629 image placed as a luminosity glow behind the white logo on every cover; use as a mask (screen/add blend).


#### Group: icons

### [AST-0006] Primary spawn node
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 98.0–123.0, y 98.5–123.5
- Dimensions: 208×208 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (173, 176, 175)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0006-primary-spawn-node.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §5.1; inline icon, §6.7; inline icon, §17.9
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead. red circle with slash

### [AST-0007] Encounter level 1
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 209.4–232.4, y 96.5–119.5
- Dimensions: 192×170 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (225, 224, 220)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0007-encounter-level-1.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.6; inline icon, §6.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0008] Skeleton Soldier
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 319.2–342.2, y 96.5–119.5
- Dimensions: 147×164 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (224, 225, 220)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0008-skeleton-soldier.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.2
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0009] Treasure Chest
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 428.0–453.1, y 95.5–120.6
- Dimensions: 178×197 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (218, 218, 213)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0009-treasure-chest.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.8; inline icon, §5.5; inline icon, §7.7; and 3 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0010] Secondary spawn node
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 98.0–123.0, y 122.5–147.5
- Dimensions: 208×208 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (196, 197, 194)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0010-secondary-spawn-node.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: inline icon, §5.1
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead. red circle with X

### [AST-0011] Encounter level 2
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 209.4–232.4, y 120.5–143.5
- Dimensions: 144×149 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (236, 235, 230)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0011-encounter-level-2.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.6; inline icon, §6.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0012] Skeleton Archer
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 319.2–342.2, y 120.5–143.5
- Dimensions: 147×151 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (238, 238, 233)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0012-skeleton-archer.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.2
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0013] Barrel
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 428.0–453.1, y 119.5–144.6
- Dimensions: 178×156 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (230, 230, 225)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0013-barrel.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.8; inline icon, §5.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0014] Primary terrain node
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 98.0–123.0, y 146.5–171.5
- Dimensions: 208×208 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (206, 207, 204)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0014-primary-terrain-node.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §5.1; inline icon, §6.7; inline icon, chapter 14
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead. magenta circle with star

### [AST-0015] Encounter level 3
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 209.4–232.4, y 144.5–167.5
- Dimensions: 144×149 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (241, 239, 235)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0015-encounter-level-3.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.6; inline icon, §6.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0016] Giant Skeleton Soldier
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 319.2–342.2, y 144.5–167.5
- Dimensions: 147×151 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (244, 242, 237)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0016-giant-skeleton-soldier.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.2
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0017] Gravestone
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 428.0–453.1, y 143.5–168.6
- Dimensions: 147×151 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (235, 234, 229)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0017-gravestone.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.8; inline icon, §5.5; inline icon, §7.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0018] Secondary terrain node
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 98.0–123.0, y 170.5–195.5
- Dimensions: 208×208 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (203, 204, 200)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0018-secondary-terrain-node.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: inline icon, §5.1
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead. magenta circle with trident

### [AST-0019] Giant Skeleton Archer
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 319.2–342.2, y 168.5–191.5
- Dimensions: 147×151 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 245, 240)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0019-giant-skeleton-archer.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.2
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0020] Lever
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 429.1–452.1, y 168.5–191.5
- Dimensions: 147×151 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (241, 241, 235)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0020-lever.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0021] Trapped encounter (trap icon, three spears)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 97.9–123.1, y 194.7–227.1
- Dimensions: 210×270 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (200, 201, 199)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0021-trapped-encounter.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.6; inline icon, §5.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead. placed as three 6.3×30.4 pt strips of the same image

### [AST-0022] Skeleton Beast
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 319.2–342.2, y 192.5–215.5
- Dimensions: 147×151 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 246, 241)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0022-skeleton-beast.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.2
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0023] Shrine
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 429.1–452.1, y 192.5–215.5
- Dimensions: 147×151 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (245, 243, 239)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0023-shrine.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0024] Necromancer
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 319.2–342.2, y 216.5–239.5
- Dimensions: 147×151 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (248, 246, 241)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0024-necromancer.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: icon reference page; inline icon, §2.2
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0025] Torch
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Encounter Cards”, bbox (pt) x 429.1–452.1, y 216.5–239.5
- Dimensions: 148×151 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 244, 240)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0025-torch.png
- Proposed placement: icon set — encounter card legend / Encounters chapter
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0026] Threat level
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Statistics”, bbox (pt) x 94.6–130.1, y 258.4–293.9
- Dimensions: 296×296 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (190, 195, 194)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0026-threat-level.png
- Proposed placement: icon set — enemy data card anatomy
- Final usage: icon reference page; inline icon, §8.2; inline icon, §9.1; inline icon, §12.1; and 1 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0027] Behaviour deck size
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Statistics”, bbox (pt) x 160.5–187.9, y 262.5–289.9
- Dimensions: 186×182 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (241, 239, 235)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0027-behaviour-deck-size.png
- Proposed placement: icon set — enemy data card anatomy
- Final usage: icon reference page; inline icon, §8.2; inline icon, §12.2; inline icon, §13.2; and 2 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0028] Block / Resist shield (enemy statistics)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Statistics”, bbox (pt) x 299.5–329.3, y 261.3–291.0
- Dimensions: 234×222 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 246, 241)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0028-block-resist-shield.png
- Proposed placement: icon set — enemy data card anatomy
- Final usage: icon reference page; inline icon, §8.2; inline icon, §12.2; inline icon, §15.4
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0029] Starting Health
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Statistics”, bbox (pt) x 369.9–397.4, y 262.5–289.9
- Dimensions: 186×186 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (248, 246, 242)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0029-starting-health.png
- Proposed placement: icon set — enemy data card anatomy
- Final usage: icon reference page; inline icon, §8.2; inline icon, §12.1; inline icon, §12.2; and 3 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0030] Heat Up Point
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Statistics”, bbox (pt) x 452.4–479.9, y 262.5–289.9
- Dimensions: 208×186 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (243, 242, 236)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0030-heat-up-point.png
- Proposed placement: icon set — enemy data card anatomy
- Final usage: icon reference page; inline icon, §8.2; inline icon, §12.2; inline icon, §13.2; and 9 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0031] Push-with-damage satellite glyph (push crest with value)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Movement”, bbox (pt) x 176.9–193.8, y 324.5–345.0
- Dimensions: 105×136 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 244, 241)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0031-push-with-damage-satellite-glyph.png
- Proposed placement: icon set — Enemy Turns chapter (movement)
- Final usage: icon reference page; inline icon, §8.2; inline icon, §8.4; inline icon, §9.2; and 1 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0032] Target: nearest character (ring glyph)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Movement”, bbox (pt) x 214.4–234.1, y 323.2–342.9
- Dimensions: 146×130 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 246, 241)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0032-target-nearest-character.png
- Proposed placement: icon set — Enemy Turns chapter (movement)
- Final usage: icon reference page; inline icon, §8.2; inline icon, §9.2; inline icon, §9.3; and 2 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0033] Enemy Movement composite symbol (Move icon with push, aggro and leap satellites)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Movement”, bbox (pt) x 174.5–235.1, y 344.7–405.3
- Dimensions: 505×506 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 244, 240)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0033-enemy-movement-composite-symbol.png
- Proposed placement: icon set — Enemy Turns chapter (movement)
- Final usage: icon reference page; inline icon, §8.2; inline icon, §9.2; inline icon, §15.5; and 1 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox. Whole anatomy diagram kept as one unit; the satellite glyphs are also available separately.

### [AST-0034] Turn 90° right
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Movement”, bbox (pt) x 99.5–150.5, y 426.3–473.5
- Dimensions: 407×393 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (231, 234, 231)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0034-turn-90-right.png
- Proposed placement: icon set — Enemy Turns chapter (movement)
- Final usage: icon reference page; inline icon, §15.6; inline icon, §16.2
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0035] Turn 90° left
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Movement”, bbox (pt) x 174.7–225.6, y 426.3–473.5
- Dimensions: 390×359 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 244, 240)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0035-turn-90-left.png
- Proposed placement: icon set — Enemy Turns chapter (movement)
- Final usage: icon reference page; inline icon, §15.6; inline icon, §16.2
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0036] Turn around (180°)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Movement”, bbox (pt) x 240.4–310.1, y 431.1–473.5
- Dimensions: 545×319 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 244, 241)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0036-turn-around.png
- Proposed placement: icon set — Enemy Turns chapter (movement)
- Final usage: icon reference page; inline icon, §15.6; inline icon, §16.2
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0037] Enemy Attack composite symbol (Attack icon with push, aggro, node and magic satellites)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Attacks”, bbox (pt) x 394.2–454.8, y 344.7–408.5
- Dimensions: 505×532 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (245, 243, 239)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0037-enemy-attack-composite-symbol.png
- Proposed placement: icon set — Enemy Turns chapter (attacks) and Boss arcs
- Final usage: icon reference page; inline icon, §8.2; inline icon, §9.3; inline icon, §15.5; and 1 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox. Whole anatomy diagram kept as one unit; the satellite glyphs are also available separately.

### [AST-0038] Area attack icon (damage all nodes in specified arcs)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Attacks”, bbox (pt) x 394.3–416.1, y 408.5–430.4
- Dimensions: 146×147 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 246, 241)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0038-area-attack-icon.png
- Proposed placement: icon set — Enemy Turns chapter (attacks) and Boss arcs
- Final usage: icon reference page; inline icon, §16.3; inline icon, §17.3
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0039] Neutral boss arc
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Attacks”, bbox (pt) x 323.8–360.4, y 434.7–471.3
- Dimensions: 217×219 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 246, 241)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0039-neutral-boss-arc.png
- Proposed placement: icon set — Enemy Turns chapter (attacks) and Boss arcs
- Final usage: icon reference page; inline icon, §15.6
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0040] Attack boss arc
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Attacks”, bbox (pt) x 378.7–415.3, y 434.7–471.3
- Dimensions: 243×244 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 246, 241)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0040-attack-boss-arc.png
- Proposed placement: icon set — Enemy Turns chapter (attacks) and Boss arcs
- Final usage: icon reference page; inline icon, §15.6; inline icon, §16.3
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0041] Weak boss arc
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Attacks”, bbox (pt) x 433.7–470.2, y 434.7–471.3
- Dimensions: 215×219 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (243, 242, 237)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0041-weak-boss-arc.png
- Proposed placement: icon set — Enemy Turns chapter (attacks) and Boss arcs
- Final usage: icon reference page; inline icon, §12.1; inline icon, §15.6; inline icon, §17.1; and 1 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0042] Deal magical damage (enemy attack star)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Attacks”, bbox (pt) x 487.3–526.5, y 432.9–473.1
- Dimensions: 310×335 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (226, 226, 223)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0042-deal-magical-damage.png
- Proposed placement: icon set — Enemy Turns chapter (attacks) and Boss arcs
- Final usage: icon reference page; inline icon, §4.3; inline icon, §8.2; inline icon, §9.3; and 4 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0043] One-handed weapon
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Equipment Icons”, bbox (pt) x 99.6–122.5, y 522.5–545.5
- Dimensions: 191×192 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (206, 207, 204)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0043-one-handed-weapon.png
- Proposed placement: icon set — Treasure / Equipment chapter
- Final usage: icon reference page; inline icon, §3.2; inline icon, §4.1; inline icon, §10.4
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0044] Weapon upgrade
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Equipment Icons”, bbox (pt) x 209.4–232.4, y 522.5–545.5
- Dimensions: 148×149 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 245, 241)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0044-weapon-upgrade.png
- Proposed placement: icon set — Treasure / Equipment chapter
- Final usage: icon reference page; inline icon, §4.2; inline icon, §6.3; inline icon, §11.4
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0045] Two-handed weapon
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Equipment Icons”, bbox (pt) x 99.6–122.5, y 546.5–569.5
- Dimensions: 191×192 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (202, 204, 201)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0045-two-handed-weapon.png
- Proposed placement: icon set — Treasure / Equipment chapter
- Final usage: icon reference page; inline icon, §3.2; inline icon, §4.1; inline icon, §10.3; and 1 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0046] Armour upgrade
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Equipment Icons”, bbox (pt) x 209.4–232.4, y 546.5–569.5
- Dimensions: 148×149 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 244, 241)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0046-armour-upgrade.png
- Proposed placement: icon set — Treasure / Equipment chapter
- Final usage: icon reference page; inline icon, §4.2; inline icon, §6.3; inline icon, §11.4
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0047] Armour
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Equipment Icons”, bbox (pt) x 99.6–122.5, y 570.5–593.5
- Dimensions: 191×192 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (201, 204, 201)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0047-armour.png
- Proposed placement: icon set — Treasure / Equipment chapter
- Final usage: icon reference page; inline icon, §3.2; inline icon, §4.1; inline icon, §6.3
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0048] Block (vs physical)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Equipment Icons”, bbox (pt) x 209.4–232.4, y 570.5–593.5
- Dimensions: 144×144 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 246, 242)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0048-block.png
- Proposed placement: icon set — Treasure / Equipment chapter
- Final usage: icon reference page; inline icon, §4.1; inline icon, §9.4
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead. Light-grey/cream glyph on parchment: keyed alpha is weak at the shield interior — re-cut from a dark-ground source or vectorise.

### [AST-0049] Upgrade slots
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Equipment Icons”, bbox (pt) x 99.5–122.5, y 594.5–617.5
- Dimensions: 192×192 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (191, 195, 193)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0049-upgrade-slots.png
- Proposed placement: icon set — Treasure / Equipment chapter
- Final usage: icon reference page; inline icon, §4.1
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0050] Resist (vs magic)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Equipment Icons”, bbox (pt) x 209.4–232.4, y 594.5–617.5
- Dimensions: 151×149 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 246, 241)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0050-resist.png
- Proposed placement: icon set — Treasure / Equipment chapter
- Final usage: icon reference page; inline icon, §4.1; inline icon, §9.4
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead. Light-grey/cream glyph on parchment: keyed alpha is weak at the shield interior — re-cut from a dark-ground source or vectorise.

### [AST-0051] Black dice
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Character Attacks”, bbox (pt) x 319.6–341.9, y 522.5–545.5
- Dimensions: 152×156 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 245, 241)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0051-black-dice.png
- Proposed placement: icon set — Character Turns chapter
- Final usage: icon reference page; inline icon, §2.7; inline icon, §4.1; inline icon, §10.3; and 2 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0052] Deal magical damage (character attack orb)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Character Attacks”, bbox (pt) x 423.6–457.6, y 518.5–549.6
- Dimensions: 234×259 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (245, 243, 238)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0052-deal-magical-damage.png
- Proposed placement: icon set — Character Turns chapter
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0053] Blue dice
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Character Attacks”, bbox (pt) x 319.6–341.9, y 546.5–569.5
- Dimensions: 152×156 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 245, 240)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0053-blue-dice.png
- Proposed placement: icon set — Character Turns chapter
- Final usage: icon reference page; inline icon, §2.7; inline icon, §4.1
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0054] Node attack (damage all enemies on target node)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Character Attacks”, bbox (pt) x 429.1–452.1, y 547.9–568.1
- Dimensions: 157×134 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 244, 240)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0054-node-attack.png
- Proposed placement: icon set — Character Turns chapter
- Final usage: icon reference page; inline icon, §9.3; inline icon, §10.3; inline icon, §16.3; and 1 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0055] Orange dice
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Character Attacks”, bbox (pt) x 319.6–341.9, y 570.5–593.5
- Dimensions: 152×156 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 246, 241)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0055-orange-dice.png
- Proposed placement: icon set — Character Turns chapter
- Final usage: icon reference page; inline icon, §2.7; inline icon, §4.1
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0056] Shaft (cannot attack at Range 0)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Character Attacks”, bbox (pt) x 429.1–452.1, y 571.5–592.6
- Dimensions: 157×141 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (245, 243, 239)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0056-shaft.png
- Proposed placement: icon set — Character Turns chapter
- Final usage: icon reference page; inline icon, §10.3; inline icon, §20.4
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0057] Shift (move indicated number of nodes in any direction)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Character Attacks”, bbox (pt) x 319.2–342.2, y 594.5–617.5
- Dimensions: 156×156 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (247, 246, 241)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0057-shift.png
- Proposed placement: icon set — Character Turns chapter
- Final usage: icon reference page; inline icon, §10.2; inline icon, §10.3; inline icon, §12.1
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0058] Push affected enemies
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Character Attacks”, bbox (pt) x 431.2–450.0, y 594.5–617.5
- Dimensions: 121×157 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (245, 242, 236)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0058-push-affected-enemies.png
- Proposed placement: icon set — Character Turns chapter
- Final usage: icon reference page; inline icon, §8.4; inline icon, §9.2; inline icon, §9.3; and 4 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0059] Taunt
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Other Icons”, bbox (pt) x 98.5–128.0, y 653.5–683.0
- Dimensions: 246×246 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (185, 189, 190)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0059-taunt.png
- Proposed placement: icon set — inline symbols throughout
- Final usage: icon reference page; inline icon, §3.1; inline icon, §7.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0060] Attack range
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Other Icons”, bbox (pt) x 179.8–207.3, y 654.5–682.0
- Dimensions: 186×186 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (238, 237, 232)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0060-attack-range.png
- Proposed placement: icon set — inline symbols throughout
- Final usage: icon reference page; inline icon, §4.1; inline icon, §8.2; inline icon, §10.3; and 2 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0061] Repeat behaviour or attack
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Other Icons”, bbox (pt) x 275.7–303.2, y 654.5–682.0
- Dimensions: 186×186 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (238, 238, 233)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0061-repeat-behaviour-or-attack.png
- Proposed placement: icon set — inline symbols throughout
- Final usage: icon reference page; inline icon, §8.2; inline icon, §9.1; inline icon, §9.3; and 5 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0062] Dodge
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Other Icons”, bbox (pt) x 421.3–448.7, y 654.5–682.0
- Dimensions: 186×186 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (224, 224, 220)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0062-dodge.png
- Proposed placement: icon set — inline symbols throughout
- Final usage: icon reference page; inline icon, §2.7; inline icon, §4.1; inline icon, §8.2; and 4 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0063] Bleed
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Conditions”, bbox (pt) x 101.7–132.3, y 710.7–741.3
- Dimensions: 255×255 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (119, 125, 127)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0063-bleed.png
- Proposed placement: icon set — Conditions section
- Final usage: icon reference page; inline icon, §2.8; inline icon, §8.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0064] Frostbite
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Conditions”, bbox (pt) x 211.6–242.2, y 710.7–741.3
- Dimensions: 255×255 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (178, 181, 180)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0064-frostbite.png
- Proposed placement: icon set — Conditions section
- Final usage: icon reference page; inline icon, §2.8; inline icon, §8.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0065] Poison
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Conditions”, bbox (pt) x 321.4–352.0, y 710.7–741.3
- Dimensions: 255×255 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (171, 176, 176)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0065-poison.png
- Proposed placement: icon set — Conditions section
- Final usage: icon reference page; inline icon, §2.8; inline icon, §8.5
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0066] Stagger
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Conditions”, bbox (pt) x 431.3–461.9, y 710.7–741.3
- Dimensions: 255×255 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (144, 153, 155)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0066-stagger.png
- Proposed placement: icon set — Conditions section
- Final usage: icon reference page; inline icon, §2.8; inline icon, §3.4; inline icon, §8.5; and 4 more sections
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0067] 2017-edition enemy icons: Hollow Soldier, Crossbow Hollow, Large Hollow Soldier, Silver Knight Swordsman, Silver Knight Greatbowman, Sentinel
- Source: DS-Core-Rules-lores.pdf, p.40
- Type: icon
- Region: back-cover key, “Encounter cards” column 3 (39×39 px rasters, pre-composited onto parchment, no soft mask)
- Dimensions: 6 files; 156–172 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/icons/ast-0067-*.png (6 files, listed as sub-entries AST-0067.1 to AST-0067.6)
- Proposed placement: icon set — core-set enemies (needed if the 2E book keeps the 2017 roster)
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-Core-Rules-lores.pdf p.40. Phase 0 note: Only sources are flattened 39 px rasters (work/pdfimages/Core_p40_rgba/005–010) or the 400 dpi render (assets/diagrams/… -2017.png). Re-cut from the 400/600 dpi render with parchment keying as done for the 2022 set.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0067.1 | 2017 enemy icon: Hollow Soldier | `assets/icons/ast-0067-enemy-icon-2017-hollow-soldier.png` | 172×172 px | DS-Core-Rules-lores.pdf, p.40 | bbox (pt) x 302.5–325, y 88.3–110.8 | pdftoppm 600 dpi render crop → parchment-key alpha (bg (218, 215, 211)) → trimmed to inked bounds | Source is a flattened 39 px raster (150 ppi) on parchment: the 600 dpi crop is a ×4 upsample, keyed like the 2022 set. Inline size only. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0067.2 | 2017 enemy icon: Crossbow Hollow | `assets/icons/ast-0067-enemy-icon-2017-crossbow-hollow.png` | 157×172 px | DS-Core-Rules-lores.pdf, p.40 | bbox (pt) x 302.5–325, y 112.3–134.8 | pdftoppm 600 dpi render crop → parchment-key alpha (bg (234, 231, 226)) → trimmed to inked bounds | Source is a flattened 39 px raster (150 ppi) on parchment: the 600 dpi crop is a ×4 upsample, keyed like the 2022 set. Inline size only. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0067.3 | 2017 enemy icon: Large Hollow Soldier | `assets/icons/ast-0067-enemy-icon-2017-large-hollow-soldier.png` | 156×153 px | DS-Core-Rules-lores.pdf, p.40 | bbox (pt) x 302.5–325, y 136.3–158.8 | pdftoppm 600 dpi render crop → parchment-key alpha (bg (241, 238, 233)) → trimmed to inked bounds | Source is a flattened 39 px raster (150 ppi) on parchment: the 600 dpi crop is a ×4 upsample, keyed like the 2022 set. Inline size only. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0067.4 | 2017 enemy icon: Silver Knight Swordsman | `assets/icons/ast-0067-enemy-icon-2017-silver-knight-swordsman.png` | 156×154 px | DS-Core-Rules-lores.pdf, p.40 | bbox (pt) x 302.5–325, y 160.3–182.8 | pdftoppm 600 dpi render crop → parchment-key alpha (bg (245, 242, 237)) → trimmed to inked bounds | Source is a flattened 39 px raster (150 ppi) on parchment: the 600 dpi crop is a ×4 upsample, keyed like the 2022 set. Inline size only. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0067.5 | 2017 enemy icon: Silver Knight Greatbowman | `assets/icons/ast-0067-enemy-icon-2017-silver-knight-greatbowman.png` | 156×153 px | DS-Core-Rules-lores.pdf, p.40 | bbox (pt) x 302.5–325, y 184.3–206.8 | pdftoppm 600 dpi render crop → parchment-key alpha (bg (245, 242, 237)) → trimmed to inked bounds | Source is a flattened 39 px raster (150 ppi) on parchment: the 600 dpi crop is a ×4 upsample, keyed like the 2022 set. Inline size only. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0067.6 | 2017 enemy icon: Sentinel | `assets/icons/ast-0067-enemy-icon-2017-sentinel.png` | 156×153 px | DS-Core-Rules-lores.pdf, p.40 | bbox (pt) x 302.5–325, y 208.3–230.8 | pdftoppm 600 dpi render crop → parchment-key alpha (bg (245, 242, 237)) → trimmed to inked bounds | Source is a flattened 39 px raster (150 ppi) on parchment: the 600 dpi crop is a ×4 upsample, keyed like the 2022 set. Inline size only. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |

### [AST-0068] Trapped-encounter sword icon (2017 horizontal variant)
- Source: DS-Core-Rules-lores.pdf, p.40
- Type: icon
- Region: bbox (pt) x 82.7–130, y 184.3–206.8; catalogued as: key panel, 91×39 px raster #032
- Dimensions: 394×188 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (220, 216, 213)) → trimmed to inked bounds
- Cleaned file: assets/icons/ast-0068-trapped-encounter-icon-2017.png
- Proposed placement: icon set — alternative trap glyph
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion
- Notes: Source is a flattened 91×39 px raster on parchment (×4 upsample, keyed). Reference only: the 2022 three-spear trap icon supersedes it. Phase 0 note: 2022 edition replaced it with the three-spear trap icon (extracted). Keep for reference only.

### [AST-0069] Mini-boss (standard) and Main-boss (advanced) skull icons
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.5
- Type: icon
- Region: “Bosses” heads: skull-in-ring icons above Black Knight / Gravelord Nito (rasters with masks, p.5 #150 region)
- Dimensions: 2 files; 63 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/icons/ast-0069-*.png (2 files, listed as sub-entries AST-0069.1 to AST-0069.2)
- Proposed placement: icon set — Boss Encounters chapter
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.5. Phase 0 note: Also on Phantoms p.6 (Summon icons) and Explorers p.4; cut from a 600 dpi render of TG p.5.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0069.1 | Mini-boss (standard) skull icon | `assets/icons/ast-0069-boss-icon-mini-boss-standard-skull.png` | 63×62 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 339 (pdfimages #19) | pdfimages -png p.5 image #19 (object 339, 64×64 cmyk) + soft mask #20 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Native 64 px (150 ppi at its 15 pt printed size): use at inline size only. No larger copy exists as a separate object in any source PDF (searched by image similarity). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0069.2 | Main-boss (advanced) crowned skull icon | `assets/icons/ast-0069-boss-icon-main-boss-advanced-crowned-skull.png` | 62×63 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 335 (pdfimages #15) | pdfimages -png p.5 image #15 (object 335, 64×64 cmyk) + soft mask #16 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Native 64 px (150 ppi at its 15 pt printed size): use at inline size only. No larger copy exists as a separate object in any source PDF (searched by image similarity). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |

### [AST-0070] Mega-boss icon (dragon silhouette in flame ring)
- Source: DS-BDK-Rules-web.pdf, p.11
- Type: icon
- Region: Mega Boss Data Cards call-out 8; also on p.4 beside the Kalameet miniature
- Dimensions: 2 files; 109–348 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/icons/ast-0070-*.png (2 files, listed as sub-entries AST-0070.1 to AST-0070.2)
- Proposed placement: icon set — Mega Boss chapter
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-BDK-Rules-web.pdf p.4; DS-EC-Rules-Web.pdf p.4. Phase 0 note: Render BDK p.11 at 600 dpi and key against parchment; also present on EC p.11 (chariot variant).

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0070.1 | Mega-boss icon: Black Dragon Kalameet (dragon head with red glow) | `assets/icons/ast-0070-mega-boss-icon-black-dragon-kalameet.png` | 197×348 px | DS-BDK-Rules-web.pdf, p.4 | object 67 (pdfimages #1) | pdfimages -png p.4 image #1 (object 67, 378×425 cmyk) + soft mask #2 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | The embedded object beside the Kalameet miniature on the contents page (325 ppi); larger and cleaner than the data-card call-out on p.11. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0070.2 | Mega-boss icon: Executioner's Chariot (chariot glyph with red glow) | `assets/icons/ast-0070-mega-boss-icon-executioners-chariot.png` | 109×95 px | DS-EC-Rules-Web.pdf, p.4 | object 88 (pdfimages #11) | pdfimages -png p.4 image #11 (object 88, 167×167 rgb) + soft mask #12 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | — Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |

### [AST-0071] Expansion set symbols (Darkroot wolf, Iron Keep helm, Explorers chest, BDK dragon, EC chariot, Phantoms, Characters) and the “universal” DS globe icon
- Source: DS-Darkroot-Rules-web.pdf, p.2
- Type: icon
- Region: Introduction paragraphs (universal icon inline, ~9 pt) and card corner set symbols on contents pages
- Dimensions: 1 file; 51 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/icons/ast-0071-set-symbol-universal-icon.png (sub-entry AST-0071.1)
- Proposed placement: icon set — set-symbol legend in the components appendix
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion
- Notes: Only the universal icon exists as a separate image object (extracted as AST-0071.1). The seven expansion set symbols occur only inside the low-resolution card rasters (about 12 to 15 px across), so no print-fit source exists: redraw as vectors or obtain card artwork from the owner. Phase 2B extraction, one file per subject from DS-Darkroot-Rules-web.pdf p.2. Phase 0 note: Inline glyphs are tiny in the rulebooks; cards on the contents pages show them at ~12 pt. Needs 1200 dpi render crops or redraw as vectors.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0071.1 | Universal (all-languages) card icon | `assets/icons/ast-0071-set-symbol-universal-icon.png` | 51×51 px | DS-Darkroot-Rules-web.pdf, p.2 | object 51 (pdfimages #1) | pdfimages -png p.2 image #1 (object 51, 51×51 cmyk) + soft mask #2 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | 51 px at 300 ppi (12 pt glyph): inline size only. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |

### [AST-0072] Invader and Summon token icons (Phantoms): 14 invader portraits + 10 summon portraits in rings
- Source: DS-Phantoms-Rules-lores.pdf, p.10
- Type: icon
- Region: “Game Setup with Invader Encounters” token wheel (12 tokens) and p.4–5 miniature call-outs
- Dimensions: 36 files; 188–260 px on the long side
- Format: png
- Method: Phase 2B and Phase 3 (tools/extract_phase2b.py, tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/icons/ast-0072-*.png (36 files, listed as sub-entries AST-0072.1 to AST-0072.36)
- Proposed placement: icon set — Phantoms module (if included)
- Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 2B and Phase 3 extraction, one file per subject from DS-Phantoms-Rules-lores.pdf p.4; DS-Phantoms-Rules-lores.pdf p.5; DS-Phantoms-Rules-lores.pdf p.10. 1 related candidate(s) were held for provenance review and cleared on 2026-11-11: see Provenance Review, section F. Phase 0 note: Crop from 600 dpi render of Phantoms p.10; tokens are dark discs with white glyphs. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0072.1 | Summon icon: Ruined Aflis (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-summon-ruined-aflis.png` | 185×188 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 74 (pdfimages #3) | pdfimages -png p.4 image #3 (object 74, 207×235 cmyk) + soft mask #4 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.2 | Summon icon: Eygon of Carim (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-summon-eygon-of-carim.png` | 185×189 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 110 (pdfimages #19) | pdfimages -png p.4 image #19 (object 110, 207×235 cmyk) + soft mask #20 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.3 | Summon icon: Horace the Hushed (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-summon-horace-the-hushed.png` | 185×188 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 106 (pdfimages #15) | pdfimages -png p.4 image #15 (object 106, 207×235 cmyk) + soft mask #16 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.4 | Summon icon: Siegward of Catarina (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-summon-siegward-of-catarina.png` | 185×188 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 100 (pdfimages #9) | pdfimages -png p.4 image #9 (object 100, 207×235 cmyk) + soft mask #10 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.5 | Summon icon: Sword Master (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-summon-sword-master.png` | 185×188 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 102 (pdfimages #11) | pdfimages -png p.4 image #11 (object 102, 207×235 cmyk) + soft mask #12 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.6 | Summon icon: Rogue Witch Beatrice (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-summon-rogue-witch-beatrice.png` | 200×215 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 72 (pdfimages #1) | pdfimages -png p.4 image #1 (object 72, 207×245 cmyk) + soft mask #2 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.7 | Summon icon: Lucatiel of Mirrah (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-summon-lucatiel-of-mirrah.png` | 183×229 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 108 (pdfimages #17) | pdfimages -png p.4 image #17 (object 108, 207×245 cmyk) + soft mask #18 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.8 | Summon icon: Sellsword Luet (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-summon-sellsword-luet.png` | 185×227 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 104 (pdfimages #13) | pdfimages -png p.4 image #13 (object 104, 207×245 cmyk) + soft mask #14 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.9 | Summon icon: Sirris of the Sunless Realms (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-summon-sirris-of-the-sunless-realms.png` | 185×215 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 98 (pdfimages #7) | pdfimages -png p.4 image #7 (object 98, 207×245 cmyk) + soft mask #8 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.10 | Summon icon: Solaire of Astora (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-summon-solaire-of-astora.png` | 186×220 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 96 (pdfimages #5) | pdfimages -png p.4 image #5 (object 96, 207×259 cmyk) + soft mask #6 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.11 | Invader icon: Kirk, Knight of Thorns (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-invader-kirk-knight-of-thorns.png` | 185×188 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 141 (pdfimages #5) | pdfimages -png p.5 image #5 (object 141, 207×228 cmyk) + soft mask #6 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.12 | Invader icon: Longfinger Kirk (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-invader-longfinger-kirk.png` | 185×215 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 149 (pdfimages #7) | pdfimages -png p.5 image #7 (object 149, 207×245 cmyk) + soft mask #8 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.13 | Invader icon: Melinda the Butcher (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-invader-melinda-the-butcher.png` | 186×195 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 119 (pdfimages #3) | pdfimages -png p.5 image #3 (object 119, 207×228 cmyk) + soft mask #4 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.14 | Invader icon: Maldron the Assassin (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-invader-maldron-the-assassin.png` | 185×188 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 121 (pdfimages #21) | pdfimages -png p.5 image #21 (object 121, 207×228 cmyk) + soft mask #22 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.15 | Invader icon: Maneater Mildred (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-invader-maneater-mildred.png` | 185×188 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 159 (pdfimages #17) | pdfimages -png p.5 image #17 (object 159, 207×228 cmyk) + soft mask #18 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.16 | Invader icon: Xanthous King Jeremiah (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-invader-xanthous-king-jeremiah.png` | 185×204 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 145 (pdfimages #43) | pdfimages -png p.5 image #43 (object 145, 207×228 cmyk) + soft mask #44 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.17 | Invader icon: Oliver the Collector (portrait glyph in ring) | `assets/icons/ast-0072-phantom-icon-invader-oliver-the-collector.png` | 185×188 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 155 (pdfimages #13) | pdfimages -png p.5 image #13 (object 155, 207×228 cmyk) + soft mask #14 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.18 | Invader icon: Armorer Dennis (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-invader-armorer-dennis.png` | 184×228 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 117 (pdfimages #1) | pdfimages -png p.5 image #1 (object 117, 207×245 cmyk) + soft mask #2 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.19 | Invader icon: Marvelous Chester (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-invader-marvelous-chester.png` | 185×218 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 161 (pdfimages #19) | pdfimages -png p.5 image #19 (object 161, 207×245 cmyk) + soft mask #20 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.20 | Invader icon: Invader Brylex (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-invader-invader-brylex.png` | 186×234 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 157 (pdfimages #15) | pdfimages -png p.5 image #15 (object 157, 207×245 cmyk) + soft mask #16 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.21 | Invader icon: Paladin Leeroy (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-invader-paladin-leeroy.png` | 185×220 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 153 (pdfimages #11) | pdfimages -png p.5 image #11 (object 153, 207×245 cmyk) + soft mask #12 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.22 | Invader icon: Fencer Sharron (portrait glyph in ring, glowing: advanced tier) | `assets/icons/ast-0072-phantom-icon-invader-fencer-sharron.png` | 260×215 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 151 (pdfimages #9) | pdfimages -png p.5 image #9 (object 151, 283×245 cmyk) + soft mask #10 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Named from the miniature caption it sits beside on the contents page. Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.23 | Phantom token 01 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-01.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 299 (pdfimages #17) | pdfimages -png p.10 image #17 (object 299, 201×201 cmyk) + soft mask #18 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.24 | Phantom token 02 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-02.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 279 (pdfimages #21) | pdfimages -png p.10 image #21 (object 279, 201×201 cmyk) + soft mask #22 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.25 | Phantom token 03 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-03.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 301 (pdfimages #19) | pdfimages -png p.10 image #19 (object 301, 201×201 cmyk) + soft mask #20 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.26 | Phantom token 04 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-04.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 281 (pdfimages #23) | pdfimages -png p.10 image #23 (object 281, 201×201 cmyk) + soft mask #24 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.27 | Phantom token 05 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-05.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 283 (pdfimages #25) | pdfimages -png p.10 image #25 (object 283, 201×201 cmyk) + soft mask #26 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.28 | Phantom token 06 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-06.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 285 (pdfimages #27) | pdfimages -png p.10 image #27 (object 285, 201×201 cmyk) + soft mask #28 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.29 | Phantom token 07 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-07.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 293 (pdfimages #11) | pdfimages -png p.10 image #11 (object 293, 201×201 cmyk) + soft mask #12 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.30 | Phantom token 08 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-08.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 291 (pdfimages #9) | pdfimages -png p.10 image #9 (object 291, 201×201 cmyk) + soft mask #10 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.31 | Phantom token 09 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-09.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 289 (pdfimages #7) | pdfimages -png p.10 image #7 (object 289, 201×201 cmyk) + soft mask #8 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.32 | Phantom token 10 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-10.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 287 (pdfimages #5) | pdfimages -png p.10 image #5 (object 287, 201×201 cmyk) + soft mask #6 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.33 | Phantom token 11 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-11.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 295 (pdfimages #13) | pdfimages -png p.10 image #13 (object 295, 201×201 cmyk) + soft mask #14 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.34 | Phantom token 12 of the p.10 set-up wheel (dark disc with portrait glyph) | `assets/icons/ast-0072-phantom-token-12.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 297 (pdfimages #15) | pdfimages -png p.10 image #15 (object 297, 201×201 cmyk) + soft mask #16 composited to RGBA; trimmed to inked bounds (alpha > 12); native resolution | Token face from the Game Setup with Invader Encounters diagram; same glyphs as the named portrait icons (unlabelled on the page). The two tokens of that diagram that carry painted art were left out (see Provenance Review). Final usage: not placed: no rule in the book uses this icon (earlier-edition variant, duplicate, or a component these rules do not use). |
| AST-0072.35 | Invader set-up token with painted red eye orb (Phantoms p.10) | `assets/icons/ast-0072-phantom-token-red-eye-orb.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 275 (pdfimages #1) | pdfimages -png p.10 image #1 (object 275, 201×201 cmyk + soft mask #2 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | 201 px: inline or thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0072.36 | Invader set-up token with painted cracked red eye orb (Phantoms p.10) | `assets/icons/ast-0072-phantom-token-cracked-red-eye-orb.png` | 201×201 px | DS-Phantoms-Rules-lores.pdf, p.10 | object 277 (pdfimages #3) | pdfimages -png p.10 image #3 (object 277, 201×201 cmyk + soft mask #4 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | 201 px: inline or thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0073] Language flag icons (EN/FR/DE/IT/ES)
- Source: DS-Darkroot-Rules-web.pdf, p.2
- Type: icon
- Region: Introduction, inline
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: not needed
- Final usage: none (TO EXTRACT)
- Licensing: authorised under owner's rights assertion
- Notes: Not designated — listed for completeness.


#### Group: ornaments

### [AST-0074] Celtic-knot square ornament (rule terminal / corner)
- Source: Dark_Souls_The_Board_Game_FAQ.pdf, p.1
- Type: ornament
- Region: bbox (pt) x 42–55, y 168–181
- Dimensions: 13×13 pt (vector)
- Format: svg
- Method: pdftocairo -svg → svg_crop (12 paths)
- Cleaned file: assets/ornaments/ast-0074-knot-square.svg
- Proposed placement: rule terminals on chapter titles, folios, table corners
- Final usage: not placed: reserve ornament; the book uses the knot square and the knot rule
- Licensing: authorised under owner's rights assertion
- Notes: 12 paths; renders cleanly at any size.

### [AST-0075] Celtic-knot square ornament (raster, black on transparent)
- Source: Dark_Souls_The_Board_Game_FAQ.pdf, p.1
- Type: ornament
- Region: bbox (pt) x 42–55, y 168–181
- Dimensions: 404×404 px
- Format: png
- Method: pdftoppm 2400 dpi crop → parchment-key alpha (bg (255, 255, 255))
- Cleaned file: assets/ornaments/ast-0075-knot-square.png
- Proposed placement: raster fallback for the knot
- Final usage: folio ornament, every page
- Licensing: authorised under owner's rights assertion
- Notes: Keyed from parchment at 2400 dpi; black only.

### [AST-0076] Compass/diamond corner ornament (example-box and art-frame corners)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.30
- Type: ornament
- Region: bbox (pt) x 344–356.5, y 440.5–453.5
- Dimensions: 12.5×13.0 pt (vector)
- Format: svg
- Method: pdftocairo -svg → svg_crop
- Cleaned file: assets/ornaments/ast-0076-compass-corner.svg
- Proposed placement: corners of example boxes, caption frames and art frames
- Final usage: not placed: reserve ornament; the book uses the knot square and the knot rule
- Licensing: authorised under owner's rights assertion
- Notes: 12 paths. In the 2022 book this diamond replaces the knot on example boxes; the 2017 book uses it on art frames too.

### [AST-0077] Compass/diamond corner ornament (raster)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.30
- Type: ornament
- Region: bbox (pt) x 344–356.5, y 440.5–453.5
- Dimensions: 389×408 px
- Format: png
- Method: pdftoppm 2400 dpi crop → parchment-key alpha (bg (255, 255, 255))
- Cleaned file: assets/ornaments/ast-0077-compass-corner.png
- Proposed placement: raster fallback for the compass corner
- Final usage: not placed: reserve ornament; the book uses the knot square and the knot rule
- Licensing: authorised under owner's rights assertion
- Notes: —

### [AST-0078] Chapter/section title rule lock-up: knot – rule – [title] – rule – knot (vector, title text removed)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.30
- Type: ornament
- Region: bbox (pt) x 95–580, y 61–77
- Dimensions: 485×16 pt (vector)
- Format: svg
- Method: pdftocairo -svg → svg_crop (text glyphs dropped)
- Cleaned file: assets/ornaments/ast-0078-chapter-title-rule-lockup.svg
- Proposed placement: chapter-opener title treatment (place title text in the gap)
- Final usage: not placed: reserve ornament; the book uses the knot square and the knot rule
- Licensing: authorised under owner's rights assertion
- Notes: Rules are 0.5 pt hairlines; knots 11.8 pt square; gap for a title of ~180 pt. Title text itself removed by the crop tool.

### [AST-0079] Title rule, left half (knot + hairline), raster
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.30
- Type: ornament
- Region: bbox (pt) x 95–249, y 61–77
- Dimensions: 2528×232 px
- Format: png
- Method: pdftoppm 1200 dpi crop → parchment-key alpha (bg (244, 242, 234)); mirror for right half
- Cleaned file: assets/ornaments/ast-0079-title-rule-left-half.png
- Proposed placement: raster version of the left half of the title rule (mirror for right)
- Final usage: not placed: reserve ornament; the book uses the knot square and the knot rule
- Licensing: authorised under owner's rights assertion
- Notes: —

### [AST-0080] Folio footer lock-up: knot – rule – [page number] – rule (vector, number removed)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.30
- Type: ornament
- Region: bbox (pt) x 95–580, y 760–776
- Dimensions: 485×16 pt (vector)
- Format: svg
- Method: pdftocairo -svg → svg_crop
- Cleaned file: assets/ornaments/ast-0080-folio-footer-rule-lockup.svg
- Proposed placement: running footer / folio treatment
- Final usage: not placed: reserve ornament; the book uses the knot square and the knot rule
- Licensing: authorised under owner's rights assertion
- Notes: Gap in the rule is where the page number sits (OptimusPrinceps ~9 pt).

### [AST-0081] Mid-page section divider: knot – rule – knot
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.3
- Type: ornament
- Region: bbox (pt) x 131.4–452.5, y 367.0–383.0
- Dimensions: 321.1×16.0 pt (vector)
- Format: svg
- Method: pdftocairo -svg → svg_crop
- Cleaned file: assets/ornaments/ast-0081-section-divider-knot-rule-knot.svg
- Proposed placement: section break inside a chapter (between lore and rules text)
- Final usage: not placed: reserve ornament; the book uses the knot square and the knot rule
- Licensing: authorised under owner's rights assertion
- Notes: From p.3 introduction: separates the italic lore block from the rules intro.

### [AST-0082] Mid-page section divider (raster)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.3
- Type: ornament
- Region: bbox (pt) x 131.4–452.5, y 367.0–383.0
- Dimensions: 5282×207 px
- Format: png
- Method: pdftoppm 1200 dpi crop → parchment-key alpha (bg (244, 242, 234))
- Cleaned file: assets/ornaments/ast-0082-section-divider-knot-rule-knot.png
- Proposed placement: raster fallback of AST-0081
- Final usage: front-matter rule; chapter-end ornament
- Licensing: authorised under owner's rights assertion
- Notes: —


#### Group: frames

### [AST-0083] Example/sidebar box frame: compass corners + hairline rules (vector template, content removed)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.30
- Type: frame
- Region: bbox (pt) x 343–580, y 439–521
- Dimensions: 237×82 pt (vector)
- Format: svg
- Method: pdftocairo -svg → svg_crop (icons inside are rasters, dropped automatically)
- Cleaned file: assets/frames/ast-0083-example-box-frame-small.svg
- Proposed placement: example / sidebar box frame (scale to fit)
- Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS
- Licensing: authorised under owner's rights assertion
- Notes: Vector template: four compass corners, four 0.5 pt rules inset 6 pt from the corners; the raster icons that sat inside were dropped by the tool. Resize by moving corners, not scaling strokes.

### [AST-0084] Table frame: knot corners + horizontal rules (vector template, text removed)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.26
- Type: frame
- Region: bbox (pt) x 336.1–586.5, y 291.0–429.0
- Dimensions: 250.4×138.0 pt (vector)
- Format: svg
- Method: pdftocairo -svg → svg_crop
- Cleaned file: assets/frames/ast-0084-table-frame-knot-corners.svg
- Proposed placement: tables (cost tables, turn-order tables)
- Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS
- Licensing: authorised under owner's rights assertion
- Notes: Vector template with knot corners; the 2022 book uses this for all small tables. Text removed; row rules kept.

### [AST-0085] Large art frame: compass corners + hairline rules around full-column illustrations
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.7
- Type: frame
- Region: bbox (pt) x 44–540, y 38–758; catalogued as: vector frame around the p.7 full-page illustration (corners at ~(63,42) (587,42) (63,775) (587,775) pt)
- Dimensions: 496×720 pt (vector)
- Format: svg
- Method: pdftocairo -svg p.7 (from a working copy with the purchaser line redacted) → tools/svg_crop.py (raster images and all text glyphs dropped; vector paths inside the bbox kept)
- Cleaned file: assets/frames/ast-0085-large-art-frame-compass-corners.svg
- Proposed placement: illustration frames / chapter-opener art
- Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS
- Licensing: authorised under owner's rights assertion
- Notes: 62 vector paths; the framed painting is a raster and is not in the file. Scale by moving the corners, not the strokes. Phase 0 note: Cut with tools/svg_crop.py from a pdftocairo SVG of TG p.7 (bbox 55,35,595,785); all art frames in both books use this construction.

### [AST-0086] Equipment card frame (charcoal ground, gold corner ornament, parchment text box, stat column)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.10
- Type: frame
- Region: Shortbow card, 248×372 px raster at 150 ppi (p.10 image #454)
- Dimensions: 24 files; 186–438 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/frames/ast-0086-*.png (24 files, listed as sub-entries AST-0086.1 to AST-0086.24)
- Proposed placement: card-style callouts; appendix card anatomy
- Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-Core-Rules-lores.pdf p.12; DS-Core-Rules-lores.pdf p.14; DS-Core-Rules-lores.pdf p.22; DS-Core-Rules-lores.pdf p.23; DS-Darkroot-Rules-web.pdf p.5; DS-TG-Rulebook-Compressed_compressed.pdf p.4; DS-TG-Rulebook-Compressed_compressed.pdf p.5; DS-TG-Rulebook-Compressed_compressed.pdf p.6; DS-TG-Rulebook-Compressed_compressed.pdf p.10; DS-TG-Rulebook-Compressed_compressed.pdf p.19; DS-TG-Rulebook-Compressed_compressed.pdf p.22; DS-TG-Rulebook-Compressed_compressed.pdf p.27. Phase 0 note: Embedded card images are ≤372 px — too small for print reuse. Request original card artwork from the owner or rebuild the frame as vector from the anatomy diagram AST-? (equipment card anatomy). Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0086.1 | Shortbow equipment card (2022 core p.10) | `assets/frames/ast-0086-equipment-card-shortbow.png` | 248×372 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.10 | object 929 (pdfimages #5) | pdfimages -png p.10 image #5 (object 929, 248×372 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.2 | Ember treasure card (2022 core p.10) | `assets/frames/ast-0086-equipment-card-ember.png` | 246×370 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.10 | object 931 (pdfimages #7) | pdfimages -png p.10 image #7 (object 931, 246×370 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.3 | Carthus Flame Arc upgrade card (2022 core p.10) | `assets/frames/ast-0086-equipment-card-carthus-flame-arc.png` | 233×350 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.10 | object 933 (pdfimages #9) | pdfimages -png p.10 image #9 (object 933, 233×350 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.4 | Obscuring Ring upgrade card (2022 core p.10) | `assets/frames/ast-0086-equipment-card-obscuring-ring.png` | 233×350 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.10 | object 935 (pdfimages #11) | pdfimages -png p.10 image #11 (object 935, 233×350 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.5 | Dragonslayer Spear equipment card (2022 core p.22) | `assets/frames/ast-0086-equipment-card-dragonslayer-spear.png` | 233×350 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.22 | object 1271 (pdfimages #2) | pdfimages -png p.22 image #2 (object 1271, 233×350 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.6 | Titanite Shard upgrade card (2022 core p.27) | `assets/frames/ast-0086-equipment-card-titanite-shard.png` | 154×231 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.27 | object 1417 (pdfimages #2) | pdfimages -png p.27 image #2 (object 1417, 154×231 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.7 | Morning Star equipment card (2022 core p.27) | `assets/frames/ast-0086-equipment-card-morning-star.png` | 154×231 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.27 | object 1419 (pdfimages #4) | pdfimages -png p.27 image #4 (object 1419, 154×231 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.8 | Chloranthy Ring upgrade card (2022 core p.27) | `assets/frames/ast-0086-equipment-card-chloranthy-ring.png` | 154×231 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.27 | object 1421 (pdfimages #6) | pdfimages -png p.27 image #6 (object 1421, 154×231 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.9 | Sunless Armour equipment card (2022 core p.27) | `assets/frames/ast-0086-equipment-card-sunless-armour.png` | 154×231 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.27 | object 1423 (pdfimages #8) | pdfimages -png p.27 image #8 (object 1423, 154×231 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.10 | Mace starting equipment card (2022 core p.4) | `assets/frames/ast-0086-equipment-card-mace.png` | 124×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 187 (pdfimages #44) | pdfimages -png p.4 image #44 (object 187, 124×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.11 | Hand Axe starting equipment card (2022 core p.4) | `assets/frames/ast-0086-equipment-card-hand-axe.png` | 124×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 159 (pdfimages #16) | pdfimages -png p.4 image #16 (object 159, 124×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.12 | Winged Spear treasure card (2022 core p.5) | `assets/frames/ast-0086-equipment-card-winged-spear.png` | 124×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 344 (pdfimages #24) | pdfimages -png p.5 image #24 (object 344, 124×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.13 | Dark Sword treasure card (2022 core p.5) | `assets/frames/ast-0086-equipment-card-dark-sword.png` | 124×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 353 (pdfimages #36) | pdfimages -png p.5 image #36 (object 353, 124×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.14 | Gravelord Sword boss treasure card (2022 core p.5) | `assets/frames/ast-0086-equipment-card-gravelord-sword.png` | 124×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 350 (pdfimages #32) | pdfimages -png p.5 image #32 (object 350, 124×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.15 | Green Blossom event card (2022 core p.19) | `assets/frames/ast-0086-event-card-green-blossom.png` | 248×372 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.19 | object 1230 (pdfimages #2) | pdfimages -png p.19 image #2 (object 1230, 248×372 cmyk, no soft mask); native resolution, no resampling | No catalogue entry of its own: attached to AST-0086 (the card frame family it shares) as the closest existing entry. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.16 | Lifegem event card (2022 core p.6) | `assets/frames/ast-0086-event-card-lifegem.png` | 124×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 785 (pdfimages #213) | pdfimages -png p.6 image #213 (object 785, 124×186 cmyk, no soft mask); native resolution, no resampling | No catalogue entry of its own: attached to AST-0086 (the card frame family it shares) as the closest existing entry. Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.17 | Greataxe equipment card (2017 core p.12) | `assets/frames/ast-0086-equipment-card-greataxe-2017.png` | 209×313 px | DS-Core-Rules-lores.pdf, p.12 | object 1189 (pdfimages #3) | pdfimages -png p.12 image #3 (object 1189, 209×313 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.18 | Titanite Shard upgrade card (2017 core p.12) | `assets/frames/ast-0086-equipment-card-titanite-shard-2017.png` | 200×300 px | DS-Core-Rules-lores.pdf, p.12 | object 1188 (pdfimages #20) | pdfimages -png p.12 image #20 (object 1188, 200×300 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.19 | Sunless Armour equipment card (2017 core p.14) | `assets/frames/ast-0086-equipment-card-sunless-armour-2017.png` | 155×232 px | DS-Core-Rules-lores.pdf, p.14 | object 1210 (pdfimages #12) | pdfimages -png p.14 image #12 (object 1210, 155×232 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.20 | Morning Star equipment card (2017 core p.14) | `assets/frames/ast-0086-equipment-card-morning-star-2017.png` | 155×232 px | DS-Core-Rules-lores.pdf, p.14 | object 1216 (pdfimages #6) | pdfimages -png p.14 image #6 (object 1216, 155×232 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.21 | Shortsword equipment card (2017 core p.22) | `assets/frames/ast-0086-equipment-card-shortsword-2017.png` | 292×438 px | DS-Core-Rules-lores.pdf, p.22 | object 1328 (pdfimages #1) | pdfimages -png p.22 image #1 (object 1328, 292×438 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.22 | Dragonslayer Spear equipment card (2017 core p.23) | `assets/frames/ast-0086-equipment-card-dragonslayer-spear-2017.png` | 292×438 px | DS-Core-Rules-lores.pdf, p.23 | object 1332 (pdfimages #1) | pdfimages -png p.23 image #1 (object 1332, 292×438 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.23 | Abyss Greatsword boss treasure card (Darkroot p.5) | `assets/frames/ast-0086-equipment-card-abyss-greatsword.png` | 169×254 px | DS-Darkroot-Rules-web.pdf, p.5 | object 362 (pdfimages #18) | pdfimages -png p.5 image #18 (object 362, 169×254 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0086.24 | Greatsword of Artorias boss treasure card (Darkroot p.5) | `assets/frames/ast-0086-equipment-card-greatsword-of-artorias.png` | 169×254 px | DS-Darkroot-Rules-web.pdf, p.5 | object 363 (pdfimages #20) | pdfimages -png p.5 image #20 (object 363, 169×254 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0087] Encounter card frame (parchment card with dark banner, node map area)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.16
- Type: frame
- Region: Grave Matters card, 584×1000 px raster at 300 ppi (p.16 image #624)
- Dimensions: 10 files; 175–1000 px on the long side
- Format: png
- Method: Phase 2B and Phase 3 (tools/extract_phase2b.py, tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/frames/ast-0087-*.png (10 files, listed as sub-entries AST-0087.1 to AST-0087.10)
- Proposed placement: encounter-card style callouts
- Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 2B and Phase 3 extraction, one file per subject from DS-Core-Rules-lores.pdf p.6; DS-Core-Rules-lores.pdf p.17; DS-Core-Rules-lores.pdf p.18; DS-TG-Rulebook-Compressed_compressed.pdf p.6; DS-TG-Rulebook-Compressed_compressed.pdf p.16. 1 related candidate(s) were held for provenance review and cleared on 2026-11-11: see Provenance Review, section F. Phase 0 note: Best-resolution card raster in the set (1000 px tall); crop via pdfimages -png -f 16 -l 16 and composite with its soft mask. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0087.1 | Encounter card frame, upper section: title banner, flavour strip and parchment text box (Grave Matters, card text printed in) | `assets/frames/ast-0087-encounter-card-frame-upper-section-banner-and-text-box.png` | 584×458 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.16 | object 1184 (pdfimages #2), crop px (0, 0, 584, 458) | pdfimages -png p.16 image #2 (object 1184, 584×1000 cmyk, no soft mask); cropped to px box (0, 0, 584, 458) of the object; native resolution, no resampling | Top 458 px of the 584×1000 card raster (300 ppi). The lower right of the card carries a painted scene and is left out (see Provenance Review). Card text is part of the raster. Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS. |
| AST-0087.2 | Encounter card frame, node-map panel (parchment panel with the node layout diagram) | `assets/frames/ast-0087-encounter-card-frame-node-map-panel.png` | 378×530 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.16 | object 1184 (pdfimages #2), crop px (14, 466, 392, 996) | pdfimages -png p.16 image #2 (object 1184, 584×1000 cmyk, no soft mask); cropped to px box (14, 466, 392, 996) of the object; native resolution, no resampling | Left panel of the lower half of the card raster; the painted scene to its right is left out (see Provenance Review). Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS. |
| AST-0087.3 | Grave Matters encounter card, whole (2022 core p.16, 300 ppi) | `assets/frames/ast-0087-encounter-card-grave-matters.png` | 584×1000 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.16 | object 1184 (pdfimages #2) | pdfimages -png p.16 image #2 (object 1184, 584×1000 cmyk, no soft mask); native resolution, no resampling | Largest card image in the sources. The smaller copies on p.16 (350×600) and p.6 were not extracted. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0087.4 | Lakeview Refuge encounter card (2022 core p.6) | `assets/frames/ast-0087-encounter-card-lakeview-refuge.png` | 155×266 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 634 (pdfimages #26) | pdfimages -png p.6 image #26 (object 634, 155×266 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0087.5 | The Abandoned Chest encounter card (2022 core p.6) | `assets/frames/ast-0087-encounter-card-the-abandoned-chest.png` | 155×266 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 636 (pdfimages #28) | pdfimages -png p.6 image #28 (object 636, 155×266 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0087.6 | Demon Ruins encounter card (2017 core p.17) | `assets/frames/ast-0087-encounter-card-demon-ruins-2017.png` | 249×373 px | DS-Core-Rules-lores.pdf, p.17 | object 1240 (pdfimages #1) | pdfimages -png p.17 image #1 (object 1240, 249×373 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0087.7 | The Forgotten encounter card (2017 core p.18) | `assets/frames/ast-0087-encounter-card-the-forgotten-2017.png` | 163×244 px | DS-Core-Rules-lores.pdf, p.18 | object 1278 (pdfimages #9) | pdfimages -png p.18 image #9 (object 1278, 163×244 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0087.8 | Ghostly Keep encounter card (2017 core p.6) | `assets/frames/ast-0087-encounter-card-ghostly-keep-2017.png` | 117×175 px | DS-Core-Rules-lores.pdf, p.6 | object 898 (pdfimages #78) | pdfimages -png p.6 image #78 (object 898, 117×175 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0087.9 | Prison Tower encounter card (2017 core p.6) | `assets/frames/ast-0087-encounter-card-prison-tower-2017.png` | 117×175 px | DS-Core-Rules-lores.pdf, p.6 | object 892 (pdfimages #72) | pdfimages -png p.6 image #72 (object 892, 117×175 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0087.10 | Pit of the Dead encounter card (2017 core p.6) | `assets/frames/ast-0087-encounter-card-pit-of-the-dead-2017.png` | 117×175 px | DS-Core-Rules-lores.pdf, p.6 | object 885 (pdfimages #66) | pdfimages -png p.6 image #66 (object 885, 117×175 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0088] Enemy / boss data card frame and behaviour card frame
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.24
- Type: frame
- Region: Skeleton Soldier data card (p.24 image #689/690), Gravelord Nito data card (p.28 #782 653×912), Death's Embrace behaviour card (p.28 #781 483×656)
- Dimensions: 37 files; 166–912 px on the long side
- Format: png
- Method: Phase 2B and Phase 3 (tools/extract_phase2b.py, tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/frames/ast-0088-*.png (37 files, listed as sub-entries AST-0088.1 to AST-0088.37)
- Proposed placement: enemy chapter card callouts
- Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 2B and Phase 3 extraction, one file per subject from DS-Core-Rules-lores.pdf p.4; DS-Core-Rules-lores.pdf p.24; DS-Core-Rules-lores.pdf p.26; DS-Core-Rules-lores.pdf p.27; DS-Darkroot-Rules-web.pdf p.4; DS-Darkroot-Rules-web.pdf p.5; DS-IronKeep-Rules-Web.pdf p.2; DS-IronKeep-Rules-Web.pdf p.3; DS-TG-Rulebook-Compressed_compressed.pdf p.4; DS-TG-Rulebook-Compressed_compressed.pdf p.5; DS-TG-Rulebook-Compressed_compressed.pdf p.24; DS-TG-Rulebook-Compressed_compressed.pdf p.28. 2 related candidate(s) were held for provenance review and cleared on 2026-11-11: see Provenance Review, section F. Phase 0 note: Composite from pdfimages output (image + smask) — 300 ppi sources exist for the two p.28 cards. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0088.1 | Boss data card frame, lower section: framed parchment text box (Gravelord Nito card, rule text printed in) | `assets/frames/ast-0088-data-card-frame-boss-card-text-box.png` | 653×397 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.28 | object 1442 (pdfimages #2), crop px (0, 515, 653, 912) | pdfimages -png p.28 image #2 (object 1442, 653×912 cmyk, no soft mask); cropped to px box (0, 515, 653, 912) of the object; native resolution, no resampling | Lower 397 px of the 653×912 card raster (300 ppi). The upper part of every enemy, boss and behaviour card is a character illustration and was not extracted (see Provenance Review). Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS. |
| AST-0088.2 | Skeleton Soldier enemy data card (2022 core p.24) | `assets/frames/ast-0088-enemy-card-skeleton-soldier.png` | 372×520 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.24 | object 1288 (pdfimages #2) | pdfimages -png p.24 image #2 (object 1288, 372×520 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.3 | Gravelord Nito boss data card, whole (2022 core p.28, 300 ppi) | `assets/frames/ast-0088-boss-card-gravelord-nito.png` | 653×912 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.28 | object 1442 (pdfimages #2) | pdfimages -png p.28 image #2 (object 1442, 653×912 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.4 | Death's Embrace boss behaviour card (2022 core p.28) | `assets/frames/ast-0088-behaviour-card-deaths-embrace.png` | 197×275 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.28 | object 1444 (pdfimages #10) | pdfimages -png p.28 image #10 (object 1444, 197×275 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.5 | Giant Skeleton Archer enemy data card (2022 core p.4) | `assets/frames/ast-0088-enemy-card-giant-skeleton-archer.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 167 (pdfimages #24) | pdfimages -png p.4 image #24 (object 167, 133×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.6 | Necromancer enemy data card (2022 core p.4) | `assets/frames/ast-0088-enemy-card-necromancer.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 179 (pdfimages #36) | pdfimages -png p.4 image #36 (object 179, 133×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.7 | Giant Skeleton Soldier enemy data card (2022 core p.4) | `assets/frames/ast-0088-enemy-card-giant-skeleton-soldier.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 183 (pdfimages #40) | pdfimages -png p.4 image #40 (object 183, 133×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.8 | Skeleton Archer enemy data card (2022 core p.4) | `assets/frames/ast-0088-enemy-card-skeleton-archer.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 171 (pdfimages #28) | pdfimages -png p.4 image #28 (object 171, 133×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.9 | Skeleton Beast enemy data card (2022 core p.4) | `assets/frames/ast-0088-enemy-card-skeleton-beast.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 175 (pdfimages #32) | pdfimages -png p.4 image #32 (object 175, 133×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.10 | Black Knight mini-boss data card (2022 core p.5) | `assets/frames/ast-0088-boss-card-black-knight.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 332 (pdfimages #12) | pdfimages -png p.5 image #12 (object 332, 133×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.11 | Overhead Swing boss behaviour card (2022 core p.5) | `assets/frames/ast-0088-behaviour-card-overhead-swing.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 330 (pdfimages #10) | pdfimages -png p.5 image #10 (object 330, 133×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.12 | Lunging Cleave boss behaviour card (2022 core p.5) | `assets/frames/ast-0088-behaviour-card-lunging-cleave.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 324 (pdfimages #4) | pdfimages -png p.5 image #4 (object 324, 133×186 cmyk, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.13 | Hollow Soldier enemy data card (2017 core p.24) | `assets/frames/ast-0088-enemy-card-hollow-soldier-2017.png` | 267×372 px | DS-Core-Rules-lores.pdf, p.24 | object 1336 (pdfimages #1) | pdfimages -png p.24 image #1 (object 1336, 267×372 rgb, no soft mask); native resolution, no resampling | A smaller copy on p.20 was not extracted. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.14 | Large Hollow Soldier enemy data card (2017 core p.4) | `assets/frames/ast-0088-enemy-card-large-hollow-soldier-2017.png` | 108×177 px | DS-Core-Rules-lores.pdf, p.4 | object 252 (pdfimages #46) | pdfimages -png p.4 image #46 (object 252, 108×177 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.15 | Crossbow Hollow enemy data card (2017 core p.4) | `assets/frames/ast-0088-enemy-card-crossbow-hollow-2017.png` | 127×177 px | DS-Core-Rules-lores.pdf, p.4 | object 238 (pdfimages #301) | pdfimages -png p.4 image #301 (object 238, 127×177 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.16 | Dancer of the Boreal Valley boss data card (2017 core p.26) | `assets/frames/ast-0088-boss-card-dancer-of-the-boreal-valley-2017.png` | 267×372 px | DS-Core-Rules-lores.pdf, p.26 | object 1349 (pdfimages #1) | pdfimages -png p.26 image #1 (object 1349, 267×372 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.17 | Blade Dance boss behaviour card (2017 core p.27) | `assets/frames/ast-0088-behaviour-card-blade-dance-2017.png` | 267×372 px | DS-Core-Rules-lores.pdf, p.27 | object 1371 (pdfimages #1) | pdfimages -png p.27 image #1 (object 1371, 267×372 rgb, no soft mask); native resolution, no resampling | A smaller copy on p.29 was not extracted. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.18 | Mushroom Parent enemy data card (Darkroot p.4) | `assets/frames/ast-0088-enemy-card-mushroom-parent.png` | 253×353 px | DS-Darkroot-Rules-web.pdf, p.4 | object 168 (pdfimages #23) | pdfimages -png p.4 image #23 (object 168, 253×353 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.19 | Plow Scarecrow enemy data card (Darkroot p.4) | `assets/frames/ast-0088-enemy-card-plow-scarecrow.png` | 253×353 px | DS-Darkroot-Rules-web.pdf, p.4 | object 170 (pdfimages #27) | pdfimages -png p.4 image #27 (object 170, 253×353 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.20 | Shears Scarecrow enemy data card (Darkroot p.4) | `assets/frames/ast-0088-enemy-card-shears-scarecrow.png` | 253×353 px | DS-Darkroot-Rules-web.pdf, p.4 | object 172 (pdfimages #31) | pdfimages -png p.4 image #31 (object 172, 253×353 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.21 | Demonic Foliage enemy data card (Darkroot p.4) | `assets/frames/ast-0088-enemy-card-demonic-foliage.png` | 253×353 px | DS-Darkroot-Rules-web.pdf, p.4 | object 190 (pdfimages #15) | pdfimages -png p.4 image #15 (object 190, 253×353 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.22 | Mushroom Child enemy data card (Darkroot p.4) | `assets/frames/ast-0088-enemy-card-mushroom-child.png` | 253×353 px | DS-Darkroot-Rules-web.pdf, p.4 | object 192 (pdfimages #19) | pdfimages -png p.4 image #19 (object 192, 253×353 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.23 | Stone Knight enemy data card (Darkroot p.5) | `assets/frames/ast-0088-enemy-card-stone-knight.png` | 253×353 px | DS-Darkroot-Rules-web.pdf, p.5 | object 345 (pdfimages #42) | pdfimages -png p.5 image #42 (object 345, 253×353 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.24 | Stone Guardian enemy data card (Darkroot p.5) | `assets/frames/ast-0088-enemy-card-stone-guardian.png` | 252×353 px | DS-Darkroot-Rules-web.pdf, p.5 | object 352 (pdfimages #50) | pdfimages -png p.5 image #50 (object 352, 252×353 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.25 | Knight Artorias boss data card (Darkroot p.5) | `assets/frames/ast-0088-boss-card-knight-artorias.png` | 237×331 px | DS-Darkroot-Rules-web.pdf, p.5 | object 358 (pdfimages #10) | pdfimages -png p.5 image #10 (object 358, 237×331 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.26 | Great Grey Wolf Sif boss data card (Darkroot p.5) | `assets/frames/ast-0088-boss-card-great-grey-wolf-sif.png` | 237×331 px | DS-Darkroot-Rules-web.pdf, p.5 | object 359 (pdfimages #12) | pdfimages -png p.5 image #12 (object 359, 237×331 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.27 | Overhead Cleave boss behaviour card (Darkroot p.5) | `assets/frames/ast-0088-behaviour-card-overhead-cleave.png` | 237×331 px | DS-Darkroot-Rules-web.pdf, p.5 | object 326 (pdfimages #2) | pdfimages -png p.5 image #2 (object 326, 237×331 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.28 | Sword Slam boss behaviour card (Darkroot p.5) | `assets/frames/ast-0088-behaviour-card-sword-slam.png` | 237×331 px | DS-Darkroot-Rules-web.pdf, p.5 | object 327 (pdfimages #4) | pdfimages -png p.5 image #4 (object 327, 237×331 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.29 | Alonne Bow Knight enemy data card (Iron Keep p.2) | `assets/frames/ast-0088-enemy-card-alonne-bow-knight.png` | 127×177 px | DS-IronKeep-Rules-Web.pdf, p.2 | object 136 (pdfimages #16) | pdfimages -png p.2 image #16 (object 136, 127×177 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.30 | Alonne Knight Captain enemy data card (Iron Keep p.2) | `assets/frames/ast-0088-enemy-card-alonne-knight-captain.png` | 127×177 px | DS-IronKeep-Rules-Web.pdf, p.2 | object 134 (pdfimages #12) | pdfimages -png p.2 image #12 (object 134, 127×177 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.31 | Alonne Sword Knight enemy data card (Iron Keep p.2) | `assets/frames/ast-0088-enemy-card-alonne-sword-knight.png` | 127×177 px | DS-IronKeep-Rules-Web.pdf, p.2 | object 138 (pdfimages #20) | pdfimages -png p.2 image #20 (object 138, 127×177 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.32 | Ironclad Soldier enemy data card (Iron Keep p.3) | `assets/frames/ast-0088-enemy-card-ironclad-soldier.png` | 127×177 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 301 (pdfimages #52) | pdfimages -png p.3 image #52 (object 301, 127×177 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.33 | Crystal Lizard data card (Iron Keep p.3) | `assets/frames/ast-0088-enemy-card-crystal-lizard.png` | 127×177 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 288 (pdfimages #38) | pdfimages -png p.3 image #38 (object 288, 127×177 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.34 | Sir Alonne boss data card (Iron Keep p.3) | `assets/frames/ast-0088-boss-card-sir-alonne.png` | 119×166 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 306 (pdfimages #12) | pdfimages -png p.3 image #12 (object 306, 119×166 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.35 | Smelter Demon boss data card (Iron Keep p.3) | `assets/frames/ast-0088-boss-card-smelter-demon.png` | 119×166 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 305 (pdfimages #10) | pdfimages -png p.3 image #10 (object 305, 119×166 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.36 | Charging Katana Slash boss behaviour card (Iron Keep p.3) | `assets/frames/ast-0088-behaviour-card-charging-katana-slash.png` | 119×166 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 274 (pdfimages #4) | pdfimages -png p.3 image #4 (object 274, 119×166 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0088.37 | Overhead Chop boss behaviour card (Iron Keep p.3) | `assets/frames/ast-0088-behaviour-card-overhead-chop.png` | 119×166 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 273 (pdfimages #2) | pdfimages -png p.3 image #2 (object 273, 119×166 rgb, no soft mask); native resolution, no resampling | Under 200 px on the long side (about 135 ppi as printed): thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0089] Card backs: treasure (orange ring), encounter level 1/2/3 (blue/purple ring), event card back, mini/main boss summon backs
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: frame
- Region: “Cards” section of Game Contents (p.6) and core p.6/p.9
- Dimensions: 6 files; 186–300 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/frames/ast-0089-*.png (6 files, listed as sub-entries AST-0089.1 to AST-0089.6)
- Proposed placement: appendix component list
- Final usage: 2 of 6 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.5; DS-TG-Rulebook-Compressed_compressed.pdf p.6; DS-TG-Rulebook-Compressed_compressed.pdf p.16. Phase 0 note: Small rasters (~130–300 px); photography-grade only. Extract via pdfimages p.6.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0089.1 | Treasure card back (gold ring with chest glyph) | `assets/frames/ast-0089-card-back-treasure.png` | 124×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 342 (pdfimages #22) | pdfimages -png p.5 image #22 (object 342, 124×186 cmyk, no soft mask); native resolution, no resampling | Card back, no illustration. Thumbnail-grade raster (about 130 to 150 ppi at the size printed in the rulebook): decorative use at small size only. Final usage: gallery, end of Appendix B. |
| AST-0089.2 | Boss treasure card back (gold ring with glowing skull glyph) | `assets/frames/ast-0089-card-back-boss-treasure.png` | 124×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 348 (pdfimages #30) | pdfimages -png p.5 image #30 (object 348, 124×186 cmyk, no soft mask); native resolution, no resampling | Card back, no illustration. Thumbnail-grade raster (about 130 to 150 ppi at the size printed in the rulebook): decorative use at small size only. Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS. |
| AST-0089.3 | Encounter card back, level 1 (blue flame) | `assets/frames/ast-0089-card-back-encounter-level-1.png` | 175×300 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.16 | object 1190 (pdfimages #24) | pdfimages -png p.16 image #24 (object 1190, 175×300 cmyk, no soft mask); native resolution, no resampling | Card back, no illustration. Thumbnail-grade raster (about 130 to 150 ppi at the size printed in the rulebook): decorative use at small size only. Final usage: gallery, end of Appendix B. |
| AST-0089.4 | Event card back | `assets/frames/ast-0089-card-back-event.png` | 124×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 783 (pdfimages #211) | pdfimages -png p.6 image #211 (object 783, 124×186 cmyk, no soft mask); native resolution, no resampling | Card back, no illustration. Thumbnail-grade raster (about 130 to 150 ppi at the size printed in the rulebook): decorative use at small size only. Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS. |
| AST-0089.5 | Mini-boss card back (Black Knight glyph on orange lattice) | `assets/frames/ast-0089-card-back-mini-boss-black-knight.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 328 (pdfimages #8) | pdfimages -png p.5 image #8 (object 328, 133×186 cmyk, no soft mask); native resolution, no resampling | Card back, no illustration. Thumbnail-grade raster (about 130 to 150 ppi at the size printed in the rulebook): decorative use at small size only. Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS. |
| AST-0089.6 | Main-boss card back (Gravelord Nito glyph on red lattice) | `assets/frames/ast-0089-card-back-main-boss-gravelord-nito.png` | 133×186 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 322 (pdfimages #2) | pdfimages -png p.5 image #2 (object 322, 133×186 cmyk, no soft mask); native resolution, no resampling | Card back, no illustration. Thumbnail-grade raster (about 130 to 150 ppi at the size printed in the rulebook): decorative use at small size only. Final usage: not placed: reference for the stylesheet; boxes and tables are drawn in CSS. |


#### Group: diagrams

### [AST-0090] Character dashboard anatomy (Cleric) with numbered call-outs 1–10
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.8
- Type: diagram
- Region: bbox (pt) x 78–600, y 330–748
- Dimensions: 2900×2323 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0090-character-dashboard-anatomy-2022.png
- Proposed placement: Characters chapter — dashboard anatomy
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Includes raster dashboard (1019×685 + 1019×806 px in PDF) and vector numbered call-outs (gold circles). Text labels sit outside the crop.

### [AST-0091] Equipment card anatomy (Shortbow) with call-outs 1–11
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.10
- Type: diagram
- Region: bbox (pt) x 136–292, y 335–548
- Dimensions: 1300×1775 px
- Format: png
- Method: pdftoppm 600 dpi crop
- Cleaned file: assets/diagrams/ast-0091-equipment-card-anatomy-2022.png
- Proposed placement: Treasure chapter — equipment card anatomy
- Final usage: figure, §4.1
- Licensing: authorised under owner's rights assertion
- Notes: Card raster is only 248×372 px in the PDF; call-outs are vector. For a 2E card anatomy, rebuild the card and reuse the call-out style.

### [AST-0092] Campaign dashboard anatomy (two strips) with call-outs 1–9
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.13
- Type: diagram
- Region: bbox (pt) x 45–540, y 113–400
- Dimensions: 2750×1594 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0092-campaign-dashboard-anatomy-2022.png
- Proposed placement: Campaign Dashboard chapter
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Two 979×250 px rasters at 150 ppi plus vector call-outs.

### [AST-0093] Encounter card anatomy (Grave Matters) with call-outs 1–8
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.16
- Type: diagram
- Region: bbox (pt) x 375–548, y 335–605
- Dimensions: 1442×2250 px
- Format: png
- Method: pdftoppm 600 dpi crop
- Cleaned file: assets/diagrams/ast-0093-encounter-card-anatomy-2022.png
- Proposed placement: Encounters chapter — encounter card anatomy
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Card raster 584×1000 px at 300 ppi — reusable.

### [AST-0094] Enemy data card anatomy (Skeleton Soldier) with call-outs 1–10
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.24
- Type: diagram
- Region: bbox (pt) x 102.0–324.6, y 291.0–572.4
- Dimensions: 1855×2345 px
- Format: png
- Method: pdftoppm 600 dpi crop
- Cleaned file: assets/diagrams/ast-0094-enemy-data-card-anatomy-2022.png
- Proposed placement: Enemy Turns chapter — enemy data card anatomy
- Final usage: figure, §8.2
- Licensing: authorised under owner's rights assertion
- Notes: Card raster 372×520 px at 150 ppi.

### [AST-0095] Enemy movement symbol anatomy (Move icon with call-outs 1–5)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.24
- Type: diagram
- Region: bbox (pt) x 403.3–520.1, y 170.0–286.1
- Dimensions: 973×967 px
- Format: png
- Method: pdftoppm 600 dpi crop
- Cleaned file: assets/diagrams/ast-0095-enemy-movement-symbol-anatomy.png
- Proposed placement: Enemy Turns chapter — movement symbol legend
- Final usage: figure, §9.2
- Licensing: authorised under owner's rights assertion
- Notes: Fully vector in the PDF; SVG available via svg_crop of tg_p24.svg with the same bbox.

### [AST-0096] Enemy attack symbol anatomy (Attack icon with call-outs 1–4)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.25
- Type: diagram
- Region: bbox (pt) x 58.2–227.5, y 216.7–354.8
- Dimensions: 1410×1151 px
- Format: png
- Method: pdftoppm 600 dpi crop
- Cleaned file: assets/diagrams/ast-0096-enemy-attack-symbol-anatomy.png
- Proposed placement: Enemy Turns chapter — attack symbol legend
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Fully vector; SVG available via svg_crop of tg_p25.svg.

### [AST-0097] Boss data card anatomy (Gravelord Nito) with call-outs 1–10
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.28
- Type: diagram
- Region: bbox (pt) x 116.7–317.5, y 468.0–719.0
- Dimensions: 1673×2091 px
- Format: png
- Method: pdftoppm 600 dpi crop
- Cleaned file: assets/diagrams/ast-0097-boss-data-card-anatomy-2022.png
- Proposed placement: Boss Encounters chapter — boss data card anatomy
- Final usage: figure, §15.4
- Licensing: authorised under owner's rights assertion
- Notes: Card raster 653×912 px at 300 ppi.

### [AST-0098] Boss behaviour card anatomy (Death's Embrace) with call-outs 1–5
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.28
- Type: diagram
- Region: bbox (pt) x 337.6–583.8, y 168.0–302.1
- Dimensions: 2052×1117 px
- Format: png
- Method: pdftoppm 600 dpi crop
- Cleaned file: assets/diagrams/ast-0098-boss-behaviour-card-anatomy-2022.png
- Proposed placement: Boss Encounters chapter — behaviour card anatomy
- Final usage: figure, §15.3
- Licensing: authorised under owner's rights assertion
- Notes: Card raster 483×656 px.

### [AST-0099] Boss arcs diagram A: boss base with four arcs on tile (front/left/right/back)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.29
- Type: diagram
- Region: bbox (pt) x 53–283, y 412–626
- Dimensions: 1278×1189 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0099-boss-arcs-tile-diagram-a.png
- Proposed placement: Boss Encounters chapter — arcs
- Final usage: figure, §15.6
- Licensing: authorised under owner's rights assertion
- Notes: 875×811 px raster at 300 ppi: boss base with X-arcs over tile with node colour overlay.

### [AST-0100] Boss arcs diagram B: arcs with highlighted node sets
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.29
- Type: diagram
- Region: bbox (pt) x 301–531, y 376–596
- Dimensions: 1278×1222 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0100-boss-arcs-tile-diagram-b.png
- Proposed placement: Boss Encounters chapter — arcs
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: 875×834 px raster at 300 ppi.

### [AST-0101] Boss base photo showing arc markings (X on base)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.29
- Type: diagram
- Region: bbox (pt) x 106–258, y 95–202
- Dimensions: 844×594 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0101-boss-base-arc-markings.png
- Proposed placement: Boss Encounters chapter — base markings
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Photo of a boss model base (275×182 px raster).

### [AST-0102] Boss activation worked example, six stages (full-page diagram)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.30
- Type: diagram
- Region: bbox (pt) x 55–585, y 40–790
- Dimensions: 2209×3125 px
- Format: png
- Method: pdftoppm 300 dpi crop
- Cleaned file: assets/diagrams/ast-0102-boss-activation-example-6-stages.png
- Proposed placement: Boss Activations chapter — worked example
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Six tile panels with behaviour-card icons; whole-page specimen at 300 dpi (also usable as a layout model for worked examples).

### [AST-0103] Movement example: walk + three runs on a tile (arrows over tile)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.20
- Type: diagram
- Region: bbox (pt) x 300–590, y 560–780
- Dimensions: 1611×1222 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0103-movement-example-tile.png
- Proposed placement: Character Turns chapter — movement example
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Tile raster with vector arrows; 884×360 px source.

### [AST-0104] Getting Underway: encounter track + card draw diagram
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.16
- Type: diagram
- Region: bbox (pt) x 55–335, y 440–790
- Dimensions: 1555×1945 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0104-encounter-track-getting-underway.png
- Proposed placement: Campaign Dashboard chapter — getting underway
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Composite of encounter track strip, party token and card.

### [AST-0105] Character board anatomy (Herald, 2017) call-outs 1–11
- Source: DS-Core-Rules-lores.pdf, p.11
- Type: diagram
- Region: bbox (pt) x 151.7–415.2, y 74.0–273.0
- Dimensions: 1464×1106 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0105-character-board-anatomy-2017.png
- Proposed placement: Characters chapter (2017 variant, reference)
- Final usage: figure, chapter 3
- Licensing: authorised under owner's rights assertion
- Notes: 2017 board layout; superseded by AST-0090 but useful for comparison.

### [AST-0106] Bonfire tile anatomy (2017) call-outs 1–6
- Source: DS-Core-Rules-lores.pdf, p.13
- Type: diagram
- Region: bbox (pt) x 67.4–485.4, y 86.6–494.6
- Dimensions: 2323×2267 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0106-bonfire-tile-anatomy-2017.png
- Proposed placement: Bonfire chapter (2017 only — tile not in 2022 set)
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: 788×788 px tile raster with vector call-outs 1–6.

### [AST-0107] Equipment card anatomy (Greataxe, 2017) call-outs 1–12
- Source: DS-Core-Rules-lores.pdf, p.12
- Type: diagram
- Region: bbox (pt) x 150–315, y 165–352
- Dimensions: 1375×1558 px
- Format: png
- Method: pdftoppm 600 dpi crop — fallback bbox from contact-sheet estimate
- Cleaned file: assets/diagrams/ast-0107-equipment-card-anatomy-2017.png
- Proposed placement: Treasure chapter (2017 variant, reference)
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Fallback bbox used (image object not isolated by pdfplumber); verify crop before use.

### [AST-0108] Boss arcs diagram (Dancer, 2017): arcs and node colours
- Source: DS-Core-Rules-lores.pdf, p.27
- Type: diagram
- Region: bbox (pt) x 282.6–532.3, y 529.4–753.6
- Dimensions: 1387×1246 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0108-boss-arcs-diagram-2017.png
- Proposed placement: Boss Encounters chapter (2017 variant)
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: 2017 arc diagram with coloured node highlights.

### [AST-0109] Icon key / reference page panel (2022 back cover) — complete symbol legend
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: diagram
- Region: bbox (pt) x 99.6–629.3, y 30.0–810.6
- Dimensions: 4414×6505 px
- Format: png
- Method: 600 dpi render; panel bbox auto-detected as bright region (L>200) excluding top 30 pt
- Cleaned file: assets/diagrams/ast-0109-icon-key-reference-page-2022.png
- Proposed placement: reference appendix / back cover
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Full legend panel; individual icons extracted as the icon set above. Panel bbox auto-detected from the bright region.

### [AST-0110] Icon key / reference page (2017 back cover)
- Source: DS-Core-Rules-lores.pdf, p.40
- Type: diagram
- Region: bbox (pt) x 40–555, y 38–770
- Dimensions: 2861×4067 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0110-icon-key-reference-page-2017.png
- Proposed placement: reference appendix (2017 variant)
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: 2017 legend including 2017-only enemy icons; see icon TO EXTRACT entries.

### [AST-0111] Encounter setup worked example (The Forgotten) — card + tile with placed tokens
- Source: DS-Core-Rules-lores.pdf, p.18
- Type: diagram
- Region: bbox (pt) x 66–558, y 336–756; catalogued as: framed example box, right-hand page (~x 40–585, y 395–830 pt)
- Dimensions: 2733×2333 px
- Format: png
- Method: pdftoppm 400 dpi page-region crop
- Cleaned file: assets/diagrams/ast-0111-encounter-setup-example-2017.png
- Proposed placement: Encounters chapter — setup example
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Whole example box with its compass-corner frame, heading and explanatory text, on the 2017 parchment. 2017 components (Hollow Soldiers, Silver Knight Greatbowman); the 2017 PDF carries no purchaser line. Phase 0 note: Crop from a 400 dpi render of core p.18; frame uses compass corners.

### [AST-0112] Node adjacency diagram (green highlighted nodes)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.11
- Type: diagram
- Region: embedded image object 945 (pdfimages #5), placed at bbox (pt) x 63.0–272.8, y 531.3–741.0; catalogued as: “Movement” example box lower-left (~x 60–300, y 560–780 pt); 875×875 px tile raster
- Dimensions: 875×875 px
- Format: png
- Method: pdfimages -png p.11 image #5 (object 945, 875×875 cmyk, no soft mask); native resolution, no resampling
- Cleaned file: assets/diagrams/ast-0112-node-adjacency-diagram.png
- Proposed placement: Tiles and Nodes chapter
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Embedded raster with the diagram artwork baked in (no page crop, so no parchment, caption or watermark). Mean difference to the page render of the same placement: 2.3/255 (nothing is drawn over it on the page). Phase 0 note: Render TG p.11 at 400 dpi and crop.

### [AST-0113] Range / doorway diagram (tile with arrow through door)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.11
- Type: diagram
- Region: embedded image object 946 (pdfimages #6), placed at bbox (pt) x 310.9–521.1, y 182.9–285.1; catalogued as: right column box (~x 311–521, y 183–285 pt), 438×213 px raster
- Dimensions: 438×213 px
- Format: png
- Method: pdfimages -png p.11 image #6 (object 946, 438×213 cmyk, no soft mask); native resolution, no resampling
- Cleaned file: assets/diagrams/ast-0113-range-and-doorway-diagram.png
- Proposed placement: Tiles and Nodes chapter
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Embedded raster with the diagram artwork baked in (no page crop, so no parchment, caption or watermark). Mean difference to the page render of the same placement: 4.2/255 (nothing is drawn over it on the page).

### [AST-0114] Timer track diagram (0–8 track with hourglass marker)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.18
- Type: diagram
- Region: top of page (~x 55–585, y 95–230 pt)
- Dimensions: —
- Format: png
- Method: not required (Phase 2B decision)
- Cleaned file: none (not required)
- Proposed placement: Encounters chapter — timer track
- Final usage: none (not required)
- Licensing: authorised under owner's rights assertion
- Notes: The timer track belongs to a rule this ruleset does not use; not extracted.

### [AST-0115] Equipment modifier strip ([0] 1 +1 / [3] 2 +1)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.21
- Type: diagram
- Region: embedded image object 1260 (pdfimages #9), placed at bbox (pt) x 62.0–273.9, y 133.9–220.2; catalogued as: example box top-left (~x 60–305, y 92–175 pt), 884×360 px raster
- Dimensions: 884×352 px
- Format: png
- Method: pdfimages -png p.21 image #9 (object 1260, 884×360 cmyk, no soft mask); cropped to px box (0, 0, 884, 352) of the object; native resolution, no resampling
- Cleaned file: assets/diagrams/ast-0115-equipment-modifier-strip.png
- Proposed placement: Character Turns chapter — modifiers
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Embedded raster with the diagram artwork baked in (no page crop, so no parchment, caption or watermark). The bottom 8 px of the object (tops of the next row of card icons, clipped away on the page) are cropped off. Mean difference to the page render of the same placement: 12.5/255 (vector overlays are drawn over it on the page and are not in this file).

### [AST-0116] Enemy attack dice resolution strip (attack 5 → dice → damage cubes)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.25
- Type: diagram
- Region: bbox (pt) x 309–523, y 417–479.5; catalogued as: example box left column (~x 60–305, y 455–545 pt)
- Dimensions: 1783×521 px
- Format: png
- Method: pdftoppm 600 dpi page-region crop; rendered from a working copy with the purchaser line redacted; crop verified pixel-identical to the unredacted page region and 30 pt clear of page head and foot
- Cleaned file: assets/diagrams/ast-0116-enemy-attack-resolution-strip.png
- Proposed placement: Enemy Turns chapter
- Final usage: not placed: reference plate: it carries source text, shows components these rules do not use, or duplicates a placed plate
- Licensing: authorised under owner's rights assertion
- Notes: Vector attack symbol with small dice and wound-token rasters (about 150 ppi) on the page parchment; strip only, the example-box frame and the italic caption below it are outside the crop. Phase 0 note: Vector + small rasters.

### [AST-0117] Mega-boss game board (round Chariot arena; Kalameet forest board)
- Source: DS-EC-Rules-Web.pdf, p.5
- Type: diagram
- Region: p.5 top (board raster 846×1245 region) and BDK p.5
- Dimensions: 3 files; 604–1352 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/photography/ast-0117-*.png (3 files, listed as sub-entries AST-0117.1 to AST-0117.3)
- Proposed placement: Mega Boss chapter (if included)
- Final usage: 3 of 3 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-BDK-Rules-web.pdf p.5; DS-EC-Rules-Web.pdf p.5; DS-EC-Rules-Web.pdf p.9. Phase 0 note: SFG tile art; crop via pdfimages.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0117.1 | Black Dragon Kalameet mega-boss game board (forest clearing, node markers printed on the board) | `assets/photography/ast-0117-mega-boss-board-kalameet-forest.png` | 1352×1352 px | DS-BDK-Rules-web.pdf, p.5 | object 663 (pdfimages #99) | pdfimages -png p.5 image #99 (object 663, 1352×1352 cmyk + soft mask #100 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Square board art with its own soft mask (rounded outline). Final usage: gallery, end of chapter 16. |
| AST-0117.2 | Executioner's Chariot mega-boss game board (round arena) | `assets/photography/ast-0117-mega-boss-board-executioners-chariot-arena.png` | 654×654 px | DS-EC-Rules-Web.pdf, p.5 | object 1127 (pdfimages #143) | pdfimages -png p.5 image #143 (object 1127, 654×654 rgb + soft mask #144 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | — Final usage: gallery, end of chapter 16. |
| AST-0117.3 | Executioner's Chariot game board, second board image on p.9 | `assets/photography/ast-0117-mega-boss-board-executioners-chariot-reverse.png` | 604×604 px | DS-EC-Rules-Web.pdf, p.9 | object 1823 (pdfimages #1) | pdfimages -png p.9 image #1 (object 1823, 604×604 rgb + soft mask #2 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | — Final usage: gallery, end of chapter 16. |


#### Group: arts

### [AST-0118] 2017 core rulebook front cover composition (lava-scale texture + white logo lock-up)
- Source: DS-Core-Rules-lores.pdf, p.1
- Type: art
- Region: bbox (pt) x 0–595.3, y 0–807.9
- Dimensions: 2480×3366 px
- Format: png
- Method: pdftoppm 300 dpi full page
- Cleaned file: assets/art/ast-0118-core-2017-front-cover-composition.png
- Proposed placement: cover concept reference (texture + logo); 2E cover to be re-composed
- Final usage: front cover
- Licensing: authorised under owner's rights assertion
- Notes: Composition only: texture (AST-0142) + logo (AST-0004).

### [AST-0119] 2022 Tomb of Giants cover art (Gravelord Nito on black)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.1
- Type: art
- Region: whole embedded image (see Method)
- Dimensions: 1312×1690 px
- Format: png
- Method: pdfimages -png p.1 image #0 (1312×1690 CMYK @150 ppi)
- Cleaned file: assets/art/ast-0119-tg-2022-cover-art-gravelord-nito.png
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: chapter 20
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Gravelord Nito artwork is FromSoftware/Bandai Namco licensed art reproduced on the SFG cover; the owner's assertion covers the SFG PDF but the lead must decide whether licensed third-party key art is in scope. Provenance confirmed by the author, 2026-11-11.

### [AST-0120] Firelink-style bonfire with seated knight (full-page painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.14
- Type: art
- Region: right column illustration, ~x 385–585, y 470–790 pt
- Dimensions: 1 file; 1055 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/art/ast-0120-knight-resting-at-bonfire.jpg (sub-entry AST-0120.1)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 1 of 1 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.14. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0120.1 | Knight resting at a bonfire among ruins (2022 core p.14, 300 ppi) | `assets/art/ast-0120-knight-resting-at-bonfire.jpg` | 934×1055 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.14 | object 1152 (pdfimages #27) | pdfimages -png p.14 image #27 (object 1152, 934×1055 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The 2017 book prints a wider framing of the same painting: see the next file of AST-0121. Final usage: back cover. |

### [AST-0121] Knight resting at bonfire among ruins (full-page painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.31
- Type: art
- Region: ~x 55–585, y 150–790 pt (also core p.31)
- Dimensions: 2 files; 1142–1967 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/art/ast-0121-*.jpg (2 files, listed as sub-entries AST-0121.1 to AST-0121.2)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 2 of 2 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-Core-Rules-lores.pdf p.31; DS-TG-Rulebook-Compressed_compressed.pdf p.31. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0121.1 | Cavern tomb with a skull-studded pillar (2022 core p.31, 300 ppi) | `assets/art/ast-0121-tomb-cavern-with-skull-pillar.jpg` | 1967×1553 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.31 | object 1488 (pdfimages #1) | pdfimages -png p.31 image #1 (object 1488, 1967×1553 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The catalogue entry cites p.31 of the 2022 book for "knight resting at bonfire"; the image object on that page is this cavern painting. The bonfire painting named by the entry is the next file (2017 p.31) and AST-0120. Final usage: chapter header, chapter 5. |
| AST-0121.2 | Knight resting at a bonfire among ruins, wider framing (2017 core p.31) | `assets/art/ast-0121-knight-resting-at-bonfire-wide-2017.jpg` | 982×1142 px | DS-Core-Rules-lores.pdf, p.31 | objects 1476, 1477, 1478, 1479, 1480, 1481; bbox (pt) x 48.1–518.8, y 198.1–745.1 | pdfimages -png p.31: 6 abutting image tiles (objects 1476 to 1481) re-joined edge to edge exactly as placed on the page; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Stored in the 2017 PDF as six abutting tiles at 150 ppi. Shows more of the scene than AST-0120 (which is sharper where they overlap). Final usage: chapter header, chapter 11. |

### [AST-0122] Graveyard and ruined tower under storm sky (full-page painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: art
- Region: ~x 55–585, y 270–790 pt (also core p.32)
- Dimensions: 2 files; 984–2905 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/art/ast-0122-*.jpg (2 files, listed as sub-entries AST-0122.1 to AST-0122.2)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 1 of 2 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-Core-Rules-lores.pdf p.32; DS-TG-Rulebook-Compressed_compressed.pdf p.7. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0122.1 | Ruined keep above a misty graveyard under a storm sky, portrait framing (2022 core p.7, 300 ppi) | `assets/art/ast-0122-ruined-keep-over-graveyard-portrait.jpg` | 1970×2905 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.7 | object 793 (pdfimages #1) | pdfimages -png p.7 image #1 (object 793, 1970×2905 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Largest version in the sources. The catalogue entry cites p.32; the painting is on p.7 of the 2022 book and p.32 of the 2017 book. Final usage: chapter header, chapter 1. |
| AST-0122.2 | Ruined keep above a misty graveyard, wide framing (2017 core p.32) | `assets/art/ast-0122-ruined-keep-over-graveyard-wide-2017.jpg` | 984×900 px | DS-Core-Rules-lores.pdf, p.32 | object 1484 (pdfimages #1) | pdfimages -png p.32 image #1 (object 1484, 984×900 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Wider field of view than the portrait framing of the 2022 book, at 150 ppi. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0123] Anor Londo spires at sunset (full-page painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.23
- Type: art
- Region: full page
- Dimensions: 1 file; 2900 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/art/ast-0123-anor-londo-spires-at-sunset.jpg (sub-entry AST-0123.1)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 1 of 1 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.23. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0123.1 | Cathedral spires stacked up a cliff in red evening light (2022 core p.23, 300 ppi) | `assets/art/ast-0123-anor-londo-spires-at-sunset.jpg` | 1966×2900 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.23 | object 1278 (pdfimages #1) | pdfimages -png p.23 image #1 (object 1278, 1966×2900 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | — Final usage: chapter header, chapter 19. |

### [AST-0124] Black Knight with greatsword in flame light (character key art)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.19
- Type: art
- Region: ~x 60–300, y 450–790 pt (also core p.26)
- Dimensions: 1 file; 1384 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/art/ast-0124-black-knight-in-flames.jpg (sub-entry AST-0124.1)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 1 of 1 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.19. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0124.1 | Black Knight with greatsword, wreathed in flame (2022 core p.19, 300 ppi) | `assets/art/ast-0124-black-knight-in-flames.jpg` | 936×1384 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.19 | object 1231 (pdfimages #3) | pdfimages -png p.19 image #3 (object 1231, 936×1384 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Also in the 2017 book (p.26) at half the resolution; not extracted twice. Final usage: chapter header, chapter 8. |

### [AST-0125] Cathedral interior with light shafts (concept painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.9
- Type: art
- Region: ~x 330–585, y 300–790 pt (also core p.19)
- Dimensions: 1 file; 1383 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/art/ast-0125-ruined-cathedral-interior.jpg (sub-entry AST-0125.1)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 1 of 1 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.9. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0125.1 | Ruined cathedral interior with light through the broken apse (2022 core p.9, 300 ppi) | `assets/art/ast-0125-ruined-cathedral-interior.jpg` | 934×1383 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.9 | object 885 (pdfimages #22) | pdfimages -png p.9 image #22 (object 885, 934×1383 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Also in the 2017 book (p.19) at half the resolution; not extracted twice. Final usage: chapter header, chapter 21. |

### [AST-0126] Gravelord Nito on his throne / Tomb of Giants (concept painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.15
- Type: art
- Region: ~x 55–585, y 150–790 pt
- Dimensions: 1 file; 2131 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/art/ast-0126-tomb-colossus-and-lone-knight.jpg (sub-entry AST-0126.1)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 1 of 1 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.15. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0126.1 | Monochrome concept painting of a blade-crowned colossus with a lone knight at its foot (2022 core p.15, 300 ppi) | `assets/art/ast-0126-tomb-colossus-and-lone-knight.jpg` | 1958×2131 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.15 | object 1158 (pdfimages #1) | pdfimages -png p.15 image #1 (object 1158, 1958×2131 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | — Final usage: chapter header, chapter 16. |

### [AST-0127] Chosen Undead knight in dark forest (2017 cover-style key art)
- Source: DS-Core-Rules-lores.pdf, p.38
- Type: art
- Region: full page
- Dimensions: 1 file; 1456 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/art/ast-0127-knight-kneeling-in-dark-forest.jpg (sub-entry AST-0127.1)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 1 of 1 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-Core-Rules-lores.pdf p.38. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0127.1 | Armoured knight kneeling in a moonlit forest (2017 core p.38) | `assets/art/ast-0127-knight-kneeling-in-dark-forest.jpg` | 984×1456 px | DS-Core-Rules-lores.pdf, p.38 | object 1505 (pdfimages #1) | pdfimages -png p.38 image #1 (object 1505, 984×1456 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | 150 ppi: about 120 ppi if run across a full page. Final usage: chapter header, chapter 10. |

### [AST-0128] Ashen One with coiled sword (Dark Souls III key art)
- Source: DS-Core-Rules-lores.pdf, p.36
- Type: art
- Region: ~x 150–445, y 360–790 pt
- Dimensions: 1 file; 800 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/art/ast-0128-ashen-one-key-art.jpg (sub-entry AST-0128.1)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 1 of 1 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-Core-Rules-lores.pdf p.36. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0128.1 | Ember-scarred knight striding forward on a yellow ground (2017 core p.36) | `assets/art/ast-0128-ashen-one-key-art.jpg` | 640×800 px | DS-Core-Rules-lores.pdf, p.36 | object 1497 (pdfimages #1) | pdfimages -png p.36 image #1 (object 1497, 640×800 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | 640 px wide: column width at most. Final usage: chapter 17. |

### [AST-0129] Environment concept sketches: Undead Burg, Sen's Fortress, Anor Londo, Lothric, Darkroot, Iron Keep, Lost Bastille etc.
- Source: DS-Core-Rules-lores.pdf, p.35
- Type: art
- Region: section thumbnails on p.35/37 and on every expansion campaign page
- Dimensions: 28 files; 288–1801 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0129-* in assets/art (28 files, jpg/png, listed as sub-entries AST-0129.1 to AST-0129.28)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 16 of 28 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-BDK-Rules-web.pdf p.15; DS-Core-Rules-lores.pdf p.15; DS-Core-Rules-lores.pdf p.16; DS-Core-Rules-lores.pdf p.23; DS-Core-Rules-lores.pdf p.34; DS-Core-Rules-lores.pdf p.35; DS-Core-Rules-lores.pdf p.37; DS-Darkroot-Rules-web.pdf p.11; DS-EC-Rules-Web.pdf p.19; DS-Explorers-Rules-Web.pdf p.15; DS-IronKeep-Rules-Web.pdf p.7; DS-Phantoms-Rules-lores.pdf p.16 and others. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0129.1 | Environment sketch: gate tower at the end of a walled road (2017 core p.35) | `assets/art/ast-0129-env-gate-tower-2017.png` | 639×455 px | DS-Core-Rules-lores.pdf, p.35 | object 1492 (pdfimages #1) | pdfimages -png p.35 image #1 (object 1492, 639×455 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.2 | Environment sketch: boulder engine in a dark fortress (2017 core p.35) | `assets/art/ast-0129-env-fortress-boulder-engine-2017.png` | 639×455 px | DS-Core-Rules-lores.pdf, p.35 | object 1493 (pdfimages #2) | pdfimages -png p.35 image #2 (object 1493, 639×455 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.3 | Environment sketch: white cathedral city (2017 core p.35) | `assets/art/ast-0129-env-white-city-spires-2017.png` | 639×455 px | DS-Core-Rules-lores.pdf, p.35 | object 1494 (pdfimages #3) | pdfimages -png p.35 image #3 (object 1494, 639×455 rgb, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.4 | Key art: knight before a burning town and castle (2017 core p.37) | `assets/art/ast-0129-env-burning-town-below-castle.png` | 639×451 px | DS-Core-Rules-lores.pdf, p.37 | object 1500 (pdfimages #1) | pdfimages -png p.37 image #1 (object 1500, 639×451 rgb, no soft mask); native resolution, no resampling | — Final usage: chapter 5. |
| AST-0129.5 | Key art: armoured figure trailing frost, sword drawn (2017 core p.37) | `assets/art/ast-0129-env-frost-knight.png` | 639×455 px | DS-Core-Rules-lores.pdf, p.37 | object 1501 (pdfimages #2) | pdfimages -png p.37 image #2 (object 1501, 639×455 rgb, no soft mask); native resolution, no resampling | — Final usage: chapter 20. |
| AST-0129.6 | Key art: veiled figure with a flaming curved blade (2017 core p.37) | `assets/art/ast-0129-env-dancer-flaming-blade.png` | 639×455 px | DS-Core-Rules-lores.pdf, p.37 | object 1502 (pdfimages #3) | pdfimages -png p.37 image #3 (object 1502, 639×455 rgb, no soft mask); native resolution, no resampling | — Final usage: chapter 19. |
| AST-0129.7 | Environment sketch: boulder engine in a dark fortress, squarer framing (Phantoms p.17, 300 ppi) | `assets/art/ast-0129-env-fortress-boulder-engine-phantoms.png` | 710×682 px | DS-Phantoms-Rules-lores.pdf, p.17 | object 470 (pdfimages #2) | pdfimages -png p.17 image #2 (object 470, 710×682 cmyk, no soft mask); native resolution, no resampling | — Final usage: chapter 10. |
| AST-0129.8 | Environment sketch: gate tower, upright framing (Phantoms p.17, 300 ppi) | `assets/art/ast-0129-env-gate-tower-phantoms.png` | 583×657 px | DS-Phantoms-Rules-lores.pdf, p.17 | object 469 (pdfimages #1) | pdfimages -png p.17 image #1 (object 469, 583×657 cmyk, no soft mask); native resolution, no resampling | — Final usage: chapter 2. |
| AST-0129.9 | Environment sketch: white cathedral city, close framing (Phantoms p.17, 300 ppi) | `assets/art/ast-0129-env-white-city-spires-phantoms.png` | 579×585 px | DS-Phantoms-Rules-lores.pdf, p.17 | object 471 (pdfimages #3) | pdfimages -png p.17 image #3 (object 471, 579×585 cmyk, no soft mask); native resolution, no resampling | — Final usage: chapter 6. |
| AST-0129.10 | Campaign art: sealed stone door split by white light (Darkroot p.11) | `assets/art/ast-0129-env-sealed-door-of-light.jpg` | 844×846 px | DS-Darkroot-Rules-web.pdf, p.11 | object 438 (pdfimages #2) | pdfimages -png p.11 image #2 (object 438, 844×846 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | In-game render rather than a painting. Final usage: chapter 20. |
| AST-0129.11 | Campaign art: knight wading a forest lake at night (Darkroot p.11) | `assets/art/ast-0129-env-knight-wading-forest-lake.png` | 582×632 px | DS-Darkroot-Rules-web.pdf, p.11 | object 437 (pdfimages #1) | pdfimages -png p.11 image #1 (object 437, 582×632 cmyk, no soft mask); native resolution, no resampling | In-game render rather than a painting. Same scene as the Darkroot cover, without the logo. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.12 | Campaign art: Artorias crouched with greatsword (Darkroot p.11) | `assets/art/ast-0129-env-artorias-crouched.png` | 579×534 px | DS-Darkroot-Rules-web.pdf, p.11 | object 439 (pdfimages #3) | pdfimages -png p.11 image #3 (object 439, 579×534 cmyk, no soft mask); native resolution, no resampling | — Final usage: chapter 19. |
| AST-0129.13 | Campaign art: knight facing the black dragon (Kalameet p.15) | `assets/art/ast-0129-env-kalameet-breath-and-knight.png` | 579×430 px | DS-BDK-Rules-web.pdf, p.15 | object 2025 (pdfimages #1) | pdfimages -png p.15 image #1 (object 2025, 579×430 cmyk, no soft mask); native resolution, no resampling | In-game render rather than a painting. Final usage: chapter 2. |
| AST-0129.14 | Campaign thumbnail: iron keep forecourt lit by braziers (Iron Keep p.7) | `assets/art/ast-0129-env-iron-keep-forecourt.png` | 291×292 px | DS-IronKeep-Rules-Web.pdf, p.7 | object 359 (pdfimages #3) | pdfimages -png p.7 image #3 (object 359, 291×292 rgb, no soft mask); native resolution, no resampling | In-game render rather than a painting. 291 px: thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.15 | Campaign thumbnail: figure silhouetted in a hall of tall arches (Iron Keep p.7) | `assets/art/ast-0129-env-throne-hall-arches.png` | 290×268 px | DS-IronKeep-Rules-Web.pdf, p.7 | object 360 (pdfimages #4) | pdfimages -png p.7 image #4 (object 360, 290×268 rgb, no soft mask); native resolution, no resampling | In-game render rather than a painting. 290 px: thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.16 | Campaign thumbnail: tower hung with windmill sails (Explorers p.15) | `assets/art/ast-0129-env-windmill-tower.png` | 292×355 px | DS-Explorers-Rules-Web.pdf, p.15 | object 1031 (pdfimages #2) | pdfimages -png p.15 image #2 (object 1031, 292×355 rgb + soft mask #3 (opaque everywhere, dropped)); native resolution, no resampling | 292 px: thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.17 | Campaign thumbnail: bonfire in fallen leaves (Explorers p.15) | `assets/art/ast-0129-env-bonfire-in-autumn-leaves.png` | 292×216 px | DS-Explorers-Rules-Web.pdf, p.15 | object 1030 (pdfimages #1) | pdfimages -png p.15 image #1 (object 1030, 292×216 rgb, no soft mask); native resolution, no resampling | In-game render rather than a painting. 292 px: thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.18 | Campaign thumbnail: torch-lit arena tunnel (Executioner's Chariot p.19) | `assets/art/ast-0129-env-torchlit-arena-tunnel.png` | 290×226 px | DS-EC-Rules-Web.pdf, p.19 | object 2927 (pdfimages #4) | pdfimages -png p.19 image #4 (object 2927, 290×226 rgb, no soft mask); native resolution, no resampling | In-game render rather than a painting. 290 px: thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.19 | Campaign thumbnail: warrior with a great blade above a dusk forest (Executioner's Chariot p.19) | `assets/art/ast-0129-env-greatsword-bearer-above-forest.png` | 288×225 px | DS-EC-Rules-Web.pdf, p.19 | object 2926 (pdfimages #3) | pdfimages -png p.19 image #3 (object 2926, 288×225 rgb, no soft mask); native resolution, no resampling | In-game render rather than a painting. 288 px: thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.20 | Concept painting: mass of twisted roots stained dark red (2022 core p.12, 300 ppi) | `assets/art/ast-0129-concept-blood-stained-roots.jpg` | 934×905 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.12 | object 1052 (pdfimages #52) | pdfimages -png p.12 image #52 (object 1052, 934×905 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0129 as the closest existing entry. Final usage: chapter header, chapter 9. |
| AST-0129.21 | Concept painting: great stone bridge with a city beyond (2022 core p.13, 300 ppi) | `assets/art/ast-0129-concept-stone-bridge-and-city.jpg` | 934×875 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.13 | object 1089 (pdfimages #26) | pdfimages -png p.13 image #26 (object 1089, 934×875 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0129 as the closest existing entry. Final usage: chapter header, chapter 18. |
| AST-0129.22 | Concept painting: shaft of light into a flooded cavern (2022 core p.22, 300 ppi) | `assets/art/ast-0129-concept-flooded-cavern-light-shaft.jpg` | 934×1801 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.22 | object 1272 (pdfimages #3) | pdfimages -png p.22 image #3 (object 1272, 934×1801 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0129 as the closest existing entry. Very tall (1:1.93): suits a full column height. Final usage: chapter 18. |
| AST-0129.23 | Concept painting: hooded figure seated before pillars of light (2022 core p.26, 300 ppi) | `assets/art/ast-0129-concept-hooded-figure-and-light-pillars.jpg` | 935×1376 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.26 | object 1384 (pdfimages #1) | pdfimages -png p.26 image #1 (object 1384, 935×1376 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0129 as the closest existing entry. Also in the 2017 book (p.14) at half the resolution; not extracted twice. Final usage: chapter 2. |
| AST-0129.24 | Concept sketch in green ink: ruined tower and courtyard with a crow (2017 core p.15) | `assets/art/ast-0129-concept-ruined-parish-green-ink.png` | 465×842 px | DS-Core-Rules-lores.pdf, p.15 | object 1224 (pdfimages #11) | pdfimages -png p.15 image #11 (object 1224, 465×842 rgb, no soft mask); native resolution, no resampling | No catalogue entry of its own: attached to AST-0129 as the closest existing entry. 465 px wide. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.25 | Concept painting: ruined gate overgrown with roots, wide framing (2017 core p.16) | `assets/art/ast-0129-concept-ruined-gate-with-roots-wide.jpg` | 984×693 px | DS-Core-Rules-lores.pdf, p.16 | object 1235 (pdfimages #1) | pdfimages -png p.16 image #1 (object 1235, 984×693 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0129 as the closest existing entry. The Darkroot book prints an upright framing at 300 ppi (AST-0130). Final usage: chapter header, chapter 6. |
| AST-0129.26 | Concept painting: panorama of ruins in mist (2017 core p.23) | `assets/art/ast-0129-concept-misty-ruins-panorama.png` | 984×501 px | DS-Core-Rules-lores.pdf, p.23 | object 1333 (pdfimages #2) | pdfimages -png p.23 image #2 (object 1333, 984×501 rgb, no soft mask); native resolution, no resampling | No catalogue entry of its own: attached to AST-0129 as the closest existing entry. Already about 2:1. Final usage: chapter header, chapter 7. |
| AST-0129.27 | Concept painting: rose marble cathedral hall with a small red figure (2017 core p.34) | `assets/art/ast-0129-concept-rose-marble-hall-2017.jpg` | 639×805 px | DS-Core-Rules-lores.pdf, p.34 | object 1489 (pdfimages #1) | pdfimages -png p.34 image #1 (object 1489, 639×805 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0129 as the closest existing entry. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0129.28 | Concept painting: rose marble hall, lower part at 300 ppi (Phantoms p.16) | `assets/art/ast-0129-concept-rose-marble-hall-phantoms.jpg` | 808×759 px | DS-Phantoms-Rules-lores.pdf, p.16 | object 452 (pdfimages #1) | pdfimages -png p.16 image #1 (object 452, 808×759 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0129 as the closest existing entry. Sharper crop of the lower half of the 2017 p.34 painting. Final usage: chapter 19. |

### [AST-0130] Expansion cover key art (Phantoms knight, Darkroot Artorias/Hydra lake, Iron Keep gate, Explorers Pursuer, Kalameet, Executioner's Chariot)
- Source: DS-*-Rules-*.pdf, p.1
- Type: art
- Region: cover art rasters 1754×2551 (300 ppi) or ~850×1245 (150 ppi)
- Dimensions: 45 files; 605–3000 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0130-* in assets/art (45 files, jpg/png, listed as sub-entries AST-0130.1 to AST-0130.45)
- Proposed placement: cover and chapter art: candidates listed in layout/art_candidates.json
- Final usage: 32 of 45 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-BDK-Rules-web.pdf p.1; DS-BDK-Rules-web.pdf p.3; DS-BDK-Rules-web.pdf p.6; DS-BDK-Rules-web.pdf p.10; DS-BDK-Rules-web.pdf p.16; DS-Characters-Rules-lores.pdf p.1; DS-Characters-Rules-lores.pdf p.3; DS-Characters-Rules-lores.pdf p.8; DS-Darkroot-Rules-web.pdf p.1; DS-Darkroot-Rules-web.pdf p.3; DS-Darkroot-Rules-web.pdf p.8; DS-Darkroot-Rules-web.pdf p.9 and others. Phase 0 note: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Held, not extracted, in Phase 0. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0130.1 | Phantoms expansion front cover: white phantom duellist on black, logo baked in | `assets/art/ast-0130-cover-phantoms.jpg` | 1754×2551 px | DS-Phantoms-Rules-lores.pdf, p.1 | object 24 (pdfimages #0) | pdfimages -png p.1 image #0 (object 24, 1754×2551 index + soft mask #1 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The white "DARK SOULS / THE BOARD GAME" logo lock-up is baked into the image (lower third). The same figure without the logo is AST-0138 (phantom figure with soft mask). Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.2 | Phantoms front cover, art above the logo | `assets/art/ast-0130-cover-phantoms-art-only.jpg` | 1754×1569 px | DS-Phantoms-Rules-lores.pdf, p.1 | object 24 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 24, 1754×2551 index + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. Final usage: chapter header, chapter 12. |
| AST-0130.3 | Black Dragon Kalameet expansion front cover, logo baked in | `assets/art/ast-0130-cover-kalameet.jpg` | 1754×2551 px | DS-BDK-Rules-web.pdf, p.1 | object 22 (pdfimages #0) | pdfimages -png p.1 image #0 (object 22, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The white "DARK SOULS / THE BOARD GAME" logo lock-up is baked into the image (lower third). The same painting without the logo, and larger, is the next file. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.4 | Black Dragon Kalameet hanging in a sulphur sky above a lone knight, no logo (Kalameet p.6, largest version) | `assets/art/ast-0130-kalameet-over-lone-knight.jpg` | 1776×3000 px | DS-BDK-Rules-web.pdf, p.6 | object 693 (pdfimages #1) | pdfimages -png p.6 image #1 (object 693, 1776×3000 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free and larger than the cover image. A third, smaller copy on p.14 was not extracted. Final usage: chapter header, chapter 15. |
| AST-0130.5 | Executioner's Chariot expansion front cover, logo baked in | `assets/art/ast-0130-cover-executioners-chariot.jpg` | 846×1245 px | DS-EC-Rules-Web.pdf, p.1 | object 21 (pdfimages #0) | pdfimages -png p.1 image #0 (object 21, 846×1245 rgb + soft mask #1 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The white "DARK SOULS / THE BOARD GAME" logo lock-up is baked into the image (lower third). 846 px wide (150 ppi). Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.6 | Executioner's Chariot front cover, art above the logo | `assets/art/ast-0130-cover-executioners-chariot-art-only.jpg` | 846×766 px | DS-EC-Rules-Web.pdf, p.1 | object 21 (pdfimages #0), crop px (0, 0, 846, 766) | pdfimages -png p.1 image #0 (object 21, 846×1245 rgb + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 846, 766) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.7 | Darkroot expansion front cover, logo baked in | `assets/art/ast-0130-cover-darkroot.jpg` | 1754×2551 px | DS-Darkroot-Rules-web.pdf, p.1 | object 22 (pdfimages #0) | pdfimages -png p.1 image #0 (object 22, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The white "DARK SOULS / THE BOARD GAME" logo lock-up is baked into the image (lower third). Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.8 | Darkroot front cover, art above the logo | `assets/art/ast-0130-cover-darkroot-art-only.jpg` | 1754×1569 px | DS-Darkroot-Rules-web.pdf, p.1 | object 22 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 22, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image. Final usage: chapter header, chapter 14. |
| AST-0130.9 | Iron Keep expansion front cover, logo baked in | `assets/art/ast-0130-cover-iron-keep.jpg` | 850×1245 px | DS-IronKeep-Rules-Web.pdf, p.1 | object 20 (pdfimages #0) | pdfimages -png p.1 image #0 (object 20, 850×1245 rgb + soft mask #1 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The white "DARK SOULS / THE BOARD GAME" logo lock-up is baked into the image (lower third). 850 px wide (150 ppi). Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.10 | Iron Keep front cover, art above the logo | `assets/art/ast-0130-cover-iron-keep-art-only.jpg` | 850×766 px | DS-IronKeep-Rules-Web.pdf, p.1 | object 20 (pdfimages #0), crop px (0, 0, 850, 766) | pdfimages -png p.1 image #0 (object 20, 850×1245 rgb + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 850, 766) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image. Final usage: chapter 16. |
| AST-0130.11 | Explorers expansion front cover, logo baked in | `assets/art/ast-0130-cover-explorers.jpg` | 849×1245 px | DS-Explorers-Rules-Web.pdf, p.1 | object 21 (pdfimages #0) | pdfimages -png p.1 image #0 (object 21, 849×1245 rgb + soft mask #1 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The white "DARK SOULS / THE BOARD GAME" logo lock-up is baked into the image (lower third). 849 px wide (150 ppi). Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.12 | Explorers front cover, art above the logo | `assets/art/ast-0130-cover-explorers-art-only.jpg` | 849×766 px | DS-Explorers-Rules-Web.pdf, p.1 | object 21 (pdfimages #0), crop px (0, 0, 849, 766) | pdfimages -png p.1 image #0 (object 21, 849×1245 rgb + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 849, 766) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image. Final usage: chapter header, chapter 13. |
| AST-0130.13 | Characters expansion front cover, logo baked in | `assets/art/ast-0130-cover-characters.jpg` | 1754×2551 px | DS-Characters-Rules-lores.pdf, p.1 | object 21 (pdfimages #0) | pdfimages -png p.1 image #0 (object 21, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The white "DARK SOULS / THE BOARD GAME" logo lock-up is baked into the image (lower third). Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.14 | Characters front cover, art above the logo | `assets/art/ast-0130-cover-characters-art-only.jpg` | 1754×1569 px | DS-Characters-Rules-lores.pdf, p.1 | object 21 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 21, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image; the figure is cut at the knee by the crop. Final usage: chapter header, chapter 4. |
| AST-0130.15 | Phantoms back cover: red phantom knight on black | `assets/art/ast-0130-backcover-phantoms-red-invader.jpg` | 1754×2489 px | DS-Phantoms-Rules-lores.pdf, p.20 | object 507 (pdfimages #2) | pdfimages -png p.20 image #2 (object 507, 1754×2489 index + soft mask #3 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | — Final usage: chapter 20. |
| AST-0130.16 | Black Dragon Kalameet back cover: the dragon close, fading to black | `assets/art/ast-0130-backcover-kalameet-close.jpg` | 1517×2203 px | DS-BDK-Rules-web.pdf, p.16 | object 2040 (pdfimages #1) | pdfimages -png p.16 image #1 (object 2040, 1517×2203 cmyk + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The lower third is black (room for back-cover text). Final usage: chapter header, chapter 17. |
| AST-0130.17 | Executioner's Chariot back cover: torch-bearer on a rope bridge, fading to black | `assets/art/ast-0130-backcover-chariot-rope-bridge.jpg` | 846×1245 px | DS-EC-Rules-Web.pdf, p.20 | object 2937 (pdfimages #1) | pdfimages -png p.20 image #1 (object 2937, 846×1245 rgb + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | In-game render rather than a painting. 846 px wide (150 ppi). The lower third is black. Final usage: chapter 18. |
| AST-0130.18 | Darkroot back cover: Artorias on black | `assets/art/ast-0130-backcover-darkroot-artorias.jpg` | 1754×2551 px | DS-Darkroot-Rules-web.pdf, p.12 | object 453 (pdfimages #2) | pdfimages -png p.12 image #2 (object 453, 1754×2551 cmyk + soft mask #3 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | — Final usage: chapter 15. |
| AST-0130.19 | Iron Keep back cover: crumbling tower in a lake of fire | `assets/art/ast-0130-backcover-iron-keep-tower.jpg` | 850×1246 px | DS-IronKeep-Rules-Web.pdf, p.8 | object 373 (pdfimages #2) | pdfimages -png p.8 image #2 (object 373, 850×1246 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | 850 px wide (150 ppi). Final usage: chapter 2. |
| AST-0130.20 | Explorers back cover: ruined stone arch on a mountain path | `assets/art/ast-0130-backcover-explorers-stone-arch.jpg` | 849×1245 px | DS-Explorers-Rules-Web.pdf, p.16 | object 1046 (pdfimages #2) | pdfimages -png p.16 image #2 (object 1046, 849×1245 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | 849 px wide (150 ppi). Final usage: chapter header, chapter 22. |
| AST-0130.21 | Characters back cover: suit of dark plate armour on black | `assets/art/ast-0130-backcover-characters-armour.jpg` | 1754×2551 px | DS-Characters-Rules-lores.pdf, p.8 | object 200 (pdfimages #1) | pdfimages -png p.8 image #1 (object 200, 1754×2551 cmyk + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.22 | Phantoms p.3: red phantom figure on black | `assets/art/ast-0130-phantoms-red-phantom-smear.jpg` | 1259×2106 px | DS-Phantoms-Rules-lores.pdf, p.3 | object 62 (pdfimages #1) | pdfimages -png p.3 image #1 (object 62, 1259×2106 index + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Final usage: chapter 7. |
| AST-0130.23 | Phantoms p.9: armoured knight silhouetted against blue spirits | `assets/art/ast-0130-phantoms-knight-among-blue-spirits.jpg` | 1559×881 px | DS-Phantoms-Rules-lores.pdf, p.9 | object 265 (pdfimages #5) | pdfimages -png p.9 image #5 (object 265, 1559×881 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Final usage: chapter header, chapter 20. |
| AST-0130.24 | Phantoms p.12: monochrome sketch of warriors on a great stair | `assets/art/ast-0130-phantoms-procession-sketch.jpg` | 1258×760 px | DS-Phantoms-Rules-lores.pdf, p.12 | object 386 (pdfimages #1) | pdfimages -png p.12 image #1 (object 386, 1258×760 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Final usage: chapter 17. |
| AST-0130.25 | Phantoms p.13: ruined castle of spires on a cliff | `assets/art/ast-0130-phantoms-ruined-castle-on-cliff.jpg` | 1416×1287 px | DS-Phantoms-Rules-lores.pdf, p.13 | object 419 (pdfimages #1) | pdfimages -png p.13 image #1 (object 419, 1416×1287 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Final usage: chapter header, chapter 2. |
| AST-0130.26 | Phantoms p.15: shanty town on stilts in a murky cavern | `assets/art/ast-0130-phantoms-shanty-town-in-the-murk.jpg` | 1250×1609 px | DS-Phantoms-Rules-lores.pdf, p.15 | object 440 (pdfimages #1) | pdfimages -png p.15 image #1 (object 440, 1250×1609 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. The 2017 book (p.21) carries a smaller copy inside a photographed art-book spread with caption text; that object was not extracted. Final usage: chapter header, Appendix B. |
| AST-0130.27 | Kalameet p.3: the black dragon close from below | `assets/art/ast-0130-kalameet-close-from-below.jpg` | 640×1080 px | DS-BDK-Rules-web.pdf, p.3 | object 56 (pdfimages #1) | pdfimages -png p.3 image #1 (object 56, 640×1080 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | In-game render rather than a painting. Uncropped frame of the back-cover image, 640 px wide. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.28 | Kalameet p.10: overgrown temple gate in a red-gold forest | `assets/art/ast-0130-kalameet-overgrown-forest-gate.jpg` | 1402×1542 px | DS-BDK-Rules-web.pdf, p.10 | object 1348 (pdfimages #1) | pdfimages -png p.10 image #1 (object 1348, 1402×1542 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Final usage: chapter 5. |
| AST-0130.29 | Executioner's Chariot p.3: knight seated by a bonfire below a cliff fortress | `assets/art/ast-0130-chariot-knight-by-bonfire.jpg` | 626×1063 px | DS-EC-Rules-Web.pdf, p.3 | object 55 (pdfimages #1) | pdfimages -png p.3 image #1 (object 55, 626×1063 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | In-game render rather than a painting. 626 px wide. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.30 | Executioner's Chariot p.6: rope bridge under a green dusk sky | `assets/art/ast-0130-chariot-rope-bridge-at-dusk.png` | 626×504 px | DS-EC-Rules-Web.pdf, p.6 | object 1151 (pdfimages #1) | pdfimages -png p.6 image #1 (object 1151, 626×504 rgb, no soft mask); native resolution, no resampling | In-game render rather than a painting. 626 px wide. Final usage: chapter 5. |
| AST-0130.31 | Executioner's Chariot p.10: the chariot horse breathing mist in the arena | `assets/art/ast-0130-chariot-horse-in-the-arena.png` | 626×691 px | DS-EC-Rules-Web.pdf, p.10 | object 1858 (pdfimages #1) | pdfimages -png p.10 image #1 (object 1858, 626×691 rgb, no soft mask); native resolution, no resampling | In-game render rather than a painting. 626 px wide. Final usage: chapter 16. |
| AST-0130.32 | Executioner's Chariot p.13: torch-bearer in a fire-lit corridor | `assets/art/ast-0130-chariot-torch-bearer-in-corridor.jpg` | 626×879 px | DS-EC-Rules-Web.pdf, p.13 | object 2731 (pdfimages #1) | pdfimages -png p.13 image #1 (object 2731, 626×879 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | In-game render rather than a painting. 626 px wide. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.33 | Executioner's Chariot p.15: red-armoured warrior fighting shield-bearing skeletons | `assets/art/ast-0130-chariot-warrior-against-skeletons.png` | 626×502 px | DS-EC-Rules-Web.pdf, p.15 | object 2845 (pdfimages #1) | pdfimages -png p.15 image #1 (object 2845, 626×502 rgb, no soft mask); native resolution, no resampling | In-game render rather than a painting. 626 px wide. Final usage: chapter 20. |
| AST-0130.34 | Darkroot p.3: ink sketch of a great gravestone ringed by planted swords | `assets/art/ast-0130-darkroot-grave-with-planted-swords.jpg` | 1055×1759 px | DS-Darkroot-Rules-web.pdf, p.3 | object 74 (pdfimages #1) | pdfimages -png p.3 image #1 (object 74, 1055×1759 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Final usage: chapter header, Appendix A. |
| AST-0130.35 | Darkroot p.8: ruined gate overgrown with roots, upright framing (300 ppi) | `assets/art/ast-0130-darkroot-ruined-gate-with-roots-upright.jpg` | 1259×1484 px | DS-Darkroot-Rules-web.pdf, p.8 | object 388 (pdfimages #1) | pdfimages -png p.8 image #1 (object 388, 1259×1484 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Upright, sharper framing of the 2017 p.16 painting. Final usage: chapter 8. |
| AST-0130.36 | Darkroot p.9: Artorias concept art, front and back views | `assets/art/ast-0130-darkroot-artorias-concept-front-and-back.jpg` | 1250×1480 px | DS-Darkroot-Rules-web.pdf, p.9 | object 409 (pdfimages #1) | pdfimages -png p.9 image #1 (object 409, 1250×1480 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Final usage: chapter 11. |
| AST-0130.37 | Darkroot p.10: sketch of an overgrown arched stone doorway | `assets/art/ast-0130-darkroot-overgrown-stone-doorway.jpg` | 808×1209 px | DS-Darkroot-Rules-web.pdf, p.10 | object 420 (pdfimages #1) | pdfimages -png p.10 image #1 (object 420, 808×1209 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Final usage: chapter 12. |
| AST-0130.38 | Iron Keep p.4: iron throne-keep in clouds of fire, wide | `assets/art/ast-0130-iron-keep-throne-in-fire-clouds.png` | 628×317 px | DS-IronKeep-Rules-Web.pdf, p.4 | object 319 (pdfimages #1) | pdfimages -png p.4 image #1 (object 319, 628×317 rgb, no soft mask); native resolution, no resampling | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. 628 px wide (about 2:1): too small for a full-width strip. Final usage: chapter 22. |
| AST-0130.39 | Explorers p.3: gothic castle over water in red dusk | `assets/art/ast-0130-explorers-castle-at-dusk.jpg` | 630×1051 px | DS-Explorers-Rules-Web.pdf, p.3 | object 55 (pdfimages #1) | pdfimages -png p.3 image #1 (object 55, 630×1051 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. 630 px wide. Final usage: chapter 7. |
| AST-0130.40 | Explorers p.7: shrine mirrored in still water under a column of light | `assets/art/ast-0130-explorers-shrine-mirrored-in-water.jpg` | 632×1080 px | DS-Explorers-Rules-Web.pdf, p.7 | object 797 (pdfimages #1) | pdfimages -png p.7 image #1 (object 797, 632×1080 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. 632 px wide. Final usage: chapter 22. |
| AST-0130.41 | Explorers p.8: rain-lashed ruined stair lined with statues | `assets/art/ast-0130-explorers-rain-lashed-ruined-stair.png` | 628×680 px | DS-Explorers-Rules-Web.pdf, p.8 | object 806 (pdfimages #1) | pdfimages -png p.8 image #1 (object 806, 628×680 rgb, no soft mask); native resolution, no resampling | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. 628 px wide. Final usage: chapter 5. |
| AST-0130.42 | Explorers p.9: chapel interior with a great stained-glass window | `assets/art/ast-0130-explorers-chapel-with-stained-glass.jpg` | 632×800 px | DS-Explorers-Rules-Web.pdf, p.9 | object 815 (pdfimages #1) | pdfimages -png p.9 image #1 (object 815, 632×800 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. 632 px wide. Final usage: chapter 3. |
| AST-0130.43 | Explorers p.13: lone wanderer before a great buried doorway | `assets/art/ast-0130-explorers-wanderer-before-buried-door.jpg` | 632×792 px | DS-Explorers-Rules-Web.pdf, p.13 | object 1001 (pdfimages #1) | pdfimages -png p.13 image #1 (object 1001, 632×792 rgb, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. 632 px wide. Final usage: chapter 2. |
| AST-0130.44 | Explorers p.14: knight on a fallen column in a golden hall | `assets/art/ast-0130-explorers-knight-in-golden-hall.png` | 406×605 px | DS-Explorers-Rules-Web.pdf, p.14 | object 1012 (pdfimages #1) | pdfimages -png p.14 image #1 (object 1012, 406×605 rgb, no soft mask); native resolution, no resampling | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. 406 px wide. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0130.45 | Characters p.3: lone pilgrim before a golden city of spires (largest painting with a figure) | `assets/art/ast-0130-characters-pilgrim-before-golden-city.jpg` | 1778×2969 px | DS-Characters-Rules-lores.pdf, p.3 | object 55 (pdfimages #1) | pdfimages -png p.3 image #1 (object 55, 1778×2969 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | No catalogue entry of its own: attached to AST-0130 as the closest existing entry. Final usage: chapter header, chapter 3. |


#### Group: photographys

### [AST-0131] Miniature renders, 2022 core: Cleric, Pyromancer, Thief; Giant Skeleton Archer/Soldier, Necromancer, Skeleton Archer/Beast/Soldier; Black Knight; Gravelord Nito
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.4
- Type: photography
- Region: Game Contents pp.4–5: grey resin renders with drop shadows (CMYK rasters 457–666 px with soft masks)
- Dimensions: 11 files; 212–903 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/photography/ast-0131-*.png (11 files, listed as sub-entries AST-0131.1 to AST-0131.11)
- Proposed placement: Components appendix / chapter openers
- Final usage: 11 of 11 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.4; DS-TG-Rulebook-Compressed_compressed.pdf p.5. Phase 0 note: pdfimages -png -f 4 -l 5 then composite with masks (tools/composite_pdfimages.py already produced 216 composites for p.6 as a test). SFG sculpts — clean.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0131.1 | Cleric miniature render (2022 core) | `assets/photography/ast-0131-miniature-cleric.png` | 189×218 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 222 (pdfimages #77) | pdfimages -png p.4 image #77 (object 222, 189×218 cmyk + soft mask #78 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 2. |
| AST-0131.2 | Pyromancer miniature render (2022 core) | `assets/photography/ast-0131-miniature-pyromancer.png` | 150×307 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 224 (pdfimages #79) | pdfimages -png p.4 image #79 (object 224, 150×307 cmyk + soft mask #80 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 2. |
| AST-0131.3 | Thief miniature render (2022 core) | `assets/photography/ast-0131-miniature-thief.png` | 199×212 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 226 (pdfimages #81) | pdfimages -png p.4 image #81 (object 226, 199×212 cmyk + soft mask #82 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 2. |
| AST-0131.4 | Giant Skeleton Archer miniature render | `assets/photography/ast-0131-miniature-giant-skeleton-archer.png` | 307×365 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 216 (pdfimages #71) | pdfimages -png p.4 image #71 (object 216, 307×365 cmyk + soft mask #72 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 1. |
| AST-0131.5 | Necromancer miniature render | `assets/photography/ast-0131-miniature-necromancer.png` | 162×255 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 218 (pdfimages #73) | pdfimages -png p.4 image #73 (object 218, 162×255 cmyk + soft mask #74 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 2. |
| AST-0131.6 | Giant Skeleton Soldier miniature render | `assets/photography/ast-0131-miniature-giant-skeleton-soldier.png` | 261×362 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 220 (pdfimages #75) | pdfimages -png p.4 image #75 (object 220, 261×362 cmyk + soft mask #76 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 1. |
| AST-0131.7 | Skeleton Archer miniature render | `assets/photography/ast-0131-miniature-skeleton-archer.png` | 148×299 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 215 (pdfimages #69) | pdfimages -png p.4 image #69 (object 215, 148×299 cmyk + soft mask #70 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 1. |
| AST-0131.8 | Skeleton Beast miniature render | `assets/photography/ast-0131-miniature-skeleton-beast.png` | 379×218 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 206 (pdfimages #63) | pdfimages -png p.4 image #63 (object 206, 379×218 cmyk + soft mask #64 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 2. |
| AST-0131.9 | Skeleton Soldier miniature render | `assets/photography/ast-0131-miniature-skeleton-soldier.png` | 211×266 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 208 (pdfimages #65) | pdfimages -png p.4 image #65 (object 208, 211×266 cmyk + soft mask #66 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 1. |
| AST-0131.10 | Black Knight mini-boss miniature render | `assets/photography/ast-0131-miniature-black-knight.png` | 374×382 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 382 (pdfimages #65) | pdfimages -png p.5 image #65 (object 382, 374×382 cmyk + soft mask #66 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 1. |
| AST-0131.11 | Gravelord Nito main-boss miniature render | `assets/photography/ast-0131-miniature-gravelord-nito.png` | 903×410 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | object 380 (pdfimages #63) | pdfimages -png p.5 image #63 (object 380, 903×410 cmyk + soft mask #64 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 1. |

### [AST-0132] Token and terrain photography set (wound/soul tokens, luck, heroic action, estus, ember, aggro, party, condition tokens, spark dial, chest, gravestone, barrel, shrine, lever, torch, trap, skeleton ball, Patches, enemy tokens)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: “Tokens and Terrain Elements” rows (146 masked rasters, 93–284 px)
- Dimensions: 9 files; 100–3885 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/photography/ast-0132-*.png (9 files, listed as sub-entries AST-0132.1 to AST-0132.9)
- Proposed placement: Components appendix; inline token references
- Final usage: 4 of 9 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-Explorers-Rules-Web.pdf p.5; DS-TG-Rulebook-Compressed_compressed.pdf p.6. Phase 0 note: Already split to RGBA in work/pdfimages/TG_p06_rgba/ (unlabelled); needs naming pass using the p.6 captions.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0132.1 | Spark dial (2022 core, p.6) | `assets/photography/ast-0132-token-spark-dial.png` | 175×175 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 720 (pdfimages #118) | pdfimages -png p.6 image #118 (object 720, 175×175 index + soft mask #119 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | — Final usage: gallery, end of chapter 11. |
| AST-0132.2 | Gravestone terrain piece render (Explorers) | `assets/photography/ast-0132-token-terrain-gravestone-render.png` | 149×254 px | DS-Explorers-Rules-Web.pdf, p.5 | object 599 (pdfimages #300) | pdfimages -png p.5 image #300 (object 599, 149×254 rgb + soft mask #301 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 14. |
| AST-0132.3 | Bonfire terrain piece render (Explorers) | `assets/photography/ast-0132-token-terrain-bonfire-render.png` | 149×220 px | DS-Explorers-Rules-Web.pdf, p.5 | object 595 (pdfimages #296) | pdfimages -png p.5 image #296 (object 595, 149×220 rgb + soft mask #297 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0132.4 | Barrels terrain piece render (Explorers) | `assets/photography/ast-0132-token-terrain-barrels-render.png` | 92×100 px | DS-Explorers-Rules-Web.pdf, p.5 | object 603 (pdfimages #304) | pdfimages -png p.5 image #304 (object 603, 92×100 rgb + soft mask #305 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | — Final usage: gallery, end of chapter 14. |
| AST-0132.5 | Treasure Chest terrain piece render (Explorers) | `assets/photography/ast-0132-token-terrain-treasure-chest-render.png` | 267×132 px | DS-Explorers-Rules-Web.pdf, p.5 | object 597 (pdfimages #298) | pdfimages -png p.5 image #298 (object 597, 267×132 rgb + soft mask #299 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 14. |
| AST-0132.6 | Token and terrain-token array as arranged on p.6 (soul, wound, aggro, luck, heroic action, estus, ember, party, condition and terrain tokens, spark dial), captions omitted | `assets/photography/ast-0132-token-array-souls-wounds-conditions-terrain.png` | 3885×1359 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | objects 640, 643, 646, 649, 652, 655, 658, 661, 664, 667, 670, 673, 676, 679, 682, 685, 688, 693, 696, 699, 702, 705, 708, 711, 714, 717, 720, 725, 746, 753, 760, 767; bbox (pt) x 98.4–576.5, y 294.0–463.1 | composite of 48 placements of 32 embedded image objects (objects 640, 643, 646, 649, 652, 655, 658, 661, 664, 667, 670, 673, 676, 679, 682, 685, 688, 693, 696, 699, 702, 705, 708, 711, 714, 717, 720, 725, 746, 753, 760, 767) decoded with pdfimages -png + soft masks, re-assembled with their page placement matrices in draw order on a transparent ground at 600 px/in of page size (objects are ~149 ppi as placed, i.e. upsampled ×4.0 bicubic); no page render involved | Source objects are only ~150 ppi at page size; this composite is an upsample for layout convenience, keep it small in print (≤ the size it has in the source rulebook, about 6.6 in wide, for full sharpness). Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0132.7 | Enemy token set as arranged on p.6 (six enemy types) | `assets/photography/ast-0132-token-enemy-tokens.png` | 856×1067 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | objects 728, 731, 734, 737, 740, 743; bbox (pt) x 448.3–557.0, y 497.0–631.1 | composite of 6 placements of 6 embedded image objects (objects 728, 731, 734, 737, 740, 743) decoded with pdfimages -png + soft masks, re-assembled with their page placement matrices in draw order on a transparent ground at 600 px/in of page size (objects are ~151 ppi as placed, i.e. upsampled ×4.0 bicubic); no page render involved | Source objects are only ~150 ppi at page size; this composite is an upsample for layout convenience, keep it small in print (≤ the size it has in the source rulebook, about 1.5 in wide, for full sharpness). Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0132.8 | Soul and wound token row as arranged on p.6 (1/3/5 soul tokens, 1/3/5 wound tokens and neighbours) | `assets/photography/ast-0132-token-row-soul-and-wound-tokens.png` | 3645×250 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | objects 667, 670, 673, 676, 679, 682, 685, 688; bbox (pt) x 118.6–562.0, y 294.0–330.0 | composite of 8 placements of 8 embedded image objects (objects 667, 670, 673, 676, 679, 682, 685, 688) decoded with pdfimages -png + soft masks, re-assembled with their page placement matrices in draw order on a transparent ground at 600 px/in of page size (objects are ~150 ppi as placed, i.e. upsampled ×4.0 bicubic); no page render involved | Source objects are only ~150 ppi at page size; this composite is an upsample for layout convenience, keep it small in print (≤ the size it has in the source rulebook, about 6.2 in wide, for full sharpness). Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0132.9 | Terrain token row as arranged on p.6 (gravestone, shrine, barrel, lever, trap, skeleton ball and neighbours) | `assets/photography/ast-0132-token-row-terrain-tokens.png` | 3336×317 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | objects 693, 696, 699, 702, 705, 708, 711, 714, 717; bbox (pt) x 164.3–570.6, y 419.0–463.1 | composite of 9 placements of 9 embedded image objects (objects 693, 696, 699, 702, 705, 708, 711, 714, 717) decoded with pdfimages -png + soft masks, re-assembled with their page placement matrices in draw order on a transparent ground at 600 px/in of page size (objects are ~149 ppi as placed, i.e. upsampled ×4.0 bicubic); no page render involved | Source objects are only ~150 ppi at page size; this composite is an upsample for layout convenience, keep it small in print (≤ the size it has in the source rulebook, about 5.6 in wide, for full sharpness). Final usage: not placed: reserve image, or a component these rules do not use. |

### [AST-0133] Game tile photography (4 double-sided tiles; 2017: 6 exploration + bonfire + boss tiles)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: p.6 tile fan (1389×271 + 1004×166 px); core p.7 tile grid
- Dimensions: 6 files; 284–2630 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/photography/ast-0133-*.png (6 files, listed as sub-entries AST-0133.1 to AST-0133.6)
- Proposed placement: Tiles chapter
- Final usage: 5 of 6 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-Core-Rules-lores.pdf p.13; DS-TG-Rulebook-Compressed_compressed.pdf p.6. Phase 0 note: SFG tile art; low-res in PDF (≤1389 px). Larger single-tile rasters exist on TG p.11 (875×875) and core p.13 (788×788).

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0133.1 | Tomb of Giants game tile A (2022 core, tile fan on p.6) | `assets/photography/ast-0133-game-tile-tomb-of-giants-a.png` | 284×284 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 774 (pdfimages #202) | pdfimages -png p.6 image #202 (object 774, 284×284 cmyk, no soft mask); native resolution, no resampling | 284 px at ~140 ppi: small-scale use only. Final usage: gallery, end of chapter 5. |
| AST-0133.2 | Tomb of Giants game tile B (2022 core) | `assets/photography/ast-0133-game-tile-tomb-of-giants-b.png` | 284×284 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 776 (pdfimages #204) | pdfimages -png p.6 image #204 (object 776, 284×284 cmyk, no soft mask); native resolution, no resampling | 284 px at ~140 ppi: small-scale use only. Final usage: gallery, end of chapter 5. |
| AST-0133.3 | Tomb of Giants game tile C (2022 core) | `assets/photography/ast-0133-game-tile-tomb-of-giants-c.png` | 284×284 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 778 (pdfimages #206) | pdfimages -png p.6 image #206 (object 778, 284×284 cmyk, no soft mask); native resolution, no resampling | 284 px at ~140 ppi: small-scale use only. Final usage: gallery, end of chapter 5. |
| AST-0133.4 | Tomb of Giants game tile D (2022 core) | `assets/photography/ast-0133-game-tile-tomb-of-giants-d.png` | 284×284 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 780 (pdfimages #208) | pdfimages -png p.6 image #208 (object 780, 284×284 cmyk, no soft mask); native resolution, no resampling | 284 px at ~140 ppi: small-scale use only. Final usage: gallery, end of chapter 5. |
| AST-0133.5 | Bonfire tile (2017 core set), clean tile art without the anatomy call-outs | `assets/photography/ast-0133-game-tile-bonfire-2017.png` | 788×788 px | DS-Core-Rules-lores.pdf, p.13 | object 1198 (pdfimages #1) | pdfimages -png p.13 image #1 (object 1198, 788×788 rgb, no soft mask); native resolution, no resampling | Opaque square tile (no soft mask in the 2017 PDF). The numbered call-outs of the p.13 anatomy diagram are vector overlays and are not in this image. Final usage: gallery, end of chapter 11. |
| AST-0133.6 | Fan of the four double-sided Tomb of Giants game tiles as arranged on p.6 | `assets/photography/ast-0133-game-tile-tomb-of-giants-fan.png` | 2630×1245 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | objects 774, 776, 778, 780; bbox (pt) x 93.9–415.4, y 484.6–640.0 | composite of 4 placements of 4 embedded image objects (objects 774, 776, 778, 780) decoded with pdfimages -png + soft masks, re-assembled with their page placement matrices in draw order on a transparent ground at 600 px/in of page size (objects are ~150 ppi as placed, i.e. upsampled ×4.0 bicubic); no page render involved | Source objects are only ~150 ppi at page size; this composite is an upsample for layout convenience, keep it small in print (≤ the size it has in the source rulebook, about 4.5 in wide, for full sharpness). Final usage: not placed: reserve image, or a component these rules do not use. |

### [AST-0134] Campaign board photograph (full strip)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: bottom of p.6, 1x Campaign board (1389×271 px)
- Dimensions: 3 files; 979–1004 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/photography/ast-0134-*.png (3 files, listed as sub-entries AST-0134.1 to AST-0134.3)
- Proposed placement: Campaign Dashboard chapter
- Final usage: not placed: reserve image, or a component these rules do not use
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.6; DS-TG-Rulebook-Compressed_compressed.pdf p.13. Phase 0 note: Higher-res halves on p.13 (979×250 each).

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0134.1 | Campaign board, left half (2022 core, p.13) | `assets/photography/ast-0134-campaign-board-left-half.png` | 979×250 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.13 | object 1080 (pdfimages #1) | pdfimages -png p.13 image #1 (object 1080, 979×250 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0134.2 | Campaign board, right half (2022 core, p.13) | `assets/photography/ast-0134-campaign-board-right-half.png` | 979×250 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.13 | object 1088 (pdfimages #13) | pdfimages -png p.13 image #13 (object 1088, 979×250 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0134.3 | Campaign board, full strip (2022 core, p.6) | `assets/photography/ast-0134-campaign-board-full-strip.png` | 1004×166 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 787 (pdfimages #215) | pdfimages -png p.6 image #215 (object 787, 1004×166 cmyk, no soft mask); native resolution, no resampling | Lower resolution than the two halves (1004 px for the whole board). Final usage: not placed: reserve image, or a component these rules do not use. |

### [AST-0135] Character dashboard photograph (clean, no call-outs)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.8
- Type: photography
- Region: 1019×685 and 1019×806 px rasters at 150 ppi
- Dimensions: 10 files; 461–1019 px on the long side
- Format: png
- Method: Phase 2B and Phase 3 (tools/extract_phase2b.py, tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/photography/ast-0135-*.png (10 files, listed as sub-entries AST-0135.1 to AST-0135.10)
- Proposed placement: Characters chapter
- Final usage: 2 of 10 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 2B and Phase 3 extraction, one file per subject from DS-Core-Rules-lores.pdf p.4; DS-Core-Rules-lores.pdf p.9; DS-Core-Rules-lores.pdf p.11; DS-TG-Rulebook-Compressed_compressed.pdf p.4; DS-TG-Rulebook-Compressed_compressed.pdf p.8. 1 related candidate(s) were held for provenance review and cleared on 2026-11-11: see Provenance Review, section F. Phase 0 note: pdfimages -png -f 8 -l 8 → images #380/#382 + masks #379/#381. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0135.1 | Character dashboard, lower section (ability box, stat grid, equipment-slot labels, endurance bar), clean, no call-outs | `assets/photography/ast-0135-character-dashboard-lower-section-a.png` | 1019×570 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.8 | object 809 (pdfimages #4), crop px (0, 236, 1019, 806) | pdfimages -png p.8 image #4 (object 809, 1019×806 cmyk + soft mask #5 composited to RGBA); cropped to px box (0, 236, 1019, 806) of the object; trimmed to alpha bounds; native resolution, no resampling | Cropped below the name band: the top 236 px of the dashboard object carry a painted class portrait and item roundels (see Provenance Review) and are left out. The cube slots of the grid and bar are transparent holes in the source mask. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0135.2 | Character dashboard, lower section with printed stat values (second dashboard state on p.8), clean | `assets/photography/ast-0135-character-dashboard-lower-section-b.png` | 1019×449 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.8 | object 807 (pdfimages #2), crop px (0, 236, 1019, 685) | pdfimages -png p.8 image #2 (object 807, 1019×685 cmyk, no soft mask); cropped to px box (0, 236, 1019, 685) of the object; native resolution, no resampling | Cropped below the name band (top 236 px with the painted class portrait left out, see Provenance Review). Opaque rectangle. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0135.3 | Character dashboard, whole, Cleric with class portrait (2022 core p.8, largest clean copy) | `assets/photography/ast-0135-character-dashboard-whole-cleric-large.png` | 1019×685 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.8 | object 807 (pdfimages #2) | pdfimages -png p.8 image #2 (object 807, 1019×685 cmyk, no soft mask); native resolution, no resampling | Phase 2B stored only the lower section of this object (AST-0135.2). Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0135.4 | Character dashboard, whole, Cleric with ability text and empty cube slots (2022 core p.8) | `assets/photography/ast-0135-character-dashboard-whole-cleric-with-ability.png` | 1019×806 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.8 | object 809 (pdfimages #4) | pdfimages -png p.8 image #4 (object 809, 1019×806 cmyk + soft mask #5 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | The cube slots of the stat grid and endurance bar are transparent in the source mask. Phase 2B stored only the lower section (AST-0135.1). Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0135.5 | Character dashboard, whole, Pyromancer with class portrait (2022 core p.4) | `assets/photography/ast-0135-character-dashboard-whole-pyromancer.png` | 666×532 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 147 (pdfimages #4) | pdfimages -png p.4 image #4 (object 147, 666×532 cmyk, no soft mask); native resolution, no resampling | — Final usage: gallery, end of chapter 3. |
| AST-0135.6 | Character dashboard, whole, Thief with class portrait (2022 core p.4) | `assets/photography/ast-0135-character-dashboard-whole-thief.png` | 666×532 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 151 (pdfimages #8) | pdfimages -png p.4 image #8 (object 151, 666×532 cmyk, no soft mask); native resolution, no resampling | — Final usage: gallery, end of chapter 3. |
| AST-0135.7 | Character dashboard, whole, Cleric with class portrait (2022 core p.4) | `assets/photography/ast-0135-character-dashboard-whole-cleric.png` | 665×531 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | object 145 (pdfimages #2) | pdfimages -png p.4 image #2 (object 145, 665×531 cmyk, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0135.8 | Character board, 2017 edition, Warrior with class portrait (2017 core p.9) | `assets/photography/ast-0135-character-board-2017-warrior.png` | 461×349 px | DS-Core-Rules-lores.pdf, p.9 | object 1061 (pdfimages #26) | pdfimages -png p.9 image #26 (object 1061, 461×349 icc, no soft mask); native resolution, no resampling | A smaller copy on p.4 was not extracted. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0135.9 | Character board, 2017 edition, Herald with class portrait (2017 core p.11) | `assets/photography/ast-0135-character-board-2017-herald.png` | 466×352 px | DS-Core-Rules-lores.pdf, p.11 | object 1171 (pdfimages #7) | pdfimages -png p.11 image #7 (object 1171, 466×352 icc, no soft mask); native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0135.10 | Character board, 2017 edition, Knight with class portrait, partly shaded (2017 core p.4) | `assets/photography/ast-0135-character-board-2017-knight.png` | 536×406 px | DS-Core-Rules-lores.pdf, p.4 | object 310 (pdfimages #99) | pdfimages -png p.4 image #99 (object 310, 536×406 icc, no soft mask); native resolution, no resampling | The source image is darkened where the next board of the fan lay over it. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0136] Dice photography (black, blue, orange, green)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: “Dice” group (4 masked rasters ~452×452 px)
- Dimensions: 5 files; 63–1260 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/photography/ast-0136-*.png (5 files, listed as sub-entries AST-0136.1 to AST-0136.5)
- Proposed placement: Combat chapter
- Final usage: 1 of 5 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.6. Phase 0 note: Also core p.7 (2017 set with green dodge dice).

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0136.1 | Black die (2022 core, p.6) | `assets/photography/ast-0136-dice-black.png` | 63×63 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 631 (pdfimages #15) | pdfimages -png p.6 image #15 (object 631, 63×63 cmyk + soft mask #16 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | ~63 px at 150 ppi: inline size only; see the dice-set composite for a larger arrangement. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0136.2 | Blue die (2022 core, p.6) | `assets/photography/ast-0136-dice-blue.png` | 64×62 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 629 (pdfimages #9) | pdfimages -png p.6 image #9 (object 629, 64×62 cmyk + soft mask #10 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | ~63 px at 150 ppi: inline size only. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0136.3 | Orange die (2022 core, p.6) | `assets/photography/ast-0136-dice-orange.png` | 64×62 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 627 (pdfimages #7) | pdfimages -png p.6 image #7 (object 627, 64×62 cmyk + soft mask #8 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | ~63 px at 150 ppi: inline size only. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0136.4 | Green die (2022 core, p.6) | `assets/photography/ast-0136-dice-green.png` | 64×63 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | object 625 (pdfimages #1) | pdfimages -png p.6 image #1 (object 625, 64×63 cmyk + soft mask #2 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | ~63 px at 150 ppi: inline size only. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0136.5 | Dice set as arranged on p.6 (5 black, 4 blue, 2 orange, 4 green) | `assets/photography/ast-0136-dice-set.png` | 1260×1050 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | objects 625, 627, 629, 631; bbox (pt) x 424.1–581.3, y 90.0–222.0 | composite of 15 placements of 4 embedded image objects (objects 625, 627, 629, 631) decoded with pdfimages -png + soft masks, re-assembled with their page placement matrices in draw order on a transparent ground at 600 px/in of page size (objects are ~151 ppi as placed, i.e. upsampled ×4.0 bicubic); no page render involved | Source objects are only ~150 ppi at page size; this composite is an upsample for layout convenience, keep it small in print (≤ the size it has in the source rulebook, about 2.2 in wide, for full sharpness). Final usage: gallery, end of chapter 8. |

### [AST-0137] Card fan photographs (encounter cards, event cards, treasure decks)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: “Cards” and “Treasure Deck” groups
- Dimensions: 8 files; 233–993 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: assets/photography/ast-0137-*.png (8 files, listed as sub-entries AST-0137.1 to AST-0137.8)
- Proposed placement: Components appendix
- Final usage: 1 of 8 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-TG-Rulebook-Compressed_compressed.pdf p.4; DS-TG-Rulebook-Compressed_compressed.pdf p.5; DS-TG-Rulebook-Compressed_compressed.pdf p.6. Phase 2B had held this entry: Provenance review: every card fan in the sources shows card faces (encounter, event, treasure and boss cards) that carry painted illustrations, so no fan was extracted. The card backs, which carry none, are extracted singly as AST-0089.1 to AST-0089.6. 2 related candidate(s) were held for provenance review and cleared on 2026-11-11: see Provenance Review, section F. Phase 0 note: Low-res; decorative only. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0137.1 | Encounter card fan: Grave Matters, The Abandoned Chest, Lakeview Refuge (2022 core p.6) | `assets/photography/ast-0137-card-fan-encounter-cards.png` | 382×282 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | objects 634, 636, 638; bbox (pt) x 78.4–265.5, y 85.0–224.5 | pdfimages -png p.6: 3 placements of 3 embedded objects (634, 636, 638), each decoded natively with its soft mask and re-assembled with its placement matrix in page draw order on a transparent ground at 150 ppi (the highest native resolution in the group); drop shadows, captions and every other page element are left out | — Final usage: gallery, end of Appendix B. |
| AST-0137.2 | Event deck: card back and the Lifegem card (2022 core p.6) | `assets/photography/ast-0137-card-fan-event-deck.png` | 233×196 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.6 | objects 783, 785; bbox (pt) x 279.4–395.2, y 123.2–221.4 | pdfimages -png p.6: 2 placements of 2 embedded objects (783, 785), each decoded natively with its soft mask and re-assembled with its placement matrix in page draw order on a transparent ground at 150 ppi (the highest native resolution in the group); drop shadows, captions and every other page element are left out | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0137.3 | Treasure deck row: class, common, legendary and boss treasure, each a card back and a face (2022 core p.5) | `assets/photography/ast-0137-card-fan-treasure-decks.png` | 993×196 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | objects 342, 344, 155, 348, 350, 353; bbox (pt) x 51.6–532.3, y 471.2–569.4 | pdfimages -png p.5: 8 placements of 6 embedded objects (342, 344, 155, 348, 350, 353), each decoded natively with its soft mask and re-assembled with its placement matrix in page draw order on a transparent ground at 150 ppi (the highest native resolution in the group); drop shadows, captions and every other page element are left out | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0137.4 | Black Knight boss cards: card back, data card and Overhead Swing behaviour card (2022 core p.5) | `assets/photography/ast-0137-card-spread-black-knight.png` | 346×197 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | objects 328, 330, 332; bbox (pt) x 82.9–253.0, y 108.8–207.3 | pdfimages -png p.5: 3 placements of 3 embedded objects (328, 330, 332), each decoded natively with its soft mask and re-assembled with its placement matrix in page draw order on a transparent ground at 150 ppi (the highest native resolution in the group); drop shadows, captions and every other page element are left out | On the page the miniature stands in front of this group; it is left out here. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0137.5 | Gravelord Nito boss cards: card back, data card and Lunging Cleave behaviour card (2022 core p.5) | `assets/photography/ast-0137-card-spread-gravelord-nito.png` | 346×197 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.5 | objects 322, 324, 326; bbox (pt) x 331.0–501.0, y 108.8–207.3 | pdfimages -png p.5: 3 placements of 3 embedded objects (322, 324, 326), each decoded natively with its soft mask and re-assembled with its placement matrix in page draw order on a transparent ground at 150 ppi (the highest native resolution in the group); drop shadows, captions and every other page element are left out | On the page the miniature stands in front of this group; it is left out here. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0137.6 | Cleric set: dashboard, class token and starting equipment cards as fanned on p.4 (2022 core) | `assets/photography/ast-0137-character-set-cleric.png` | 664×644 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | objects 145, 185, 187, 192; bbox (pt) x 90.3–253.7, y 115.0–277.4 | pdfimages -png p.4: 4 placements of 4 embedded objects (145, 185, 187, 192), each decoded natively with its soft mask and re-assembled with its placement matrix in page draw order on a transparent ground at 300 ppi (the highest native resolution in the group); drop shadows, captions and every other page element are left out | On the page the miniature stands in front of this group; it is left out here. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0137.7 | Pyromancer set: dashboard, class token and starting equipment cards as fanned on p.4 (2022 core) | `assets/photography/ast-0137-character-set-pyromancer.png` | 666×647 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | objects 147, 157, 159, 188; bbox (pt) x 255.6–419.4, y 114.3–277.4 | pdfimages -png p.4: 4 placements of 4 embedded objects (147, 157, 159, 188), each decoded natively with its soft mask and re-assembled with its placement matrix in page draw order on a transparent ground at 300 ppi (the highest native resolution in the group); drop shadows, captions and every other page element are left out | On the page the miniature stands in front of this group; it is left out here. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0137.8 | Thief set: dashboard, class token and starting equipment cards as fanned on p.4 (2022 core) | `assets/photography/ast-0137-character-set-thief.png` | 666×644 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.4 | objects 151, 153, 155, 190; bbox (pt) x 421.0–584.8, y 115.0–277.4 | pdfimages -png p.4: 4 placements of 4 embedded objects (151, 153, 155, 190), each decoded natively with its soft mask and re-assembled with its placement matrix in page draw order on a transparent ground at 300 ppi (the highest native resolution in the group); drop shadows, captions and every other page element are left out | On the page the miniature stands in front of this group; it is left out here. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0138] Expansion miniature renders (Sif, Artorias, Mushroom Parent/Child, Smelter Demon, Sir Alonne, Pursuer, Mimic, Kalameet, Executioner's Chariot, invaders, summons)
- Source: DS-*-Rules-*.pdf, p.4
- Type: photography
- Region: Contents pages of each expansion (CMYK 300 ppi rasters up to 1776×3000 px in Phantoms/BDK)
- Dimensions: 70 files; 149–2175 px on the long side
- Format: png
- Method: Phase 2B and Phase 3 (tools/extract_phase2b.py, tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0138-* in assets/art, assets/photography (70 files, jpg/png, listed as sub-entries AST-0138.1 to AST-0138.70)
- Proposed placement: Expansion module openers
- Final usage: 52 of 70 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 2B and Phase 3 extraction, one file per subject from DS-BDK-Rules-web.pdf p.4; DS-BDK-Rules-web.pdf p.11; DS-Characters-Rules-lores.pdf p.4; DS-Characters-Rules-lores.pdf p.5; DS-Darkroot-Rules-web.pdf p.4; DS-Darkroot-Rules-web.pdf p.5; DS-Darkroot-Rules-web.pdf p.7; DS-EC-Rules-Web.pdf p.4; DS-EC-Rules-Web.pdf p.16; DS-EC-Rules-Web.pdf p.17; DS-Explorers-Rules-Web.pdf p.4; DS-Explorers-Rules-Web.pdf p.5 and others. 5 related candidate(s) were held for provenance review and cleared on 2026-11-11: see Provenance Review, section F. Phase 0 note: Phantoms p.4–5 and BDK p.4 have the largest renders. Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0138.1 | Great Grey Wolf Sif miniature render (Darkroot) | `assets/photography/ast-0138-expansion-miniature-great-grey-wolf-sif.png` | 2175×1361 px | DS-Darkroot-Rules-web.pdf, p.5 | object 347 (pdfimages #43) | pdfimages -png p.5 image #43 (object 347, 2175×1361 cmyk + soft mask #44 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: figure, §17.4. |
| AST-0138.2 | Artorias miniature render (Darkroot) | `assets/photography/ast-0138-expansion-miniature-artorias.png` | 923×794 px | DS-Darkroot-Rules-web.pdf, p.5 | object 349 (pdfimages #45) | pdfimages -png p.5 image #45 (object 349, 923×794 cmyk + soft mask #46 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: figure, §17.4. |
| AST-0138.3 | Stone Knight miniature render (Darkroot) | `assets/photography/ast-0138-expansion-miniature-stone-knight.png` | 705×761 px | DS-Darkroot-Rules-web.pdf, p.5 | object 355 (pdfimages #53) | pdfimages -png p.5 image #53 (object 355, 705×761 cmyk + soft mask #54 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of Appendix A. |
| AST-0138.4 | Stone Guardian miniature render (Darkroot) | `assets/photography/ast-0138-expansion-miniature-stone-guardian.png` | 739×755 px | DS-Darkroot-Rules-web.pdf, p.5 | object 353 (pdfimages #51) | pdfimages -png p.5 image #51 (object 353, 739×755 cmyk + soft mask #52 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 7. |
| AST-0138.5 | Mushroom Parent miniature render (Darkroot) | `assets/photography/ast-0138-expansion-miniature-mushroom-parent.png` | 532×603 px | DS-Darkroot-Rules-web.pdf, p.4 | object 177 (pdfimages #36) | pdfimages -png p.4 image #36 (object 177, 532×603 cmyk + soft mask #37 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 7. |
| AST-0138.6 | Mushroom Child miniature render (Darkroot) | `assets/photography/ast-0138-expansion-miniature-mushroom-child.png` | 296×340 px | DS-Darkroot-Rules-web.pdf, p.4 | object 175 (pdfimages #34) | pdfimages -png p.4 image #34 (object 175, 296×340 cmyk + soft mask #35 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 7. |
| AST-0138.7 | Shears Scarecrow miniature render (Darkroot) | `assets/photography/ast-0138-expansion-miniature-shears-scarecrow.png` | 273×573 px | DS-Darkroot-Rules-web.pdf, p.4 | object 181 (pdfimages #40) | pdfimages -png p.4 image #40 (object 181, 273×573 cmyk + soft mask #41 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 7. |
| AST-0138.8 | Plow Scarecrow miniature render (Darkroot) | `assets/photography/ast-0138-expansion-miniature-plow-scarecrow.png` | 538×502 px | DS-Darkroot-Rules-web.pdf, p.4 | object 179 (pdfimages #38) | pdfimages -png p.4 image #38 (object 179, 538×502 cmyk + soft mask #39 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 7. |
| AST-0138.9 | Demonic Foliage miniature render (Darkroot) | `assets/photography/ast-0138-expansion-miniature-demonic-foliage.png` | 414×535 px | DS-Darkroot-Rules-web.pdf, p.4 | object 173 (pdfimages #32) | pdfimages -png p.4 image #32 (object 173, 414×535 cmyk + soft mask #33 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 7. |
| AST-0138.10 | Black Dragon Kalameet mega-boss miniature render | `assets/photography/ast-0138-expansion-miniature-black-dragon-kalameet.png` | 2036×1701 px | DS-BDK-Rules-web.pdf, p.4 | object 69 (pdfimages #3) | pdfimages -png p.4 image #3 (object 69, 2036×1701 cmyk + soft mask #4 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: figure, §17.8. |
| AST-0138.11 | Executioner's Chariot mega-boss miniature render | `assets/photography/ast-0138-expansion-miniature-executioners-chariot.png` | 708×484 px | DS-EC-Rules-Web.pdf, p.4 | object 86 (pdfimages #7) | pdfimages -png p.4 image #7 (object 86, 708×484 rgb + soft mask #8 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: figure, §17.9. |
| AST-0138.12 | Black Hollow Mage miniature render (Executioner's Chariot) | `assets/photography/ast-0138-expansion-miniature-black-hollow-mage.png` | 300×237 px | DS-EC-Rules-Web.pdf, p.4 | object 84 (pdfimages #5) | pdfimages -png p.4 image #5 (object 84, 300×237 rgb + soft mask #6 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 2. |
| AST-0138.13 | Falchion Skeleton miniature render (Executioner's Chariot) | `assets/photography/ast-0138-expansion-miniature-falchion-skeleton.png` | 311×244 px | DS-EC-Rules-Web.pdf, p.4 | object 76 (pdfimages #1) | pdfimages -png p.4 image #1 (object 76, 311×244 rgb + soft mask #2 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 2. |
| AST-0138.14 | Smelter Demon miniature render (Iron Keep) | `assets/photography/ast-0138-expansion-miniature-smelter-demon.png` | 780×502 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 289 (pdfimages #39) | pdfimages -png p.3 image #39 (object 289, 780×502 rgb + soft mask #40 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: figure, §17.5. |
| AST-0138.15 | Sir Alonne miniature render (Iron Keep) | `assets/photography/ast-0138-expansion-miniature-sir-alonne.png` | 267×574 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 298 (pdfimages #47) | pdfimages -png p.3 image #47 (object 298, 267×574 rgb + soft mask #48 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of Appendix A. |
| AST-0138.16 | Ironclad Soldier miniature render (Iron Keep) | `assets/photography/ast-0138-expansion-miniature-ironclad-soldier.png` | 193×332 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 302 (pdfimages #53) | pdfimages -png p.3 image #53 (object 302, 193×332 rgb + soft mask #54 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of Appendix A. |
| AST-0138.17 | Crystal Lizard miniature render (Iron Keep) | `assets/photography/ast-0138-expansion-miniature-crystal-lizard.png` | 149×53 px | DS-IronKeep-Rules-Web.pdf, p.3 | object 296 (pdfimages #45) | pdfimages -png p.3 image #45 (object 296, 149×53 rgb + soft mask #46 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Only 149 px wide in the source (150 ppi): small-scale use only. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 14. |
| AST-0138.18 | Mimic miniature render, open (Explorers) | `assets/photography/ast-0138-expansion-miniature-mimic.png` | 265×381 px | DS-Explorers-Rules-Web.pdf, p.4 | object 250 (pdfimages #111) | pdfimages -png p.4 image #111 (object 250, 265×381 rgb + soft mask #112 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.19 | Mimic miniature render, closed chest (Explorers) | `assets/photography/ast-0138-expansion-miniature-mimic-closed.png` | 268×135 px | DS-Explorers-Rules-Web.pdf, p.4 | object 248 (pdfimages #109) | pdfimages -png p.4 image #109 (object 248, 272×141 rgb + soft mask #110 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.20 | The Pursuer miniature render (Explorers) | `assets/photography/ast-0138-expansion-miniature-the-pursuer.png` | 332×417 px | DS-Explorers-Rules-Web.pdf, p.5 | object 583 (pdfimages #286) | pdfimages -png p.5 image #286 (object 583, 332×417 rgb + soft mask #287 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: figure, §17.6. |
| AST-0138.21 | Silver Knight Spearman miniature render (Explorers) | `assets/photography/ast-0138-expansion-miniature-silver-knight-spearman.png` | 179×334 px | DS-Explorers-Rules-Web.pdf, p.5 | object 591 (pdfimages #294) | pdfimages -png p.5 image #294 (object 591, 179×334 rgb + soft mask #295 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of Appendix A. |
| AST-0138.22 | Firebomb Hollow miniature render (Explorers) | `assets/photography/ast-0138-expansion-miniature-firebomb-hollow.png` | 146×164 px | DS-Explorers-Rules-Web.pdf, p.5 | object 589 (pdfimages #292) | pdfimages -png p.5 image #292 (object 589, 207×164 rgb + soft mask #293 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.23 | Summon: Ruined Aflis miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-ruined-aflis.png` | 382×698 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 80 (pdfimages #25) | pdfimages -png p.4 image #25 (object 80, 382×698 cmyk + soft mask #26 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 12. |
| AST-0138.24 | Summon: Eygon of Carim miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-eygon-of-carim.png` | 422×587 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 88 (pdfimages #33) | pdfimages -png p.4 image #33 (object 88, 422×587 cmyk + soft mask #34 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 12. |
| AST-0138.25 | Summon: Horace the Hushed miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-horace-the-hushed.png` | 296×498 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 76 (pdfimages #21) | pdfimages -png p.4 image #21 (object 76, 296×498 cmyk + soft mask #22 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 12. |
| AST-0138.26 | Summon: Siegward of Catarina miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-siegward-of-catarina.png` | 333×506 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 92 (pdfimages #37) | pdfimages -png p.4 image #37 (object 92, 333×506 cmyk + soft mask #38 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 12. |
| AST-0138.27 | Summon: Sword Master miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-sword-master.png` | 389×601 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 84 (pdfimages #29) | pdfimages -png p.4 image #29 (object 84, 389×601 cmyk + soft mask #30 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.28 | Summon: Rogue Witch Beatrice miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-rogue-witch-beatrice.png` | 323×502 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 86 (pdfimages #31) | pdfimages -png p.4 image #31 (object 86, 323×502 cmyk + soft mask #32 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 12. |
| AST-0138.29 | Summon: Lucatiel of Mirrah miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-lucatiel-of-mirrah.png` | 296×588 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 94 (pdfimages #39) | pdfimages -png p.4 image #39 (object 94, 296×588 cmyk + soft mask #40 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 12. |
| AST-0138.30 | Summon: Sellsword Luet miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-sellsword-luet.png` | 426×506 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 82 (pdfimages #27) | pdfimages -png p.4 image #27 (object 82, 426×506 cmyk + soft mask #28 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 12. |
| AST-0138.31 | Summon: Sirris of the Sunless Realms miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-sirris-of-the-sunless-realms.png` | 470×487 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 90 (pdfimages #35) | pdfimages -png p.4 image #35 (object 90, 470×487 cmyk + soft mask #36 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 12. |
| AST-0138.32 | Summon: Solaire of Astora miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-summon-solaire-of-astora.png` | 340×528 px | DS-Phantoms-Rules-lores.pdf, p.4 | object 78 (pdfimages #23) | pdfimages -png p.4 image #23 (object 78, 340×528 cmyk + soft mask #24 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.33 | Invader: Kirk, Knight of Thorns / Longfinger Kirk miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-kirk-knight-of-thorns.png` | 376×567 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 129 (pdfimages #29) | pdfimages -png p.5 image #29 (object 129, 376×567 cmyk + soft mask #30 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 20. |
| AST-0138.34 | Invader: Melinda the Butcher miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-melinda-the-butcher.png` | 384×519 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 143 (pdfimages #41) | pdfimages -png p.5 image #41 (object 143, 384×519 cmyk + soft mask #42 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 20. |
| AST-0138.35 | Invader: Maldron the Assassin miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-maldron-the-assassin.png` | 517×442 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 139 (pdfimages #39) | pdfimages -png p.5 image #39 (object 139, 517×442 cmyk + soft mask #40 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 20. |
| AST-0138.36 | Invader: Maneater Mildred miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-maneater-mildred.png` | 390×509 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 137 (pdfimages #37) | pdfimages -png p.5 image #37 (object 137, 390×509 cmyk + soft mask #38 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.37 | Invader: Xanthous King Jeremiah miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-xanthous-king-jeremiah.png` | 340×730 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 147 (pdfimages #45) | pdfimages -png p.5 image #45 (object 147, 340×730 cmyk + soft mask #46 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.38 | Invader: Oliver the Collector miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-oliver-the-collector.png` | 725×647 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 133 (pdfimages #33) | pdfimages -png p.5 image #33 (object 133, 725×647 cmyk + soft mask #34 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 20. |
| AST-0138.39 | Invader: Armorer Dennis miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-armorer-dennis.png` | 400×423 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 123 (pdfimages #23) | pdfimages -png p.5 image #23 (object 123, 400×423 cmyk + soft mask #24 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.40 | Invader: Marvelous Chester miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-marvelous-chester.png` | 382×552 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 131 (pdfimages #31) | pdfimages -png p.5 image #31 (object 131, 382×552 cmyk + soft mask #32 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 20. |
| AST-0138.41 | Invader: Invader Brylex miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-brylex.png` | 657×510 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 125 (pdfimages #25) | pdfimages -png p.5 image #25 (object 125, 657×510 cmyk + soft mask #26 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 20. |
| AST-0138.42 | Invader: Paladin Leeroy miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-paladin-leeroy.png` | 341×538 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 135 (pdfimages #35) | pdfimages -png p.5 image #35 (object 135, 341×538 cmyk + soft mask #36 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 20. |
| AST-0138.43 | Invader: Fencer Sharron miniature render (Phantoms) | `assets/photography/ast-0138-expansion-miniature-invader-fencer-sharron.png` | 475×600 px | DS-Phantoms-Rules-lores.pdf, p.5 | object 127 (pdfimages #27) | pdfimages -png p.5 image #27 (object 127, 475×600 cmyk + soft mask #28 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 20. |
| AST-0138.44 | Thief character miniature render (Characters expansion, 300 ppi) | `assets/photography/ast-0138-expansion-miniature-character-thief.png` | 399×426 px | DS-Characters-Rules-lores.pdf, p.4 | object 71 (pdfimages #23) | pdfimages -png p.4 image #23 (object 71, 399×426 cmyk + soft mask #24 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 10. |
| AST-0138.45 | Mercenary character miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-character-mercenary.png` | 402×481 px | DS-Characters-Rules-lores.pdf, p.4 | object 121 (pdfimages #17) | pdfimages -png p.4 image #17 (object 121, 402×481 cmyk + soft mask #18 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 10. |
| AST-0138.46 | Cleric character miniature render (Characters expansion, 300 ppi) | `assets/photography/ast-0138-expansion-miniature-character-cleric.png` | 379×438 px | DS-Characters-Rules-lores.pdf, p.4 | object 117 (pdfimages #13) | pdfimages -png p.4 image #13 (object 117, 379×438 cmyk + soft mask #14 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 10. |
| AST-0138.47 | Pyromancer character miniature render (Characters expansion, 300 ppi) | `assets/photography/ast-0138-expansion-miniature-character-pyromancer.png` | 302×614 px | DS-Characters-Rules-lores.pdf, p.4 | object 123 (pdfimages #19) | pdfimages -png p.4 image #19 (object 123, 302×614 cmyk + soft mask #20 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 10. |
| AST-0138.48 | Sorcerer character miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-character-sorcerer.png` | 394×482 px | DS-Characters-Rules-lores.pdf, p.4 | object 69 (pdfimages #21) | pdfimages -png p.4 image #21 (object 69, 394×482 cmyk + soft mask #22 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 10. |
| AST-0138.49 | Deprived character miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-character-deprived.png` | 345×465 px | DS-Characters-Rules-lores.pdf, p.4 | object 119 (pdfimages #15) | pdfimages -png p.4 image #15 (object 119, 345×465 cmyk + soft mask #16 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Subject is cut by the bottom edge of the source image (as in the rulebook): keep that edge against a frame, rule or page edge, or fade it. Final usage: gallery, end of chapter 10. |
| AST-0138.50 | Black Iron Armour set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-black-iron.png` | 305×468 px | DS-Characters-Rules-lores.pdf, p.5 | object 157 (pdfimages #6) | pdfimages -png p.5 image #6 (object 157, 310×480 cmyk + soft mask #7 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of Appendix A. |
| AST-0138.51 | Catarina Armour set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-catarina.png` | 322×483 px | DS-Characters-Rules-lores.pdf, p.5 | object 161 (pdfimages #10) | pdfimages -png p.5 image #10 (object 161, 327×490 cmyk + soft mask #11 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 4. |
| AST-0138.52 | Black Knight Armour set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-black-knight.png` | 463×532 px | DS-Characters-Rules-lores.pdf, p.5 | object 159 (pdfimages #8) | pdfimages -png p.5 image #8 (object 159, 470×537 cmyk + soft mask #9 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.53 | Guardian Armour set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-guardian.png` | 344×514 px | DS-Characters-Rules-lores.pdf, p.5 | object 171 (pdfimages #20) | pdfimages -png p.5 image #20 (object 171, 346×518 cmyk + soft mask #21 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 4. |
| AST-0138.54 | Havel's Armour set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-havels.png` | 275×569 px | DS-Characters-Rules-lores.pdf, p.5 | object 173 (pdfimages #22) | pdfimages -png p.5 image #22 (object 173, 284×578 cmyk + soft mask #23 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 4. |
| AST-0138.55 | Embraced Armour of Favour set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-embraced-armour-of-favour.png` | 365×505 px | DS-Characters-Rules-lores.pdf, p.5 | object 155 (pdfimages #4) | pdfimages -png p.5 image #4 (object 155, 376×513 cmyk + soft mask #5 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of Appendix A. |
| AST-0138.56 | Crimson Robes set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-crimson-robes.png` | 278×610 px | DS-Characters-Rules-lores.pdf, p.5 | object 167 (pdfimages #16) | pdfimages -png p.5 image #16 (object 167, 280×617 cmyk + soft mask #17 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: not placed: reserve image, or a component these rules do not use. |
| AST-0138.57 | Adventurer's Armour set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-adventurers.png` | 489×547 px | DS-Characters-Rules-lores.pdf, p.5 | object 165 (pdfimages #14) | pdfimages -png p.5 image #14 (object 165, 489×547 cmyk + soft mask #15 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 4. |
| AST-0138.58 | Dark Armour set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-dark.png` | 357×505 px | DS-Characters-Rules-lores.pdf, p.5 | object 163 (pdfimages #12) | pdfimages -png p.5 image #12 (object 163, 363×511 cmyk + soft mask #13 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of chapter 4. |
| AST-0138.59 | Gold-Trimmed Black Robes set miniature render (Characters expansion) | `assets/photography/ast-0138-expansion-miniature-armour-gold-trimmed-black-robes.png` | 364×425 px | DS-Characters-Rules-lores.pdf, p.5 | object 169 (pdfimages #18) | pdfimages -png p.5 image #18 (object 169, 370×431 cmyk + soft mask #19 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render (grey/coloured resin 3D render), cut out by its own soft mask. Final usage: gallery, end of Appendix A. |
| AST-0138.60 | White phantom duellist, cut out by its soft mask (Phantoms p.6) | `assets/art/ast-0138-art-phantom-duellist-white.png` | 815×812 px | DS-Phantoms-Rules-lores.pdf, p.6 | object 187 (pdfimages #2) | pdfimages -png p.6 image #2 (object 187, 815×1110 cmyk + soft mask #3 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Soft mask fades the figure into transparency at the foot: place on a dark ground. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0138.61 | Red phantom figure, cut out by its soft mask (Phantoms p.12) | `assets/art/ast-0138-art-phantom-red-smear.png` | 815×812 px | DS-Phantoms-Rules-lores.pdf, p.12 | object 393 (pdfimages #3) | pdfimages -png p.12 image #3 (object 393, 815×1110 cmyk + soft mask #4 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Soft mask fades the image into transparency at the foot: place on a dark ground. Named as a second object of the same review item, but it is a different image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0138.62 | Mushroom Parent and Child artwork (Darkroot p.7, 300 ppi) | `assets/art/ast-0138-art-mushroom-parent-and-child.jpg` | 1258×1576 px | DS-Darkroot-Rules-web.pdf, p.7 | object 378 (pdfimages #1) | pdfimages -png p.7 image #1 (object 378, 1258×1576 cmyk + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | The soft mask is opaque apart from noise (min alpha 243), so the dark ground is part of the image. Final usage: chapter 9. |
| AST-0138.63 | Knight pierced by arrows in a burning waste (Iron Keep p.6) | `assets/art/ast-0138-art-knight-in-burning-waste.png` | 406×605 px | DS-IronKeep-Rules-Web.pdf, p.6 | object 338 (pdfimages #1) | pdfimages -png p.6 image #1 (object 338, 406×605 rgb + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling | 406 px wide. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0138.64 | Executioner's Chariot horse artwork (p.16) | `assets/art/ast-0138-art-chariot-horse.jpg` | 847×926 px | DS-EC-Rules-Web.pdf, p.16 | object 2867 (pdfimages #1) | pdfimages -png p.16 image #1 (object 2867, 847×926 rgb + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | — Final usage: chapter 15. |
| AST-0138.65 | Executioner's Chariot and rider artwork (p.17) | `assets/art/ast-0138-art-chariot-and-rider.jpg` | 847×926 px | DS-EC-Rules-Web.pdf, p.17 | object 2886 (pdfimages #1) | pdfimages -png p.17 image #1 (object 2886, 847×926 rgb + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Named as a second object of the same review item, but it is a different image. Final usage: chapter 17. |
| AST-0138.66 | Black Dragon Kalameet head artwork from the mega-boss data card, cut out by its soft mask (Kalameet p.11) | `assets/art/ast-0138-art-kalameet-head.png` | 530×541 px | DS-BDK-Rules-web.pdf, p.11 | object 1431 (pdfimages #6) | pdfimages -png p.11 image #6 (object 1431, 530×721 cmyk + soft mask #7 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Soft mask fades the image into transparency below: place on a dark ground. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0138.67 | Painted treasure chest, closed (Explorers p.10) | `assets/art/ast-0138-art-treasure-chest-closed.png` | 201×148 px | DS-Explorers-Rules-Web.pdf, p.10 | object 841 (pdfimages #7) | pdfimages -png p.10 image #7 (object 841, 201×148 rgb, no soft mask); native resolution, no resampling | Below the 400 px rule (201 px): kept because the Mimic and Crystal Lizard chapters have no other art. Thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0138.68 | Painted treasure chest, open with a crystal glow (Explorers p.10) | `assets/art/ast-0138-art-treasure-chest-crystal-glow.png` | 201×148 px | DS-Explorers-Rules-Web.pdf, p.10 | object 843 (pdfimages #12) | pdfimages -png p.10 image #12 (object 843, 201×148 rgb, no soft mask); native resolution, no resampling | Below the 400 px rule (201 px): kept for the Crystal Lizard chapter. Thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0138.69 | Painted Mimic: chest open, lined with teeth (Explorers p.10) | `assets/art/ast-0138-art-mimic-chest-open.png` | 201×148 px | DS-Explorers-Rules-Web.pdf, p.10 | object 844 (pdfimages #13) | pdfimages -png p.10 image #13 (object 844, 201×148 rgb, no soft mask); native resolution, no resampling | Below the 400 px rule (201 px): kept for the Mimic chapter. Thumbnail size only. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0138.70 | Mimic walking on long limbs, cut out by its soft mask (Explorers p.11) | `assets/art/ast-0138-art-mimic-walking.png` | 275×240 px | DS-Explorers-Rules-Web.pdf, p.11 | object 879 (pdfimages #2) | pdfimages -png p.11 image #2 (object 879, 275×374 rgb + soft mask #3 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Below the 400 px rule (275 px wide): kept for the Mimic chapter. Soft mask fades it out below: place on a dark ground. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |


#### Group: textures

### [AST-0139] Open-book parchment page background, full spread (2022 print master)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.2
- Type: texture
- Region: whole embedded image (see Method)
- Dimensions: 5174×3378 px
- Format: png
- Method: pdfimages -png p.2 image #0 (5174×3378 CMYK JPEG @300 ppi → sRGB)
- Cleaned file: assets/textures/ast-0139-parchment-book-spread-bg.png
- Proposed placement: master page background (place as a spread, 629×811 pt per page)
- Final usage: not placed: reserve texture
- Licensing: authorised under owner's rights assertion
- Notes: 5174×3378 px = 2 × 629.3 pt at 300 ppi exactly; CMYK (U.S. Web Coated SWOP) in source, converted to sRGB by pdfimages. Left page carries the dark leather gutter; right page the page-block edge. Also present on p.1 (cover) as 1312×1690 for the dark cover.

### [AST-0140] Open-book parchment background, right-hand page only
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.2
- Type: texture
- Region: whole embedded image (see Method)
- Dimensions: 2587×3378 px
- Format: png
- Method: AST-0139 cropped to right half (x 2587–5174 px)
- Cleaned file: assets/textures/ast-0140-parchment-right-page-bg.png
- Proposed placement: right-hand (recto) page background
- Final usage: not placed: reserve texture
- Licensing: authorised under owner's rights assertion
- Notes: —

### [AST-0141] Open-book parchment background, left-hand page only
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.2
- Type: texture
- Region: whole embedded image (see Method)
- Dimensions: 2587×3378 px
- Format: png
- Method: AST-0139 cropped to left half (x 0–2587 px)
- Cleaned file: assets/textures/ast-0141-parchment-left-page-bg.png
- Proposed placement: left-hand (verso) page background
- Final usage: not placed: reserve texture
- Licensing: authorised under owner's rights assertion
- Notes: —

### [AST-0142] Cracked lava-scale cover texture (2017 box-lid artwork; SFG "Texture Design" credit)
- Source: DS-Core-Rules-lores.pdf, p.1
- Type: texture
- Region: whole embedded image (see Method)
- Dimensions: 1245×1688 px
- Format: png
- Method: pdfimages -png p.1 image #1 (1245×1688 RGB JPEG @150 ppi)
- Cleaned file: assets/textures/ast-0142-lava-scale-cover-texture.png
- Proposed placement: cover ground, chapter-opener backdrops
- Final usage: cover field and chapter banner ground (logo-free crop)
- Licensing: authorised under owner's rights assertion
- Notes: Credited "Texture Design: Alex Cairns" in the 2017 credits block — SFG-originated, not FromSoftware art. 150 ppi: at A4 it prints at ~106 ppi; upscale or re-texture for print.

### [AST-0143] Back-cover dark stone/leather background (includes baked-in parchment panel)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: texture
- Region: whole embedded image (see Method)
- Dimensions: 1312×1690 px
- Format: png
- Method: pdfimages -png p.32 image #0 (1312×1690 CMYK @150 ppi); centre luminance 245, edge 21
- Cleaned file: assets/textures/ast-0143-back-cover-dark-stone-bg.png
- Proposed placement: back-cover ground / dark sidebar ground
- Final usage: back cover ground
- Licensing: authorised under owner's rights assertion
- Notes: Panel is baked in (centre luminance ≫ edges); crop the dark border strips for a seamless dark stone texture.

### [AST-0144] Open-book parchment spread background, 2017 web edition (RGB, lower res)
- Source: DS-Core-Rules-lores.pdf, p.1
- Type: texture
- Region: whole embedded image (see Method)
- Dimensions: 2516×1719 px
- Format: png
- Method: pdfimages -png p.1 image #0 (2516×1719 RGB @150 ppi)
- Cleaned file: assets/textures/ast-0144-parchment-spread-bg-2017.png
- Proposed placement: low-res alternative background (2017 RGB export)
- Final usage: not placed: reserve texture
- Licensing: authorised under owner's rights assertion
- Notes: Keep only as colour reference; AST-0139 supersedes.

### [AST-0145] Card text-box parchment fill (worn cream paper)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.16
- Type: texture
- Region: inside the encounter card raster (p.16 #624, 584×1000 px) and equipment cards
- Dimensions: 2 files; 563–683 px on the long side
- Format: png
- Method: Phase 2B (tools/extract_phase2b.py): see the sub-entries, one per file
- Cleaned file: assets/textures/ast-0145-*.png (2 files, listed as sub-entries AST-0145.1 to AST-0145.2)
- Proposed placement: card-style callout fills
- Final usage: not placed: reserve texture
- Licensing: authorised under owner's rights assertion
- Notes: Phase 2B extraction, one file per subject from DS-Phantoms-Rules-lores.pdf p.6; DS-TG-Rulebook-Compressed_compressed.pdf p.28. Phase 0 note: Crop a text-box area from the composited encounter card raster.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0145.1 | Card text-box parchment plate: blank worn-cream panel with its hairline frame (Phantoms summon card) | `assets/textures/ast-0145-card-textbox-parchment-blank-plate.png` | 683×267 px | DS-Phantoms-Rules-lores.pdf, p.6 | object 207 (pdfimages #16) | pdfimages -png p.6 image #16 (object 207, 683×267 cmyk + soft mask #17 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | Blank plate with soft mask at 445 ppi as placed: the cleanest text-box parchment in the sources (the 2022 encounter card boxes have their text printed in). Crop the centre for a pure fill. Final usage: not placed: reserve texture. |
| AST-0145.2 | Card text-box parchment fill: blank area of the Gravelord Nito data card text box | `assets/textures/ast-0145-card-textbox-parchment-fill-2022-boss-card.png` | 563×216 px | DS-TG-Rulebook-Compressed_compressed.pdf, p.28 | object 1442 (pdfimages #2), crop px (45, 662, 608, 878) | pdfimages -png p.28 image #2 (object 1442, 653×912 cmyk, no soft mask); cropped to px box (45, 662, 608, 878) of the object; native resolution, no resampling | Text-free lower part of the text box of the 653×912 card raster (300 ppi). Final usage: not placed: reserve texture. |

### [AST-0146] Dashboard stone/parchment panel texture
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.8
- Type: texture
- Region: embedded image object 809 (pdfimages #4), placed at bbox (pt) x 92.9–581.8, y 345.6–732.5; catalogued as: dashboard raster 1019×685 px
- Dimensions: 180×250 px
- Format: png
- Method: pdfimages -png p.8 image #4 (object 809, 1019×806 cmyk + soft mask #5 composited to RGBA); cropped to px box (112, 405, 292, 655) of the object; native resolution, no resampling
- Cleaned file: assets/textures/ast-0146-dashboard-parchment-panel-texture.png
- Proposed placement: sidebar fills
- Final usage: not placed: reserve texture
- Licensing: authorised under owner's rights assertion
- Notes: 180×250 px at 150 ppi: small swatch, tile or stretch with care. The dark stone ground of the dashboard is visible only as narrow margins and gives no usable swatch.

### [AST-0147] Tile floor textures (flagstone, dirt, bone pit)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.11
- Type: texture
- Region: 875×875 px tile raster
- Dimensions: —
- Format: png
- Method: BLOCKED (Phase 2B decision)
- Cleaned file: none (BLOCKED)
- Proposed placement: backgrounds for example diagrams
- Final usage: none (BLOCKED)
- Licensing: authorised under owner's rights assertion
- Notes: No usable floor texture can be cut from the sources: every tile and board raster is covered with node rings and markers at 70 to 170 px spacing (rasters are 140 to 300 ppi), and the largest marker-free square found by masking is 44 to 270 px. Whole tiles and boards are available as tile art (AST-0133, AST-0117); a seamless flagstone, dirt or bone-pit texture needs node-free tile artwork from the owner or a redraw.


#### Group: typographic specimens

### [AST-0148] Table styling specimen (Firekeeper upgrade costs): knot corners, hairline rules, Caslon body
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.26
- Type: typographic specimen
- Region: bbox (pt) x 336.1–586.5, y 291.0–429.0
- Dimensions: 2087×1150 px
- Format: png
- Method: pdftoppm 600 dpi crop
- Cleaned file: assets/type-specimens/ast-0148-table-specimen-firekeeper-costs.png
- Proposed placement: style guide — table styling
- Final usage: not placed: reference for the type scale
- Licensing: authorised under owner's rights assertion
- Notes: Caslon regular at ~8.5 pt in cells, hairline rules, knot corners.

### [AST-0149] Chapter title specimen: OptimusPrinceps caps with rule + knot terminals ("The Campaign Dashboard")
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.13
- Type: typographic specimen
- Region: bbox (pt) x 48.3–535.6, y 50.4–96.4
- Dimensions: 4060×383 px
- Format: png
- Method: pdftoppm 600 dpi crop — title size 30.0 pt
- Cleaned file: assets/type-specimens/ast-0149-chapter-title-optimusprinceps.png
- Proposed placement: style guide — chapter title
- Final usage: not placed: reference for the type scale
- Licensing: authorised under owner's rights assertion
- Notes: Title size recorded in method; OptimusPrinceps caps, letter-spaced, centred between rules.

### [AST-0150] Body text specimen: Adobe Caslon Pro Regular + Bold run-in heads, numbered list
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.13
- Type: typographic specimen
- Region: bbox (pt) x 45.0–307.3, y 462.3–543.3
- Dimensions: 2186×675 px
- Format: png
- Method: pdftoppm 600 dpi crop — sizes [9.0] pt
- Cleaned file: assets/type-specimens/ast-0150-body-text-caslon.png
- Proposed placement: style guide — body text
- Final usage: not placed: reference for the type scale
- Licensing: authorised under owner's rights assertion
- Notes: Adobe Caslon Pro Regular with Bold run-in heads; sizes recorded in method (8.5–9 pt range).

### [AST-0151] Sub-head specimen: OptimusPrinceps small caps ("Exploration Basics / Encounter Cards")
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.16
- Type: typographic specimen
- Region: bbox (pt) x 128.2–543.5, y 97.5–127.5
- Dimensions: 3461×250 px
- Format: png
- Method: pdftoppm 600 dpi crop — size [18.0] pt
- Cleaned file: assets/type-specimens/ast-0151-subhead-optimusprinceps.png
- Proposed placement: style guide — sub-heads
- Final usage: not placed: reference for the type scale
- Licensing: authorised under owner's rights assertion
- Notes: OptimusPrinceps small caps ~13 pt, centred.

### [AST-0152] Caption / flavour specimen: Adobe Caslon Pro Italic
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.26
- Type: typographic specimen
- Region: bbox (pt) x 350.4–573.3, y 600.3–669.3
- Dimensions: 1857×575 px
- Format: png
- Method: pdftoppm 600 dpi crop — size [9.0] pt
- Cleaned file: assets/type-specimens/ast-0152-caption-caslon-italic.png
- Proposed placement: style guide — captions
- Final usage: not placed: reference for the type scale
- Licensing: authorised under owner's rights assertion
- Notes: Caslon Italic ~8 pt, set as a hanging caption beside diagrams.

### [AST-0153] Folio specimen: footer rule with knot and page number
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.13
- Type: typographic specimen
- Region: bbox (pt) x 90–585, y 757–781
- Dimensions: 4125×200 px
- Format: png
- Method: pdftoppm 600 dpi crop
- Cleaned file: assets/type-specimens/ast-0153-folio-footer.png
- Proposed placement: style guide — folio
- Final usage: not placed: reference for the type scale
- Licensing: authorised under owner's rights assertion
- Notes: Page number in OptimusPrinceps ~9 pt within the footer rule gap.

### [AST-0154] Cover subtitle specimen: "Tomb of Giants" in OptimusPrinceps SemiBold, white
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.1
- Type: typographic specimen
- Region: bbox (pt) x 144.1–485.1, y 698.1–761.8
- Dimensions: 2842×530 px
- Format: png
- Method: pdftoppm 600 dpi crop — size [43.6] pt
- Cleaned file: assets/type-specimens/ast-0154-cover-subtitle-optimusprinceps-semibold.png
- Proposed placement: style guide — cover subtitle
- Final usage: not placed: reference for the type scale
- Licensing: authorised under owner's rights assertion
- Notes: OptimusPrinceps SemiBold, white, tracked; used for every expansion title on covers.

### [AST-0155] Introduction / lore block specimen: Caslon Italic paragraphs
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.3
- Type: typographic specimen
- Region: bbox (pt) x 127.7–456.0, y 102.3–303.3
- Dimensions: 1824×1117 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/type-specimens/ast-0155-lore-block-caslon-italic.png
- Proposed placement: style guide — lore block
- Final usage: not placed: reference for the type scale
- Licensing: authorised under owner's rights assertion
- Notes: Italic lore paragraphs open each chapter/expansion; measure ~330 pt, ragged right.


#### Group: mega-boss expansion sets

### [AST-0156] The Four Kings mega-boss expansion booklet: logo-free cover art, boss painting or concept, miniature render, game board (both sides)
- Source: DS-Four-Kings-Rules-web.pdf, p.1
- Type: mega-boss expansion set
- Region: whole booklet (16 pp): cover p.1, paintings pp.3/6/10/14–16, miniature p.4, board and card fans p.5, level 4 encounter card p.8, encounter side of the board p.9, data and behaviour cards p.11, behaviour decks p.12, custom game elements p.13
- Dimensions: 5 files; 1041–1754 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0156-* in assets/art, assets/photography (5 files, jpg/png, listed as sub-entries AST-0156.1 to AST-0156.5)
- Proposed placement: Boss Encounters, Boss Turns, Boss Special Rules and Campaigns chapters
- Final usage: 3 of 5 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-Four-Kings-Rules-web.pdf p.1; DS-Four-Kings-Rules-web.pdf p.4; DS-Four-Kings-Rules-web.pdf p.5; DS-Four-Kings-Rules-web.pdf p.9; DS-Four-Kings-Rules-web.pdf p.10. Phase 0 note: Booklet supplied by the author on 2026-11-11, after the reconnaissance pass; catalogued in Phase 3, which took the essentials only. Not extracted: the cover with its baked-in logo, the back cover, the other interior paintings, and the card faces and special-rule plates (these exist only as a texture, an art layer and live text, so they need page-region crops). Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0156.1 | The Four Kings front cover, art above the logo | `assets/art/ast-0156-four-kings-cover-art-only.jpg` | 1754×1569 px | DS-Four-Kings-Rules-web.pdf, p.1 | object 20 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 20, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. The lower third of the cover carries the baked-in game logo. Final usage: chapter 2. |
| AST-0156.2 | The Four Kings booklet p.10: ink concept of one of the Four Kings, on white | `assets/art/ast-0156-four-kings-concept-king-on-white.jpg` | 1261×1375 px | DS-Four-Kings-Rules-web.pdf, p.10 | object 1334 (pdfimages #1) | pdfimages -png p.10 image #1 (object 1334, 1261×1375 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | White ground is part of the image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0156.3 | The Four Kings miniature render (one king, full figure) | `assets/photography/ast-0156-four-kings-miniature.png` | 1041×894 px | DS-Four-Kings-Rules-web.pdf, p.4 | object 65 (pdfimages #1) | pdfimages -png p.4 image #1 (object 65, 1041×894 cmyk + soft mask #2 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render, cut out by its own soft mask. Largest copy in the booklet. Final usage: figure, §17.10. |
| AST-0156.4 | The Four Kings mega-boss game board, boss side (p.5) | `assets/photography/ast-0156-four-kings-game-board-boss-side.png` | 1307×1307 px | DS-Four-Kings-Rules-web.pdf, p.5 | object 626 (pdfimages #99) | pdfimages -png p.5 image #99 (object 626, 1307×1307 cmyk + soft mask #100 (opaque everywhere, dropped)); native resolution, no resampling | Node markers are printed on the board. Use this side to show where the special rule plays out. Final usage: gallery, end of chapter 17. |
| AST-0156.5 | The Four Kings mega-boss game board, encounter side (p.9, larger of the two copies) | `assets/photography/ast-0156-four-kings-game-board-encounter-side.png` | 1208×1208 px | DS-Four-Kings-Rules-web.pdf, p.9 | object 1299 (pdfimages #1) | pdfimages -png p.9 image #1 (object 1299, 1208×1208 cmyk + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling | The tokens and the card that lie on it on p.9 are separate objects and are not in this image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0157] Gaping Dragon mega-boss expansion booklet: logo-free cover art, boss painting or concept, miniature render, game board (both sides)
- Source: DS-GaD-Rules-web.pdf, p.1
- Type: mega-boss expansion set
- Region: whole booklet (16 pp): cover p.1, paintings pp.3/6/10/14–16, miniature p.4, board and card fans p.5, level 4 encounter card p.8, encounter side of the board p.9, data and behaviour cards p.11, behaviour decks p.12, custom game elements p.13
- Dimensions: 5 files; 1235–2024 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0157-* in assets/art, assets/photography (5 files, jpg/png, listed as sub-entries AST-0157.1 to AST-0157.5)
- Proposed placement: Boss Encounters, Boss Turns, Boss Special Rules and Campaigns chapters
- Final usage: 3 of 5 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-GaD-Rules-web.pdf p.1; DS-GaD-Rules-web.pdf p.4; DS-GaD-Rules-web.pdf p.5; DS-GaD-Rules-web.pdf p.9; DS-GaD-Rules-web.pdf p.10. Phase 0 note: Booklet supplied by the author on 2026-11-11, after the reconnaissance pass; catalogued in Phase 3, which took the essentials only. Not extracted: the cover with its baked-in logo, the back cover, the other interior paintings, and the card faces and special-rule plates (these exist only as a texture, an art layer and live text, so they need page-region crops). Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0157.1 | Gaping Dragon front cover, art above the logo | `assets/art/ast-0157-gaping-dragon-cover-art-only.jpg` | 1754×1569 px | DS-GaD-Rules-web.pdf, p.1 | object 20 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 20, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. The lower third of the cover carries the baked-in game logo. Final usage: chapter 19. |
| AST-0157.2 | Gaping Dragon booklet p.10: pencil concept sheet of the Gaping Dragon, on white | `assets/art/ast-0157-gaping-dragon-concept-sheet-on-white.jpg` | 1258×1379 px | DS-GaD-Rules-web.pdf, p.10 | object 1545 (pdfimages #1) | pdfimages -png p.10 image #1 (object 1545, 1258×1379 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | White ground is part of the image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0157.3 | Gaping Dragon mega-boss miniature render | `assets/photography/ast-0157-gaping-dragon-miniature.png` | 2024×1594 px | DS-GaD-Rules-web.pdf, p.4 | object 79 (pdfimages #15) | pdfimages -png p.4 image #15 (object 79, 2024×1594 cmyk + soft mask #16 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render, cut out by its own soft mask. Largest copy in the booklet. Final usage: figure, §17.10. |
| AST-0157.4 | Gaping Dragon mega-boss game board, boss side (p.5) | `assets/photography/ast-0157-gaping-dragon-game-board-boss-side.png` | 1338×1338 px | DS-GaD-Rules-web.pdf, p.5 | object 795 (pdfimages #105) | pdfimages -png p.5 image #105 (object 795, 1338×1338 cmyk + soft mask #106 (opaque everywhere, dropped)); native resolution, no resampling | Node markers are printed on the board. Use this side to show where the special rule plays out. Final usage: gallery, end of chapter 17. |
| AST-0157.5 | Gaping Dragon mega-boss game board, encounter side (p.9, larger of the two copies) | `assets/photography/ast-0157-gaping-dragon-game-board-encounter-side.png` | 1235×1235 px | DS-GaD-Rules-web.pdf, p.9 | object 1506 (pdfimages #1) | pdfimages -png p.9 image #1 (object 1506, 1235×1235 cmyk + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling | The tokens and the card that lie on it on p.9 are separate objects and are not in this image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0158] Guardian Dragon mega-boss expansion booklet: logo-free cover art, boss painting or concept, miniature render, game board (both sides)
- Source: DS-GD-Rules-web.pdf, p.1
- Type: mega-boss expansion set
- Region: whole booklet (16 pp): cover p.1, paintings pp.3/6/10/14–16, miniature p.4, board and card fans p.5, level 4 encounter card p.8, encounter side of the board p.9, data and behaviour cards p.11, behaviour decks p.12, custom game elements p.13
- Dimensions: 5 files; 1302–2154 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0158-* in assets/art, assets/photography (5 files, jpg/png, listed as sub-entries AST-0158.1 to AST-0158.5)
- Proposed placement: Boss Encounters, Boss Turns, Boss Special Rules and Campaigns chapters
- Final usage: 4 of 5 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-GD-Rules-web.pdf p.1; DS-GD-Rules-web.pdf p.4; DS-GD-Rules-web.pdf p.5; DS-GD-Rules-web.pdf p.9; DS-GD-Rules-web.pdf p.10. Phase 0 note: Booklet supplied by the author on 2026-11-11, after the reconnaissance pass; catalogued in Phase 3, which took the essentials only. Not extracted: the cover with its baked-in logo, the back cover, the other interior paintings, and the card faces and special-rule plates (these exist only as a texture, an art layer and live text, so they need page-region crops). Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0158.1 | Guardian Dragon front cover, art above the logo | `assets/art/ast-0158-guardian-dragon-cover-art-only.jpg` | 1754×1569 px | DS-GD-Rules-web.pdf, p.1 | object 20 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 20, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. The lower third of the cover carries the baked-in game logo. Final usage: chapter 7. |
| AST-0158.2 | Guardian Dragon booklet p.10: Guardian Dragon concept sketches on grey | `assets/art/ast-0158-guardian-dragon-concept-sketches-on-grey.jpg` | 856×1377 px | DS-GD-Rules-web.pdf, p.10 | object 1496 (pdfimages #1) | pdfimages -png p.10 image #1 (object 1496, 856×1377 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Grey ground is part of the image. Final usage: chapter 17. |
| AST-0158.3 | Guardian Dragon mega-boss miniature render | `assets/photography/ast-0158-guardian-dragon-miniature.png` | 2154×1286 px | DS-GD-Rules-web.pdf, p.4 | object 79 (pdfimages #15) | pdfimages -png p.4 image #15 (object 79, 2154×1286 cmyk + soft mask #16 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render, cut out by its own soft mask. Largest copy in the booklet. Final usage: figure, §17.10. |
| AST-0158.4 | Guardian Dragon mega-boss game board, boss side (p.5) | `assets/photography/ast-0158-guardian-dragon-game-board-boss-side.png` | 1380×1380 px | DS-GD-Rules-web.pdf, p.5 | object 748 (pdfimages #99) | pdfimages -png p.5 image #99 (object 748, 1380×1380 cmyk + soft mask #100 (opaque everywhere, dropped)); native resolution, no resampling | Node markers are printed on the board. Use this side to show where the special rule plays out. Final usage: gallery, end of chapter 17. |
| AST-0158.5 | Guardian Dragon mega-boss game board, encounter side (p.9, larger of the two copies) | `assets/photography/ast-0158-guardian-dragon-game-board-encounter-side.png` | 1302×1302 px | DS-GD-Rules-web.pdf, p.9 | object 1457 (pdfimages #1) | pdfimages -png p.9 image #1 (object 1457, 1302×1302 cmyk + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling | The tokens and the card that lie on it on p.9 are separate objects and are not in this image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0159] The Last Giant mega-boss expansion booklet: logo-free cover art, boss painting or concept, miniature render, game board (both sides)
- Source: DS-TLG-Rules.pdf, p.1
- Type: mega-boss expansion set
- Region: whole booklet (16 pp): cover p.1, paintings pp.3/6/10/14–16, miniature p.4, board and card fans p.5, level 4 encounter card p.8, encounter side of the board p.9, data and behaviour cards p.11, behaviour decks p.12, custom game elements p.13
- Dimensions: 5 files; 1196–1754 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0159-* in assets/art, assets/photography (5 files, jpg/png, listed as sub-entries AST-0159.1 to AST-0159.5)
- Proposed placement: Boss Encounters, Boss Turns, Boss Special Rules and Campaigns chapters
- Final usage: 3 of 5 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-TLG-Rules.pdf p.1; DS-TLG-Rules.pdf p.4; DS-TLG-Rules.pdf p.5; DS-TLG-Rules.pdf p.9; DS-TLG-Rules.pdf p.10. Phase 0 note: Booklet supplied by the author on 2026-11-11, after the reconnaissance pass; catalogued in Phase 3, which took the essentials only. Not extracted: the cover with its baked-in logo, the back cover, the other interior paintings, and the card faces and special-rule plates (these exist only as a texture, an art layer and live text, so they need page-region crops). Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0159.1 | The Last Giant front cover, art above the logo | `assets/art/ast-0159-last-giant-cover-art-only.jpg` | 1754×1569 px | DS-TLG-Rules.pdf, p.1 | object 20 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 20, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. The lower third of the cover carries the baked-in game logo. Final usage: chapter 3. |
| AST-0159.2 | The Last Giant booklet p.10: Last Giant concept art, front and back views | `assets/art/ast-0159-last-giant-concept-front-and-back.png` | 1196×1187 px | DS-TLG-Rules.pdf, p.10 | object 1582 (pdfimages #1) | pdfimages -png p.10 image #1 (object 1582, 1261×1292 cmyk + soft mask #2 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0159.3 | The Last Giant mega-boss miniature render | `assets/photography/ast-0159-last-giant-miniature.png` | 844×1553 px | DS-TLG-Rules.pdf, p.4 | object 77 (pdfimages #13) | pdfimages -png p.4 image #13 (object 77, 844×1553 cmyk + soft mask #14 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render, cut out by its own soft mask. Largest copy in the booklet. Final usage: figure, §17.10. |
| AST-0159.4 | The Last Giant mega-boss game board, boss side (p.5) | `assets/photography/ast-0159-last-giant-game-board-boss-side.png` | 1404×1404 px | DS-TLG-Rules.pdf, p.5 | object 842 (pdfimages #2) | pdfimages -png p.5 image #2 (object 842, 1404×1404 cmyk + soft mask #3 (opaque everywhere, dropped)); native resolution, no resampling | Node markers are printed on the board. Use this side to show where the special rule plays out. Final usage: gallery, end of chapter 17. |
| AST-0159.5 | The Last Giant mega-boss game board, encounter side (p.9, larger of the two copies) | `assets/photography/ast-0159-last-giant-game-board-encounter-side.png` | 1300×1300 px | DS-TLG-Rules.pdf, p.9 | object 1540 (pdfimages #1) | pdfimages -png p.9 image #1 (object 1540, 1300×1300 cmyk + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling | The tokens and the card that lie on it on p.9 are separate objects and are not in this image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0160] Manus, Father of the Abyss mega-boss expansion booklet: logo-free cover art, boss painting or concept, miniature render, game board (both sides)
- Source: DS-MFA-Rules.pdf, p.1
- Type: mega-boss expansion set
- Region: whole booklet (16 pp): cover p.1, paintings pp.3/6/10/14–16, miniature p.4, board and card fans p.5, level 4 encounter card p.8, encounter side of the board p.9, data and behaviour cards p.11, behaviour decks p.12, custom game elements p.13
- Dimensions: 5 files; 844–2240 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0160-* in assets/art, assets/photography (5 files, jpg/png, listed as sub-entries AST-0160.1 to AST-0160.5)
- Proposed placement: Boss Encounters, Boss Turns, Boss Special Rules and Campaigns chapters
- Final usage: 3 of 5 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-MFA-Rules.pdf p.1; DS-MFA-Rules.pdf p.4; DS-MFA-Rules.pdf p.5; DS-MFA-Rules.pdf p.9; DS-MFA-Rules.pdf p.15. Phase 0 note: Booklet supplied by the author on 2026-11-11, after the reconnaissance pass; catalogued in Phase 3, which took the essentials only. Not extracted: the cover with its baked-in logo, the back cover, the other interior paintings, and the card faces and special-rule plates (these exist only as a texture, an art layer and live text, so they need page-region crops). Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0160.1 | Manus, Father of the Abyss front cover, art above the logo | `assets/art/ast-0160-manus-cover-art-only.jpg` | 1754×1569 px | DS-MFA-Rules.pdf, p.1 | object 20 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 20, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. The lower third of the cover carries the baked-in game logo. Final usage: chapter 20. |
| AST-0160.2 | Manus, Father of the Abyss booklet p.15: Manus looming over a small blue figure | `assets/art/ast-0160-manus-art-manus-over-small-figure.jpg` | 757×844 px | DS-MFA-Rules.pdf, p.15 | object 1997 (pdfimages #3) | pdfimages -png p.15 image #3 (object 1997, 757×844 cmyk + soft mask #4 (opaque everywhere, dropped)); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0160.3 | Manus, Father of the Abyss mega-boss miniature render | `assets/photography/ast-0160-manus-miniature.png` | 2240×1941 px | DS-MFA-Rules.pdf, p.4 | object 67 (pdfimages #3) | pdfimages -png p.4 image #3 (object 67, 2240×1941 cmyk + soft mask #4 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render, cut out by its own soft mask. Largest copy in the booklet. Final usage: figure, §17.10. |
| AST-0160.4 | Manus, Father of the Abyss mega-boss game board, boss side (p.5) | `assets/photography/ast-0160-manus-game-board-boss-side.png` | 1446×1446 px | DS-MFA-Rules.pdf, p.5 | object 592 (pdfimages #106) | pdfimages -png p.5 image #106 (object 592, 1446×1446 cmyk + soft mask #107 (opaque everywhere, dropped)); native resolution, no resampling | Node markers are printed on the board. Use this side to show where the special rule plays out. Final usage: gallery, end of chapter 17. |
| AST-0160.5 | Manus, Father of the Abyss mega-boss game board, encounter side (p.9, larger of the two copies) | `assets/photography/ast-0160-manus-game-board-encounter-side.png` | 1217×1217 px | DS-MFA-Rules.pdf, p.9 | object 1227 (pdfimages #1) | pdfimages -png p.9 image #1 (object 1227, 1217×1217 cmyk + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling | The tokens and the card that lie on it on p.9 are separate objects and are not in this image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0161] Old Iron King mega-boss expansion booklet: logo-free cover art, boss painting or concept, miniature render, game board (both sides)
- Source: DS-OIK-Rules-web.pdf, p.1
- Type: mega-boss expansion set
- Region: whole booklet (16 pp): cover p.1, paintings pp.3/6/10/14–16, miniature p.4, board and card fans p.5, level 4 encounter card p.8, encounter side of the board p.9, data and behaviour cards p.11, behaviour decks p.12, custom game elements p.13
- Dimensions: 4 files; 604–846 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0161-* in assets/art, assets/photography (4 files, jpg/png, listed as sub-entries AST-0161.1 to AST-0161.4)
- Proposed placement: Boss Encounters, Boss Turns, Boss Special Rules and Campaigns chapters
- Final usage: 3 of 4 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-OIK-Rules-web.pdf p.1; DS-OIK-Rules-web.pdf p.4; DS-OIK-Rules-web.pdf p.5; DS-OIK-Rules-web.pdf p.9. Phase 0 note: Booklet supplied by the author on 2026-11-11, after the reconnaissance pass; catalogued in Phase 3, which took the essentials only. Not extracted: the cover with its baked-in logo, the back cover, the other interior paintings, and the card faces and special-rule plates (these exist only as a texture, an art layer and live text, so they need page-region crops). Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0161.1 | Old Iron King front cover, art above the logo | `assets/art/ast-0161-old-iron-king-cover-art-only.jpg` | 846×766 px | DS-OIK-Rules-web.pdf, p.1 | object 22 (pdfimages #0), crop px (0, 0, 846, 766) | pdfimages -png p.1 image #0 (object 22, 846×1245 icc + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 846, 766) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. The lower third of the cover carries the baked-in game logo. Final usage: chapter 11. |
| AST-0161.2 | Old Iron King mega-boss miniature render | `assets/photography/ast-0161-old-iron-king-miniature.png` | 695×584 px | DS-OIK-Rules-web.pdf, p.4 | object 80 (pdfimages #1) | pdfimages -png p.4 image #1 (object 80, 695×584 icc + soft mask #2 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render, cut out by its own soft mask. Largest copy in the booklet. Final usage: figure, §17.10. |
| AST-0161.3 | Old Iron King mega-boss game board, boss side (p.5) | `assets/photography/ast-0161-old-iron-king-game-board-boss-side.png` | 654×654 px | DS-OIK-Rules-web.pdf, p.5 | object 815 (pdfimages #109) | pdfimages -png p.5 image #109 (object 815, 654×654 icc + soft mask #110 (opaque everywhere, dropped)); native resolution, no resampling | Node markers are printed on the board. Use this side to show where the special rule plays out. Final usage: gallery, end of chapter 17. |
| AST-0161.4 | Old Iron King mega-boss game board, encounter side (p.9, larger of the two copies) | `assets/photography/ast-0161-old-iron-king-game-board-encounter-side.png` | 604×604 px | DS-OIK-Rules-web.pdf, p.9 | object 1548 (pdfimages #1) | pdfimages -png p.9 image #1 (object 1548, 604×604 icc + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling | The tokens and the card that lie on it on p.9 are separate objects and are not in this image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0162] Vordt of the Boreal Valley mega-boss expansion booklet: logo-free cover art, boss painting or concept, miniature render, game board (both sides)
- Source: DS-VotBV-Rules-web.pdf, p.1
- Type: mega-boss expansion set
- Region: whole booklet (16 pp): cover p.1, paintings pp.3/6/10/14–16, miniature p.4, board and card fans p.5, level 4 encounter card p.8, encounter side of the board p.9, data and behaviour cards p.11, behaviour decks p.12, custom game elements p.13
- Dimensions: 5 files; 1236–1754 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0162-* in assets/art, assets/photography (5 files, jpg/png, listed as sub-entries AST-0162.1 to AST-0162.5)
- Proposed placement: Boss Encounters, Boss Turns, Boss Special Rules and Campaigns chapters
- Final usage: 3 of 5 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-VotBV-Rules-web.pdf p.1; DS-VotBV-Rules-web.pdf p.4; DS-VotBV-Rules-web.pdf p.5; DS-VotBV-Rules-web.pdf p.9; DS-VotBV-Rules-web.pdf p.10. Phase 0 note: Booklet supplied by the author on 2026-11-11, after the reconnaissance pass; catalogued in Phase 3, which took the essentials only. Not extracted: the cover with its baked-in logo, the back cover, the other interior paintings, and the card faces and special-rule plates (these exist only as a texture, an art layer and live text, so they need page-region crops). Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0162.1 | Vordt of the Boreal Valley front cover, art above the logo | `assets/art/ast-0162-vordt-cover-art-only.jpg` | 1754×1569 px | DS-VotBV-Rules-web.pdf, p.1 | object 20 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 20, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. The lower third of the cover carries the baked-in game logo. Final usage: chapter 9. |
| AST-0162.2 | Vordt of the Boreal Valley booklet p.10: Vordt of the Boreal Valley on black | `assets/art/ast-0162-vordt-art-vordt-on-black.jpg` | 1261×1383 px | DS-VotBV-Rules-web.pdf, p.10 | object 1750 (pdfimages #1) | pdfimages -png p.10 image #1 (object 1750, 1261×1383 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | — Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0162.3 | Vordt of the Boreal Valley mega-boss miniature render | `assets/photography/ast-0162-vordt-miniature.png` | 1236×1056 px | DS-VotBV-Rules-web.pdf, p.4 | object 79 (pdfimages #15) | pdfimages -png p.4 image #15 (object 79, 1236×1056 cmyk + soft mask #16 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render, cut out by its own soft mask. Largest copy in the booklet. Final usage: figure, §17.10. |
| AST-0162.4 | Vordt of the Boreal Valley mega-boss game board, boss side (p.5) | `assets/photography/ast-0162-vordt-game-board-boss-side.png` | 1347×1347 px | DS-VotBV-Rules-web.pdf, p.5 | object 899 (pdfimages #37) | pdfimages -png p.5 image #37 (object 899, 1347×1347 cmyk + soft mask #38 (opaque everywhere, dropped)); native resolution, no resampling | Node markers are printed on the board. Use this side to show where the special rule plays out. Final usage: gallery, end of chapter 17. |
| AST-0162.5 | Vordt of the Boreal Valley mega-boss game board, encounter side (p.9, larger of the two copies) | `assets/photography/ast-0162-vordt-game-board-encounter-side.png` | 1244×1244 px | DS-VotBV-Rules-web.pdf, p.9 | object 1419 (pdfimages #2) | pdfimages -png p.9 image #2 (object 1419, 1244×1244 cmyk + soft mask #3 (opaque everywhere, dropped)); native resolution, no resampling | The tokens and the card that lie on it on p.9 are separate objects and are not in this image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

### [AST-0163] Asylum Demon mega-boss expansion booklet: logo-free cover art, boss painting or concept, miniature render, game board (both sides)
- Source: DS-AD-Rules-web-EN.pdf, p.1
- Type: mega-boss expansion set
- Region: whole booklet (16 pp): cover p.1, paintings pp.3/6/10/14–16, miniature p.4, board and card fans p.5, level 4 encounter card p.8, encounter side of the board p.9, data and behaviour cards p.11, behaviour decks p.12, custom game elements p.13
- Dimensions: 5 files; 1148–1754 px on the long side
- Format: png
- Method: Phase 3 (tools/extract_phase3.py): see the sub-entries, one per file
- Cleaned file: ast-0163-* in assets/art, assets/photography (5 files, jpg/png, listed as sub-entries AST-0163.1 to AST-0163.5)
- Proposed placement: Boss Encounters, Boss Turns, Boss Special Rules and Campaigns chapters
- Final usage: 3 of 5 files placed (see the sub-entries)
- Licensing: authorised under owner's rights assertion (provenance confirmed by the author, 2026-11-11)
- Notes: Phase 3 extraction, one file per subject from DS-AD-Rules-web-EN.pdf p.1; DS-AD-Rules-web-EN.pdf p.4; DS-AD-Rules-web-EN.pdf p.5; DS-AD-Rules-web-EN.pdf p.9; DS-AD-Rules-web-EN.pdf p.12. Phase 0 note: Booklet supplied by the author on 2026-11-11, after the reconnaissance pass; catalogued in Phase 3, which took the essentials only. Not extracted: the cover with its baked-in logo, the back cover, the other interior paintings, and the card faces and special-rule plates (these exist only as a texture, an art layer and live text, so they need page-region crops). Provenance confirmed by the author, 2026-11-11.

| Sub-entry | Subject | Cleaned file | Dimensions | Source | Region / image object | Method | Notes |
|---|---|---|---|---|---|---|---|
| AST-0163.1 | Asylum Demon front cover, art above the logo | `assets/art/ast-0163-asylum-demon-cover-art-only.jpg` | 1754×1569 px | DS-AD-Rules-web-EN.pdf, p.1 | object 20 (pdfimages #0), crop px (0, 0, 1754, 1569) | pdfimages -png p.1 image #0 (object 20, 1754×2551 cmyk + soft mask #1 (opaque everywhere, dropped)); cropped to px box (0, 0, 1754, 1569) of the object; native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | Text-free crop: the top 61.5 % of the cover image, ending just above the logo flourish. The lower third of the cover carries the baked-in game logo. Final usage: chapter 17. |
| AST-0163.2 | Asylum Demon booklet p.12: demon concept art on white | `assets/art/ast-0163-asylum-demon-concept-stray-demon-on-white.jpg` | 1256×1034 px | DS-AD-Rules-web-EN.pdf, p.12 | object 1786 (pdfimages #1) | pdfimages -png p.12 image #1 (object 1786, 1256×1034 cmyk, no soft mask); native resolution, no resampling; saved as JPEG quality 92 (4:4:4) | White ground is part of the image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |
| AST-0163.3 | Asylum Demon / Stray Demon mega-boss miniature render | `assets/photography/ast-0163-asylum-demon-miniature.png` | 1148×1075 px | DS-AD-Rules-web-EN.pdf, p.4 | object 65 (pdfimages #1) | pdfimages -png p.4 image #1 (object 65, 1148×1075 cmyk + soft mask #2 composited to RGBA); trimmed to alpha bounds; native resolution, no resampling | SFG miniature render, cut out by its own soft mask. Largest copy in the booklet. Final usage: figure, §17.3. |
| AST-0163.4 | Asylum Demon mega-boss game board, boss side (p.5) | `assets/photography/ast-0163-asylum-demon-game-board-boss-side.png` | 1386×1386 px | DS-AD-Rules-web-EN.pdf, p.5 | object 864 (pdfimages #101) | pdfimages -png p.5 image #101 (object 864, 1386×1386 cmyk + soft mask #102 (opaque everywhere, dropped)); native resolution, no resampling | Node markers are printed on the board. Use this side to show where the special rule plays out. Final usage: gallery, end of chapter 17. |
| AST-0163.5 | Asylum Demon mega-boss game board, encounter side (p.9, larger of the two copies) | `assets/photography/ast-0163-asylum-demon-game-board-encounter-side.png` | 1302×1302 px | DS-AD-Rules-web-EN.pdf, p.9 | object 1545 (pdfimages #1) | pdfimages -png p.9 image #1 (object 1545, 1302×1302 cmyk + soft mask #2 (opaque everywhere, dropped)); native resolution, no resampling | The tokens and the card that lie on it on p.9 are separate objects and are not in this image. Final usage: not placed: cleared for use on 2026-11-11 and offered to the designer in layout/art_candidates.json; not yet placed. |

## Provenance Review

**The review was closed on 2026-11-11.** The author confirmed in writing: "I own the rights to all source material, painted illustrations, and artwork." The painted art, card faces, dashboards and card fans listed in sections A and F are therefore cleared for use, and Phase 3 (`tools/extract_phase3.py`) has extracted them; their catalogue entries now read "authorised under owner's rights assertion" with the note "provenance confirmed by the author, 2026-11-11". The lists below are kept unchanged as the record of what was held and why (before the confirmation, AST-0119, the TG cover art, was the only held item with a file). Two things are not changed by the confirmation: the community PDFs of section D, whose art is credited to third parties and is not used, and the font licences of section E.

### A. Third-party (FromSoftware / Bandai Namco) artwork inside the SFG PDFs
The owner's rights assertion covers the SFG publications. The paintings, screenshots and key art below are, however, FromSoftware/Bandai Namco intellectual property that SFG reproduced under licence (every credits block reads "Dark Souls™ & ©BANDAI NAMCO Entertainment Inc. / ©FromSoftware, Inc."). The lead must decide whether the assertion extends to this licensed art. (Decided 2026-11-11 by the author's confirmation: it does.)

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

### F. Phase 2B: candidates seen during extraction and not extracted
Rule applied in Phase 2B: Steamforged product imagery (miniature renders, tiles, boards, tokens, dice, card backs, layout ornaments, icons) is extracted; anything that looks like a painting, and any card or dashboard face whose painted illustration cannot be left out, is listed here instead. Where an illustration-free part could be had, that part was extracted and is named in the reason.

Phase 2C decision: the anatomy plates extracted in Phase 0 that show the same painted card and dashboard illustrations (AST-0105, AST-0091, AST-0094, AST-0097) and the printed model discs of the arcs diagram (AST-0099) are placed in the book with those areas blanked (`masks` in `layout/tuning.json`); the stored plates are unchanged. The project lead is asked to rule (`14_open_issues.md`, item 21).

Closed on 2026-11-11: every item of this table is cleared, and the last column names the Phase 3 files that now hold it.

| Review ID | Asset | Where | What | Reason / what was done (as recorded in Phase 2B) | Cleared 2026-11-11: extracted as |
|---|---|---|---|---|---|
| AST-0072.R1 | AST-0072 | DS-Phantoms-Rules-lores.pdf, p.10, object(s) 275, 277 | Two tokens of the invader set-up wheel, 201×201 px | Token faces filled with painted art (red eye / red figure) instead of a glyph. Not extracted. | AST-0072.35, AST-0072.36 |
| AST-0087.R1 | AST-0087 | DS-TG-Rulebook-Compressed_compressed.pdf, p.16, object(s) 1184, 1188 | Whole encounter card (Grave Matters, 584×1000 px) | Lower right of the card is a painted scene. Only the illustration-free parts were extracted (AST-0087.1, AST-0087.2). | AST-0087.3 |
| AST-0088.R1 | AST-0088 | DS-TG-Rulebook-Compressed_compressed.pdf, p.24, object(s) 1288 | Whole enemy data card (Skeleton Soldier, 372×520 px) | The card centre is a coloured character illustration, not the grey miniature render. Not extracted. | AST-0088.2 |
| AST-0088.R2 | AST-0088 | DS-TG-Rulebook-Compressed_compressed.pdf, p.28, object(s) 1442, 1444 | Whole boss data card (Gravelord Nito) and behaviour card (Death's Embrace) | Upper half of both cards is a painted boss illustration. Only the text-box section of the data card was extracted (AST-0088.1). | AST-0088.3, AST-0088.4 |
| AST-0135.R1 | AST-0135 | DS-TG-Rulebook-Compressed_compressed.pdf, p.8, object(s) 809, 807 | Whole character dashboard (1019×806 and 1019×685 px) | The name band (top 236 px) is a painted class portrait with painted item roundels. Only the portrait-free lower section was extracted (AST-0135.1, AST-0135.2). | AST-0135.3, AST-0135.4 |
| AST-0137.R1 | AST-0137 | DS-TG-Rulebook-Compressed_compressed.pdf, p.6, object(s) 638, 636, 634, 785 | Encounter card fan and event card face (Lifegem) | Card faces with painted scenes / a painted figure. Not extracted. | AST-0086.16, AST-0087.4, AST-0087.5, AST-0137.1, AST-0137.2 |
| AST-0137.R2 | AST-0137 | DS-TG-Rulebook-Compressed_compressed.pdf, p.5, object(s) 155, 344, 353, 350, 332, 326 | Treasure deck fan and boss data cards (Shortbow, Winged Spear, Dark Sword, Gravelord Sword, Black Knight, Gravelord Nito) | Card faces with painted item and boss illustrations. Not extracted. | AST-0088.10, AST-0137.3, AST-0137.4, AST-0137.5 |
| AST-0138.R1 | AST-0138 | DS-Phantoms-Rules-lores.pdf, p.6, object(s) 187 (also p.12 object 393) | Phantom figure artwork, 815×1110 px with soft mask | Looks like a painting (dark painted figure fading to black), not a miniature render. Not extracted. | AST-0138.60, AST-0138.61 |
| AST-0138.R2 | AST-0138 | DS-Darkroot-Rules-web.pdf, p.7, object(s) 378 | Mushroom Parent and Child artwork, 1258×1576 px with soft mask | Coloured character art on a dark ground, not the grey miniature render. Not extracted. | AST-0138.62 |
| AST-0138.R3 | AST-0138 | DS-IronKeep-Rules-Web.pdf, p.6, object(s) 338 | Knight in a burning landscape, 406×605 px with soft mask | Painting. Not extracted. | AST-0138.63 |
| AST-0138.R4 | AST-0138 | DS-EC-Rules-Web.pdf, p.16, object(s) 2867 (also p.17 object 2886) | Executioner's Chariot horse artwork, 847×926 px with soft mask | Dark rendered creature art on a grey ground, not the miniature render. Not extracted. | AST-0138.64, AST-0138.65 |
| AST-0138.R5 | AST-0138 | DS-BDK-Rules-web.pdf, p.11, object(s) 1431 | Kalameet head artwork on the mega-boss data card, 530×721 px | Painted boss illustration. Not extracted. | AST-0138.66 |

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
