# Dark Souls: The Board Game, Second Edition — rulebook production

An unofficial, non-commercial fan rulebook: edited manuscript, final rulings, layout, assets, and the typeset PDF.

| Read this | For |
|---|---|
| `31_final_dark_souls_the_board_game_second_edition_v2.pdf` | the book (screen edition, 124 pages); `…_v2_print.pdf` is the white-ground print edition |
| `17_final_report.md` | what the finished book contains, what changed since version 1, and what is not perfect |
| `40_bloat_audit.md` | the audit of the rules text against the author's manuscript: where the 57,000 added words are, how they got there, and what should come out |
| `41_rules_workshop.md` | the open decisions: for each rule that differs from the author's manuscript, the author's version, the book's, what four house rulesets do, and a recommendation |
| `tools/sim/` | the rules simulator of sections 12 and 13 of the workshop record (calibrated against the official 2017 game in section 13): the printed enemy, boss, encounter and equipment cards played move by move under the official 2017 and 2022 rules, the manuscript, and any variant; `test_sim.py` checks it against hand calculation |
| `06_final_rulings.md` | every rules question that was open, how it was settled, and on what evidence |
| `10_manuscript_chapter_*.md`, `12_glossary.md` | the manuscript, one file per chapter |
| `11_change_log.md` | every change to the source manuscript, with mechanical changes marked |
| `14_open_issues.md` | what remains: no rules question, only facts the supplied files cannot confirm |
| `01_audit_report.md`, `02_audit_table.csv`, `15_finding_status.csv` | the audit and the status of each finding |
| `16_gate2_report.md` | the report on version 1 (superseded in part by `17_final_report.md`) |
| `20_layout_spec.md`, `21_asset_manifest.csv`, `22_asset_extraction_log.md` | layout specification, asset manifest, extraction log |
| `30_pdf_production_notes.md`, `32_pdf_qa_report.md` | how the PDF is built and checked, and what a printer needs to know |

Rebuild: `python3 tools/build_pdf.py && python3 tools/qa_pdf.py` (see `30_pdf_production_notes.md` §2).
