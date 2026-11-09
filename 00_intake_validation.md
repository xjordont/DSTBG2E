# 00 — Intake Validation (Phase 0)

Project: Dark Souls: The Board Game — Second Edition (homebrew) editorial, completion and production pipeline.
Working directory: `/home/user/DSTBG2E` (branch `claude/lucid-ptolemy-l5w2fk`). Date: 2026-11-09.

## 1. Input inventory

Thirteen files were supplied. The brief's manifest names eleven (it says "ten" but lists eleven); two further official expansion booklets were also attached and are accepted as supplementary official references. Originals are copied to `sources/` (git-ignored; checksums below). Text extracts (`pdftotext -layout`) are in `work/text/`; the manuscript conversion (`pandoc` → GFM) is at `work/docx/manuscript.md`.

| # | File | Role | Pages | Size | SHA-256 (first 16) | Extracted words | Status | Warnings |
|---|---|---|---|---|---|---|---|---|
| 1 | DarkSoulsTBG2E.docx | Primary manuscript (baseline of truth) | ~77 (per its TOC) | 437 KB | e3bb943371e09849 | 21,371 | READABLE | Footer artefact; TOC stale; stubs — see §3 |
| 2 | DS-Core-Rules-lores.pdf | Official SFG 2017 core rulebook | 40 | 8.2 MB | 7dc6bd249c9bd684 | 14,357 | READABLE | None. Not encrypted |
| 3 | DS-TG-Rulebook-Compressed_compressed.pdf | Official 2022 V2 core rulebook (Tomb of Giants) | 32 | 8.0 MB | e0fad3f4103eac17 | 12,307 | READABLE | Owner-encrypted (copy:no); opens with empty user password. iLovePDF-recompressed |
| 4 | Dark_Souls_The_Board_Game_FAQ.pdf | Official FAQ / errata | 1 | 549 KB | 44f8cc3523cd47f7 | 540 | READABLE | Single page is the complete official document, not a truncation |
| 5 | DS-Characters-Rules-lores.pdf | Expansion: Characters | 8 | 7.0 MB | 35f28a4ce1c4e237 | 1,141 | READABLE | Owner-encrypted |
| 6 | DS-Phantoms-Rules-lores.pdf | Expansion: Phantoms | 20 | 14.3 MB | d14809f08a58539c | 3,852 | READABLE | Owner-encrypted |
| 7 | DS-Darkroot-Rules-web.pdf | Expansion: Darkroot Basin | 12 | 11.9 MB | 2dc0fd821f31b874 | 1,427 | READABLE | Owner-encrypted |
| 8 | DS-IronKeep-Rules-Web.pdf | Expansion: Iron Keep | 8 | 1.0 MB | f7155899ac9d4e5a | 1,411 | READABLE | Owner-encrypted |
| 9 | DS-Explorers-Rules-Web.pdf | Expansion: Explorers | 16 | 2.2 MB | 04442e9a7bbb0cee | 2,749 | READABLE | Owner-encrypted |
| 10 | Hollowed_Edition_v1.3.pdf | Community homebrew | 10 | 9.7 MB | bafaac498cda58e7 | 3,668 | READABLE | Affinity Publisher export; not encrypted |
| 11 | DS-Extended-Rules-V45.pdf | Community homebrew | 27 | 2.7 MB | d0a7b3fcb2b1e887 | 23,140 | READABLE | Word export; not encrypted |
| 12 | DS-BDK-Rules-web.pdf | Supplementary official: Black Dragon Kalameet | 16 | 13.5 MB | 68a769d1c9405979 | 2,792 | READABLE | Not in manifest; accepted |
| 13 | DS-EC-Rules-Web.pdf | Supplementary official: Executioner's Chariot | 20 | 2.9 MB | 0cff5d334b07edcd | 3,730 | READABLE | Not in manifest; accepted |

Truncation check: first and last page of every PDF yield text; page counts match the known published page counts for each booklet. No file is below 50% of expected length. The "owner-encrypted" flag is a permissions flag only (print allowed, copy disallowed); every file opens without a password. Extraction proceeds under the owner's rights assertion recorded in the brief.

Manifest cross-check: all eleven named files are present. The brief's Phase 1 agent E names "the truncated Combat Cards section" and "the weapon-stat-revision table on pp. 91–93"; this DOCX revision has no section titled Combat Cards and its TOC ends at p. 77. The weapon stat table exists (in COMMUNITY UPDATE PACK). Combat Cards is logged in the coverage tracker as NOT PRESENT and raised as an open question (OQ-04).

## 2. Manuscript structure (DOCX)

- 1,522 paragraphs, 7 tables, 1 section, US Letter (8.5 × 11 in). No embedded images.
- Styles: Title ×7, Heading 1 ×34, Heading 2 ×81, Heading 3 ×93, body ×1,307.
- After dropping the TOC block: 24 chapters, 166 sections, 20 empty headings (see `03_coverage_tracker.md`).
- Byline: "By PittedPanda — Based on related works by Steam Forged Games (SFG), Konami, Santuric, Wilhelm, …" (front matter; Class B disposition pending OQ-01).

## 3. Structural checks

### 3.1 Duplicate footer artefact — FLAGGED FOR REMOVAL
The DOCX page footer carries a rules paragraph that repeats on every page:

> **Estus Flask** — The character may flip their estus flask token to the used side as a major action to remove all damage cubes from their endurance bar. Stamina cubes are not removed.

This is the only place the Estus Flask token rule exists. The body's "Character Tokens" section announces three token types, then says "one of each of the four following tokens", and lists only Heroic Action, Luck and Ember. The TOC lists an "Estus Flask" sub-heading at p. 16 that has no body counterpart. Disposition: delete the footer; restore the rule as a proper sub-section (completion CMP, Phase 1 agent E).

### 3.2 TOC / body mismatch
- TOC page numbers are stale throughout.
- Renamed or restructured headings: Soul Rewards → Souls; Character Turn (Overview / Character Actions) → Character Turn Order / Recover one stamina. / Minor Actions: / Major Action:; Node → Area-of-Effect (AoE); Encounter Rewards → Encounter Soul Rewards + Encounter Treasure Rewards.
- Body headings absent from TOC: Boss Aggro; Bonfire Ascetic; seven of the thirteen campaign entries.
- TOC headings absent from body: Estus Flask; **GLOSSARY** (TOC p. 74; the Introduction also promises a glossary of italicised terms). The glossary does not exist.
- Full reconciliation table is at the foot of `03_coverage_tracker.md`.

### 3.3 Orphan / malformed headings
- 20 empty headings (`#  `, `##  `, `###  `) used as page breaks — delete.
- "Spells" is an H2 immediately followed by an H3 also titled "Spells".
- "Recover one stamina.", "Minor Actions:" and "Major Action:" are procedural steps set as H3 headings.
- Duplicate campaign: "Facing the Abyss - Dark Souls (Darkroot Basin)" and "Facing the Abyss - Dark Souls (Darkroot)" have identical section lists with different preambles.

### 3.4 Stubs, truncations and placeholders
| Location | Finding |
|---|---|
| F.A.Q. (line 3098) | Empty heading. STUB |
| COMMUNITY UPDATE PACK (line 3102–end) | Skeleton: card-name lists, one-line errata notes, a 60-row weapon stat table in plain text, two bare lists (Enemy Data, Boss Data & Behaviours). No rules prose. SKELETON |
| GLOSSARY | Promised, absent. MISSING |
| Characters › Estus Flask | Absent from body (footer only). MISSING |
| Boss Special Rules | Covers Asylum/Stray Demon only; the mega-boss setup step defers to "the mega-boss rule booklet" (external reference). INCOMPLETE |
| Summons › Phantoms, line 1993 | "…if their health dial is reduced to or the encounter ends" — missing word ("zero"). TRUNCATED |
| Setup After the mini-boss, step 11 | "…where they may now without spending a spark" — missing verb ("rest"). TRUNCATED |
| Shop Setup › After Boss is Defeated, step 2.3 | "Shuffle five random legendary treasure cards." — destination omitted (into the tier two deck). TRUNCATED |
| Invader Encounter Setup | "starting decks deck size"; "blocked by train" (terrain). DEFECT |
| Soul Reward Table / Phantoms step 7 | Stray "i" characters ("per characteri", "deck.i"). DEFECT |
| Game Components › Enemies | "1x HungryVoracious Mimic" (two names run together). DEFECT |

### 3.5 Internal contradictions detected at intake (to be audited in Phase 1)
- Campaign Play › Setup: "This rule-set includes three campaigns … all three sections long" vs. thirteen campaigns of three to six sections in CAMPAIGNS.
- Character Tokens: "three different types" vs. "four following tokens"; Ember is said to live in the token supply, not on the dashboard.
- Tokens: "35x Condition tokens" vs. itemised 7×4 + 4×2 = 36.
- Stat Tier Costs (basic): Tier Three 8, Tier Four 8 (campaign table is 4/8/16/20).
- "first player token" is used in Encounter Start but is not a listed component.
- Parry requires "a shield as their left weapon"; dashboards never define left/right weapon slots.
- "lost" (character removed from play after dying while hollow) is used but never defined.
- Mimics: the expansion is called "Encounters" and "Explorers" in consecutive sentences.
- A Hollow Pursuit (Explorers campaign) repeats Demon Hunting's requirements line ("core set and Asylum Demon expansion").

### 3.6 Cross-reference errors
Prose cross-references only ("explained in detail later on in the section title 'Character Attacks'", "See the detailed rules on mimics later", "Refer to 'Boss Encounter' rules", "as described earlier"). No numbered §-references exist. One external reference: "special rules described in the mega-boss rule booklet". All are scheduled for conversion/removal in Phase 2A.

### 3.7 Style baseline (grep)
- Hedge words: should ×34, might ×4, could ×4, reasonably ×1, likely ×1 (44 total).
- Americanisms (armor/behavior/center/favor/color/defense/license/gray…): 0 — the manuscript is already British-spelled. Misspellings: "publically", "Titanate", "Andor Londo", "Earthern", "Jeramiah"/"Jeremiah".
- "you": 1 occurrence (front matter).
- Italicised keywords: ~45 distinct terms, inconsistently applied (e.g. *bonfire* ×36 vs plain "bonfire" elsewhere; *hollow.* with trailing punctuation inside italics).

## 4. Tooling inventory (honest)
| Need | Available | Substitution |
|---|---|---|
| PDF text/metadata/fonts/images | poppler: pdfinfo, pdftotext, pdffonts, pdfimages, pdftoppm, pdftocairo | — |
| PDF parsing in Python | pypdf, pdfplumber | — (no PyMuPDF/fitz) |
| DOCX conversion | pandoc 3.x, python-docx, LibreOffice | — |
| Raster editing | ImageMagick `convert`, Pillow | no ghostscript, no inkscape (vector SVG via pdftocairo only) |
| Typesetting to PDF | **none of LaTeX / WeasyPrint / InDesign present**; reportlab is installed; LibreOffice can print ODT/HTML → PDF | Phase 2C will attempt `pip install weasyprint` (needs libpango) and fall back to pandoc → HTML → LibreOffice → PDF or reportlab; recorded in `30_pdf_production_notes.md` |
| Fonts | fc-list available; inventory pending asset agent | open-font substitutes to be logged in `22_asset_extraction_log.md` |

## 5. Asset reconnaissance
Running as a sub-agent (Phase 0 step 4). Outputs: `22_asset_extraction_log.md`, `21_asset_manifest.csv`, `assets/`. Summary appended below on completion.

## 6. Verdict

**READY_FOR_PHASE_1.** All inputs are present and readable; no truncation; the manuscript's defects are editorial, not blocking. Open question raised at intake: OQ-04 — the brief's "Combat Cards" section does not exist in this DOCX revision; confirm whether a newer manuscript revision exists.
