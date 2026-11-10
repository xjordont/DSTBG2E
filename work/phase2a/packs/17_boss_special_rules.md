# Drafting pack — chapter 17 (boss_special_rules) — manuscript chapter "BOSS SPECIAL RULES"

Source text: `work/phase2a/source/17_boss_special_rules.md` (manuscript.md lines 2199–2216).

## Tracker rows (section · status · notes)

- **(chapter)** · present — incomplete · line 2199. Only Asylum/Stray Demon covered; text elsewhere defers to "the mega-boss rule booklet" (external reference).
- **Asylum Demon & Stray Demon** · present — to audit · line 2201.
- **Pillar Smasher** · present — to audit · line 2203.
- **Wind Up** · present — to audit · line 2211.
- **(empty heading)** · ORPHAN — delete · line 2215: empty H1 used as page break

## Audit findings mapped to this chapter (10)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-115 · omission · Major · PROPOSED
- Location: BOSS SPECIAL RULES (manuscript.md lines 2199–2213); Setup After the main-boss step 11 (line 1195)
- Evidence: manuscript.md:1195, 1640, 2199–2213; DS-BDK-Rules-web.txt p.12–13 (Strafe cards, Signature cards, Calamity); DS-EC-Rules-Web.txt p.12–15 (track deck, No Starting Health, Death Race, Central Wall, Chariot Crash)
- Current text: The characters now begin combat with the mega-boss employing any special rules described in the mega-boss rule booklet.
- Proposed fix: Replace the external reference with sections under Boss Special Rules for each supported mega-boss. For the supplied booklets: Black Dragon Kalameet (Signature cards always in the deck; Strafe deck; Strafe attack targets the nodes shown and lands the boss on the landing node, pushing characters there to any adjacent node; Calamity condition). Executioner's Chariot (track behaviour deck resolved in numbered order; the boss has no health until every other enemy is slain; track attacks target the nodes shown and push hit characters to untargeted adjacent nodes; the board centre is treated as a gravestone node; on heat-up remove the chariot, flip the data card and switch to the heat-up deck).
- Rationale: The manuscript's own goal (line 375) is a rulebook that needs no other text, yet nine mega-bosses are listed and only the Asylum/Stray Demon is covered. The Calamity condition (1640) is defined but the Strafe mechanic that delivers it is not.
- Gameplay impact: Mega-boss games are unplayable from the manuscript alone.
- Decision needed: N

### C-081 · cross-ref · Major · REQUIRED
- Location: L1195; L2199-2213
- Evidence: 'employing any special rules described in the mega-boss rule booklet' - external reference; §BOSS SPECIAL RULES covers only Asylum Demon and Stray Demon
- Current text: described in the mega-boss rule booklet
- Proposed fix: 'employing that boss's special rules (see §Boss Special Rules)' - and complete §Boss Special Rules for every listed mega-boss, or state explicitly that each mega-boss's expansion rules apply
- Rationale: A self-contained rulebook (L375 goal) cannot point to an external booklet.
- Gameplay impact: None
- Decision needed: Y

### A-114 · omission · Minor · CLEAN-UP
- Location: BOSS SPECIAL RULES › Pillar Smasher (manuscript.md line 2205); GAME COMPONENTS (lines 679–723)
- Evidence: manuscript.md:679–723, 2205–2209
- Current text: place one pillar token on each of the four pillar nodes found on the mega-boss game board.
- Proposed fix: Add to Tokens & Terrain Elements: 4x Pillar tokens (Asylum Demon expansion). Add to The Basics: pillar nodes are terrain nodes printed on the Asylum Demon mega-boss board.
- Rationale: Pillar tokens and pillar nodes are used but never listed or located.
- Gameplay impact: Cosmetic.
- Decision needed: N

### C-030 · italics · Minor · REQUIRED
- Location: Whole body
- Evidence: Inconsistent keyword italicisation (italic/plain in rules text L361-3100): bonfire 39/79; soul 35/33; dodge 27/17; cleared 27/5; spark 25/16; ember 23/10; hollow 19/8; block 17/8; resist 15/6; aggro 14/10; luck 12/4; heroic action 11/5; attack option 10/5; threat 10/14; stamina 8/34; run 12/1; walk 8/0; shift 8/1; parry 7/0; push 2/49; heat-up 2/15; endurance bar 1/16
- Current text: *bonfire* ... the bonfire
- Proposed fix: Adopt one policy (recommended: italicise a glossary keyword at its first use in each H2 section and in headings/tables; plain thereafter) and apply it mechanically from the glossary headword list.
- Rationale: Readers cannot tell which words are defined terms; the Introduction (L381) promises every italicised term is in the glossary.
- Gameplay impact: None
- Decision needed: Y

### C-077 · table-text · Minor · CLEAN-UP
- Location: L679-723; L1277; L2205; L2055; L1997; L1137; L1975; L1315
- Evidence: Items used in rules but absent from Tokens & Terrain Elements: first player token (1277), pillar tokens (2205), Titanite Scale cards (2055), invader tokens and blank invader tokens (1997-2007), ambush cards (1137), phantom cards (1975), hollow cubes (781). L1315 'Mark the encounter card *cleared* with a black cube' uses a stamina cube as a marker.
- Current text: (absent)
- Proposed fix: Decide the scope of the component list (core only vs all supported content) and either add the expansion components under their expansion name or state that expansion components are listed in their own booklets; state that the cleared marker is a black stamina cube.
- Rationale: Component list is the reader's inventory check.
- Gameplay impact: None
- Decision needed: Y

### C-098 · heading · Minor · REQUIRED
- Location: L893; L983; L1059; L1441; L1842; L1882; L1910; L1925; L1959; L1965; L2049; L2059; L2215; L2308; L2324; L2336; L2400; L3036; L3096; L3100
- Evidence: 20 empty headings ('# ', '## ', '### ') used as page breaks
- Current text: #  (empty)
- Proposed fix: Delete all 20; page breaks belong to layout, not structure.
- Rationale: Empty headings produce blank TOC entries and broken numbering.
- Gameplay impact: None
- Decision needed: N

### C-104 · heading · Minor · CLEAN-UP
- Location: L2350; L1662; L679-2237 (9 headings); L3038; L3098; L1967
- Evidence: '# CAMPAIGNS' (2350) jumps to H3 with no H2; '## Overview' (1662) is generic; '&' in nine headings (679, 895, 1199, 1203, 1710, 1766, 2161, 2201, 2237); '# PLAYER VS PLAYER' (3038) vs 'Target versus Hit' (1483); '# F.A.Q.' (3098); '# SUMMONS' (1967) contains Invaders
- Current text: CAMPAIGNS > ### ; Overview; Tokens & Terrain Elements; PLAYER VS PLAYER; F.A.Q.; SUMMONS
- Proposed fix: Promote campaign headings to H2; 'Enemy Turn Overview'; 'and' for '&' in headings; 'PLAYER VERSUS PLAYER (PvP)'; 'FAQ'; 'PHANTOMS'
- Rationale: Consistent hierarchy and wording.
- Gameplay impact: None
- Decision needed: N

### C-112 · punctuation · Minor · CLEAN-UP
- Location: L679; L895; L1199; L1203; L1710; L1766; L2161; L2201; L2237; L449; L2398
- Evidence: '&' in nine headings and in list items 'Mushroom Child & Parent' (449), 'Ornstein & Smough' (2398, 2500, 2660, 2934)
- Current text: &
- Proposed fix: 'and' in headings and prose; '&' only inside an official product or card name
- Rationale: Ampersand is a logo/label device, not prose.
- Gameplay impact: None
- Decision needed: N

### C-114 · punctuation · Minor · REQUIRED
- Location: L919; L1931; L2069; L2157; L2185; L2207
- Evidence: Sentences beginning with lower-case 'characters': 'characters must choose a friendly model' (919); 'characters cannot equip weapons' (1931); 'characters can expect to die often' (2069); 'characters must take an equal number of turns' (2157); 'characters targeted by an *area* attack' (2185); 'characters within one node range' (2207)
- Current text: characters ...
- Proposed fix: Characters ...
- Rationale: Capitalise sentence starts (likely a global find-and-replace artefact).
- Gameplay impact: None
- Decision needed: N

### C-123 · voice · Minor · CLEAN-UP
- Location: L979; L1596; L1674; L1676; L2157; L2191; L2207; L1963
- Evidence: Conversational filler: 'simply stop adding trap tokens' (979); 'Of course,' (1596); 'it simply does not move' (1674, 1676); 'and so-on' (2157); 'one can assume... simply move' (2191); 'it is possible for a demon to smash through multiple pillars' (2207); 'nearly ready to resume' (1963)
- Current text: simply / Of course / and so-on / one can assume / it is possible
- Proposed fix: Delete the filler; state the rule: 'the enemy does not move'; 'A demon may destroy several pillars with one attack.'
- Rationale: Terse voice.
- Gameplay impact: None
- Decision needed: N

## Completion entries that apply (2) — approved at Gate 1

### [CMP-0005] BOSS SPECIAL RULES (chapter) — Proposed Completion (partly BLOCKED — source booklet not supplied)
- Read `04_completion_backlog.md` lines 563–682 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0017] BOSS SPECIAL RULES › Wind Up — Scope — Proposed Completion
- Read `04_completion_backlog.md` lines 1094–1103 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

