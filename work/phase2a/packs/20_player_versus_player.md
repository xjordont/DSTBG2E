# Drafting pack — chapter 20 (player_versus_player) — manuscript chapter "PLAYER VS PLAYER"

Source text: `work/phase2a/source/20_player_versus_player.md` (manuscript.md lines 3038–3097).

## Tracker rows (section · status · notes)

- **(chapter)** · present — defect · line 3038. "intimate victor" (ultimate); dodge-difficulty table formatting; rules sparse.
- **(empty heading)** · ORPHAN — delete · line 3096: empty H1 used as page break

## Audit findings mapped to this chapter (29)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-032 · undefined-state · Blocker · REQUIRED
- Location: PLAYER VS PLAYER (manuscript.md lines 3040–3094)
- Evidence: manuscript.md:1485, 1708–1797, 1846–1872, 3060, 3082–3094
- Current text: Character turn structure is unchanged from basic rules. ... Dodge difficulty is based on an the attacker attack option's stamina cost
- Proposed fix: When a character attacks another character, the attacker resolves the attack option as if against an enemy and determines the final attack value. The defender then chooses to block, resist, dodge or parry exactly as against an enemy attack whose attack value equals that final attack value and whose dodge difficulty is given by the stamina-cost table. Damage suffered equals the attack value minus the defence total. Push, condition, shift and area-of-effect icons apply to characters as they apply to enemies; an area-of-effect attack targets every other character on the target node. A parry requires the attacker to share the defender's node; a successful parry staggers the attacker and permits a riposte. Block and resist values of defenders are never subtracted from the attack value; defence is always rolled.
- Rationale: The PvP chapter supplies turn order, traps and a dodge table but never says how a character-versus-character attack is resolved: the enemy-attack procedure assumes a fixed attack value, the character-attack procedure assumes a fixed block value, and neither covers push, AoE, conditions or parry against a character.
- Gameplay impact: PvP cannot be played from the text.
- Decision needed: N

### A-031 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Objective & Loss Conditions (manuscript.md line 1201) vs PLAYER VS PLAYER (line 3042)
- Evidence: manuscript.md:1201, 3042, 3078–3080
- Current text: Players may also choose to add a player versus player (PvP) encounter after the final boss is defeated ... / After each boss (mini, main, and mega) a PvP encounter will occur.
- Proposed fix: If the players chose PvP during setup, a PvP encounter is played after each boss encounter (mini, main and mega) is cleared and before the characters rest at the bonfire.
- Rationale: The objective text says PvP happens once, after the final boss; the PvP chapter says after every boss and its '+1 attack damage in future PvP' rule only makes sense with several PvP rounds. Alternative: a single PvP encounter after the final boss and deletion of the +1 rule.
- Gameplay impact: Decides how many PvP rounds a game contains.
- Decision needed: Y

### A-033 · undefined-state · Major · REQUIRED
- Location: PLAYER VS PLAYER (manuscript.md lines 3062–3066)
- Evidence: manuscript.md:713, 967–981, 3062–3066; DS-Core-Rules-lores.txt p.18 (trap tokens show a dodge value and damage, or are blank)
- Current text: Players place a trap token on an outermost available node after each turn. Characters that move onto a trap token may attempt to dodge. Characters that fail to dodge a trap immediately die.
- Proposed fix: After each character turn, the player who took that turn draws a random trap token from the supply and places it face-up on an unoccupied outermost node (a node touching the tile edge) that holds no terrain or trap token; if no such node exists, the token is placed on any unoccupied node. A character who moves onto or is pushed onto a trap token rolls dodge dice against the trap's dodge difficulty; a blank token has no effect and is removed. On a failed dodge the character dies.
- Rationale: Which player places the token, which token, whether it is face-up, what 'available' and 'outermost' mean, and how a trap's dodge difficulty is read are all unstated. The arena-shrinking effect is the only mechanism that ends a ranged stalemate, so it must work.
- Gameplay impact: Without this the PvP end condition can never be reached between two cautious players.
- Decision needed: N

### A-083 · omission · Major · REQUIRED
- Location: TILES & NODES › Terrain › Traps (manuscript.md lines 967–981)
- Evidence: manuscript.md:713, 967–981, 3064; DS-Core-Rules-lores.txt p.18 (trap tokens: blank or damage; dodge or suffer; cannot be blocked; no effect on enemies)
- Current text: When a character is pushed onto or moves into a node containing a face-down trap token, flip the token face-up and resolve its effect on all models on that node.
- Proposed fix: A trap token shows either nothing (blank) or a dodge difficulty and a damage value. When a trap token is revealed, each character on that node must either suffer the damage or attempt to dodge it as an attack with that dodge difficulty; trap damage is not reduced by block or resist. A blank token has no effect. Enemy models on the node suffer the trap's damage without rolling. A revealed trap does not trigger again until the encounter is reset.
- Rationale: What a trap token shows and how it is resolved is never described; 'resolve its effect on all models' extends traps to enemies, which the official rule forbids, so the intent must be stated. Alternative: traps have no effect on enemies.
- Gameplay impact: Traps appear on roughly a third of encounter cards.
- Decision needed: Y

### B-024 · balance · Major · PROPOSED
- Location: L3082-3094 (Player vs Player, dodge difficulty table)
- Evidence: Table [0]->4, [1]->3, [2]->2, [3]->1, [4]->1, [5+]->0. With green dice at p = 0.5, difficulty 4 is impossible with fewer than four dice (P = 0.062 with four); difficulty 3 is impossible with two dice. Free and 1-stamina options (the weakest attacks on most cards, e.g. Shortsword [0] 2 black, Core p.22) become the hardest to avoid, while [5+] attacks are dodged automatically. [3] and [4] share the same value.
- Current text: - [0] -> 4
- [1] -> 3
- [2] -> 2
- [3] -> 1
- [4] -> 1
- [5+] -> 0
- Proposed fix: - [0] -> 3
- [1] -> 2
- [2] -> 2
- [3] -> 1
- [4] -> 1
- [5+] -> 1
- Rationale: Keeps the intended inversion (cheap attacks harder to dodge) within the range the dice can produce and removes automatic outcomes in either direction.
- Gameplay impact: A two-dice defender dodges a free attack 25% of the time instead of 0%; a 5-stamina attack is dodged 50-94% instead of always.
- Decision needed: Y

### C-033 · italics · Major · REQUIRED
- Location: L1399; L1890; L1906; L2235; L1397; L1277; L3056; L2175; L2017; L1985
- Evidence: Undefined keywords: '*lost*' used at 1890/1906/2235 ('lost to the hollow', 'revives lost characters who have been removed from play due to dying while hollow') but never defined and conflicts with L1223 (hollow death forces a rest, no removal) and L1195 (mega-boss death = permanent removal); 'mastering the encounter' (1397) undefined; '*first player* token' (1277) placed but never used and not a component; 'First turn token' (3056) different name for same thing; boss '*leaps*' (2175) icon undefined; 'Heat Up value' for invaders (2017) undefined on invader cards; 'entrance node' (1985)
- Current text: lost / mastering / first player token / leaps
- Proposed fix: Define *lost* once (proposed: 'A character who dies while *hollow* is *lost*: remove the model from play until the party next rests at the *bonfire*'), then make L1223, L1906 and L1195 agree; delete 'mastering'; either define the first player token's effect or delete L1277 and use 'first player' in PvP only; define *leap*; use 'entry node'.
- Rationale: A term used as a keyword must be defined once.
- Gameplay impact: Whether a hollow character's death removes it from play or ends the encounter
- Decision needed: Y

### C-050 · terminology · Major · REQUIRED
- Location: L781; L805; L1215; L1231; L1367; L1379; L1898; L3074; L771; L993; L1914; L689
- Evidence: 'block off the two furthest right spaces... with a marker such as white cubes. The effect of these *hollow* markers' (781); 'discard any *hollow* tokens' (805, 1379); 'Place two white cubes' (1215, 1367); 'Remove all *hollow* cubes' (1231, 1898, 3074). 'White cubes' are also the stat cubes (771, 993, 1914) and the component list has exactly 16 stat tier cubes (689) = 4 characters x 4 stats, none spare.
- Current text: hollow markers / hollow tokens / hollow cubes / white cubes
- Proposed fix: 'hollow cube' throughout; add a component line '8x Hollow cubes (white)' or specify the colour and source of the marker once in §Death & Hollowing
- Rationale: One component, four names; and the marker is not in the component list.
- Gameplay impact: Players may be short of markers; 'white cube' is ambiguous with stat cubes
- Decision needed: Y

### C-064 · terminology · Major · REQUIRED
- Location: L543; L1967; L1969; L1971; L3052; L805; L1239
- Evidence: 'Phantoms' heading (543) covers Invaders and Summons; chapter 'SUMMONS' (1967) contains both 'Phantoms' (= summons only, 1969-1993) and 'Invaders' (1995); 'summon a random friendly phantom' (1971); 'Phantoms (Summons and Invaders)' (3052); 'enable the character to summon phantoms, but also attract malicious invaders' (805)
- Current text: Phantoms (two senses); chapter SUMMONS
- Proposed fix: *phantom* = umbrella (summons and invaders); *summon* = friendly phantom; *invader* = hostile phantom. Rename chapter 'PHANTOMS' with sections 'Summons' and 'Invaders'; L1969 heading -> 'Summons'.
- Rationale: The same word names the superset and one subset within two pages.
- Gameplay impact: Reader confusion over which rules apply to invaders
- Decision needed: N

### C-119 · voice · Major · REQUIRED
- Location: L1205-1253; L1299-1399; L1445-1479; L1935-1949; L859-887; L931-981; L1604-1658; L2243-2293; L2314-2322; L3040-3094
- Evidence: Rules stated as bullet fragments: Death & Hollowing, Embering, Sparks (1205-1253); Encounter Resolution/Recovery, Souls (1299-1399); Treasure Rewards (1445-1479); Shop Rules (1935-1949); Spells (859-887); Terrain (931-981); Conditions (1604-1658); campaign Soul/Treasure Rewards and Shop (2243-2322); the whole PLAYER VS PLAYER chapter (3040-3094) is 27 bullets with no sentence structure
- Current text: - Encounters are *failed* if either all characters die.
- Proposed fix: Policy: PROCEDURES (setup, turn sequence, defence rolls, encounter start, resting, transposition) = numbered steps; DEFINITIONS and component anatomies (dashboard parts, data-card fields, condition effects, terrain) = bulleted lists of complete sentences; RULES (everything else) = short declarative paragraphs in 'When [trigger], [subject] must/may [action].' form. Rewrite PvP as prose plus a dodge table.
- Rationale: Fragments omit the trigger and subject that lawbook syntax requires ('Encounters are failed if either all characters die' has a dangling 'either').
- Gameplay impact: None
- Decision needed: Y

### A-005 · contradiction · Minor · REQUIRED
- Location: GAMEPLAY › Death & Hollowing (manuscript.md line 1221) vs Resting at The Bonfire (line 1898), Boss Death (line 2195), PvP (line 3046)
- Evidence: manuscript.md:1221, 1898, 1908, 2195, 3046
- Current text: Hollow status is only removed by using a spark or an ember token.
- Proposed fix: Hollow status is removed only by resting at the bonfire or by becoming embered.
- Rationale: Resting after a boss (2195) and before PvP (3046) costs no spark yet removes hollow cubes (1898). The restriction must name the rest, not the spark.
- Gameplay impact: Literal reading leaves characters hollow after the free post-boss rest.
- Decision needed: N

### A-014 · undefined-state · Minor · OPTIONAL
- Location: SETUP › Character Setup step 7 (manuscript.md line 1001); Encounter Start step 8 (line 1275); Encounter Turn Order step 2 (line 1289)
- Evidence: manuscript.md:1001, 1275, 1289, 3056–3058
- Current text: Each character takes their turn one-by-one in descending threat value.
- Proposed fix: If two or more characters share a threat value, the players choose which of them receives the aggro token and the order in which the tied characters take their turns.
- Rationale: Several character dashboards share threat values; no tie-break is given for either the aggro assignment or the turn order.
- Gameplay impact: Common with two characters of the same class family; cheap to fix.
- Decision needed: N

### A-017 · omission · Minor · REQUIRED
- Location: GAMEPLAY › Encounters › Encounter Start step 9 (manuscript.md line 1277); PLAYER VS PLAYER (line 3056)
- Evidence: manuscript.md:679–723 (no such component), 1277, 1289, 3056; DS-Core-Rules-lores.txt p.7 (1x First Activation Token exists officially)
- Current text: Place the first player token on the character with the highest threat value.
- Proposed fix: Delete Encounter Start step 9. In PLAYER VS PLAYER replace the first turn token bullet with: Characters take their turns in descending threat order; ties are broken by the players' choice.
- Rationale: The first player token is not in the component list and is never used: character order is fixed by threat value (1289), so the token has no function. PvP calls the same object a 'First turn token'.
- Gameplay impact: Removes a phantom component and a contradiction between two names.
- Decision needed: N

### A-034 · undefined-state · Minor · OPTIONAL
- Location: PLAYER VS PLAYER (manuscript.md lines 3050, 3076–3078)
- Evidence: manuscript.md:1213, 1357, 3046, 3050, 3076–3078
- Current text: Dead characters are excluded from PvP. ... Victory on non-final bosses provides +1 attack damage in future PvP only.
- Proposed fix: The PvP encounter is played after dead characters have been revived and every character has been restored as if rested. A PvP encounter with fewer than two living characters is not played. Record a PvP victory by placing a 1-soul token from the supply on the champion's dashboard; in later PvP encounters the champion adds one to the attack value of every attack against a character.
- Rationale: Clearing a boss revives the dead as hollow (1213) and PvP restores everyone (3046), so 'dead characters are excluded' is unreachable; and no marker is defined for the +1 bonus.
- Gameplay impact: Removes an unreachable rule and gives the bonus a physical tracker.
- Decision needed: N

### A-035 · loop/exploit · Minor · OPTIONAL
- Location: PLAYER VS PLAYER (manuscript.md line 3076)
- Evidence: manuscript.md:3062–3076
- Current text: The last character alive is awarded victory.
- Proposed fix: If three consecutive rounds pass in which no character suffers damage, every character suffers one damage at the end of each further round until the encounter ends.
- Rationale: Two ranged characters can retreat indefinitely; traps shrink the arena only slowly and a player may choose placements that never threaten themself. Alternative: rely on trap placement alone.
- Gameplay impact: Guarantees termination of the optional mode.
- Decision needed: Y

### B-030 · table-text-mismatch · Minor · REQUIRED
- Location: L1277 (Encounter Start step 9) and L3058 (PvP 'First turn token') vs component list L681-716
- Evidence: A 'first player' token (and in PvP a 'First turn token') is used but not listed among components. Core p.7 lists '1x First Activation Token'.
- Current text: 9.  Place the *first player* token on the character with the highest threat value.
- Proposed fix: Add "1x First player token" to Tokens & Terrain Elements; use the term "first player token" in both the Encounter Start and Player vs Player sections.
- Rationale: Component used in play must be listed; one term throughout.
- Gameplay impact: None.
- Decision needed: N

### C-015 · spelling · Minor · REQUIRED
- Location: L793; L849; L887; L979; L1517; L1664; L1880; L2017; L2021; L2043; L2045; L2053; L2456; L2504; L3082; L377
- Evidence: Typos: L793 'a read and a used side'; L849 'play mail', 'used up grade armour'; L887 'a characters' catalyst'; L979 'the tiles entry'; L1517 'the enemies block'; L1664 'wound token's'; L1880 'who's stats', 'its' attack options'; L2017 'starting decks deck size'; L2021 'blocked by train'; L2043 'The then are faced'; L2045 'reveal one an ambush card', 'min-boss'; L2053 'offer character's powerful rewards'; L2456/L2504 'Do no place'; L3082 'based on an the attacker attack option's'; L377 'desist in google docs'
- Current text: (see Evidence)
- Proposed fix: ready side; plate mail; used to upgrade armour; a character's catalyst; the tile's entry nodes; the enemy's block; wound tokens; whose stats; its attack options; starting deck size; blocked by terrain; They then are faced; reveal the ambush card; mini-boss; offer characters powerful rewards; Do not place; based on the attacker's attack option's; reside in Google Docs
- Rationale: Plain typographical errors; 'Do no place' and 'blocked by train' change sense.
- Gameplay impact: L2456/L2504 'Do no place' reads as a permission, not a prohibition
- Decision needed: N

### C-028 · italics · Minor · REQUIRED
- Location: L787; L1341; L1794; L1880; L2145; L3082
- Evidence: Split or partial italics: 'stagger*ed*' x2 (787); '*C*haracters' (1341); 'block*/*resist' (1794); 'attack option*s*' (1880); 'dodge*s*' (2145); 'attack option*'s*' (3082)
- Current text: stagger*ed*
- Proposed fix: *staggered*; Characters; *block*/*resist*; *attack options*; *dodges*; *attack option*'s
- Rationale: Italicise the whole inflected word or none.
- Gameplay impact: None
- Decision needed: N

### C-029 · italics · Minor · REQUIRED
- Location: L705; L1529; L1890; L1345; L3056; L1640; L1650; L1808-L1832
- Evidence: Italicised fragments/non-terms: '*4x Corrosion*' (705, repeats quantity); '*repeat to*' (1529); '*spark to*' (1890); '*clear an*' (1345); '*First* *turn*' (3056); headings '*Calamity (*Kalameet Expansion*)*' and '*Corrosion (*Gaping Dragon Expansion*)*' (1640, 1650); bold **AND**/**OR** connectors (1808-1832)
- Current text: *4x Corrosion*
- Proposed fix: '4x each of *calamity* and *corrosion* tokens'; '*repeat* to'; '*spark* to'; '*clear* an'; '*first player* token'; '*Calamity* (Kalameet expansion)'; replace AND/OR connectors with a numbered procedure
- Rationale: Italics mark glossary keywords only.
- Gameplay impact: None
- Decision needed: N

### C-030 · italics · Minor · REQUIRED
- Location: Whole body
- Evidence: Inconsistent keyword italicisation (italic/plain in rules text L361-3100): bonfire 39/79; soul 35/33; dodge 27/17; cleared 27/5; spark 25/16; ember 23/10; hollow 19/8; block 17/8; resist 15/6; aggro 14/10; luck 12/4; heroic action 11/5; attack option 10/5; threat 10/14; stamina 8/34; run 12/1; walk 8/0; shift 8/1; parry 7/0; push 2/49; heat-up 2/15; endurance bar 1/16
- Current text: *bonfire* ... the bonfire
- Proposed fix: Adopt one policy (recommended: italicise a glossary keyword at its first use in each H2 section and in headings/tables; plain thereafter) and apply it mechanically from the glossary headword list.
- Rationale: Readers cannot tell which words are defined terms; the Introduction (L381) promises every italicised term is in the glossary.
- Gameplay impact: None
- Decision needed: Y

### C-047 · terminology · Minor · CLEAN-UP
- Location: L2115; L3082; L831; L1501; L1734
- Evidence: 'Dodge difficulty' plain capital (2115, 3082); '*Dodge*' italic capital in lists/headings (831, 1501, 1734); '*dodge*' x22 and plain 'dodge' x16 elsewhere
- Current text: Dodge
- Proposed fix: *dodge* (lower-case keyword; capital only at sentence start or in a heading)
- Rationale: Keyword case must be uniform.
- Gameplay impact: None
- Decision needed: N

### C-079 · table-text · Minor · REQUIRED
- Location: L3082-3094
- Evidence: PvP dodge difficulty given as an escaped list: '\[0\] -\> 4', '\[1\] -\> 3' ... '\[5+\] -\> 0'
- Current text: \[0\] -\> 4
- Proposed fix: Two-column table: 'Attack option stamina cost | Dodge difficulty' with rows 0/4, 1/3, 2/2, 3/1, 4/1, 5+/0
- Rationale: Escaped brackets and ASCII arrows are conversion artefacts; a table is the correct form.
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

### C-104 · heading · Minor · CLEAN-UP
- Location: L2350; L1662; L679-2237 (9 headings); L3038; L3098; L1967
- Evidence: '# CAMPAIGNS' (2350) jumps to H3 with no H2; '## Overview' (1662) is generic; '&' in nine headings (679, 895, 1199, 1203, 1710, 1766, 2161, 2201, 2237); '# PLAYER VS PLAYER' (3038) vs 'Target versus Hit' (1483); '# F.A.Q.' (3098); '# SUMMONS' (1967) contains Invaders
- Current text: CAMPAIGNS > ### ; Overview; Tokens & Terrain Elements; PLAYER VS PLAYER; F.A.Q.; SUMMONS
- Proposed fix: Promote campaign headings to H2; 'Enemy Turn Overview'; 'and' for '&' in headings; 'PLAYER VERSUS PLAYER (PvP)'; 'FAQ'; 'PHANTOMS'
- Rationale: Consistent hierarchy and wording.
- Gameplay impact: None
- Decision needed: N

### C-109 · punctuation · Minor · REQUIRED
- Location: L1033; L1035; L1043; L1045; L1563-1577; L3084-3094; L3182; L3184; L925
- Evidence: '=\>' used for 'greater than or equal to' (1033-1045: 'without a required statistic =\> 25'); '1 -&gt; 2' in the scaling table (1563-1577); '-\>' in the PvP list; escaped '\[25/25/0/0 Common\]' (3182, 3184); 'Range ∞ (inﬁnity)' (925)
- Current text: =\> 25; 1 -&gt; 2; -\>
- Proposed fix: '25 or more' in prose (or '≥ 25' in tables only); '1 → 2' or 'becomes 2'; tables for the PvP list; '[25/25/0/0, common]'; 'Range ∞ (infinity)' with the ligature removed
- Rationale: '=>' is not the symbol for 'greater than or equal'; ASCII arrows and escaped brackets are pandoc artefacts.
- Gameplay impact: L1033-1045 as written literally means 'equals-implies 25'
- Decision needed: N

### C-124 · voice · Minor · REQUIRED
- Location: L1107; L1109; L1137; L1141; L2041; L2053; L1201; L3040
- Evidence: Optional rules are introduced inconsistently: 'if they wish... if they like' (1107); 'For added challenge the players may forgo choice' (1109); 'If playing with optional mimics for increased challenge' (1137); 'if they prefer more variety' (1141); 'may choose whether they wish to include mimics' (2041); 'as an optional game component' (2053); 'Players should agree on whether they will include a mega-boss and/or PvP' (1201); 'Decide during setup if PvP rules will be used' (3040)
- Current text: (eight phrasings)
- Proposed fix: One pattern: a boxed 'Optional rule: <name>' heading, then 'If the players choose this option during setup, ...'. List all options (random bosses, all-expansion decks, mimics, crystal lizards, mega-boss, PvP) once in §Setup.
- Rationale: Options are rules too; they need a fixed form.
- Gameplay impact: None
- Decision needed: N

### D-018 · component-count · Minor · REQUIRED
- Location: manuscript.md 679–723 (Tokens & Terrain Elements) vs 1277, 3056
- Evidence: Core p.7 lists 1x First Activation Token. The manuscript's component list omits it but uses a 'first player token' (1277) and a 'first turn token' (3056).
- Current text: (absent from list)
- Proposed fix: 1x First Activation token
- Rationale: Either list the token or delete the two references (characters act in threat order, so the token has no function outside PvP).
- Gameplay impact: None if removed.
- Decision needed: Y

### F-053 · prose-crossref · Minor · CLEAN-UP
- Location: L2221, L2229, L2233, L2235, L2243, L2245, L2289, L2297, L2312, L3060
- Evidence: 'the basic game' / 'the basic rules' used ten times as if naming another book.
- Current text: …largely the same as the basic game… as it does in the basic game… just as in the basic game… as in the basic rules… essentially unchanged from the basic rules… Use the basic rules for Andre's Shop… unchanged from basic rules.
- Proposed fix: Adopt one term, 'the standard game', defined once in §18 intro: 'A campaign uses the rules of the standard game (§6–§17) except as stated in this chapter.' Then each occurrence becomes '(see §x.y)' or is deleted.
- Rationale: Consistent internal term plus § references; no implied second rulebook.
- Gameplay impact: none
- Decision needed: N

### F-085 · register-shift · Minor · CLEAN-UP
- Location: L1203–1479 §Gameplay; L1598–1658 §Combat Basics › Conditions; L3038–3094 §PvP
- Evidence: Bullet-fragment register ('- Remove all damage cubes.', '- Souls cannot be transferred between characters.', '- Aggro token is not used.') alongside declarative-prose chapters (§3, §4, §8–§10) and numbered-procedure chapters (§6).
- Current text: - Drop all *souls* from the dashboard onto the current encounter tile. / - *Aggro* token is not used. / - Dying in PvP does not cause any penalty.
- Proposed fix: Normalise per the Voice Guide: sequences → numbered steps; standing rules → full declarative sentences with a subject ('The *aggro* token is not used in PvP.'); keep bullets only for unordered lists of conditions or components.
- Rationale: Three registers for the same kind of content; readers cannot tell a procedure from a standing rule.
- Gameplay impact: none
- Decision needed: N

### F-088 · register-shift · Minor · CLEAN-UP
- Location: L1241, L1461, L1479, L1670, L1848, L2047, L2057, L2151, L3040, L3042, L1115, L1109
- Evidence: Future tense in rules: 'Invaders will attempt to kill the characters'; 'the treasure will be awarded'; 'how an enemy model will move'; 'will instead do magical damage'; 'The mimic will take its turn first'; 'no further crystal lizards will spawn'; 'a PvP encounter will occur'; 'This will create a linear route'.
- Current text: - Invaders will attempt to kill the characters. … After each boss (mini, main, and mega) a PvP encounter will occur.
- Proposed fix: Present tense throughout: 'Invaders attack the characters.'; 'the treasure is awarded to…'; 'The mimic takes the first turn.'; 'a PvP encounter follows each boss'.
- Rationale: Tense policy: present.
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (2) — approved at Gate 1

### [CMP-0009] PLAYER VS PLAYER (chapter) — Proposed Completion
- Current state: Lines 3038–3094: twenty-seven bullets and a six-line dodge-difficulty list. No prose. Gaps: how a character attacks a character (which defence rolls, which dodge difficulty, how damage is placed); parry and riposte; pushes; conditions; what "outermost available node" means; what a trap token does in PvP; simultaneous death; how the "+1 attack damage" carry-over is tracked; ties in threat; what the champion is; "intimate victor" (line 1201) for "ultimate". The bullet "First turn token is given to the character with the highest threat value" (line 3056) duplicates the turn-order bullet (see CMP-0011).
- Proposed completion (full chapter; the manuscript's bullets are the skeleton):

  > # PLAYER VS PLAYER
  >
  > Player versus player (PvP) is an optional contest fought between the characters after each boss is defeated. The players must agree during setup whether PvP encounters will be played. If they are, a PvP encounter is fought after every mini-boss, main-boss and mega-boss encounter that is won.
  >
  > ## Setup
  >
  > 1. Remove every enemy model, wound token and trap token from the boss encounter tile(s). Terrain tokens remain.
  > 2. Restore every surviving character as if they had rested at the *bonfire*: remove all damage cubes, stamina cubes, *hollow* markers and condition tokens, and flip *luck*, *estus flask* and *heroic action* tokens to the ready side. *Ember* tokens are kept.
  > 3. Characters who died in the boss encounter take no part in the PvP encounter. Summons and invaders take no part.
  > 4. Place each character on a different corner node of the boss encounter tile(s). The character with the highest *threat* chooses first, then the next highest, and so on.
  > 5. The *aggro* token is not used.
  > 6. Set the trap tokens face down beside the tile, shuffled.
  >
  > ## Turn Order
  >
  > Characters take turns one at a time in descending *threat* order. If two characters share a *threat* value, the players decide their order before the first turn; if they cannot agree, decide at random. The order is kept for the whole PvP encounter. After the last character has taken a turn, the first takes the next, and so on until one character remains.
  >
  > ## Character Turns
  >
  > A character's turn is unchanged from the basic rules: recover one stamina; take any minor actions (*Walk*, *Run*, *Equip*, *Heroic Action*); take one major action (*Attack*, *Rest*, *Drink Estus* or *Ember*). A character may not leave the tile(s). The limit of one spell attack option per turn applies.
  >
  > After a character's major action, that character's player draws one trap token and places it face down on an outermost available node. The outermost available nodes are the nodes along the tile's edges that contain no model, no terrain token and no trap token; when every edge node is occupied, the next ring of nodes inward is the outermost. If no trap token remains, none is placed.
  >
  > ## Attacking a Character
  >
  > A character attacks another character exactly as they would attack an enemy: choose an attack option, pay its stamina cost, nominate a character within the attack's range as the target, roll the dice, apply modifiers, and use any rerolls (two-handed, *luck*, equipment). The result is the attack value. Attack options with the *shaft* icon may not target a character on the attacker's node. An *AoE* attack option targets every other character on the chosen node; roll once and resolve each defence separately. A *scaled* weapon's +1 and any PvP victory bonus (below) apply.
  >
  > The target then defends as against an enemy attack, choosing one of the following before any dice are rolled.
  >
  > - *Block* or *resist*: roll the block dice (against a physical attack option) or resist dice (against a magical attack option) of every equipped card; the defence total is the sum of the two highest dice. The defender suffers damage equal to the attack value minus the defence total, to a minimum of zero. The defender is hit.
  > - *Dodge*: pay one stamina (or three stamina for one additional die) and roll dodge dice against the dodge difficulty given by the table below. On a success the attack misses entirely and the defender must move to an adjacent node. On a failure the defender is hit and rolls only their armour card's block or resist dice.
  > - *Parry*: pay one stamina. A *parry* is allowed only if the defender has a shield in the left weapon slot, shares a node with the attacker, and the attack option has no push icon and is not *AoE*. Roll dodge dice against the table below. On a success the attack misses, the attacker receives a *stagger* token and the defender may at once make one *riposte* with any attack option of the weapon in their right weapon slot, paying its stamina cost; the attacker defends against the *riposte* by blocking, resisting or dodging but may not *parry* it. On a failure the defender suffers the full attack value, with no defence roll, and receives a *stagger* token.
  > - Do nothing: the defender suffers the full attack value and is hit.
  >
  > Damage suffered is placed as damage cubes on the defender's endurance bar. An *embered* defender reduces damage of three or more from a single attack by one, as usual.
  >
  > **Dodge difficulty in PvP.** The dodge difficulty of a character's attack option is set by its stamina cost:
  >
  > | Stamina cost of the attack option | Dodge difficulty |
  > |---|---|
  > | 0 | 4 |
  > | 1 | 3 |
  > | 2 | 2 |
  > | 3 | 1 |
  > | 4 | 1 |
  > | 5 or more | 0 |
  >
  > A *riposte* uses the dodge difficulty of the attack option chosen for it.
  >
  > ## Pushes and Conditions
  >
  > An attack option with the push icon pushes each character it hits one node directly away from the attacker, as Pushing describes; a character is not pushed into a node containing a gravestone or chest, and a barrel in the destination node is destroyed. Condition icons on attack options place the matching condition token on each character hit. Conditions on characters are resolved as Combat Basics › Conditions describes: *bleed* deals three damage when a second token would be placed; *poison* deals damage at the end of the character's turn; *frostbite* stops stamina recovery; *stagger* subtracts one from every roll total.
  >
  > ## Traps
  >
  > When a character moves onto, dodges onto, shifts onto or is pushed onto a node containing a face-down trap token, flip the token. If it shows a trap, the character must attempt to *dodge* against the trap's printed dodge difficulty, paying one stamina as usual; a character who fails, or who cannot pay, dies. A trap token showing nothing has no effect. A flipped trap token stays on its node and does not trigger again.
  >
  > ## Death
  >
  > A character whose endurance bar is full of damage cubes, or who fails to dodge a trap, dies and is removed from the tile. Death in PvP has no cost: *souls* are not dropped, the *ember* token is not removed, and no *hollow* markers are placed. The character is restored with the others at the end of the PvP encounter.
  >
  > ## Victory
  >
  > The last character on the tile wins the PvP encounter. If the last two or more characters die at the same time, no character wins.
  >
  > The winner of a PvP encounter fought after a mini-boss or a non-final main-boss gains a PvP victory bonus: place one wound token beside the winner's dashboard. In every later PvP encounter the character adds one to the attack value of each attack option per wound token beside their dashboard. The bonus has no effect outside PvP and is cumulative.
  >
  > The winner of the PvP encounter fought after the final boss is the champion of the game. The players still share the victory over the final boss.
  >
  > ## After the PvP Encounter
  >
  > Return all trap tokens to the supply. Place every character, including those who died, on the *bonfire* tile and rest there without spending a *spark*, as after a boss. Remove the wound tokens used to mark PvP victory bonuses only when the game ends.

  Consequential edit to Gameplay › Objective & Loss Conditions (line 1201): "…to determine a single ultimate victor." Delete the bullet "*First* *turn* token is given to the character with the highest threat value" (line 3056; see CMP-0011).
- Design rationale: Every mechanic is the manuscript's own, applied symmetrically: the defender rolls exactly as against an enemy (two highest dice; armour-only after a failed dodge; parry conditions and stagger results from Enemy Turn › Parry & Riposte), and the attacker's fixed enemy-style dodge difficulty is replaced by the manuscript's stamina-cost table. The outermost-node ring rule gives the trap bullet a definite meaning that shrinks the arena and ends stalemates. Simultaneous death yields no winner so the carry-over bonus cannot be awarded twice. The bonus is tracked with a wound token because wound tokens are otherwise unused on characters and no new component is needed. "A riposte may not be parried" prevents an endless chain of parries between two shield-bearers.
- Mechanical impact: PvP becomes fully playable. The only numeric additions are the trap death rule (already in the bullets) and the cumulative +1 bonus tracking. Terrain is kept on the tile (the bullets remove only enemies and traps), which keeps gravestones and chests as cover.
- Follow-on changes required: Delete the empty heading at line 3096. Add "Resting at the *bonfire*" after PvP to Returning to the Bonfire line 1908 (already states it). Glossary entries Dodge difficulty and Riposte (CMP-0002) reference this chapter. If the editor prefers a dedicated marker to the wound token, add "4x PvP victory tokens" to Game Components.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0011] Gameplay › Encounter Start step 9 and Player vs Player — "First player token" — Proposed Completion
- Current state: Encounter Start step 9 (line 1277): "Place the *first player* token on the character with the highest threat value." Player vs Player (line 3056): "*First* *turn* token is given to the character with the highest threat value." No such token is listed in Game Components › Tokens & Terrain Elements (lines 679–723). Turn order is fixed by *threat* in both places (lines 1289, 3058), so the token has no function.
- Proposed completion: Remove the token. Delete Encounter Start step 9 and the PvP bullet at line 3056, and replace Encounter Start step 8 (line 1275) with:

  > 8. Place the *aggro* token on the character with the highest *threat* value. That character takes the first character turn of the encounter; ties in *threat* are settled by the players before the first turn and the order is kept for the encounter.

  Replacement for PvP turn-order bullet (line 3058), as drafted in CMP-0009: "Characters take turns one at a time in descending *threat* order. If two characters share a *threat* value, the players decide their order before the first turn; if they cannot agree, decide at random."
- Design rationale: Removal is recommended over definition. Threat order already fixes the first character, so a first-player token would duplicate information the dashboards carry; the Core rulebook's First Activation token existed only because its turn order went clockwise, which this edition has abandoned. Defining the token would also require adding a component. The tie rule supplies the one thing the token's position would have recorded.
- Mechanical impact: None.
- Follow-on changes required: Remove "first player" from the italicised-term inventory; no Glossary entry. Renumber Encounter Start.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

