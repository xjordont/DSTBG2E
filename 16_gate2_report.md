# 16 — Gate 2 Report: Phases 2A, 2B, and 2C (Class A)

Date: 2026-11-11. This report states each gate criterion of the brief, the evidence for it, and every place where the result departs from the letter of the brief. Gate 1 was answered "Approve all" (`05_gate1_decisions.md`).

## Gate 2A — Manuscript

| Criterion | Result | Evidence |
|---|---|---|
| All chapters drafted | met | 23 chapter files (`10_manuscript_chapter_00` to `_20`, `_22`, `_23`) and `12_glossary.md` as chapter 21; 68,872 words; `03_coverage_tracker.md` has no undrafted row |
| Zero style violations | met | `13_style_enforcement_report.md`: 0 (hedge words, Americanisms, second person outside examples, external references, meta tags, undefined keywords) |
| Zero external citations | met | style check and the PDF text check; the colophon's nominative statement is the one permitted mention |
| Zero meta-commentary | met | no tag, note to the reader, or editorial aside in any Class B file |
| All approved completions integrated | met | CMP-0001 to CMP-0023 appear in the tracker against their sections and in `11_change_log.md` (732 entries) |
| Glossary complete | met | 172 headwords; every italic keyword in the chapters has an entry (style check: 0 undefined) |
| All examples verified | met | an independent pass re-derived all 80 worked examples and every table: 78 were right, 2 were corrected, and 9 cross-chapter inconsistencies were fixed (`work/phase2a/qa_examples_report.md`; change-log entries cite QA-001 to QA-011) |
| All REQUIRED fixes applied | met | `15_finding_status.csv`: 485 findings, 474 resolved, 11 declined, 0 open; no Blocker or Major finding is open |
| All OPTIONAL fixes applied or declined | met | the 11 declined findings each cite, in `15_finding_status.csv`, the change-log entries that state the reason |
| One commit per chapter | met | `git log` shows one "manuscript: chapter NN" commit per chapter, followed by reconciliation commits |

Mechanical changes are marked `[MECHANICAL CHANGE]` in `11_change_log.md`. Decisions that remain the author's are listed in `14_open_issues.md` (20 lead items, then the per-chapter lists).

## Gate 2B — Layout specification and assets

| Criterion | Result | Evidence |
|---|---|---|
| Every icon, ornament, and frame in the manuscript has a manifest entry | met | 55 icon tokens, all in `21_asset_manifest.csv`; the two ornaments (AST-0075, AST-0082) and both grounds (AST-0142, AST-0143) are listed; 72 asset IDs are referenced by the book and all 72 are in the manifest; no frame asset is placed (boxes and tables are drawn in CSS) |
| Every chapter opener has a designated hero asset | met | 24 of 24 openers (chapters 1 to 22, Appendix A, Appendix B): `20_layout_spec.md` §6 |
| Cover fully specified | met | `20_layout_spec.md` §11 (front) and §6 (back cover row) |
| All substitutions logged | met | `20_layout_spec.md` §12, Substitutions; manifest rows FONT-01 to FONT-03; `30_pdf_production_notes.md` §3 |
| Manifest complete, with status | met | 300 rows: 158 placed, 133 extracted and not placed (each with a reason), 5 blocked, 3 substitutions, 1 not required |
| Extraction log final | met | `22_asset_extraction_log.md`: method, region, and final usage for every entry; Provenance Review with section F for Phase 2B |

Phase 2B extraction added 162 files (98 component images, 46 icons, 10 frames and card backs, 5 diagrams, 3 textures). Four catalogue entries could not be extracted and are marked blocked with the reason: expansion set symbols (only one exists as a separate object), the equipment card frame (too small), card fans (every fan shows painted card faces), and tile floor textures (no marker-free area).

## Gate 2C — PDF

| Criterion | Result | Evidence |
|---|---|---|
| The PDF exists | met | `31_final_dark_souls_the_board_game_second_edition_v1.pdf` (screen) and `…_v1_print.pdf` (print), 100 pages each |
| Automated QA passes | met | `tools/qa_pdf.py`, both editions: QA PASSED (`30_pdf_production_notes.md` §4) |
| Independent page review | done | `work/phase2c/pdf_review.md`, with the fixes made from it |

## Departures from the letter of the brief

1. **"Every extracted asset is present in the rendered book."** 151 of 276 extracted files are placed. The other 125 are deliberately left out and each says why in the manifest: superseded and unused icons, source diagrams that carry source text or show components these rules do not use, reference frames, spares, the logo, and held art. QA verifies both directions.
2. **Painted illustrations are withheld.** The brief asks that an asset of unclear provenance be flagged and that the author be asked before extraction. Painted key art was never placed. Phase 2B found that four anatomy plates extracted in Phase 0 also show painted card and portrait illustrations, which the cards credit to the game's licensors. Those areas are blanked in the book, and the question is put to the author (see below). Nothing else in the plates was changed.
3. **Anatomy diagrams were not redrawn** (Gate 1 OQ-03 recommended redrawing over the extracted plates). The extracted plates are used, with captions keyed to their printed call-outs.
4. **Colour and resolution.** The PDFs are sRGB, not CMYK, and some product renders are 150 ppi at placed size because the sources are web exports (`30_pdf_production_notes.md` §5).
5. **Nine bosses have placeholder rules.** Their rule booklets were not among the inputs; each is played from its data card and the general boss rules (CMP-0005, Gate 1 OQ-02).

## Questions for the author

1. **Rights in the painted illustrations.** Do the rights you hold cover the painted illustrations printed on the cards and dashboards (class portraits, enemy and boss paintings, item paintings) and the cover and chapter paintings? If yes, the four plates are restored by deleting their `masks` keys, and the held key art can be placed on the cover and openers. If no, the book stays as built.
2. **The 20 rules decisions in `14_open_issues.md`**, of which the weightiest are: campaign soul rewards (standard rewards with doubled stat costs, CH-18-038); when an invader's encounter counts as cleared; two hollow cubes; the expansion treasure and encounter card totals that cannot be reconciled from the supplied booklets; and the nine bosses without booklets.

## Acceptance criteria

| Criterion | Result |
|---|---|
| Every audit finding has a status | 485 of 485 (474 resolved, 11 declined, 0 open) |
| Every completion has a status | 23 of 23 approved and integrated |
| Zero Blocker or Major open | 0 open |
| Glossary covers every keyword | 172 headwords; 0 undefined keywords |
| All examples reproduce the current rules | 80 of 80 after the two corrections |
| All tables reconcile | verified by the same pass; the expansion totals in §2.5 and §2.6 are the manuscript's own and are flagged for a recount |
| All cross-references resolve | 0 broken in the manuscript; 0 dangling links in the PDF |
| Clean git history | one commit per chapter, then reconciliation, verification, layout, and asset commits |
