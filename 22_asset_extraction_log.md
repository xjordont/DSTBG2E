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

_(filled in below once sampling is complete — see "Colour Palette" section further down; placeholder kept so the section order matches the brief)_

## Asset Catalogue

_(entries appended progressively; numbering AST-0001 onward)_

## Provenance Review

_(appended progressively)_

## Font Substitution

_(appended at the end)_
