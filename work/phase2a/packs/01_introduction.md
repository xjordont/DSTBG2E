# Drafting pack — chapter 01 (introduction) — manuscript chapter "INTRODUCTION"

Source text: `work/phase2a/source/01_introduction.md` (manuscript.md lines 361–370).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 361.

## Audit findings mapped to this chapter (4)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### C-030 · italics · Minor · REQUIRED
- Location: Whole body
- Evidence: Inconsistent keyword italicisation (italic/plain in rules text L361-3100): bonfire 39/79; soul 35/33; dodge 27/17; cleared 27/5; spark 25/16; ember 23/10; hollow 19/8; block 17/8; resist 15/6; aggro 14/10; luck 12/4; heroic action 11/5; attack option 10/5; threat 10/14; stamina 8/34; run 12/1; walk 8/0; shift 8/1; parry 7/0; push 2/49; heat-up 2/15; endurance bar 1/16
- Current text: *bonfire* ... the bonfire
- Proposed fix: Adopt one policy (recommended: italicise a glossary keyword at its first use in each H2 section and in headings/tables; plain thereafter) and apply it mechanically from the glossary headword list.
- Rationale: Readers cannot tell which words are defined terms; the Introduction (L381) promises every italicised term is in the glossary.
- Gameplay impact: None
- Decision needed: Y

### C-101 · heading · Minor · CLEAN-UP
- Location: L1111; L1119; L1143; L1173; L1680-1700; L523; L1015; L1041; L1091; L2454ff; L361; L2217
- Evidence: Case and whitespace: sentence-case H3s 'Encounter tiles' (1111), 'Encounter cards' (1119), 'Towards aggro', 'Away from aggro', 'Towards nearest', 'Away from nearest', 'Push-move', 'Push-attack' (1680-1700); mixed 'Setup After the mini-boss' (1143, 1173); 'Mega-bosses' (523) vs 'Mini-Bosses'/'Main-Bosses'; 'Class-specific Treasure' (1015); trailing spaces (1041, 1091, 2454, 2502, 2548, 2594, 2662, 2718, 2764, 2810, 2882, 2946, 2992); double space '#  INTRODUCTION' (361), '#  CAMPAIGN PLAY' (2217)
- Current text: Encounter tiles / Towards aggro / Mega-bosses
- Proposed fix: H1 ALL CAPS (chapter), H2 and H3 Title Case ('Encounter Tiles', 'Towards Aggro', 'Mega-Bosses', 'Setup After the Mini-Boss'); keyword italics permitted inside headings; no trailing or double spaces
- Rationale: One case convention per heading level.
- Gameplay impact: None
- Decision needed: N

### F-008 · tone · Minor · CLEAN-UP
- Location: L363 §Introduction ¶1
- Evidence: Future tense and abbreviation in the opening paragraph: 'Each player will control one character…'; '(DStBG 2E)'
- Current text: Dark Souls the Board Game Second Edition (DStBG 2E) is a cooperative dungeon crawl board game for one to four players. Each player will control one character of a party of one to four characters…
- Proposed fix: REWRITE-IN-VOICE — see Introduction draft in F_report.md §9.
- Rationale: Present tense; the abbreviation is never needed again once 'DStBG has many expansion sets' (L1057, L1141) is rewritten.
- Gameplay impact: none
- Decision needed: N

### F-007 · second-person · Note · OPTIONAL
- Location: L369 §Introduction
- Evidence: Imperative addressed to the reader in chapter-intro flavour: 'Nameless accursed undead, seek strength, and prepare to die.'
- Current text: Nameless accursed undead, seek strength, and prepare to die.
- Proposed fix: KEEP-AS-INTRO (unchanged). Flavour imperatives are permitted in the Introduction only.
- Rationale: Chapter-intro flavour is permitted; it is the single sanctioned second-person voice in the book.
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (1) — approved at Gate 1

### [CMP-0013] INTRODUCTION / SECOND EDITION NOTES — Foreword options (OQ-01) and colophon credits — Proposed Completion
- Current state: SECOND EDITION NOTES (lines 371–381) is design-process commentary in the first person, with complaints about the publisher ("SFG had lied"), requests for comment, and a note about diagrams and copyright. The Introduction (lines 361–369) is four short paragraphs. The front matter byline (lines 1–3) reads "By PittedPanda / Based on related works by Steam Forged Games (SFG), Konami, Santuric, Wilhelm, Astray, Manuel, Chud, Winston, Jyace, Absolute Disgrace, Zed, Gorus, and the rest of the DStBG Community." Line 381 (the glossary promise) is the one sentence in the chapter that belongs in the book.
- Proposed completion:

  **Option A — Foreword (≤200 words), replacing SECOND EDITION NOTES in full:**

  > # FOREWORD
  >
  > Dark Souls: The Board Game was published in 2017 and grew, expansion by expansion, into a large and uneven body of rules. This Second Edition gathers those rules into one book, revises the mechanics that long play exposed as weak, and states every rule once, in one place, so that a table needs no other text.
  >
  > The core of the game is unchanged: a party of one to four characters explores a string of encounters, learns the patterns of its enemies, returns to the bonfire to rest and grow stronger, and at last faces a boss. What has changed is the pace and the balance. Enemies act first and in threat order. Blocking, resisting, dodging and parrying each cost something and each reward a different kind of equipment. The shop restocks only when a boss falls. Death drops souls, and the hollow fight with less endurance until they rest or find an ember.
  >
  > These rules were shaped by the community that kept the game alive. Every mechanic in this book has been played, argued over and played again. Where a term is set in italics, its definition is in the Glossary.
  >
  > Prepare to die.

  (171 words.)

  **Option B — Expanded Introduction (≤120 words), replacing INTRODUCTION in full, with SECOND EDITION NOTES cut entirely:**

  > # INTRODUCTION
  >
  > Dark Souls: The Board Game Second Edition is a cooperative dungeon crawl for one to four players. Each player controls one character. The characters explore a chain of encounters, defeat a mini-boss and then a main-boss, and, if the players choose, a mega-boss after that.
  >
  > To succeed the characters must learn their enemies' behaviours, raise their stats, seek out powerful weapons and work together through increasingly dangerous encounters. When a character dies they rise again hollow, weaker until they rest at the bonfire or consume an ember. The bonfire's sparks are few, and every rest spends one.
  >
  > This edition collects the rules of the game and its expansions into one revised, self-contained book. Terms set in italics are defined in the Glossary.
  >
  > Nameless accursed undead, seek strength, and prepare to die.

  (119 words.)

  **Colophon credits block (two lines), replacing the byline at lines 1–3:**

  > Second Edition rules by PittedPanda, with the Dark Souls: The Board Game community: Santuric, Wilhelm, Astray, Manuel, Chud, Winston, Jyace, Absolute Disgrace, Zed and Gorus.
  > Based on Dark Souls: The Board Game by Steamforged Games Ltd. Dark Souls is a trademark of Bandai Namco Entertainment Inc. and FromSoftware, Inc. This is an unofficial, non-commercial fan work.

- Design rationale: Option A keeps a foreword's function (why the edition exists, what changed) without first person, process notes or grievance; its description of the changes is drawn from the manuscript's own chapters. Option B assumes the Notes chapter is cut and folds the one necessary sentence (the glossary promise) into the Introduction, preserving the original closing line. The credits block names the same contributors, drops "Konami" (the Dark Souls rights-holders are Bandai Namco and FromSoftware, as every supplied booklet states) and adds the fan-work disclaimer the original front matter lacks.
- Mechanical impact: None.
- Follow-on changes required: Editor decision on OQ-01 (A or B). Whichever is chosen, delete lines 371–381. Confirm the contributor list and the handle "PittedPanda" with the author. Regenerate TOC.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

