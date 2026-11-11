# Dark Souls: The Board Game, Second Edition — rulebook production

An unofficial, non-commercial fan rulebook: edited manuscript, layout, assets, and the typeset PDF.

| Read this | For |
|---|---|
| `31_final_dark_souls_the_board_game_second_edition_v1.pdf` | the book (screen edition); `…_v1_print.pdf` is the white-ground print edition. **These v1 files predate the final rulings of 2026-11-11** (`06_final_rulings.md`); the manuscript is ahead of them until v2 is built |
| `16_gate2_report.md` | what was done, what departs from the brief, and the questions still open for the author |
| `14_open_issues.md` | every rules decision that remains the author's |
| `10_manuscript_chapter_*.md`, `12_glossary.md` | the manuscript, one file per chapter |
| `11_change_log.md` | every change to the source manuscript, with mechanical changes marked |
| `01_audit_report.md`, `02_audit_table.csv`, `15_finding_status.csv` | the audit and the status of each finding |
| `20_layout_spec.md`, `21_asset_manifest.csv`, `22_asset_extraction_log.md` | layout specification, asset manifest, extraction log and Provenance Review |
| `30_pdf_production_notes.md` | how the PDF is built and checked, and what a printer needs to know |

Rebuild: `python3 tools/build_pdf.py && python3 tools/qa_pdf.py` (see `30_pdf_production_notes.md` §2).
