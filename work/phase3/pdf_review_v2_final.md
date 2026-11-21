# Final-build visual proof check of build/book_screen.pdf (124 pages): 0 MAJOR, 11 MINOR lines

p.3 · MINOR · the Contents stop at Appendix B and give no entry for the Icon Reference on p.123 · add an "Icon Reference … 123" line after Appendix B.
pp.10, 42, 75, 91, 93 · MINOR · a small-caps sub-heading that opens the right column ("Mega-boss expansions", "Failed dodge", "Smelter Demon", "Section Four: Royal Wood", "Section One: Darkroot Garden") sits about 7.5 pt lower than a sub-heading normally sits at a column top, so the right column starts visibly below the left · discard the space-before of a heading when it is the first thing in a column (same cause as pp.38, 76, 114, 116).
p.38 · MINOR · misaligned column tops: the ruled heading "9.2 Enemy Movement" at the top of the right column sits about 10 pt lower than "9.1 Overview" beside it · discard the heading's space-before at a column top.
p.64 · MINOR · "Boss arcs" diagram, left column: the top row of node markers is cut through by the picture's top edge while the other three sides are whole · re-crop the diagram so the top row is either complete or wholly outside the frame.
p.72 · MINOR · right column: the black-and-white sketch placed directly under the gargoyle picture is 24 pt narrower than the column (inset 12 pt each side), so the edges of the two stacked pictures do not line up · crop or scale the lower picture to the full column width, or drop it.
p.76 · MINOR · misaligned column tops: "17.7 Tomb of Giants" at the top of the right column sits about 10 pt lower than "17.6 Explorers" beside it · discard the heading's space-before at a column top.
p.102 · MINOR · dodge-difficulty table, first column: the "0" is centred while "1 or 2" and "3 or more" are set left · give all three cells the same alignment.
p.114 · MINOR · misaligned column tops: "22.2 Attack and Defence" sits about 10 pt lower than "22.1 Characters and Actions" beside it · discard the heading's space-before at a column top.
p.115 · MINOR · right column: the lower picture is about 7 pt narrower than the tall picture directly above it (inset about 3.5 pt each side), so their edges do not line up · crop or scale the lower picture to the full column width.
p.116 · MINOR · misaligned column tops: "22.5 Bosses" sits about 10 pt lower than "22.4 Encounters, Souls, and the Bonfire" beside it · discard the heading's space-before at a column top.
p.122 · MINOR · card gallery: the caption "Encounter card, Level 1" breaks so that the "1" stands alone on a second line · widen that caption cell or keep "Level 1" unbroken.

Checked and found clean: running heads and page numbers on every page (page numbers 2 to 123 match the physical pages; chapter and section heads match the page content; the Glossary carries a chapter head only, having no numbered sections); no heading as the last line of a column; no lone short line at a column top; no text below the bottom margin; no text over a picture; no clipped, stretched, squashed or blocky picture (every placed picture keeps its proportions and is above 70 ppi at its printed size); no picture seen twice in the body; no table or example box split unreadably (the appendix tables repeat their header row where they continue); no empty page or empty column inside a chapter, and no column inside a chapter left more than about a quarter empty at its foot (the limit asked for was a third).

Privacy: no picture on any page shows a line of text naming a person or an email address; the card, tile and game-board pictures (pp.11, 14, 15, 21, 34, 52, 62, 64, 70, 84, 122) were enlarged and carry only the publisher's trademark line.

Pages checked: 1 to 124

The final build is clean and fit to release: there are no major defects, and the minor ones are one recurring spacing fault at column tops, two stacked pictures of unequal width, and four small single-page blemishes.

## Editor's response (2026-11-12)

All eleven points were fixed and the book was rebuilt. Page numbers above are those of the build that was checked.

| Finding | Fix | Where |
|---|---|---|
| A heading that opens a column sits 7.5 or 10 pt low (pp.10, 38, 42, 75, 76, 91, 93, 114, 116) | A heading that opens a column after an unforced break is set flush with the column head. The build finds such headings after the layout has settled and renders again; one that, without its space, would fit at the foot of the column before is pinned to the column head with a column break of its own | `ATTOP` in `tools/build_pdf.py`; `h2.attop, h3.attop` in `layout/book.css` |
| Two stacked pictures of unequal width (pp.72, 115) | A painting stands at exactly the column width. One that the room's height made up to a tenth narrower is set at full width and loses a strip at top and foot; one that full width would enlarge beyond 150 ppi is not used | `choose_plates` (`cover`) |
| Boss arcs diagram: top row of node markers cut by the picture's edge (p.64) | The crop now starts below that row; the source diagram is itself a detail of a tile | `figures` in `layout/tuning.json` |
| Dodge-difficulty table: one cell centred, two set left (p.102) | A table column that mixes numbers and words is set left throughout | table pass in `tools/build_pdf.py` |
| Caption "Encounter card, Level 1" breaks before the "1" (p.122) | "Level 1" is kept together | `captions_fixed` |
| The contents have no entry for the Icon Reference (p.3) | Entry added | `contents()` |

The bonfire painting behind the title of chapter 11 and on the back cover are two different files of the same scene (a wide and an upright version); the repeat is deliberate.
