# Dark Souls: The Board Game, Second Edition — rulebook production

An unofficial, non-commercial fan rulebook: edited manuscript, final rulings, layout, assets, and the typeset PDF.

| Read this | For |
|---|---|
| `10_manuscript_chapter_*.md`, `12_glossary.md` | **the manuscript as rewritten to the settled rules** (27,500 words, one file per chapter); what was done and the judgement calls made are in section 22 of `41_rules_workshop.md`; the brief it was written to is `work/phase12/REWRITE_BRIEF.md` |
| `31_final_dark_souls_the_board_game_second_edition_v2.pdf` | the earlier book (screen edition, 124 pages, the 77,500-word text before the rewrite); `…_v2_print.pdf` is the white-ground print edition. **Not yet rebuilt from the rewritten manuscript** |
| `17_final_report.md` | what the finished book contains, what changed since version 1, and what is not perfect |
| `40_bloat_audit.md` | the audit of the rules text against the author's manuscript: where the 57,000 added words are, how they got there, and what should come out |
| `41_rules_workshop.md` | the rules workshop, round by round. **Section 16 is the ruleset as decided,** gathered from the author's rule-by-rule review in section 15, and amended by 17.2 (stats are raised only at a rest) section 18 (every owned set in the treasure decks, the simulator checked against the author's card tables) and section 19 (the simulator completed: every card's text, all ten classes, the other sets' enemies, encounters and bosses; recommendations on treasure sorting, boss health and difficulty; 19.8 brings in the manuscript's own card amendments); **section 20 records the author's answers of 2026-11-17 (the between treasure split, sparks five less the number of characters, boss health +4 a character beyond the first), an audit that corrected the simulated players' boss fights, and what a web search found; its figures supersede the earlier ones; section 21 records the last answers and gathers the rules as settled; section 22 records the rewrite of the manuscript to those rules and the judgement calls made in it; section 23 tests boss scaling and the order of a round again (characters now act in ascending threat) and records what the author's card sheets settled; section 24 (one round for every encounter) was withdrawn by the author; **section 25 is the latest: the round and the bosses as in the author's manuscript and the 2017 rules, bosses not scaled, only treasure cards from the 2022 sets, and the community Events Expansion II as the event deck;** section 14 compares every rule across the 2017 and 2022 official rules, the author's manuscript and 28 house rulesets |
| `tools/sim/` | the rules simulator of sections 12 to 16 of the workshop record (calibrated against the official 2017 game in section 13; the ruleset as decided is tested in sections 15 and 16): the printed enemy, boss, encounter and equipment cards played move by move under the official 2017 and 2022 rules, the manuscript, and any variant; `test_sim.py` checks it against hand calculation |
| `06_final_rulings.md` | every rules question that was open, how it was settled, and on what evidence |
| `11_change_log.md` | every change to the source manuscript, with mechanical changes marked |
| `14_open_issues.md` | what remains: no rules question, only facts the supplied files cannot confirm |
| `01_audit_report.md`, `02_audit_table.csv`, `15_finding_status.csv` | the audit and the status of each finding |
| `16_gate2_report.md` | the report on version 1 (superseded in part by `17_final_report.md`) |
| `20_layout_spec.md`, `21_asset_manifest.csv`, `22_asset_extraction_log.md` | layout specification, asset manifest, extraction log |
| `30_pdf_production_notes.md`, `32_pdf_qa_report.md` | how the PDF is built and checked, and what a printer needs to know |

Rebuild: `python3 tools/build_pdf.py && python3 tools/qa_pdf.py` (see `30_pdf_production_notes.md` §2).
