# 30 — PDF Production Notes (Class A)

How the book in `31_final_dark_souls_the_board_game_second_edition_v1.pdf` is made, what was substituted, what the automated QA covers, and what a printer or a designer still has to do. Everything here can be repeated from the repository with the commands in §2.

## 1. What was built

| File | Edition | Ground | Images | Use |
|---|---|---|---|---|
| `31_final_dark_souls_the_board_game_second_edition_v1.pdf` | screen | parchment `#f4f2ea` | 200 ppi at most at placed size | reading on screen, home printing |
| `31_final_dark_souls_the_board_game_second_edition_v1_print.pdf` | print | white | 300 ppi at most at placed size | print-on-demand or office printing on white stock |

Both editions have the same metrics and the same pagination: 100 pages, US Letter (612 x 792 pt), two columns of 252 pt. Only the page ground differs. Internal links (contents, cross-references, glossary keywords, icon reference) and PDF bookmarks are live in both.

## 2. Pipeline

No InDesign-class tool is present in the environment. The book is typeset with the brief's second preferred pipeline: Markdown to HTML with pandoc, structured with BeautifulSoup, laid out by WeasyPrint with a stylesheet that implements `20_layout_spec.md`.

| Step | Tool | Version |
|---|---|---|
| Markdown to HTML | pandoc (`commonmark_x`) | 3.1.3 |
| Structuring, links, figures, galleries | Python, BeautifulSoup | 4.15 |
| Layout and PDF | WeasyPrint | 70.0, with the patch in `tools/wp_patch.py` |
| Image preparation | Pillow | 12.3 |
| QA | PyMuPDF | 2.1 |

```
python3 tools/make_fonts.py                      # static cuts of Cinzel and Libre Caslon Text
python3 tools/make_layout_assets.py              # cover crop, trimmed icons, figure crops with withheld areas blanked
python3 tools/build_pdf.py                       # build/book_screen.pdf, .html, pagemap_screen.json
python3 tools/build_pdf.py --edition print       # build/book_print.pdf
python3 tools/qa_pdf.py                          # automated QA of the screen edition; exits 1 on any failure
python3 tools/qa_pdf.py --edition print
python3 tools/mark_asset_placement.py            # work/asset_placement.json: where each asset file is used
python3 tools/build_asset_docs.py                # 21_asset_manifest.csv and 22_asset_extraction_log.md
python3 tools/build_layout_spec.py               # 20_layout_spec.md
```

`build_pdf.py --only 08,09` builds single chapters for proofing. The final files are copies of `build/book_screen.pdf` and `build/book_print.pdf` under the `31_final_…` names.

### How a build runs

1. Each `10_manuscript_chapter_NN_*.md` file (and `12_glossary.md` as chapter 21) is converted and wrapped: banner, intro, one two-column flow, sections, example boxes, tables, figures, the closing ornament.
2. `{{icon:ast-NNNN-slug}}` tokens become inline images. `(see §N.M)` references and italic glossary keywords become links. An unresolved reference or a missing icon is reported and fails QA.
3. First render. The build reads back where every element fell (`pagemap`). A closing ornament stranded at a page top is dropped, and the empty room under every other closing ornament is measured.
4. Second render. Each chapter with 114 pt or more of room receives its gallery, sized to that room. A gallery that slips to another page is withdrawn and the book is rendered once more.
5. The contents page takes its page numbers from WeasyPrint's `target-counter`, so they cannot drift from the pages.

### The WeasyPrint patch

WeasyPrint balances the last column set of a multi-column container by growing the trial height by the height of the first leftover block. With sections wrapped in blocks, that step is a whole section, and the last page of a chapter ends with one column far longer than the other. `tools/wp_patch.py` makes the step the first line or first unbreakable block. It is applied at import and reports if the WeasyPrint source no longer matches; the build then runs unpatched and says so (`"patch": false` in the build report).

## 3. Substitutions

| Brief or source | Used here | Why |
|---|---|---|
| InDesign, or pandoc to LaTeX | pandoc to HTML to WeasyPrint | no InDesign in the environment; WeasyPrint is the brief's named alternative and gives CSS control of the two-column flow |
| OptimusPrinceps (display face of the source books) | Cinzel, SIL OFL | approved at Gate 1 (OQ-33) |
| Adobe Caslon Pro (body) | Libre Caslon Text, SIL OFL | approved at Gate 1 (OQ-33) |
| Helvetica (small print) | body face | no sans is needed |
| DARK SOULS logo lock-up | title set in Cinzel | nominative use only (OQ-33) |
| Painted cover and chapter art | lava-scale texture on the cover; product renders on banners and at chapter ends | key art is held under Provenance Review (OQ-33) |
| Painted illustrations inside four anatomy plates and the two model discs of the arcs diagram | blanked areas; frames, icons, values, and call-outs kept | same rights question; see §6 |
| Anatomy diagrams redrawn over the extracted plates (OQ-03) | the extracted plates themselves, cropped, with captions keyed to their printed call-outs | redrawing was not needed to make them legible; say if redrawn plates are wanted |
| CMYK print master | sRGB | WeasyPrint writes RGB; see §5 |

Fonts are cut from the variable OFL files by `tools/make_fonts.py`, which also removes the discretionary and historical ligature features and the `s_t` and `s_p` ligatures of the italic. Licence texts are in `assets/fonts/`.

## 4. Automated QA

`tools/qa_pdf.py` reads the finished PDF, the saved HTML, the page map, and the manifest. Result for both editions: **QA PASSED**.

| Brief criterion | Check | Result |
|---|---|---|
| No unresolved placeholders | no `{{…}}`, `[ASSET…]`, `[MECHANICAL CHANGE]`, tag, or template text in the PDF text; no unresolved reference or missing icon in the build report | pass |
| No overflow boxes | no text outside the side margins; all fonts embedded; no fallback typeface | pass |
| No orphan headings | no heading within 34 pt of a column foot | pass |
| No widow rows in tables | no body row alone at the head or foot of a column where a table breaks (16 tables, 4 broken) | pass |
| All cross-references resolve | 6,438 internal links, none dangling; `tools/xref_check.py` reports 0 broken references in the manuscript | pass |
| Page count within 10% of target | 100 pages against a target of 100 | pass |
| Style report at zero | `13_style_enforcement_report.md`: 0 violations | pass |
| No external citation | no rulebook, edition, publisher, or page citation in the PDF text (the colophon's nominative statement is the one permitted mention) | pass |
| Every extracted asset present | see below | pass, with the deviation stated below |
| (added) completeness | all 1,750 manuscript passages are found in the PDF text | pass |
| (added) privacy | no purchaser watermark, name, or e-mail address in the PDF text | pass |

**Deviation on "every extracted asset is present".** 276 asset files are extracted. 151 are placed in the book. 125 are not, and each carries a reason in the manifest's placement column: earlier-edition and unused icons (52), source diagrams that carry source text or show components these rules do not use (19), spare component images and images of components these rules do not use (15), stylesheet reference frames and card backs (10), type specimens (8), spare ornaments (7), spare textures (7), the logo files (5), and the held cover art (2). QA checks both directions: everything marked `placed` is in the book, and everything extracted but not placed says why. Placing all 276 would have meant printing superseded icons, an unused campaign board, and held art.

Informational results (not failures): 15 columns end more than 60 pt short in mid-chapter, the largest by 152 pt, where a table, an example box, or a kept heading would not fit; measured line length is 57 characters (median).

A page-by-page review by an independent proofreader followed the automated QA; its report is `work/phase2c/pdf_review.md`, and the fixes made from it are listed at the end of that file.

## 5. Limits a printer should know

- **Colour.** The files are sRGB. A press needs conversion to its CMYK profile; the palette's CMYK values in `20_layout_spec.md` §4 are the targets for the ink and gold tones. Rich black text will convert to four-colour black unless the conversion maps `#231f20` to K only.
- **Bleed.** The cover and back cover are drawn to the trim with no bleed, and there are no crop marks. For trimmed printing, add 0.125 in of bleed to pages 1 and 100 (the cover ground is flat near-black and the back cover ground is a texture that extends cleanly).
- **Image resolution.** The source PDFs are web exports. Miniature renders are 150 ppi in four of the source books and 300 ppi in the other four; no image is enlarged beyond 150 ppi at placed size, so some are below the 300 ppi print standard. Six token composites were assembled at four times their native size and are soft at high magnification. Higher-resolution originals would drop in under the same file names.
- **Fonts.** Embedded as subsets. Both are OFL.
- **PDF standard.** Plain PDF 1.7, not PDF/X. WeasyPrint can write PDF/A; a PDF/X file needs a prepress tool.

## 6. Withheld material

The rights statement covers the Steamforged reference material. Painted illustrations credited on the cards themselves to the game's licensors are treated as unclear and are not shown until the author confirms (Gate 1 OQ-33; `22_asset_extraction_log.md`, Provenance Review, including section F).

- No painted cover, chapter, or card art is placed.
- In the dashboard, equipment card, enemy data card, and boss data card plates (AST-0105, AST-0091, AST-0094, AST-0097) the illustration area is blanked. In the boss arcs diagram (AST-0099) the two printed model discs are replaced by plain discs.
- To restore them, delete the `masks` and `badges` keys of those figures in `layout/tuning.json` and rebuild.

## 7. Handing the book to a designer

A designer who prefers InDesign can work from the same sources without further questions:

- text: the `10_manuscript_chapter_*.md` files and `12_glossary.md`, in book order (see `20_layout_spec.md` §10);
- styles: `layout/book.css` is the complete paragraph and character style sheet (type scale in `20_layout_spec.md` §3, palette in §4);
- master pages: one chapter-opening master (banner, intro, two columns) and one text master (running head, two columns, folio with knot squares), specified in `20_layout_spec.md` §1, §2, and §6;
- assets: `21_asset_manifest.csv` lists every file, its placement, and its status; `work/asset_placement.json` lists placements file by file; `layout/tuning.json` holds every decision made by eye (figure positions and crops, hero images, gallery pools, captions);
- export: US Letter, two-page spreads off, sRGB for screen or the printer's CMYK profile for press, fonts subset-embedded, bookmarks and hyperlinks on.

## 8. Versioning

The file name carries the version (`_v1`). A later build with changed content is saved as `_v2` and the change recorded in `11_change_log.md`; a rebuild with unchanged content replaces the file of the same version.
