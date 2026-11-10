# Drafting pack — chapter 19 (campaigns) — manuscript chapter "CAMPAIGNS"

Source text: `work/phase2a/source/19_campaigns.md` (manuscript.md lines 2350–3037).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 2350.
- **The First Journey - Dark Souls (Core)** · present — defect · line 2352. "Gargoyle (Mini-Boss)" listed twice; "Andor Londo" (Anor Londo).
- **(empty heading)** · ORPHAN — delete · line 2400: empty H3 used as page break
- **The Coiled Sword - Dark Souls 3 (Core)** · present — to audit · line 2402.
- **Ambush Lies Ahead - Dark Souls (Phantoms)** · present — defect · line 2454. "Do no place"; Jeramiah/Jeremiah inconsistent; Gargoyle twice.
- **The Gauntlet - Dark Souls (Phantoms)** · present — to audit · line 2502.
- **Facing the Abyss - Dark Souls (Darkroot Basin)** · present — to audit · line 2548.
- **Demon Hunting - Dark Souls (Asylum Demon)** · present — defect · line 2594. Section One has no Bonfire Tile (intentional?); Gargoyle twice; Andor Londo.
- **Call of the Abyss - Dark Souls (The Four Kings)** · present · line 2662. Four Kings expansion not among supplied references.
- **A Hollow Pursuit - Dark Souls 2 (Explorers)** · present — defect · line 2718. Requirements line copied from Demon Hunting ("Asylum Demon expansion"); "Earthern".
- **Facing the Abyss - Dark Souls (Darkroot)** · DUPLICATE · line 2764. Second copy of "Facing the Abyss" with different preamble; sections identical.
- **The Undead Colosseum - Dark Souls (Executioner Chariot)** · present — to audit · line 2810.
- **Into the Depths - Dark Souls (Gaping Dragon)** · present — to audit · line 2882.
- **Playing with Fire - Dark Souls 2 (Iron Keep)** · present — to audit · line 2946.
- **Big Game Hunting - Dark Souls (Manus)** · present — defect · line 2992. "The Last Giant (Mega Boss)" — not in component list; campaign overrides boss tiles.
- **(empty heading)** · ORPHAN — delete · line 3036: empty H1 used as page break

## Audit findings mapped to this chapter (44)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-039 · undefined-state · Major · PROPOSED
- Location: GAME COMPONENTS › Main-Bosses (manuscript.md lines 509–511) vs CAMPAIGNS (lines 2398, 2500, 2660, 2934); Node Model Limits (line 921)
- Evidence: manuscript.md:509, 511, 921, 2157, 2191, 2398; DS-Core-Rules-lores.txt p.5 ('Dragon Slayer Ornstein & Executioner Smough' is one main boss), p.21
- Current text: Dragon Slayer Ornstein (Core) / Executioner Smough (Core) ... Ornstein & Smough (main-boss)
- Proposed fix: Multiple-boss encounters: When a boss encounter contains two bosses, each boss has its own behaviour deck, health dial and heat-up point. During each boss turn both bosses act, in descending threat order; if tied, the players choose. The aggro token is assessed once for both bosses. The special rules on the bosses' data cards state what happens when one of them is slain. The encounter is cleared when both bosses are slain, and a single boss treasure is awarded.
- Rationale: The component list splits the pair while every campaign lists them as one boss. The only multi-boss rule in the manuscript is the node push (921). Alternative: list the pair as one main boss and play both bosses on a single alternating sequence (boss A, character, boss B, character).
- Gameplay impact: The core set's main boss cannot be played from the text.
- Decision needed: Y

### A-040 · undefined-state · Major · PROPOSED
- Location: CAMPAIGNS › The First Journey, Ambush Lies Ahead, Demon Hunting (manuscript.md lines 2366–2368, 2468–2470, 2616–2618)
- Evidence: manuscript.md:2366–2368, 2468–2470, 2616–2618; DS-Core-Rules-lores.txt p.35 footnote; DS-Phantoms-Rules-lores.txt p.17 footnote
- Current text: Gargoyle (Mini-Boss) / Gargoyle (Mini-Boss)
- Proposed fix: Gargoyle ×2: The characters fight two Gargoyle boss encounters in succession on the boss tile without resting between them. The second Gargoyle encounter begins immediately after the first Gargoyle is slain, with the characters' endurance bars and tokens unchanged and a fresh behaviour deck. Boss treasure, the spark and ember tokens are awarded only after the second Gargoyle is slain. If the characters fail against either Gargoyle, both must be fought again.
- Rationale: Listed twice in three campaigns with no rule; the official footnote (treasure only for back-to-back wins, re-fight both after a defeat) is omitted. Alternative: a single encounter containing two Gargoyle models under the multiple-boss rule (A-039).
- Gameplay impact: First campaign section of the core set is undefined at its climax.
- Decision needed: Y

### A-048 · undefined-state · Major · REQUIRED
- Location: CAMPAIGN PLAY › Sparks (manuscript.md line 2235); SETUP › Setup After the mini-boss steps 10–11 (lines 1167–1169); CAMPAIGNS (Gauntlet 2502–2546, Facing the Abyss S1 2564, Playing with Fire S1 2962)
- Evidence: manuscript.md:1167–1169, 2235, 2314, 2564, 2962, 2502–2546; DS-Darkroot-Rules-web.txt p.11 ('The party proceeds to Section 2 when the encounter is defeated'); DS-Phantoms-Rules-lores.txt p.19
- Current text: characters no longer rest at the bonfire for free after defeating a boss except for the final boss of each section.
- Proposed fix: When a section ends with an encounter rather than a boss, clearing that encounter counts as defeating the section's final boss: the characters gain one spark, rest at the bonfire without spending a spark, restock the shops and set up the next section. When a section contains more than one boss, the characters gain one spark for each boss slain but rest without spending a spark only after the section's final boss.
- Rationale: Four campaign sections end in a named encounter and the Gauntlet has no bosses at all; sparks, free rests, restocks and section setup are all keyed to 'boss' in the manuscript.
- Gameplay impact: Three supplied campaigns cannot progress between sections as written.
- Decision needed: N

### A-049 · contradiction · Major · REQUIRED
- Location: SETUP › Setup After the main-boss step 11 (manuscript.md line 1195) vs CAMPAIGNS › Demon Hunting Section Four (line 2644), Big Game Hunting (lines 3012–3034)
- Evidence: manuscript.md:1195, 2235, 2644, 2996, 3018–3034
- Current text: If a character dies they are permanently removed from play. If all characters die, the players lose the game. If any character survives to defeat the mega-boss, the players win the game.
- Proposed fix: The permanent-death and victory rules of the mega-boss encounter apply only when the mega-boss is the final boss of the game. In campaign play a mega-boss that is not the campaign's final boss is fought under the normal boss rules; when slain it awards a spark, ember tokens and boss treasure like any other boss, and the campaign continues.
- Rationale: Demon Hunting places the Stray Demon in Section Four of five, and Big Game Hunting has three mega-bosses; under the literal text the game ends at the first of them.
- Gameplay impact: Two campaigns end early or lose characters permanently mid-campaign.
- Decision needed: Y

### A-094 · undefined-state · Major · PROPOSED
- Location: CAMPAIGNS › Call of the Abyss Section Four (manuscript.md lines 2712–2714); Into the Depths Sections Four–Five (lines 2932, 2940–2942); Demon Hunting Section Four (line 2642); Big Game Hunting (lines 3016–3032)
- Evidence: manuscript.md:1179, 1193, 2642, 2712–2714, 2932, 2940–2942, 3016–3032; DS-EC-Rules-Web.txt p.7–8 and DS-BDK-Rules-web.txt p.7–8, p.15 (Level 4 encounters are played on the encounter side of the mega-boss game board)
- Current text: Level 4 Encounter / Level 4 Encounter / The Four Kings (Mega Boss)
- Proposed fix: In campaign play a Level 4 encounter is always played on the encounter side of a mega-boss game board placed in the section's tile sequence. When a section lists two Level 4 encounters, the second is played on a second mega-boss board if one is available; otherwise the same board is cleared and reused after the first encounter is cleared. The board is flipped to its boss side only when the section's mega-boss is reached.
- Rationale: The basic game puts the single Level 4 encounter on the mega-boss tile (1179); campaigns list Level 4 encounters mid-section and twice in a row with no board rule.
- Gameplay impact: Four campaign sections cannot be laid out as written.
- Decision needed: Y

### A-104 · undefined-state · Major · PROPOSED
- Location: CAMPAIGNS › Demon Hunting Section One (manuscript.md lines 2598–2608)
- Evidence: manuscript.md:1223, 1341, 1894, 2598–2608
- Current text: Section One - Undead Asylum: Level 1 Encounter, Level 1 Encounter, Asylum Demon (Mini-Boss) ... Bonfire Tile (characters revive here if they die in Section One)
- Proposed fix: Demon Hunting, Section One: there is no bonfire tile. If the characters are forced to rest during Section One, they spend a spark, revive and restore their characters as if resting, and restart Section One from its first encounter tile; the Firekeeper, Andre and the shop are not available until Section Two.
- Rationale: Every forced rest in the manuscript sends the party to the bonfire tile; Section One has none, and the parenthetical only says where characters revive, not what happens to the section. Alternative: the party is moved to Section Two's bonfire and Section One is abandoned.
- Gameplay impact: The opening section of the campaign has no defeat procedure.
- Decision needed: Y

### A-108 · omission · Major · REQUIRED
- Location: CAMPAIGNS › Big Game Hunting (manuscript.md lines 2994, 3018); GAME COMPONENTS › Mega-bosses (lines 523–541)
- Evidence: manuscript.md:523–541, 2994, 3018
- Current text: The Last Giant (Mega Boss)
- Proposed fix: Add 'The Last Giant (The Last Giant)' to the Mega-bosses component list and 'the Last Giant expansion' to the campaign's requirements.
- Rationale: A boss used by a campaign is absent from the components and from the campaign's own requirements line.
- Gameplay impact: Campaign cannot be assembled from the component list.
- Decision needed: N

### C-018 · hedge · Major · REQUIRED
- Location: L845; L1057; L1141; L2041; L2053; L2596; L2664; L2720; L2766; L2812; L2884; L2948; L2994
- Evidence: 14 'should' in optional-content advice, e.g. L845 'Players should include all equipment cards from expansions'; L1141 'players should include only the encounter cards from the same set'; L2041 'Groups with new players should default to leaving mimics out... Experienced players should include mimics'; L2596ff 'players should add the Explorers and Characters expansions if available' (x8)
- Current text: Players should include / should add / should default to
- Proposed fix: Rewrite as permissions or labelled recommendations: 'Players may include equipment cards from every expansion they own.' / 'By default, build each encounter deck only from cards of the next boss's set.' / 'Mimics are an optional rule; the players decide during setup whether to use them.' / campaign lines: 'Recommended: Explorers and Characters expansions.' Full per-line rewrites in C_report.md Task 2.
- Rationale: 'Should' leaves it unclear whether expansions are required, optional or recommended. Lawbook voice uses must/may or a labelled 'Recommended' line.
- Gameplay impact: Which components a group must own to play a campaign
- Decision needed: Y

### C-074 · table-text · Major · REQUIRED
- Location: L2223; L2225; L2350-3034
- Evidence: L2223 'the included campaigns are all three sections long'; L2225 'This rule-set includes three campaigns which require only the components available in the core set' vs CAMPAIGNS chapter: 13 campaigns, 3 to 6 sections each, of which 2 are core-only (The First Journey, The Coiled Sword)
- Current text: all three sections long; three campaigns which require only the... core set
- Proposed fix: 'The included campaigns are three to six sections long.' / 'Two campaigns require only the core set; the others require the expansions listed in each campaign's requirements line.'
- Rationale: Introductory prose contradicts the chapter it introduces.
- Gameplay impact: None
- Decision needed: N

### C-075 · table-text · Major · REQUIRED
- Location: L523-541; L3018; L2994
- Evidence: Mega-bosses component list (523-541) omits The Last Giant, used at L3018 'The Last Giant (Mega Boss)'; 'Big Game Hunting' requirements (L2994) list 'Core set, Manus expansion, and Asylum Demon expansion' only
- Current text: (absent from list; absent from requirements)
- Proposed fix: Add '- The Last Giant (The Last Giant)' to Mega-bosses; add 'The Last Giant expansion' to the Big Game Hunting requirements
- Rationale: A campaign uses a boss that the component list and the requirements line do not mention. (The Last Giant is a Kickstarter mega-boss expansion; verify against its booklet, which is not among the supplied sources.)
- Gameplay impact: Players cannot play Section Two A without the expansion
- Decision needed: Y

### C-076 · table-text · Major · REQUIRED
- Location: L2720; L2812; L2884; L2596
- Evidence: 'A Hollow Pursuit' (2720) requires 'core set and Asylum Demon expansion' but its sections use Old Dragonslayer, Voracious Mimic and Pursuer (all Explorers) and no Asylum Demon content - the line is copied from Demon Hunting (2596); 'The Undead Colosseum' (2812) omits Explorers though it uses Old Dragonslayer and Pursuer; 'Into the Depths' (2884) lists Darkroot as 'should add if available' though Artorias (Darkroot) is Section Three's boss
- Current text: requires the core set and Asylum Demon expansion
- Proposed fix: A Hollow Pursuit: 'Requires: Core set, Explorers.' Undead Colosseum: add Explorers to Requires. Into the Depths: move Darkroot from recommended to Requires.
- Rationale: Requirements lines must list every expansion whose bosses or enemies appear in the campaign.
- Gameplay impact: Players discover mid-campaign that they lack a boss
- Decision needed: N

### C-102 · heading · Major · REQUIRED
- Location: L2548-2592; L2764-2808
- Evidence: Two campaigns titled 'Facing the Abyss - Dark Souls (Darkroot Basin)' and 'Facing the Abyss - Dark Souls (Darkroot)' with identical section lists; preambles differ ('Use encounters from only the Darkroot basin expansion' vs 'requires the Core set and Darkroot expansion but players should add the Explorers and Characters expansions')
- Current text: (duplicate campaign)
- Proposed fix: Delete one; merge the preamble into 'Requires: Core set, Darkroot Basin. Recommended: Explorers, Characters. Use Darkroot Basin encounters only.'
- Rationale: Duplicate content.
- Gameplay impact: None
- Decision needed: Y

### D-013 · dropped-rule · Major · REQUIRED
- Location: manuscript.md 2810–2880 (The Undead Colosseum)
- Evidence: EC p.18: encounter cards are never turned face down when the party rests; a defeated encounter is never fought again; the party gains 4 souls per player per encounter regardless of level; sections 5 and 6 each contain a Level 4 encounter drawn from the Vordt/Chariot decks. The manuscript lists the sections but omits all three special rules and the Level 4 encounter of section six.
- Current text: Section Six - Terror of the Ring: Bonfire Tile / Level 3 Encounter - Desolate Cemetery / Vordt of the Boreal Valley (Mega Boss)
- Proposed fix: Section Six: Bonfire Tile; Level 3 Encounter – Desolate Cemetery; Level 4 Encounter; Vordt of the Boreal Valley (Mega Boss). In this campaign cleared encounters are not reset when the characters rest and are never fought again; each cleared encounter rewards four souls per character irrespective of its level.
- Rationale: The campaign's identity is its no-reset rule; without it the listing is just a longer standard campaign.
- Gameplay impact: Campaign difficulty and economy.
- Decision needed: N

### F-089 · tone · Major · CLEAN-UP
- Location: L765, L979, L1131, L1159, L1201, L1461, L1479, L1666, L1880, L2065, L2169, L2596 ff.
- Evidence: 'should' used as a rule modal: 'players should not interact with their character's inventory cards' (L765); 'Players should fill the basic nodes furthest from the tiles entry' (L979); 'Encounter levels should increase' (L1131); 'the character should mark the equipped item' (L1880); 'the fog gate tile should be removed' (L2065); 'The target character model should remain static' (L2169); 'players should add the Explorers and Characters expansions if available' (campaign headers ×9).
- Current text: Once the encounter has started players should not interact with their character's inventory cards.
- Proposed fix: Modal policy (Voice Guide §2): 'must' for obligations, 'may' for permissions, 'cannot' for prohibitions, 'is/are' for states. E.g. 'During an encounter the inventory cannot be accessed.'; 'Trap tokens are placed first on the basic nodes furthest from the entry.'; 'Encounter levels increase from the tile adjacent to the *bonfire* tile towards the boss tile.'; 'Mark the item with a red cube.'; campaign headers: 'Recommended additions: Explorers, Characters.'
- Rationale: 'should' is advisory and leaves the rule optional.
- Gameplay impact: none
- Decision needed: N

### F-090 · tone · Major · CLEAN-UP
- Location: L859, L979, L1674, L1676, L1852, L2073, L2103, L2121, L2123, L2191, L2221, L2245, L2297, L2312, L2456, L2504
- Evidence: Hedge and filler words in rules text: 'usually' (L859, L2073), 'simply' (L979, L1674, L1676, L1852, L2191), 'typically' (L2073, L2123), 'generally' (L2121), 'often' (L2103), 'largely' (L2221), 'just' (L2245, L2456, L2504), 'essentially' (L2297), 'similarly' (L2312).
- Current text: If an enemy movement icon instructs an enemy to move towards a character it already shares a node with, then it simply does not move. / Mega-boss encounters usually have a unique mega-boss encounter tile…
- Proposed fix: Delete the adverb or state the exception: 'An enemy instructed to move towards a character on its own node does not move.'; 'A mega-boss encounter uses the tile supplied with that mega-boss.'
- Rationale: No hedge words in rules.
- Gameplay impact: none
- Decision needed: N

### A-102 · contradiction · Minor · REQUIRED
- Location: CAMPAIGNS › A Hollow Pursuit Section Two (manuscript.md line 2748)
- Evidence: manuscript.md:2748, 2043–2047; DS-Explorers-Rules-Web.txt p.15 ('Do not place an Ambush card beside this tile; the chest is automatically a mimic. The party proceeds to Section 3 when the mimic is defeated')
- Current text: Add Voracious Mimic during encounter set-up..
- Proposed fix: Gallery of the Hidden Warrior: do not place an ambush card beside this tile; the chest is a Voracious Mimic. The section is completed when the mimic is slain.
- Rationale: 'During encounter set-up' places the mimic as an ordinary enemy, which contradicts the manuscript's own post-clear mimic procedure.
- Gameplay impact: Section progression depends on it.
- Decision needed: N

### A-103 · contradiction · Minor · REQUIRED
- Location: CAMPAIGN PLAY › Setup (manuscript.md lines 2223–2225)
- Evidence: manuscript.md:2223, 2225, 2352–3034
- Current text: the included campaigns are all three sections long. ... This rule-set includes three campaigns which require only the components available in the core set.
- Proposed fix: This rule-set includes thirteen campaigns, of which two require only the core set; the others list their required expansions. Campaigns are between three and six sections long.
- Rationale: Thirteen campaigns are listed; two are core-only; lengths run from three to six sections.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-106 · contradiction · Minor · CLEAN-UP
- Location: CAMPAIGNS › Facing the Abyss (manuscript.md lines 2548 and 2764)
- Evidence: manuscript.md:2548–2592, 2764–2808; DS-Darkroot-Rules-web.txt p.11
- Current text: Facing the Abyss - Dark Souls (Darkroot Basin) / Facing the Abyss - Dark Souls (Darkroot)
- Proposed fix: Keep one entry: Facing the Abyss – Dark Souls (Darkroot). This campaign requires the core set and the Darkroot expansion; use only Darkroot encounters.
- Rationale: Identical section lists with two preambles.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-107 · contradiction · Minor · CLEAN-UP
- Location: CAMPAIGNS › A Hollow Pursuit (manuscript.md line 2720)
- Evidence: manuscript.md:2596, 2720, 2734–2762; DS-Explorers-Rules-Web.txt p.14–15
- Current text: This campaign requires the core set and Asylum Demon expansion but players should add the Explorers and characters expansions if available.
- Proposed fix: This campaign requires the core set and the Explorers expansion.
- Rationale: Copied from Demon Hunting; the Old Dragonslayer, mimic and Pursuer are all Explorers components.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-109 · terminology · Minor · CLEAN-UP
- Location: CAMPAIGNS › The Gauntlet Section Three (manuscript.md line 2534)
- Evidence: manuscript.md:2506, 2534; DS-Phantoms-Rules-lores.txt p.19 ('Invader Spire')
- Current text: Section Three - Invader Ruins
- Proposed fix: Section Three – Invader Spire
- Rationale: Duplicates Section One's name; the official name is Invader Spire.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-110 · omission · Minor · OPTIONAL
- Location: CAMPAIGNS › The Undead Colosseum (manuscript.md lines 2810–2880)
- Evidence: manuscript.md:2812, 2830, 2874–2880; DS-EC-Rules-Web.txt p.18–19 (Section 6: Desolate Cemetery L3, Level 4, Vordt; campaign special rules: no face-down reset, 4 souls per player per encounter)
- Current text: Section Six - Terror of the Ring: Bonfire Tile, Level 3 Encounter - Desolate Cemetery, Vordt of the Boreal Valley (Mega Boss)
- Proposed fix: Section Six: Bonfire Tile; Level 3 Encounter – Desolate Cemetery; Level 4 Encounter; Vordt of the Boreal Valley (Mega-Boss). Correct 'Bonfire Tiles' in Section Two. Add the campaign's special rules or state that the standard campaign rules apply.
- Rationale: The Level 4 encounter is missing from the final section; the official campaign's distinctive rules (no reset, flat soul reward) are silently dropped. Alternative: keep standard rules and only add the missing Level 4.
- Gameplay impact: Final section is shorter than intended.
- Decision needed: Y

### C-003 · spelling · Minor · REQUIRED
- Location: L2384; L2486; L2646
- Evidence: 'Section Three - Andor Londo' (x2); 'Section Five - Andor Londo'
- Current text: Andor Londo
- Proposed fix: Anor Londo
- Rationale: Official location name (Core/TG rulebooks: 'Anor Londo' x5).
- Gameplay impact: None
- Decision needed: N

### C-004 · spelling · Minor · REQUIRED
- Location: L2736
- Evidence: 'Section Two - Lower Earthern Peak'
- Current text: Lower Earthern Peak
- Proposed fix: Lower Earthen Peak
- Rationale: Canonical name is Earthen Peak (Explorers booklet p.4 body text 'Earthen Peak'; the booklet's own campaign list repeats the typo).
- Gameplay impact: None
- Decision needed: N

### C-005 · spelling · Minor · REQUIRED
- Location: L557
- Evidence: 'Xanthous King Jeramiah' vs L2492/L2528 'Xanthous King Jeremiah'
- Current text: Xanthous King Jeramiah
- Proposed fix: Xanthous King Jeremiah
- Rationale: Phantoms booklet prints 'Xanthous King Jeremiah' (x3); the manuscript is internally inconsistent.
- Gameplay impact: None
- Decision needed: N

### C-009 · spelling · Minor · REQUIRED
- Location: L2734
- Evidence: 'Old Dragon Slayer (Mini-Boss)' vs L495/L2838 'Old Dragonslayer'
- Current text: Old Dragon Slayer
- Proposed fix: Old Dragonslayer
- Rationale: Explorers booklet: 'Old Dragonslayer' (x11); manuscript inconsistent.
- Gameplay impact: None
- Decision needed: N

### C-013 · spelling · Minor · CLEAN-UP
- Location: L2452; L2398; L2500; L2660; L2934
- Evidence: L2452 'The Dancer of the Boreal Valley' vs L507 'Dancer of the Boreal Valley'; 'Ornstein & Smough' vs components 'Dragonslayer Ornstein' (L509) and 'Executioner Smough' (L511)
- Current text: The Dancer of the Boreal Valley; Ornstein & Smough
- Proposed fix: Dancer of the Boreal Valley; Dragonslayer Ornstein and Executioner Smough (one boss encounter, two models) - state this once in the Main-Bosses component list
- Rationale: Boss names must match the component list so a reader can find the models and data cards.
- Gameplay impact: None
- Decision needed: N

### C-015 · spelling · Minor · REQUIRED
- Location: L793; L849; L887; L979; L1517; L1664; L1880; L2017; L2021; L2043; L2045; L2053; L2456; L2504; L3082; L377
- Evidence: Typos: L793 'a read and a used side'; L849 'play mail', 'used up grade armour'; L887 'a characters' catalyst'; L979 'the tiles entry'; L1517 'the enemies block'; L1664 'wound token's'; L1880 'who's stats', 'its' attack options'; L2017 'starting decks deck size'; L2021 'blocked by train'; L2043 'The then are faced'; L2045 'reveal one an ambush card', 'min-boss'; L2053 'offer character's powerful rewards'; L2456/L2504 'Do no place'; L3082 'based on an the attacker attack option's'; L377 'desist in google docs'
- Current text: (see Evidence)
- Proposed fix: ready side; plate mail; used to upgrade armour; a character's catalyst; the tile's entry nodes; the enemy's block; wound tokens; whose stats; its attack options; starting deck size; blocked by terrain; They then are faced; reveal the ambush card; mini-boss; offer characters powerful rewards; Do not place; based on the attacker's attack option's; reside in Google Docs
- Rationale: Plain typographical errors; 'Do no place' and 'blocked by train' change sense.
- Gameplay impact: L2456/L2504 'Do no place' reads as a permission, not a prohibition
- Decision needed: N

### C-030 · italics · Minor · REQUIRED
- Location: Whole body
- Evidence: Inconsistent keyword italicisation (italic/plain in rules text L361-3100): bonfire 39/79; soul 35/33; dodge 27/17; cleared 27/5; spark 25/16; ember 23/10; hollow 19/8; block 17/8; resist 15/6; aggro 14/10; luck 12/4; heroic action 11/5; attack option 10/5; threat 10/14; stamina 8/34; run 12/1; walk 8/0; shift 8/1; parry 7/0; push 2/49; heat-up 2/15; endurance bar 1/16
- Current text: *bonfire* ... the bonfire
- Proposed fix: Adopt one policy (recommended: italicise a glossary keyword at its first use in each H2 section and in headings/tables; plain thereafter) and apply it mechanically from the glossary headword list.
- Rationale: Readers cannot tell which words are defined terms; the Introduction (L381) promises every italicised term is in the glossary.
- Gameplay impact: None
- Decision needed: Y

### C-041 · terminology · Minor · CLEAN-UP
- Location: L483; L501; L523; L2073; L2366ff; L2692ff; L2716ff; L2826ff; L2996
- Evidence: mini-boss x47 / Mini-Boss x15 / Mini Boss x5 / mini boss x1 / 'mini bosses'; main-boss x31 / Main-Boss x1 / Main Boss x11; mega-boss x28 / Mega-boss x2 / Mega Boss x7 / 'mega boss' x1 (L2996)
- Current text: Mini Boss / Main Boss / Mega Boss / mini boss
- Proposed fix: mini-boss, main-boss, mega-boss (lower-case, hyphenated) in prose and campaign lists; Title Case 'Mini-Boss' only as a heading word
- Rationale: Six spellings of three terms; the campaign lists (L2692-3034) use the unhyphenated Title Case form throughout.
- Gameplay impact: None
- Decision needed: N

### C-042 · terminology · Minor · CLEAN-UP
- Location: L771; L849; L1131; L1171; L1179; L1886; L1892; L2195; L2295; L2358ff
- Evidence: 'The Bonfire' capitalised mid-sentence x10 (e.g. 771 'resting at The Bonfire'); '*bonfire*' x35; plain 'the bonfire' x27; 'Bonfire Tile' x48 in campaign lists; 'The Bonfire tile' (1131, 1171, 1179)
- Current text: The Bonfire / Bonfire Tile
- Proposed fix: the *bonfire* (lower-case keyword); 'bonfire tile' for the component; headings may read 'The Bonfire'
- Rationale: Game locations are common nouns (cf. fog gate, shop); capital 'The' mid-sentence is inconsistent with the keyword form.
- Gameplay impact: None
- Decision needed: N

### C-059 · terminology · Minor · CLEAN-UP
- Location: L969; L1017; L1021; L1025; L1029; L1201; L2055; L2748; L1473
- Evidence: 'set-up' x8 (noun), 'setup' x21 (noun), 'set up' (1473, verb)
- Current text: set-up
- Proposed fix: Noun 'setup' (and 'Setup' in headings); verb 'set up'
- Rationale: Standard British usage distinguishes noun and phrasal verb.
- Gameplay impact: None
- Decision needed: N

### C-098 · heading · Minor · REQUIRED
- Location: L893; L983; L1059; L1441; L1842; L1882; L1910; L1925; L1959; L1965; L2049; L2059; L2215; L2308; L2324; L2336; L2400; L3036; L3096; L3100
- Evidence: 20 empty headings ('# ', '## ', '### ') used as page breaks
- Current text: #  (empty)
- Proposed fix: Delete all 20; page breaks belong to layout, not structure.
- Rationale: Empty headings produce blank TOC entries and broken numbering.
- Gameplay impact: None
- Decision needed: N

### C-101 · heading · Minor · CLEAN-UP
- Location: L1111; L1119; L1143; L1173; L1680-1700; L523; L1015; L1041; L1091; L2454ff; L361; L2217
- Evidence: Case and whitespace: sentence-case H3s 'Encounter tiles' (1111), 'Encounter cards' (1119), 'Towards aggro', 'Away from aggro', 'Towards nearest', 'Away from nearest', 'Push-move', 'Push-attack' (1680-1700); mixed 'Setup After the mini-boss' (1143, 1173); 'Mega-bosses' (523) vs 'Mini-Bosses'/'Main-Bosses'; 'Class-specific Treasure' (1015); trailing spaces (1041, 1091, 2454, 2502, 2548, 2594, 2662, 2718, 2764, 2810, 2882, 2946, 2992); double space '#  INTRODUCTION' (361), '#  CAMPAIGN PLAY' (2217)
- Current text: Encounter tiles / Towards aggro / Mega-bosses
- Proposed fix: H1 ALL CAPS (chapter), H2 and H3 Title Case ('Encounter Tiles', 'Towards Aggro', 'Mega-Bosses', 'Setup After the Mini-Boss'); keyword italics permitted inside headings; no trailing or double spaces
- Rationale: One case convention per heading level.
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

### C-105 · heading · Minor · CLEAN-UP
- Location: L2854; L2864; L2944; L2692; L2794; L2830; L2748; L2478-2546; L2438; L2366-2368
- Evidence: Campaign list defects: 'Section Four- Haunting Warrior' (2854); 'Section Five Dark Champion' (2864, no dash); 'Gaping Dragon(Mega Boss)' (2944); 'Great Grey Wolf Sif (Main Boss).' trailing stop (2692, 2794); 'Bonfire Tiles' plural (2830); 'set-up..' (2748); invader lines end with a full stop in Sections Two/Three of Ambush Lies Ahead and Section Three of The Gauntlet but not Section Two (2526-2532); 'Section Three - High Wall of Lothric' repeats Section One's name (2438); 'Gargoyle (Mini-Boss)' listed twice (2366-2368, 2468-2470, 2616-2618)
- Current text: (see Evidence)
- Proposed fix: Normalise to 'Section N - Name' / 'Boss Name (mini-boss)' with no terminal punctuation on list items; confirm the double Gargoyle is intentional (two Bell Gargoyles) and if so write 'Gargoyle x2 (mini-boss, fought together)'; rename L2438 or confirm the return to High Wall.
- Rationale: List items follow one pattern.
- Gameplay impact: Double Gargoyle may be read as two separate boss encounters
- Decision needed: Y

### C-106 · punctuation · Minor · REQUIRED
- Location: L793; L2221; L2748; L2047
- Evidence: Double full stops: 'at the start of the game..' (793); 'at least a few times..' (2221); 'during encounter set-up..' (2748); '*cleared.*.' (2047)
- Current text: ..
- Proposed fix: Single full stop.
- Rationale: Typo.
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

### C-122 · voice · Minor · CLEAN-UP
- Location: L1115; L1141; L1241; L1461; L1479; L2027; L2047; L2055; L2057; L1171; L2996
- Evidence: Future tense for rules: 'This will create a linear route' (1115); 'they would use only the encounters' (1141); 'Invaders will attempt to kill the characters' (1241); 'the treasure will be awarded' (1461, 1479); 'the invader will take many more turns' (2027); 'The mimic will take its turn first' (2047); 'the crystal lizards will respawn' (2055); 'no further crystal lizards will spawn' (2057); 'When all three section two options are complete, the players win' (2996, ok)
- Current text: will be awarded / will take / will respawn
- Proposed fix: Present indicative: 'is awarded', 'takes its turn first', 'respawn'.
- Rationale: Rules are timeless statements.
- Gameplay impact: None
- Decision needed: N

### D-012 · dropped-rule · Minor · REQUIRED
- Location: manuscript.md 2366–2368 and 2468–2470 (The First Journey; Ambush Lies Ahead, Section One)
- Evidence: Core p.35 and PH p.17 footnote: the party receives the Gargoyles' treasure only after defeating two Gargoyle encounters back-to-back; if defeated by the second, both must be fought again from the Fog Gate.
- Current text: Gargoyle (Mini-Boss) / Gargoyle (Mini-Boss)
- Proposed fix: The characters receive the Gargoyle treasure only after defeating two Gargoyle encounters in succession. If the second Gargoyle defeats the party, both Gargoyle encounters are fought again.
- Rationale: The two listed Gargoyle entries are meaningless without the footnote.
- Gameplay impact: Campaign section one cannot be resolved.
- Decision needed: N

### D-023 · component-count · Minor · REQUIRED
- Location: manuscript.md 523–541 (Mega-bosses) vs 3018
- Evidence: The Big Game Hunting campaign lists 'The Last Giant (Mega Boss)' (3018); The Last Giant is absent from the mega-boss component list.
- Current text: (absent)
- Proposed fix: The Last Giant (The Last Giant)
- Rationale: A boss used by a listed campaign must appear in the component list.
- Gameplay impact: None.
- Decision needed: N

### F-052 · external-reference · Minor · OPTIONAL
- Location: L2352, L2402, L2454, L2502, L2548, L2594, L2662, L2718, L2764, L2810, L2882, L2946, L2992 §Campaigns headings
- Evidence: Campaign titles tag the video-game source: 'The First Journey - Dark Souls (Core)', 'The Coiled Sword - Dark Souls 3 (Core)', 'A Hollow Pursuit - Dark Souls 2 (Explorers)' …
- Current text: ### The Coiled Sword - Dark Souls 3 (Core)
- Proposed fix: Keep the component tag, drop the video-game title: 'The Coiled Sword (Core)'. If the setting is wanted, give it as an in-voice subtitle: 'The Coiled Sword — Lothric (Core)'.
- Rationale: The component tag identifies required components (legitimate); the game title is a real-world source reference.
- Gameplay impact: none
- Decision needed: N

### F-081 · prose-crossref · Minor · CLEAN-UP
- Location: L2456, L2504 §Campaigns
- Evidence: Prose cross-reference: 'just add the invaders below'
- Current text: just add the invaders below
- Proposed fix: Permitted ('listed below', same section). Fix typo 'Do no place' → 'Do not place'. — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: same section list. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### A-111 · undefined-state · Note · CLEAN-UP
- Location: CAMPAIGNS (manuscript.md lines 2350–3034) — named encounter verification
- Evidence: manuscript.md:2564, 2746, 2822, 2832, 2848, 2858, 2868, 2878, 2930, 2940, 2942, 2962; DS-Darkroot-Rules-web.txt p.11 (Hydra Lake); DS-Explorers-Rules-Web.txt p.15 (Gallery of the Hidden Warrior); DS-IronKeep-Rules-Web.txt p.7 (Smoking Gallery); DS-EC-Rules-Web.txt p.18–19 (Silent Pathway, Quiet Graveyard, Mausoleum Ruins, Misty Burial Site, Corrupted Crypt, Desolate Cemetery)
- Current text: Level 3 Encounter - Hydra Lake (and other named encounters)
- Proposed fix: No change for the verified names. Mark 'Outskirts of Blighttown', 'Darkened Chamber' and 'The Depths' (Gaping Dragon), the Vordt, Four Kings and Manus content and 'The Last Giant' as unverified pending the missing booklets.
- Rationale: Nine named encounters are confirmed in the supplied booklets; the Gaping Dragon, Vordt, Four Kings, Manus and Last Giant booklets were not supplied, so their names and section lists cannot be checked.
- Gameplay impact: None; verification record.
- Decision needed: N

### D-027 · component-count · Note · OPTIONAL
- Location: manuscript.md 557, 561, 569, 2492, 2528 (Phantoms)
- Evidence: PH p.5 spells the names 'Xanthous King Jeremiah', 'Armorer Dennis', 'Marvelous Chester'. The manuscript uses 'Jeramiah' (557) and 'Jeremiah' (2492, 2528), 'Armourer Dennis', 'Marvellous Chester'.
- Current text: Xanthous King Jeramiah / Armourer Dennis / Marvellous Chester
- Proposed fix: Xanthous King Jeremiah / Armorer Dennis / Marvelous Chester
- Rationale: Card names are proper nouns and should match the printed cards even in a British-English text; 'Jeramiah' is a misspelling in any case.
- Gameplay impact: None.
- Decision needed: Y

## Completion entries that apply (3) — approved at Gate 1

### [CMP-0008] Campaign Play › Setup and CAMPAIGNS list corrections — Proposed Completion
- Read `04_completion_backlog.md` lines 750–791 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0021] CAMPAIGNS › The First Journey — Section Four "Bathed in Flame" (Black Dragon Kalameet) — Proposed Completion
- Read `04_completion_backlog.md` lines 1156–1179 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0022] CAMPAIGNS › The Undead Colosseum — Campaign special rules — Proposed Completion
- Read `04_completion_backlog.md` lines 1180–1193 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

