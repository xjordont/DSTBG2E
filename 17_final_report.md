# 17 — Final Report: the finished book (Class A)

Date: 2026-11-11. This report covers the work done after `16_gate2_report.md`, on the author's instruction of the same date:

> I own the rights to all source material, painted illustrations, and artwork. We should try to have subsection headers start on new pages when possible if it does not cause large areas of white space or excessive page bloat. Use your best judgement as a pro boardgame designer to determine the best rulings based on rules manuscript questions. Also reference the two official rulesets, two unofficial rulesets uploaded, and search online discussion … Resolve all outstanding issues so the final product can be rendered with perfected finalized ruleset, beautifully integrated illustrations, and beautiful graphic design.

and, with eight further expansion booklets attached: "Please extract the text and images we were missing and incorporate them into our final product."

The result is version 2 of the book: `31_final_dark_souls_the_board_game_second_edition_v2.pdf` (screen) and `…_v2_print.pdf` (print). Where this report and `16_gate2_report.md` differ, this report is the later one.

## 1. What changed between version 1 and version 2

| | Version 1 | Version 2 |
|---|---|---|
| Rules questions open | 22 lead questions and the per-chapter lists | none |
| Bosses played from placeholder rules | nine | one (Crossbreed Priscilla; see §5) |
| Campaigns | 12 | 16 |
| Manuscript | 68,872 words, 172 glossary headwords | 77,401 words, 176 headwords |
| Change-log entries | 732 | 1,028 |
| Painted art | withheld; anatomy plates partly blanked | placed throughout; plates shown whole |
| Cover | title set in type on a texture | the painted cover composition with the logo |
| Chapter openers | product renders | a painting behind every chapter title |
| Section starts | wherever the text fell | a new page or a new column where the cost is small |
| Pages | 99 | 124 |
| Asset files extracted / placed | 276 / 144 | 496 / 234 |

## 2. The rules are final

Every question that stood in `14_open_issues.md` is answered. The decision record is `06_final_rulings.md`; each change to the text is an entry in `11_change_log.md` that cites its ruling, marked `[MECHANICAL CHANGE]` where play changes.

- **Method.** The questions were divided among five rules areas. For each, a researcher read the chapters, the author's source manuscript, the official 2017 and 2022 rulebooks, the official F.A.Q., the official expansion booklets, the two community rulesets, and what online discussion could be reached, and wrote one entry per question with the evidence and a recommendation (`work/phase3/rulings_<area>.md`). The lead editor decided, settled the places where two areas met, and withdrew what the evidence did not support (`work/phase3/lead_overrides.json`, `edits_lead.json`).
- **Scale.** 334 questions answered. Most were confirmations that the book already said the right thing. 296 changes to the text followed, 103 of which change or settle how the game is played.
- **The standard applied.** The ruling a player would guess; one rule for like cases; no book-keeping without a choice; a special case deleted wherever deleting it closed the question.
- **Online evidence was thin.** Several forums refuse automated reading. No ruling rests on an online source alone, and each memo says which sources were reached.
- **Verification.** After the rulings were applied, two independent readers checked the whole book against itself: every worked example recomputed, every table against its text, every statement of a rule against every other statement of it, and the new boss entries against their booklets (`work/phase3/verify_a.md`, `verify_b.md`). 71 corrections followed. All 86 worked examples now compute from the rules as they stand.

The rulings of most consequence at the table are listed in `06_final_rulings.md`, section 3. Two earlier Gate 1 answers were revised and are named in `05_gate1_decisions.md`, section 4: Ornstein & Smough are fought as two models with two health dials, as the cards are printed, and the rights question is closed.

## 3. The eight added booklets

The Four Kings, Gaping Dragon, Guardian Dragon, The Last Giant, Manus, Old Iron King, Vordt of the Boreal Valley, and Asylum Demon booklets were read in full (`00_intake_validation.md`, addendum).

- **Text.** §17.10 now carries a full entry for each mega-boss: components, setup, special ability, heat-up, and unique icons, restated in this book's terms. §17.3 covers the Asylum Demon as mini-boss and the Stray Demon. Four campaigns were added (§19.13 to §19.16), and the component lists and counts of chapter 2 were reconciled against all the booklets.
- **Images.** From each booklet: the cover painting without its logo, the boss painting, the miniature render, and both sides of the game board. Each mega-boss's miniature stands under its heading in chapter 17, and the eight game boards close that chapter.

## 4. Illustration and design

- **Rights.** With the author's confirmation, 220 further files were extracted: 110 paintings, 68 card faces, and dashboards, card fans, miniatures and boards. Nothing is taken from the two community rulebooks, whose art is credited to third parties. The purchaser line printed on the pages of the 2022 rulebook and the expansion booklets appears in no file, record, or page.
- **Cover and back cover.** The painted cover composition with the logo; a painting and the opening words of the introduction on the back.
- **Chapter openers.** Every one of the 24 openers sets its title over a painting chosen for the chapter.
- **Sections start cleanly.** A numbered section starts a new page when it would otherwise begin low in the right-hand column, and a new column when it would begin low in the left-hand one. A break is kept only where it costs little: the room it leaves must be small or filled by a picture, and otherwise the section runs on. 32 sections start a page and 18 start a column. The page count rose from the 99 of version 1 to 124; about 12 of those pages are new text and the rest is the room given to section starts and pictures.
- **Illustrations fill the room.** The space a section break leaves is filled with a painting suited to the chapter, set at the full width of the column (44 placements), and 16 chapters close with a gallery of the components they describe. Each mega-boss's miniature stands under its heading. No picture appears twice in the book.
- **Anatomy plates** are shown whole, with their printed illustrations.

The full specification is `20_layout_spec.md`; every choice made by eye is in `layout/tuning.json`.

## 5. What is not perfect, stated plainly

1. **Crossbreed Priscilla and the Heavy Knight.** The Painted World of Ariamis rulebook was not among the files supplied, and nothing reliable was found online. Priscilla has a short entry that plays her from her data card and behaviour cards under the general boss rules; the Heavy Knight has no rules beyond its data card. That set's share of the card totals in chapter 2 rests on a community guide. If the booklet is supplied, the entry can be completed in the same way as the other eight.
2. **Printed card values.** A few worked examples quote values from cards that could not be checked against the printed cards themselves; they are internally consistent. Whether any enemy data card prints a repeat icon could not be confirmed, and the rule is written to work either way.
3. **Image resolution.** The sources are web exports. See `30_pdf_production_notes.md` §5 for the measured figures. Higher-resolution originals would drop in under the same file names.
4. **Card faces of the eight added booklets** were not extracted: their pages are layered, and a clean card face would have needed a page render. Those bosses are illustrated by their miniatures, paintings and boards.
5. **Colour.** The PDFs are sRGB; a press needs CMYK conversion.
6. **"Every extracted asset is present in the book"** remains a departure from the letter of the brief: 234 of 496 files are placed, and each of the other 262 states why it is not (superseded icons, spares, components these rules do not use, alternates of a placed picture). QA checks both directions.

## 6. Acceptance

| Criterion | Result |
|---|---|
| Every audit finding has a status | 485 of 485 (476 resolved, 9 declined, 0 open) |
| Every open rules question answered | 334 of 334; `14_open_issues.md` lists none |
| Style violations | 0 (`13_style_enforcement_report.md`) |
| Cross-references | 0 broken in the manuscript; 6,975 links in the PDF, none dangling |
| Worked examples | 86 of 86 compute from the rules as they stand |
| Automated PDF QA | passed, both editions (`32_pdf_qa_report.md`) |
| Independent page review | two rounds. The first v2 build: 6 major, 43 minor, 13 cosmetic findings, each acted on or answered, and the layout rules changed (`work/phase3/pdf_review_v2.md`). The rebuilt book, read cover to cover by a second reader: 0 major, 11 minor, all fixed in the final build (`work/phase3/pdf_review_v2_final.md`) |
