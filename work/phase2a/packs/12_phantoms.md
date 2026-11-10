# Drafting pack — chapter 12 (phantoms) — manuscript chapter "SUMMONS"

Source text: `work/phase2a/source/12_phantoms.md` (manuscript.md lines 1967–2038).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 1967.
- **Phantoms** · present — truncated · line 1969. "reduced to or the encounter ends" (missing "zero"); stray "i" after "behaviour deck".
- **Invaders** · present — to audit · line 1995.
- **Invader Tokens** · present — to audit · line 1997.
- **Invader Encounter Setup** · present — defect · line 2013. "starting decks deck size"; "blocked by train" (terrain).
- **Invader Combat** · present — to audit · line 2023.

## Audit findings mapped to this chapter (33)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-016 · omission · Major · PROPOSED
- Location: SUMMONS › Phantoms (manuscript.md lines 1971–1993)
- Evidence: manuscript.md:1971–1993; DS-Phantoms-Rules-lores.txt p.6 (summons have taunt levels and block/resist/dodge values like characters), p.8–9 (weak-arc die, Distract icon, deck renewal)
- Current text: Phantoms take their turn after all character turns are resolved and before the first enemy turn begins.
- Proposed fix: A phantom is treated as a character for enemy targeting, range and node limits. A phantom never holds the aggro token unless a Distract icon on its behaviour card is resolved, in which case the phantom is treated as holding the aggro token until the end of the next boss turn. A phantom defends with the block, resist and dodge values on its data card, rolling dice as a character does. A phantom's health is not scaled. Phantoms gain the weak-arc black die. When a phantom's behaviour deck is empty, flip its discard pile face-down without shuffling.
- Rationale: The manuscript gives a summoning procedure but none of the rules the Phantoms booklet supplies for how a summon is targeted, defends, interacts with aggro or renews its deck. A phantom with a health dial (1993) must be attackable, so targeting must be defined.
- Gameplay impact: Boss behaviours cannot be resolved when a phantom is nearest or holds no defined aggro status.
- Decision needed: N

### A-020 · contradiction · Major · REQUIRED
- Location: SUMMONS › Phantoms step 6 (manuscript.md line 1987) vs BOSS TURNS › Boss Turn Overview (line 2157)
- Evidence: manuscript.md:1971, 1987, 2157; DS-Phantoms-Rules-lores.txt p.8 (summon activates after each character activation)
- Current text: Phantoms take their turn after all character turns are resolved and before the first enemy turn begins.
- Proposed fix: In a boss encounter the phantom takes its turn after each character turn and before the following boss turn.
- Rationale: Phantoms are only ever summoned into boss encounters (1971), where boss and character turns alternate one at a time; 'after all character turns' has no meaning in that structure. The official rule is one phantom turn per character turn. Alternative: one phantom turn per full round of character turns.
- Gameplay impact: Phantom activation frequency changes its value by a factor of up to four.
- Decision needed: Y

### A-028 · undefined-state · Major · REQUIRED
- Location: SUMMONS › Invader Encounter Setup step 3 (manuscript.md line 2019); CRYSTAL LIZARDS (line 2055); Enemy Scaling (line 1521)
- Evidence: manuscript.md:1521–1529, 2019, 2055, 2342; DS-Phantoms-Rules-lores.txt p.12; DS-IronKeep-Rules-Web.txt p.5
- Current text: Invaders do not multiply their health by the number of characters like other enemy models.
- Proposed fix: Invaders and crystal lizards are never modified by enemy scaling or by the bonfire ascetic.
- Rationale: Both exemptions cover health only; invaders are 'non-boss enemies' and would otherwise gain +1 attack and Repeat 2, and crystal lizards would gain movement 1→2, which defeats the chase. The bonfire ascetic (2342) already exempts invaders from +1 attack, which shows the intent. Alternative: invaders receive attack scaling but not health scaling.
- Gameplay impact: A Repeat-2 invader with +1 attack acting after every character turn is lethal at four players.
- Decision needed: Y

### A-045 · undefined-state · Major · REQUIRED
- Location: SUMMONS › Invaders › Invader Tokens step 1 (manuscript.md line 1999); Boss Death (line 2195)
- Evidence: manuscript.md:1999–2011, 1147, 2195; DS-Phantoms-Rules-lores.txt p.11 ('if there are no invader tokens already in play and there is at least one unexplored tile')
- Current text: Embered characters provoke an invader if no invasion has occurred yet.
- Proposed fix: An invasion is provoked the first time a character becomes embered while at least one face-down encounter card is on the tiles. If characters become embered when no face-down encounter card exists (for example when a boss is slain), the invasion is provoked when encounter cards are next dealt. At most one invasion occurs before the mini-boss and at most one after it.
- Rationale: Boss Death embers everyone at a moment when the old encounter cards have been cleared and the new ones not yet dealt, so the token-placing procedure (2007) has nothing to place on. 'If no invasion has occurred yet' also leaves it open whether the limit is one per game or one per leg. Alternative: one invasion per game.
- Gameplay impact: Determines whether advanced invaders ever appear in a standard game.
- Decision needed: Y

### C-033 · italics · Major · REQUIRED
- Location: L1399; L1890; L1906; L2235; L1397; L1277; L3056; L2175; L2017; L1985
- Evidence: Undefined keywords: '*lost*' used at 1890/1906/2235 ('lost to the hollow', 'revives lost characters who have been removed from play due to dying while hollow') but never defined and conflicts with L1223 (hollow death forces a rest, no removal) and L1195 (mega-boss death = permanent removal); 'mastering the encounter' (1397) undefined; '*first player* token' (1277) placed but never used and not a component; 'First turn token' (3056) different name for same thing; boss '*leaps*' (2175) icon undefined; 'Heat Up value' for invaders (2017) undefined on invader cards; 'entrance node' (1985)
- Current text: lost / mastering / first player token / leaps
- Proposed fix: Define *lost* once (proposed: 'A character who dies while *hollow* is *lost*: remove the model from play until the party next rests at the *bonfire*'), then make L1223, L1906 and L1195 agree; delete 'mastering'; either define the first player token's effect or delete L1277 and use 'first player' in PvP only; define *leap*; use 'entry node'.
- Rationale: A term used as a keyword must be defined once.
- Gameplay impact: Whether a hollow character's death removes it from play or ends the encounter
- Decision needed: Y

### C-064 · terminology · Major · REQUIRED
- Location: L543; L1967; L1969; L1971; L3052; L805; L1239
- Evidence: 'Phantoms' heading (543) covers Invaders and Summons; chapter 'SUMMONS' (1967) contains both 'Phantoms' (= summons only, 1969-1993) and 'Invaders' (1995); 'summon a random friendly phantom' (1971); 'Phantoms (Summons and Invaders)' (3052); 'enable the character to summon phantoms, but also attract malicious invaders' (805)
- Current text: Phantoms (two senses); chapter SUMMONS
- Proposed fix: *phantom* = umbrella (summons and invaders); *summon* = friendly phantom; *invader* = hostile phantom. Rename chapter 'PHANTOMS' with sections 'Summons' and 'Invaders'; L1969 heading -> 'Summons'.
- Rationale: The same word names the superset and one subset within two pages.
- Gameplay impact: Reader confusion over which rules apply to invaders
- Decision needed: N

### C-065 · terminology · Major · REQUIRED
- Location: L1991; L2031
- Evidence: 'After each icon on the encounter card is resolved in left to right order, the phantom's turn ends' (1991); same for the invader (2031) - the icons are on the behaviour card just drawn (1989, 2029)
- Current text: encounter card
- Proposed fix: behaviour card
- Rationale: Wrong card named; the encounter card has no behaviour icons.
- Gameplay impact: Procedural error in phantom and invader turns
- Decision needed: N

### D-002 · hybrid · Major · REQUIRED
- Location: manuscript.md 1987 (Summons step 6) vs 2158 (Boss Turn Overview)
- Evidence: PH p.8: 'there will be a summon activation after each character activation' (boss, character, summon, boss, character, summon). The manuscript's phantom acts 'after all character turns are resolved and before the first enemy turn begins', a phase that exists only in the manuscript's round-based standard encounters (1281–1295); boss encounters keep the 1E alternation (2158), where no such phase occurs.
- Current text: Phantoms take their turn after all character turns are resolved and before the first enemy turn begins.
- Proposed fix: The phantom takes a turn immediately after each character's turn, before the boss's next turn. The phantom does not take a turn after the boss's turn.
- Rationale: The summon cadence was written for the manuscript's round structure, but summons appear only in boss encounters, which use 1E alternation. The official cadence (PH p.8) fits boss alternation without further change.
- Gameplay impact: As written the phantom never has a defined moment to act in a boss fight.
- Decision needed: Y

### D-010 · dropped-rule · Major · REQUIRED
- Location: manuscript.md 1971–1993 (Phantoms)
- Evidence: PH p.6: summons have a taunt level, block/resist/dodge values and a special ability; p.9: the Distract icon makes the summon count as holding the aggro token for the next boss activation; summon death does not force a rest. None of these appear in the manuscript, which also calls the behaviour card an 'encounter card' (1991).
- Current text: Draw a random phantom card of appropriate level … After each icon on the encounter card is resolved in left to right order, the phantom's turn ends.
- Proposed fix: A phantom defends with its own block, resist and dodge values and is targeted by enemies using its threat level as if it were a character. When a behaviour shows the distract icon, the phantom is treated as holding the aggro token during the boss's next turn; the token itself is not moved. The phantom's special ability applies as printed on its data card. A phantom's death has no effect on the characters.
- Rationale: The manuscript adopts the Phantoms expansion components but omits the rules that make the summon data card usable.
- Gameplay impact: Boss targeting with a summon present is undefined.
- Decision needed: N

### A-015 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Encounters › Encounter Turn Order step 3 (manuscript.md line 1291)
- Evidence: manuscript.md:1291–1293, 2019, 2035
- Current text: ...the character who placed the most damage tokens on enemy models.
- Proposed fix: After all characters have taken their turns, place the aggro token on the character who inflicted the most damage on enemy models during that round, counting damage recorded on an invader's or boss's health dial as well as damage tokens.
- Rationale: Invaders track damage on a dial, not with tokens; the literal measure excludes damage to invaders. The phrase 'that round' is also needed so that cumulative damage is not counted.
- Gameplay impact: Prevents the aggro token ignoring the character fighting the invader.
- Decision needed: N

### A-021 · inherits-official-silently · Minor · OPTIONAL
- Location: SUMMONS › Invaders › Invader Tokens (manuscript.md lines 2007–2011)
- Evidence: manuscript.md:2007–2011, 2025; DS-Phantoms-Rules-lores.txt p.11, p.14
- Current text: Place an invader token face-down on each face-down encounter card.
- Proposed fix: Invaders never appear in boss encounters or mimic encounters.
- Rationale: Boss tiles carry no encounter card, so the exclusion follows from the placement rule but is never stated; the invader-after-each-character turn rule (2025) would otherwise be read against the boss alternation.
- Gameplay impact: Removes a question every group asks when the invader token is still unrevealed at the fog gate.
- Decision needed: N

### A-029 · terminology · Minor · CLEAN-UP
- Location: SUMMONS › Invader Encounter Setup step 3 (manuscript.md line 2019)
- Evidence: manuscript.md:1523, 2019
- Current text: Invaders do not multiply their health by the number of characters like other enemy models.
- Proposed fix: Invaders do not increase their health for the number of characters.
- Rationale: Enemy scaling adds, it does not multiply.
- Gameplay impact: Cosmetic; avoids a reader inferring a multiplicative rule.
- Decision needed: N

### A-044 · omission · Minor · OPTIONAL
- Location: MIMICS (manuscript.md line 2047); SUMMONS › Invaders (line 2017)
- Evidence: manuscript.md:2017, 2047, 2127–2151; DS-Explorers-Rules-Web.txt p.11; DS-Phantoms-Rules-lores.txt p.13 (no arc markings)
- Current text: Refer to 'Boss Encounter' rules for more details on how to manage the mimic's behaviour cards.
- Proposed fix: Mimics, invaders and phantoms have no arcs. The boss arc movement rules and the weak-arc black die do not apply to them.
- Rationale: The mimic chapter defers to boss rules wholesale; their models have no arc bases.
- Gameplay impact: Avoids players inventing arcs for the mimic.
- Decision needed: N

### A-098 · terminology · Minor · CLEAN-UP
- Location: SUMMONS › Invader Encounter Setup steps 2 and 4 (manuscript.md lines 2017, 2021)
- Evidence: manuscript.md:2017, 2021
- Current text: deal a number equal to their starting decks deck size ... If the central node is blocked by train
- Proposed fix: deal a number equal to the behaviour deck size on the invader's data card ... If the central node contains terrain
- Rationale: Typographical defects in a procedure.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-099 · terminology · Minor · CLEAN-UP
- Location: SUMMONS › Phantoms steps 7–8 (manuscript.md lines 1989–1993); Invader Combat step 4 (line 2031)
- Evidence: manuscript.md:1989–1993, 2031
- Current text: After each icon on the encounter card is resolved in left to right order, the phantom's turn ends. / Phantoms are removed from play if their health dial is reduced to or the encounter ends.
- Proposed fix: After each icon on the behaviour card is resolved from left to right, the phantom's turn ends. Phantoms are removed from play when their health dial is reduced to zero or when the encounter ends.
- Rationale: 'Encounter card' is the wrong card (twice) and the word 'zero' is missing.
- Gameplay impact: Cosmetic but a literal reading resolves the wrong card.
- Decision needed: N

### A-100 · contradiction · Minor · REQUIRED
- Location: SUMMONS › Phantoms steps 1–3 (manuscript.md lines 1973–1981); The Bonfire (line 1890)
- Evidence: manuscript.md:1890, 1973–1981
- Current text: Characters cannot spend their hard-earned souls without resting at the bonfire. / Embered characters may elect to pay two souls to draw a phantom card.
- Proposed fix: Souls are spent only while resting at the bonfire, except that an embered character may spend two souls at the fog gate to draw one phantom data card. The players choose one drawn phantom to summon and return the others to the supply; souls paid are not refunded.
- Rationale: The general restriction contradicts the summoning cost, and the outcome of several embered characters each drawing is unstated.
- Gameplay impact: Small; affects phantom summoning only.
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

### C-037 · terminology · Minor · REQUIRED
- Location: L2019; L2099
- Evidence: 'Set the invader heal dial' (2019); 'health tracker dial' (2099) vs 'health dial' (1105, 1993, 2035, 2195)
- Current text: heal dial / health tracker dial
- Proposed fix: health dial
- Rationale: One component, one name (official: 'health dial').
- Gameplay impact: None
- Decision needed: N

### C-057 · terminology · Minor · CLEAN-UP
- Location: L1193; L2047; L2085; L2101; L2117; L2017; L2123; L2125; L943
- Evidence: 'heat-up' (1193, 2047, 2085, 2101, 2117); 'Heat Up' x11 (2017, 2123, 2125); 'heats-up' (2047); 'Heat-up' (2085, 2117); also 'Behaviour Deck' capitalised (943)
- Current text: Heat Up / heats-up / Heat-up / Behaviour Deck
- Proposed fix: 'heat-up' as noun/adjective ('heat-up point', 'heat-up card'); verb 'heats up'; 'behaviour deck' lower-case
- Rationale: Common nouns are lower-case; one hyphenation.
- Gameplay impact: None
- Decision needed: N

### C-062 · terminology · Minor · CLEAN-UP
- Location: L1985; L2065; L1179; L903; L1265
- Evidence: 'the boss tile's entrance node' (1985); 'the boss-tile entryway' (2065); 'placed at the entrance' (1179) vs 'entry node' (903, 1265)
- Current text: entrance node / entryway / entrance
- Proposed fix: entry node
- Rationale: Defined term at L903.
- Gameplay impact: None
- Decision needed: N

### C-077 · table-text · Minor · CLEAN-UP
- Location: L679-723; L1277; L2205; L2055; L1997; L1137; L1975; L1315
- Evidence: Items used in rules but absent from Tokens & Terrain Elements: first player token (1277), pillar tokens (2205), Titanite Scale cards (2055), invader tokens and blank invader tokens (1997-2007), ambush cards (1137), phantom cards (1975), hollow cubes (781). L1315 'Mark the encounter card *cleared* with a black cube' uses a stamina cube as a marker.
- Current text: (absent)
- Proposed fix: Decide the scope of the component list (core only vs all supported content) and either add the expansion components under their expansion name or state that expansion components are listed in their own booklets; state that the cleared marker is a black stamina cube.
- Rationale: Component list is the reader's inventory check.
- Gameplay impact: None
- Decision needed: Y

### C-097 · example · Minor · CLEAN-UP
- Location: L2017; L2047; L2125
- Evidence: Heat-up mechanic worded three ways: invader 'add an unused invader behaviour card to the behaviour deck and shuffle' (2017); mimic 'just shuffles in one unused normal behaviour card when it heats-up' (2047); boss 'take a random Heat Up behaviour card and shuffle it into the boss behaviour deck' (2125)
- Current text: (three wordings)
- Proposed fix: State the boss rule once in §Boss Behaviour Cards; invader and mimic sections: 'When the invader/mimic heats up, shuffle one unused normal behaviour card into its behaviour deck (it has no heat-up cards).'
- Rationale: Parallel mechanics should use parallel wording.
- Gameplay impact: None
- Decision needed: N

### C-103 · heading · Minor · CLEAN-UP
- Location: L1916/L2299; L1951/L2326; L2063/L2227; L1245/L2231; L633/L1119; L543/L1969; L385/L725; L985/L2219
- Evidence: Identical heading titles in different chapters: 'Stat Tier Costs' x2, 'Shop Price Table' x2, 'The Fog Gate' x2, 'Sparks' x2, 'Encounter cards' x2, 'Phantoms' x2, 'Characters' x2, 'Setup' x2
- Current text: Stat Tier Costs (x2)
- Proposed fix: Qualify the campaign versions: 'Stat Tier Costs (Campaign)', 'Shop Price Table (Campaign)', 'The Fog Gate in Campaigns', 'Sparks in Campaigns'; rename L633 'Encounter and Event Cards', L1969 'Summons', L385 'Character Classes'
- Rationale: Duplicate titles defeat '(see §Heading)' cross-references and index entries.
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

### C-107 · punctuation · Minor · REQUIRED
- Location: L1412; L1989
- Evidence: Stray 'i': 'per characteri' (1412, Soul Reward Table header); 'phantom behaviour deck.i' (1989)
- Current text: characteri / deck.i
- Proposed fix: character / deck.
- Rationale: Conversion or typing artefact.
- Gameplay impact: None
- Decision needed: N

### C-111 · punctuation · Minor · CLEAN-UP
- Location: L375; L529; L805; L835; L853; L1025; L1529; L1726; L1826; L1904; L1929; L1985; L2310; L2312; L2314; L837; L839; L2047
- Evidence: Mixed quotation marks: curly apostrophe ’ x146 in the body vs straight ' in ~20 lines (e.g. L529 'Executioner's Chariot (Executioner’s Chariot)' has both forms in one line); curly double quotes “ ” at 837, 839, 2047
- Current text: ' / ’ mixed
- Proposed fix: Policy: straight quotes in the Markdown source; the typesetter converts to curly. Until then, make every line consistent (curly).
- Rationale: Mixed glyphs show in print.
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

### D-036 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 2020 (Invader Encounter Setup)
- Evidence: Enemy scaling is additive (+1 health per extra character, 1523); the invader rule says invaders 'do not multiply their health by the number of characters'.
- Current text: Invaders do not multiply their health by the number of characters like other enemy models.
- Proposed fix: Invaders do not receive enemy scaling.
- Rationale: Aligns wording with the scaling rule.
- Gameplay impact: None.
- Decision needed: N

### F-022 · tone · Minor · CLEAN-UP
- Location: L2027 §Summons › Invader Combat step 2
- Evidence: Explanatory aside: 'Thus, the invader will take many more turns than any other model in the encounter.'
- Current text: The invader takes a turn each time a character completes their turn, not in threat order with the other enemies. Thus, the invader will take many more turns than any other model in the encounter.
- Proposed fix: CUT second sentence.
- Rationale: Consequence commentary; the rule is complete without it.
- Gameplay impact: none
- Decision needed: N

### F-091 · tone · Minor · OPTIONAL
- Location: L1487, L1596, L2027, L2143, L2191
- Evidence: Logical connectives in rules prose: 'Therefore' (L1487, L1596, L2191), 'Thus' (L2027, L2143), 'In other words' (L1594).
- Current text: Therefore, targets who successfully *dodge* an attack are not considered hit and therefore are not pushed or afflicted with conditions…
- Proposed fix: Delete the connective and state the consequence as its own rule: 'A model that dodges an attack is not hit: it is not pushed and receives no condition.'
- Rationale: Lawbook sentences do not argue; each states one outcome.
- Gameplay impact: none
- Decision needed: N

### A-124 · inherits-official-silently · Note · CLEAN-UP
- Location: ENEMY TURN › Overview (manuscript.md line 1664); Encounter Turn Order (lines 1281–1295) — turn structure
- Evidence: manuscript.md:1281–1295, 1664, 2025–2027; DS-Core-Rules-lores.txt p.19; Hollowed_Edition_v1.3.txt p.7 ('Enemies always activate first')
- Current text: Each encounter begins with each enemy model taking their turn before proceeding to the character's turns.
- Proposed fix: No change.
- Rationale: The manuscript's round structure (all enemies, then every character in threat order, then aggro reassignment) is complete and internally consistent and differs from both official editions by design. Recorded for the preserve list together with the invader-after-each-character rule.
- Gameplay impact: None.
- Decision needed: N

### C-115 · punctuation · Note · CLEAN-UP
- Location: Whole body
- Evidence: Serial (Oxford) comma: 20 three-item lists with, 0 without (the one regex hit at L1989 'draw and resolve' is not a list)
- Current text: (consistent)
- Proposed fix: Policy: always use the serial comma.
- Rationale: Already consistent; record in style sheet.
- Gameplay impact: None
- Decision needed: N

## Completion entries that apply (2) — approved at Gate 1

### [CMP-0007] Truncated and defective sentences (several chapters) — Proposed Completion
- Read `04_completion_backlog.md` lines 711–749 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0018] SUMMONS › Phantoms — Summoning procedure and summon icons — Proposed Completion
- Read `04_completion_backlog.md` lines 1104–1127 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

