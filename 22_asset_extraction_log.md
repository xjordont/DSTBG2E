# 22 — Asset Extraction Log

**Project:** Dark Souls: The Board Game — homebrew "Second Edition" rulebook (DSTBG2E)
**Phase:** Reconnaissance, cataloguing and initial extraction of reusable design assets
**Date:** 2026-11-09 / 2026-11-10

## Introduction

This log records the reconnaissance pass over the reference PDFs in `sources/`. Twelve PDFs were scanned: ten official Steamforged Games (SFG) publications — the 2017 core rulebook (`DS-Core-Rules-lores.pdf`, 40 pp, 595×808 pt), the 2022 *Tomb of Giants* / V2 core rulebook (`DS-TG-Rulebook-Compressed_compressed.pdf`, 32 pp, 629×811 pt, InDesign 17.2 export re-compressed by iLovePDF), the one-page FAQ, and the seven expansion rulebooks (Characters, Phantoms, Darkroot, Iron Keep, Explorers, Black Dragon Kalameet, Executioner's Chariot) — plus two community homebrews (`Hollowed_Edition_v1.3.pdf`, Affinity Publisher; `DS-Extended-Rules-V45.pdf`, Word/Quartz) which were surveyed for layout language only and whose art is **not** designated for reuse.

Methods: `pdfinfo` and `pdffonts` for metadata and font inventory; `pdfimages -list` for the embedded raster inventory (CSV consolidated at `work/imglist/_all_images.csv`); nine encrypted PDFs (empty user password, `copy:no`) were re-saved unencrypted with pypdf into `work/pdf_decrypted/` so that `pdfimages` and `pdftoppm` run without restriction; every page of every PDF was rendered at 80 dpi (`work/renders/<pdf>/p-NN.png`) and assembled into 2×2 contact sheets (`work/renders/<pdf>/sheets/`) which were then inspected visually page by page; key pages were re-rendered at 400–600 dpi (`work/renders/hires/`) for pixel-exact cropping with PIL; palette samples were taken with PIL/numpy from representative renders; vector-only elements were tested with `pdftocairo -svg`. All extracted assets live under `assets/<type>/` with the asset-ID prefix in the filename. Every "Cleaned file" path listed below exists on disk at the time of writing; anything not yet extracted is marked `not yet extracted` / `TO EXTRACT`.

Note on the "Generated for #SFU#SFU156812 …" watermark: the 2022 rulebook and all seven expansion PDFs carry a per-download personalisation line at the top of every page (text object, not part of the artwork). It is a text layer and does not appear in the embedded images; crops from the high-dpi renders avoid the top ~22 pt of the page.

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
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0033] Enemy Movement composite symbol (Move icon with push, aggro and leap satellites)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Enemy Movement”, bbox (pt) x 172.0–235.0, y 342.2–407.8 (re-cut with explicit parchment key)
- Dimensions: 505×546 px
- Format: png
- Method: pdftoppm 600 dpi render crop → parchment-key alpha (bg (246, 244, 240)); vector artwork in PDF (also croppable from work/svg/tg_p32.svg)
- Cleaned file: assets/icons/ast-0033-enemy-movement-composite-symbol.png
- Proposed placement: icon set — Enemy Turns chapter (movement)
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
- Licensing: authorised under owner's rights assertion
- Notes: Vector artwork in the PDF: a lossless SVG can be cut from work/svg/tg_p32.svg with tools/svg_crop.py using the same bbox.

### [AST-0052] Deal magical damage (character attack orb)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Character Attacks”, bbox (pt) x 423.3–455.5, y 518.2–549.9 (re-cut with explicit parchment key)
- Dimensions: 209×264 px
- Format: png
- Method: pdftoppm 600 dpi render crop → explicit parchment key bg (245,243,237), soft 26–80 (panel vignette and bottom rule excluded); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0052-deal-magical-damage.png
- Proposed placement: icon set — Character Turns chapter
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
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0063] Bleed
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Conditions”, bbox (pt) x 99.5–134.5, y 708.5–740.5 (re-cut with explicit parchment key)
- Dimensions: 292×267 px
- Format: png
- Method: pdftoppm 600 dpi render crop → explicit parchment key bg (245,243,237), soft 26–80 (panel vignette and bottom rule excluded); border-median key failed near panel rule) (orig bg (119, 125, 127)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0063-bleed.png
- Proposed placement: icon set — Conditions section
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0064] Frostbite
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Conditions”, bbox (pt) x 209.4–244.4, y 708.5–740.5 (re-cut with explicit parchment key)
- Dimensions: 292×267 px
- Format: png
- Method: pdftoppm 600 dpi render crop → explicit parchment key bg (245,243,237), soft 26–80 (panel vignette and bottom rule excluded); border-median key failed near panel rule) (orig bg (178, 181, 180)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0064-frostbite.png
- Proposed placement: icon set — Conditions section
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0065] Poison
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Conditions”, bbox (pt) x 319.2–354.2, y 708.5–740.5 (re-cut with explicit parchment key)
- Dimensions: 292×267 px
- Format: png
- Method: pdftoppm 600 dpi render crop → explicit parchment key bg (245,243,237), soft 26–80 (panel vignette and bottom rule excluded); border-median key failed near panel rule) (orig bg (171, 176, 176)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0065-poison.png
- Proposed placement: icon set — Conditions section
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0066] Stagger
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: icon
- Region: back-cover key panel, section “Conditions”, bbox (pt) x 429.1–464.1, y 708.5–740.5 (re-cut with explicit parchment key)
- Dimensions: 292×267 px
- Format: png
- Method: pdftoppm 600 dpi render crop → explicit parchment key bg (245,243,237), soft 26–80 (panel vignette and bottom rule excluded); border-median key failed near panel rule) (orig bg (144, 153, 155)); raster XObject with soft mask in PDF (srcsize small; 600 dpi render used instead)
- Cleaned file: assets/icons/ast-0066-stagger.png
- Proposed placement: icon set — Conditions section
- Licensing: authorised under owner's rights assertion
- Notes: Raster XObject with soft mask in the PDF (native size only 37–66 px), so the 600 dpi render crop was used instead.

### [AST-0067] 2017-edition enemy icons: Hollow Soldier, Crossbow Hollow, Large Hollow Soldier, Silver Knight Swordsman, Silver Knight Greatbowman, Sentinel
- Source: DS-Core-Rules-lores.pdf, p.40
- Type: icon
- Region: back-cover key, “Encounter cards” column 3 (39×39 px rasters, pre-composited onto parchment, no soft mask)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: icon set — core-set enemies (needed if the 2E book keeps the 2017 roster)
- Licensing: authorised under owner's rights assertion
- Notes: Only sources are flattened 39 px rasters (work/pdfimages/Core_p40_rgba/005–010) or the 400 dpi render (assets/diagrams/… -2017.png). Re-cut from the 400/600 dpi render with parchment keying as done for the 2022 set.

### [AST-0068] Trapped-encounter sword icon (2017 horizontal variant)
- Source: DS-Core-Rules-lores.pdf, p.40
- Type: icon
- Region: key panel, 91×39 px raster #032
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: icon set — alternative trap glyph
- Licensing: authorised under owner's rights assertion
- Notes: 2022 edition replaced it with the three-spear trap icon (extracted). Keep for reference only.

### [AST-0069] Mini-boss (standard) and Main-boss (advanced) skull icons
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.5
- Type: icon
- Region: “Bosses” heads: skull-in-ring icons above Black Knight / Gravelord Nito (rasters with masks, p.5 #150 region)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: icon set — Boss Encounters chapter
- Licensing: authorised under owner's rights assertion
- Notes: Also on Phantoms p.6 (Summon icons) and Explorers p.4; cut from a 600 dpi render of TG p.5.

### [AST-0070] Mega-boss icon (dragon silhouette in flame ring)
- Source: DS-BDK-Rules-web.pdf, p.11
- Type: icon
- Region: Mega Boss Data Cards call-out 8; also on p.4 beside the Kalameet miniature
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: icon set — Mega Boss chapter
- Licensing: authorised under owner's rights assertion
- Notes: Render BDK p.11 at 600 dpi and key against parchment; also present on EC p.11 (chariot variant).

### [AST-0071] Expansion set symbols (Darkroot wolf, Iron Keep helm, Explorers chest, BDK dragon, EC chariot, Phantoms, Characters) and the “universal” DS globe icon
- Source: DS-Darkroot-Rules-web.pdf, p.2
- Type: icon
- Region: Introduction paragraphs (universal icon inline, ~9 pt) and card corner set symbols on contents pages
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: icon set — set-symbol legend in the components appendix
- Licensing: authorised under owner's rights assertion
- Notes: Inline glyphs are tiny in the rulebooks; cards on the contents pages show them at ~12 pt. Needs 1200 dpi render crops or redraw as vectors.

### [AST-0072] Invader and Summon token icons (Phantoms): 14 invader portraits + 10 summon portraits in rings
- Source: DS-Phantoms-Rules-lores.pdf, p.10
- Type: icon
- Region: “Game Setup with Invader Encounters” token wheel (12 tokens) and p.4–5 miniature call-outs
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: icon set — Phantoms module (if included)
- Licensing: authorised under owner's rights assertion
- Notes: Crop from 600 dpi render of Phantoms p.10; tokens are dark discs with white glyphs.

### [AST-0073] Language flag icons (EN/FR/DE/IT/ES)
- Source: DS-Darkroot-Rules-web.pdf, p.2
- Type: icon
- Region: Introduction, inline
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: not needed
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
- Proposed placement: raster fallback of AST-0017
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
- Licensing: authorised under owner's rights assertion
- Notes: Vector template with knot corners; the 2022 book uses this for all small tables. Text removed; row rules kept.

### [AST-0085] Large art frame: compass corners + hairline rules around full-column illustrations
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.7
- Type: frame
- Region: vector frame around the p.7 full-page illustration (corners at ~(63,42) (587,42) (63,775) (587,775) pt)
- Dimensions: —
- Format: svg
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: illustration frames / chapter-opener art
- Licensing: authorised under owner's rights assertion
- Notes: Cut with tools/svg_crop.py from a pdftocairo SVG of TG p.7 (bbox 55,35,595,785); all art frames in both books use this construction.

### [AST-0086] Equipment card frame (charcoal ground, gold corner ornament, parchment text box, stat column)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.10
- Type: frame
- Region: Shortbow card, 248×372 px raster at 150 ppi (p.10 image #454)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: card-style callouts; appendix card anatomy
- Licensing: authorised under owner's rights assertion
- Notes: Embedded card images are ≤372 px — too small for print reuse. Request original card artwork from the owner or rebuild the frame as vector from the anatomy diagram AST-? (equipment card anatomy).

### [AST-0087] Encounter card frame (parchment card with dark banner, node map area)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.16
- Type: frame
- Region: Grave Matters card, 584×1000 px raster at 300 ppi (p.16 image #624)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: encounter-card style callouts
- Licensing: authorised under owner's rights assertion
- Notes: Best-resolution card raster in the set (1000 px tall); crop via pdfimages -png -f 16 -l 16 and composite with its soft mask.

### [AST-0088] Enemy / boss data card frame and behaviour card frame
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.24
- Type: frame
- Region: Skeleton Soldier data card (p.24 image #689/690), Gravelord Nito data card (p.28 #782 653×912), Death's Embrace behaviour card (p.28 #781 483×656)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: enemy chapter card callouts
- Licensing: authorised under owner's rights assertion
- Notes: Composite from pdfimages output (image + smask) — 300 ppi sources exist for the two p.28 cards.

### [AST-0089] Card backs: treasure (orange ring), encounter level 1/2/3 (blue/purple ring), event card back, mini/main boss summon backs
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: frame
- Region: “Cards” section of Game Contents (p.6) and core p.6/p.9
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: appendix component list
- Licensing: authorised under owner's rights assertion
- Notes: Small rasters (~130–300 px); photography-grade only. Extract via pdfimages p.6.


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
- Licensing: authorised under owner's rights assertion
- Notes: 2017 board layout; superseded by AST-0040 but useful for comparison.

### [AST-0106] Bonfire tile anatomy (2017) call-outs 1–6
- Source: DS-Core-Rules-lores.pdf, p.13
- Type: diagram
- Region: bbox (pt) x 67.4–485.4, y 86.6–494.6
- Dimensions: 2323×2267 px
- Format: png
- Method: pdftoppm 400 dpi crop
- Cleaned file: assets/diagrams/ast-0106-bonfire-tile-anatomy-2017.png
- Proposed placement: Bonfire chapter (2017 only — tile not in 2022 set)
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
- Licensing: authorised under owner's rights assertion
- Notes: 2017 legend including 2017-only enemy icons; see icon TO EXTRACT entries.

### [AST-0111] Encounter setup worked example (The Forgotten) — card + tile with placed tokens
- Source: DS-Core-Rules-lores.pdf, p.18
- Type: diagram
- Region: framed example box, right-hand page (~x 40–585, y 395–830 pt)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Encounters chapter — setup example
- Licensing: authorised under owner's rights assertion
- Notes: Crop from a 400 dpi render of core p.18; frame uses compass corners.

### [AST-0112] Node adjacency diagram (green highlighted nodes)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.11
- Type: diagram
- Region: “Movement” example box lower-left (~x 60–300, y 560–780 pt); 875×875 px tile raster
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Tiles and Nodes chapter
- Licensing: authorised under owner's rights assertion
- Notes: Render TG p.11 at 400 dpi and crop.

### [AST-0113] Range / doorway diagram (tile with arrow through door)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.11
- Type: diagram
- Region: right column box (~x 311–521, y 183–285 pt), 438×213 px raster
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Tiles and Nodes chapter
- Licensing: authorised under owner's rights assertion
- Notes: —

### [AST-0114] Timer track diagram (0–8 track with hourglass marker)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.18
- Type: diagram
- Region: top of page (~x 55–585, y 95–230 pt)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Encounters chapter — timer track
- Licensing: authorised under owner's rights assertion
- Notes: —

### [AST-0115] Equipment modifier strip ([0] 1 +1 / [3] 2 +1)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.21
- Type: diagram
- Region: example box top-left (~x 60–305, y 92–175 pt), 884×360 px raster
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Character Turns chapter — modifiers
- Licensing: authorised under owner's rights assertion
- Notes: —

### [AST-0116] Enemy attack dice resolution strip (attack 5 → dice → damage cubes)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.25
- Type: diagram
- Region: example box left column (~x 60–305, y 455–545 pt)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Enemy Turns chapter
- Licensing: authorised under owner's rights assertion
- Notes: Vector + small rasters.

### [AST-0117] Mega-boss game board (round Chariot arena; Kalameet forest board)
- Source: DS-EC-Rules-Web.pdf, p.5
- Type: diagram
- Region: p.5 top (board raster 846×1245 region) and BDK p.5
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Mega Boss chapter (if included)
- Licensing: authorised under owner's rights assertion
- Notes: SFG tile art; crop via pdfimages.


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
- Licensing: authorised under owner's rights assertion
- Notes: Composition only: texture (AST-0033) + logo (AST-0004).

### [AST-0119] 2022 Tomb of Giants cover art (Gravelord Nito on black) — PROVENANCE REVIEW
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.1
- Type: art
- Region: whole embedded image (see Method)
- Dimensions: 1312×1690 px
- Format: png
- Method: pdfimages -png p.1 image #0 (1312×1690 CMYK @150 ppi)
- Cleaned file: assets/art/ast-0119-tg-2022-cover-art-gravelord-nito.png
- Proposed placement: HOLD — not to be placed until provenance is cleared
- Licensing: PROVENANCE REVIEW
- Notes: Gravelord Nito artwork is FromSoftware/Bandai Namco licensed art reproduced on the SFG cover; the owner's assertion covers the SFG PDF but the lead must decide whether licensed third-party key art is in scope.

### [AST-0120] Firelink-style bonfire with seated knight (full-page painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.14
- Type: art
- Region: right column illustration, ~x 385–585, y 470–790 pt
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0121] Knight resting at bonfire among ruins (full-page painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.31
- Type: art
- Region: ~x 55–585, y 150–790 pt (also core p.31)
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0122] Graveyard and ruined tower under storm sky (full-page painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.32
- Type: art
- Region: ~x 55–585, y 270–790 pt (also core p.32)
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0123] Anor Londo spires at sunset (full-page painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.23
- Type: art
- Region: full page
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0124] Black Knight with greatsword in flame light (character key art)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.19
- Type: art
- Region: ~x 60–300, y 450–790 pt (also core p.26)
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0125] Cathedral interior with light shafts (concept painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.9
- Type: art
- Region: ~x 330–585, y 300–790 pt (also core p.19)
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0126] Gravelord Nito on his throne / Tomb of Giants (concept painting)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.15
- Type: art
- Region: ~x 55–585, y 150–790 pt
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0127] Chosen Undead knight in dark forest (2017 cover-style key art)
- Source: DS-Core-Rules-lores.pdf, p.38
- Type: art
- Region: full page
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0128] Ashen One with coiled sword (Dark Souls III key art)
- Source: DS-Core-Rules-lores.pdf, p.36
- Type: art
- Region: ~x 150–445, y 360–790 pt
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0129] Environment concept sketches: Undead Burg, Sen's Fortress, Anor Londo, Lothric, Darkroot, Iron Keep, Lost Bastille etc.
- Source: DS-Core-Rules-lores.pdf, p.35
- Type: art
- Region: section thumbnails on p.35/37 and on every expansion campaign page
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.

### [AST-0130] Expansion cover key art (Phantoms knight, Darkroot Artorias/Hydra lake, Iron Keep gate, Explorers Pursuer, Kalameet, Executioner's Chariot)
- Source: DS-*-Rules-*.pdf, p.1
- Type: art
- Region: cover art rasters 1754×2551 (300 ppi) or ~850×1245 (150 ppi)
- Dimensions: —
- Format: png
- Method: NOT EXTRACTED — provenance
- Cleaned file: not yet extracted
- Proposed placement: none until cleared
- Licensing: PROVENANCE REVIEW
- Notes: FromSoftware / Bandai Namco concept or key art reproduced under SFG's licence. Not extracted.


#### Group: photographys

### [AST-0131] Miniature renders, 2022 core: Cleric, Pyromancer, Thief; Giant Skeleton Archer/Soldier, Necromancer, Skeleton Archer/Beast/Soldier; Black Knight; Gravelord Nito
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.4
- Type: photography
- Region: Game Contents pp.4–5: grey resin renders with drop shadows (CMYK rasters 457–666 px with soft masks)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Components appendix / chapter openers
- Licensing: authorised under owner's rights assertion
- Notes: pdfimages -png -f 4 -l 5 then composite with masks (tools/composite_pdfimages.py already produced 216 composites for p.6 as a test). SFG sculpts — clean.

### [AST-0132] Token and terrain photography set (wound/soul tokens, luck, heroic action, estus, ember, aggro, party, condition tokens, spark dial, chest, gravestone, barrel, shrine, lever, torch, trap, skeleton ball, Patches, enemy tokens)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: “Tokens and Terrain Elements” rows (146 masked rasters, 93–284 px)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Components appendix; inline token references
- Licensing: authorised under owner's rights assertion
- Notes: Already split to RGBA in work/pdfimages/TG_p06_rgba/ (unlabelled); needs naming pass using the p.6 captions.

### [AST-0133] Game tile photography (4 double-sided tiles; 2017: 6 exploration + bonfire + boss tiles)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: p.6 tile fan (1389×271 + 1004×166 px); core p.7 tile grid
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Tiles chapter
- Licensing: authorised under owner's rights assertion
- Notes: SFG tile art; low-res in PDF (≤1389 px). Larger single-tile rasters exist on TG p.11 (875×875) and core p.13 (788×788).

### [AST-0134] Campaign board photograph (full strip)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: bottom of p.6, 1x Campaign board (1389×271 px)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Campaign Dashboard chapter
- Licensing: authorised under owner's rights assertion
- Notes: Higher-res halves on p.13 (979×250 each).

### [AST-0135] Character dashboard photograph (clean, no call-outs)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.8
- Type: photography
- Region: 1019×685 and 1019×806 px rasters at 150 ppi
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Characters chapter
- Licensing: authorised under owner's rights assertion
- Notes: pdfimages -png -f 8 -l 8 → images #380/#382 + masks #379/#381.

### [AST-0136] Dice photography (black, blue, orange, green)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: “Dice” group (4 masked rasters ~452×452 px)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Combat chapter
- Licensing: authorised under owner's rights assertion
- Notes: Also core p.7 (2017 set with green dodge dice).

### [AST-0137] Card fan photographs (encounter cards, event cards, treasure decks)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.6
- Type: photography
- Region: “Cards” and “Treasure Deck” groups
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Components appendix
- Licensing: authorised under owner's rights assertion
- Notes: Low-res; decorative only.

### [AST-0138] Expansion miniature renders (Sif, Artorias, Mushroom Parent/Child, Smelter Demon, Sir Alonne, Pursuer, Mimic, Kalameet, Executioner's Chariot, invaders, summons)
- Source: DS-*-Rules-*.pdf, p.4
- Type: photography
- Region: Contents pages of each expansion (CMYK 300 ppi rasters up to 1776×3000 px in Phantoms/BDK)
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: Expansion module openers
- Licensing: authorised under owner's rights assertion
- Notes: Phantoms p.4–5 and BDK p.4 have the largest renders.


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
- Licensing: authorised under owner's rights assertion
- Notes: 5174×3378 px = 2 × 629.3 pt at 300 ppi exactly; CMYK (U.S. Web Coated SWOP) in source, converted to sRGB by pdfimages. Left page carries the dark leather gutter; right page the page-block edge. Also present on p.1 (cover) as 1312×1690 for the dark cover.

### [AST-0140] Open-book parchment background, right-hand page only
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.2
- Type: texture
- Region: whole embedded image (see Method)
- Dimensions: 2587×3378 px
- Format: png
- Method: AST-0030 cropped to right half (x 2587–5174 px)
- Cleaned file: assets/textures/ast-0140-parchment-right-page-bg.png
- Proposed placement: right-hand (recto) page background
- Licensing: authorised under owner's rights assertion
- Notes: —

### [AST-0141] Open-book parchment background, left-hand page only
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.2
- Type: texture
- Region: whole embedded image (see Method)
- Dimensions: 2587×3378 px
- Format: png
- Method: AST-0030 cropped to left half (x 0–2587 px)
- Cleaned file: assets/textures/ast-0141-parchment-left-page-bg.png
- Proposed placement: left-hand (verso) page background
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
- Licensing: authorised under owner's rights assertion
- Notes: Keep only as colour reference; AST-0030 supersedes.

### [AST-0145] Card text-box parchment fill (worn cream paper)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.16
- Type: texture
- Region: inside the encounter card raster (p.16 #624, 584×1000 px) and equipment cards
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: card-style callout fills
- Licensing: authorised under owner's rights assertion
- Notes: Crop a text-box area from the composited encounter card raster.

### [AST-0146] Dashboard stone/parchment panel texture
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.8
- Type: texture
- Region: dashboard raster 1019×685 px
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: sidebar fills
- Licensing: authorised under owner's rights assertion
- Notes: —

### [AST-0147] Tile floor textures (flagstone, dirt, bone pit)
- Source: DS-TG-Rulebook-Compressed_compressed.pdf, p.11
- Type: texture
- Region: 875×875 px tile raster
- Dimensions: —
- Format: png
- Method: TO EXTRACT
- Cleaned file: not yet extracted
- Proposed placement: backgrounds for example diagrams
- Licensing: authorised under owner's rights assertion
- Notes: —


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
- Licensing: authorised under owner's rights assertion
- Notes: Italic lore paragraphs open each chapter/expansion; measure ~330 pt, ragged right.

## Provenance Review

Items below are **not** designated for reuse until the project lead rules on them. Nothing in this section has been extracted into `assets/` except AST-0119 (TG cover art), which was pulled because the brief asked for one cover art and is held as `BLOCKED`.

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
