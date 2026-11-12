# 30 — PDF Production Notes (Class A)

How the book in `31_final_dark_souls_the_board_game_second_edition_v2.pdf` is made, what was substituted, what the automated QA covers, and what a printer or a designer still has to do. Everything here can be repeated from the repository with the commands in §2.

## 1. What was built

| File | Edition | Ground | Images | Size | Use |
|---|---|---|---|---|---|
| `31_final_dark_souls_the_board_game_second_edition_v2.pdf` | screen | parchment `#f4f2ea` | 200 ppi at most at placed size; large opaque pictures as JPEG | 20 MB | reading on screen, home printing |
| `31_final_dark_souls_the_board_game_second_edition_v2_print.pdf` | print | white | 300 ppi at most at placed size; lossless where the source is | 40 MB | print-on-demand or office printing on white stock |

Both editions have the same metrics and the same pagination: 124 pages, US Letter (612 x 792 pt), two columns of 252 pt. Only the page ground and the image encoding differ. Internal links (contents, cross-references, glossary keywords, icon reference) and PDF bookmarks are live in both.

Version 2 replaces version 1 (99 pages). It carries the final rulings (`06_final_rulings.md`), the eight added mega-boss booklets, the painted art, and the section-start layout. `17_final_report.md` lists the differences.

## 2. Pipeline

No InDesign-class tool is present in the environment. The book is typeset with the brief's second preferred pipeline: Markdown to HTML with pandoc, structured with BeautifulSoup, laid out by WeasyPrint with a stylesheet that implements `20_layout_spec.md`.

| Step | Tool | Version |
|---|---|---|
| Markdown to HTML | pandoc (`commonmark_x`) | 3.1.3 |
| Structuring, links, figures, section starts, illustrations, galleries | Python, BeautifulSoup | 4.15 |
| Layout and PDF | WeasyPrint | 70.0, with the patch in `tools/wp_patch.py` |
| Image preparation | Pillow | 12.3 |
| QA | PyMuPDF | 2.1 |

```
python3 tools/make_fonts.py                      # static cuts of Cinzel and Libre Caslon Text
python3 tools/make_layout_assets.py              # trimmed icons and figure crops
python3 tools/assign_plates.py                   # illustration pools and captions from layout/art_candidates.json
python3 tools/build_pdf.py                       # build/book_screen.pdf, .html, pagemap_screen.json, layout_plan.json (6 to 15 minutes)
python3 tools/build_pdf.py --edition print --reuse   # build/book_print.pdf with the same layout plan (about 2 minutes)
python3 tools/mark_asset_placement.py            # work/asset_placement.json: where each asset file is used
python3 tools/build_asset_docs.py                # 21_asset_manifest.csv and 22_asset_extraction_log.md
python3 tools/qa_pdf.py                          # automated QA of the screen edition; exits 1 on any failure
python3 tools/qa_pdf.py --edition print
python3 tools/build_layout_spec.py               # 20_layout_spec.md
```

`build_pdf.py --only 08,09` builds single chapters for proofing. The build exits 1 if a cross-reference does not resolve or an icon is missing. The final files are copies of `build/book_screen.pdf` and `build/book_print.pdf` under the `31_final_…` names.

### How a build runs

1. Each `10_manuscript_chapter_NN_*.md` file (and `12_glossary.md` as chapter 21) is converted and wrapped: the title over its painting, intro, one two-column flow, sections, example boxes, tables, figures, the closing ornament.
2. `{{icon:ast-NNNN-slug}}` tokens become inline images. `(see §N.M)` references and italic glossary keywords become links.
3. **Planning (per chapter, in parallel).** Each chapter is rendered alone until its section starts settle. A numbered section that would begin in the right-hand column with 600 pt or less of the column left starts a new page; one that would begin in the left-hand column with 345 pt or less left starts a new column; a section already within 90 pt of a column head is left alone, and a chapter's closing section shorter than 400 pt never starts a new page. The thresholds are in `layout/tuning.json` (`section_starts`).
4. **Measuring passes (whole book).** The build reads back where every element fell. The room left before each section break is measured, largest first, and an illustration is chosen for it: from the chapter's own pictures first, then from the general pool. A painting is set at the full column width or not at all; two may be stacked; none is used twice. A break whose room is larger than 130 pt and takes no picture is given up: the section runs on, and the chapter is measured again. The room under each chapter's closing ornament is measured for its gallery.
5. **Verifying passes.** Illustrations and galleries are set and the book is rendered again. A picture or gallery that slipped to another page or column is withdrawn (one per chapter per pass, since one slip moves everything after it), and so is a closing ornament that now stands alone at the head of a page; the book is rendered until nothing moves. A full build takes between six and fifteen renders. A heading that opens a column after an unforced break is set flush with the column head, so that the two columns start level. Where that would let the heading slip back to the foot of the column before, it is pinned to the column head instead.
6. The contents page takes its page numbers from WeasyPrint's `target-counter`, so they cannot drift from the pages.

The plan is saved in `build/layout_plan.json`; `--reuse` builds the other edition from it, so the two paginate alike.

### The WeasyPrint patch

WeasyPrint balances the last column set of a multi-column container by growing the trial height by the height of the first leftover block. With sections wrapped in blocks, that step is a whole section, and the last page of a chapter ends with one column far longer than the other. `tools/wp_patch.py` makes the step the first line or first unbreakable block. It is applied at import and reports if the WeasyPrint source no longer matches; the build then runs unpatched and says so (`"patch": false` in the build report).

## 3. Substitutions

| Brief or source | Used here | Why |
|---|---|---|
| InDesign, or pandoc to LaTeX | pandoc to HTML to WeasyPrint | no InDesign in the environment; WeasyPrint is the brief's named alternative and gives CSS control of the two-column flow |
| OptimusPrinceps (display face of the source books) | Cinzel, SIL OFL | no font file of the source face was supplied; approved at Gate 1 (OQ-33) |
| Adobe Caslon Pro (body) | Libre Caslon Text, SIL OFL | as above |
| Helvetica (small print) | body face | no sans is needed |
| Anatomy diagrams redrawn over the extracted plates (OQ-03) | the extracted plates themselves, whole, cropped to the plate, with captions keyed to their printed call-outs | redrawing was not needed to make them legible |
| CMYK print master | sRGB | WeasyPrint writes RGB; see §5 |

The substitutions of version 1 that the rights question had forced are gone: the cover is the painted cover composition with the DARK SOULS logo, every chapter title stands over a painting, and the anatomy plates show their printed illustrations (author's confirmation of 2026-11-11; `05_gate1_decisions.md`, section 4).

Fonts are cut from the variable OFL files by `tools/make_fonts.py`, which also removes the discretionary and historical ligature features and the `s_t` and `s_p` ligatures of the italic. Licence texts are in `assets/fonts/`.

## 4. Automated QA

`tools/qa_pdf.py` reads the finished PDF, the saved HTML, the page map, the build report, and the manifest. Result for both editions: **QA PASSED** (`32_pdf_qa_report.md`).

| Brief criterion | Check | Result |
|---|---|---|
| No unresolved placeholders | no `{{…}}`, `[ASSET…]`, `[MECHANICAL CHANGE]`, tag, or template text in the PDF text; no unresolved reference or missing icon in the build report; every section reference in the text is a live link; every icon token in the manuscript is an icon in the book (183 tokens) | pass |
| No overflow boxes | no text outside the side margins; all fonts embedded; no fallback typeface | pass |
| No orphan headings | no heading within 34 pt of a column foot | pass |
| No widow rows in tables | no body row alone at the head or foot of a column where a table breaks (17 tables, 4 broken) | pass |
| All cross-references resolve | 6,975 internal links, none dangling; `tools/xref_check.py` reports 0 broken references in the manuscript | pass |
| Page count within 10% of target | 124 pages against a target of 130 (the target was raised from 100 when the author asked for sections to start on new pages) | pass |
| Style report at zero | `13_style_enforcement_report.md`: 0 violations | pass |
| No external citation | no rulebook, edition, publisher, or page citation in the PDF text (the colophon's nominative statement is the one permitted mention) | pass |
| Every extracted asset present | see below | pass, with the deviation stated below |
| (added) completeness | all 1,931 manuscript passages are found in the PDF text | pass |
| (added) privacy | no purchaser watermark, name, or e-mail address in the PDF text | pass |
| (added) no repeats | no painting, miniature, board, or card is shown twice | pass |

**Deviation on "every extracted asset is present".** 496 asset files are extracted. 234 are placed in the book. 262 are not, and each carries a reason in the manifest's placement column: earlier-edition and unused icons, images of components these rules do not use, alternates and details of a picture that is placed, card faces and paintings for which the layout had no room, source diagrams that carry source text, reference frames, type specimens, spare ornaments and textures. QA checks both directions: everything marked `placed` is in the book, and everything extracted but not placed says why.

Informational results (not failures): 52 columns end more than 60 pt short in mid-chapter, where a table, an example box, a kept list, or a kept heading would not fit, or where a section starts the next column and the room was too small for a picture; measured line length is 56 characters (median).

An independent page-by-page review of the first version 2 build followed the automated QA and found 6 major, 43 minor, and 13 cosmetic points, most of them about how illustrations were chosen and sized. The rules of the layout were changed in answer (steps 3 to 5 above) and the book was rebuilt; the report and the response to each finding are in `work/phase3/pdf_review_v2.md`. A second independent reader then checked the rebuilt book from cover to cover and found no major defect and eleven minor ones (headings sitting low at a column head, two stacked pictures of unequal width, and single blemishes); all were fixed in the final build (`work/phase3/pdf_review_v2_final.md`). (The review of version 1 is `work/phase2c/pdf_review.md`.)

## 5. Limits a printer should know

- **Colour.** The files are sRGB. A press needs conversion to its CMYK profile; the palette's CMYK values in `20_layout_spec.md` §4 are the targets for the ink and gold tones. Rich black text will convert to four-colour black unless the conversion maps `#231f20` to K only.
- **Bleed.** The cover and back cover are drawn to the trim with no bleed, and there are no crop marks. For trimmed printing, add 0.125 in of bleed to the first and last pages.
- **Image resolution.** The source PDFs are web exports. Measured at placed size: of the 147 pictures set in the text (figures, illustrations, galleries), 66 are 300 ppi or better, 47 are between 200 and 299, and 34 are between 150 and 199; none is below 150. The cover painting is 292 ppi at full page. The paintings behind the 24 chapter titles are stretched across the full measure: 13 are between 167 and 263 ppi and 11 are between 113 and 141, softened further by the dark gradient that carries the title. Six token composites were assembled at four times their native size and are soft at high magnification. Higher-resolution originals would drop in under the same file names.
- **Fonts.** Embedded as subsets. Both are OFL.
- **PDF standard.** Plain PDF 1.7, not PDF/X. WeasyPrint can write PDF/A; a PDF/X file needs a prepress tool.

## 6. Rights and what is not shown

The author confirmed on 2026-11-11 that they own the rights in all source material, painted illustrations, and artwork. The paintings, card faces, dashboards, and card fans that version 1 withheld were then extracted (`22_asset_extraction_log.md`, "Later additions"), and the masks over the anatomy plates were removed.

Three things are still deliberately absent:

- **Art from the two community rulebooks.** Their illustrations are credited to third parties and are outside the author's statement; none was extracted.
- **The purchaser line.** The 2022 rulebook and the expansion booklets print a line naming their purchaser at the top of each page. It is a separate text object, not part of any image. Every Phase 3 file was taken from an embedded image object, none from a page render, and QA searches the finished PDF for the line.
- **Card faces of the eight added booklets.** Their pages are layered, and a clean card face would have needed a page render.

## 7. Handing the book to a designer

A designer who prefers InDesign can work from the same sources without further questions:

- text: the `10_manuscript_chapter_*.md` files and `12_glossary.md`, in book order (see `20_layout_spec.md` §10);
- styles: `layout/book.css` is the complete paragraph and character style sheet (type scale in `20_layout_spec.md` §3, palette in §4);
- master pages: one chapter-opening master (title over a painting, intro, two columns) and one text master (running head, two columns, folio with knot squares), specified in `20_layout_spec.md` §1, §2, and §6;
- assets: `21_asset_manifest.csv` lists every file, its placement, and its status; `work/asset_placement.json` lists placements file by file; `layout/art_candidates.json` describes every painting, card face, and board (subject, size, suggested chapter); `layout/tuning.json` holds every decision made by eye (figure positions and crops, the painting behind each chapter title, illustration pools, gallery pools, captions, section-start thresholds);
- export: US Letter, two-page spreads off, sRGB for screen or the printer's CMYK profile for press, fonts subset-embedded, bookmarks and hyperlinks on.

## 8. Versioning

The file name carries the version. Version 1 (99 pages) was the book before the final rulings; it is in the repository history. Version 2 is the finished book. A later build with changed content is saved as `_v3` and the change recorded in `11_change_log.md`; a rebuild with unchanged content replaces the file of the same version.
