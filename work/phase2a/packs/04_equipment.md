# Drafting pack — chapter 04 (equipment) — manuscript chapter "EQUIPMENT"

Source text: `work/phase2a/source/04_equipment.md` (manuscript.md lines 807–894).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 807.
- **Equipment Cards** · present — to audit · line 809.
- **Upgrades** · present — to audit · line 847.
- **Spells** · present — structural · line 855. Duplicate heading "Spells" (H2 then H3).
- **Spells** · present — structural · line 857. Duplicate heading "Spells" (H2 then H3).
- **Embers** · present — to audit · line 889.
- **(empty heading)** · ORPHAN — delete · line 893: empty H1 used as page break

## Audit findings mapped to this chapter (41)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-006 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Embering (manuscript.md line 1229) vs CHARACTERS › Ember (line 805) and CHARACTER TURN › Major Action › Ember (line 1834)
- Evidence: manuscript.md:805, 891, 1227–1233, 1834
- Current text: Ember: Place ember token on dashboard; discard equipped ember card.
- Proposed fix: Ember (major action, or at any time outside an encounter): Discard an ember card from the back-up slot. Remove all damage cubes and all hollow markers from the endurance bar and place an ember token on the dashboard. The character is now embered.
- Rationale: Three passages define embering; only Embering (1229) says it removes all damage cubes. A full heal as a major action is a major tactical resource and must be stated identically everywhere. Alternative: delete 'Remove all damage cubes' at 1229 so that embering only removes hollow markers (Hollowed Edition precedent, p.5).
- Gameplay impact: Groups will disagree on whether embering heals; the difference is up to eight health in combat.
- Decision needed: Y

### A-046 · undefined-state · Major · REQUIRED
- Location: SETUP › Shop Setup › After Boss is Defeated (manuscript.md lines 1077–1089); EQUIPMENT › Embers (line 891)
- Evidence: manuscript.md:891, 1039, 1049, 1067–1089, 1935
- Current text: Draw tier one treasure cards one at a time to restock tier one shop: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: When a shop is restocked, every card remaining in that shop is placed on the bottom of its treasure deck before new cards are drawn. Ember cards remaining in the tier one shop stay in the shop and are never replaced; no ember card is ever added to a shop after setup.
- Rationale: Nothing says what happens to unsold shop cards on restock, and the ember restriction ('limited supply', 891) only works if the restock neither adds nor removes embers. Alternative: unsold cards remain and the restock only tops up to the quotas.
- Gameplay impact: Shop contents after the first boss are undefined.
- Decision needed: Y

### A-069 · undefined-state · Major · REQUIRED
- Location: SETUP › Shop Setup (manuscript.md line 1069); EQUIPMENT › Equipment Cards (line 811)
- Evidence: manuscript.md:811, 1069, 1079, 1085, 1876
- Current text: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: For stocking the shop: a shield is a weapon-slot card bearing the shield icon; a spell is a card whose art shows a scroll; an upgrade is a card with the weapon-upgrade or armour-upgrade icon, including rings and titanite; every other weapon-slot card, including catalysts and throwable items, is a weapon; an armour card is a card with the armour icon. A shield counts as equipment in the other hand for the two-handed rule.
- Rationale: Five shop categories are used but only armour, weapon and spell are defined; 'shield' and 'item' never are, and catalysts and consumables fall between categories.
- Gameplay impact: Shop stocking is the only treasure source before the first boss.
- Decision needed: Y

### B-022 · undefined-value · Major · REQUIRED
- Location: L1069/L1079/L1085 (Shop Setup) with L823-829 (Equipment Cards), L747-753 (Equipment Slots), L1769 (Parry)
- Evidence: The stock list requires '2 shields' per shop and the parry rule requires 'a shield as their left weapon', but the card-typing rules define only one-handed weapon, two-handed weapon, armour (by icon) and spell (by scroll art). No rule says how a shield is recognised; shields are weapon-typed cards in 1E (East-West Shield appears in the manuscript's own weapons table, L3244).
- Current text: Equipment cards include weapons, spells, shields, armour, and items which the character equips to improve their combat capabilities. ... 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: Add to Equipment Cards: "A shield is a one-handed weapon card that shows a block or resist value and has no attack option. Shields count as weapons for equipment slots and as shields for shop stocking and parrying."
- Rationale: The shop and parry procedures cannot be executed without a test for 'shield'.
- Gameplay impact: Makes the 12-card stock list and the parry prerequisite determinable.
- Decision needed: Y

### C-018 · hedge · Major · REQUIRED
- Location: L845; L1057; L1141; L2041; L2053; L2596; L2664; L2720; L2766; L2812; L2884; L2948; L2994
- Evidence: 14 'should' in optional-content advice, e.g. L845 'Players should include all equipment cards from expansions'; L1141 'players should include only the encounter cards from the same set'; L2041 'Groups with new players should default to leaving mimics out... Experienced players should include mimics'; L2596ff 'players should add the Explorers and Characters expansions if available' (x8)
- Current text: Players should include / should add / should default to
- Proposed fix: Rewrite as permissions or labelled recommendations: 'Players may include equipment cards from every expansion they own.' / 'By default, build each encounter deck only from cards of the next boss's set.' / 'Mimics are an optional rule; the players decide during setup whether to use them.' / campaign lines: 'Recommended: Explorers and Characters expansions.' Full per-line rewrites in C_report.md Task 2.
- Rationale: 'Should' leaves it unclear whether expansions are required, optional or recommended. Lawbook voice uses must/may or a labelled 'Recommended' line.
- Gameplay impact: Which components a group must own to play a campaign
- Decision needed: Y

### C-038 · terminology · Major · REQUIRED
- Location: L837; L851; L1820; L1838
- Evidence: 'used as a character's main action' (837); 'attached... as a main action' (851) vs heading 'Major Action:' (1820) and 'during an *attack* major action' (1838)
- Current text: main action
- Proposed fix: major action
- Rationale: 'Main action' is never defined; the turn structure defines Minor and Major actions.
- Gameplay impact: Readers cannot find the 'main action' rule
- Decision needed: Y

### C-048 · terminology · Major · REQUIRED
- Location: L1393; L805; L891; L919; L2239; L989; L1095
- Evidence: 'Successfully defeated invaders provide additional *souls* per player' (1393) vs Soul Reward Table 'per character' (1411); 'when that player discards an ember card' (805); 'stored in a player's inventory' (891); 'characters must choose a friendly model to push' (919 - a decision); 'If a player character leaves the characters' (2239). Note L989 'character dashboard(s)' and L1095 'character model(s)' allow one player to control several characters.
- Current text: per player / that player / player's inventory / characters must choose
- Proposed fix: Rule of use: PLAYERS decide, agree, choose and roll; CHARACTERS act, hold tokens, own cards and inventories, gain souls and die; MODELS occupy nodes, move and are pushed. L1393 -> 'per character'; L805 -> 'when that character discards'; L891 -> 'a character's inventory'; L919 -> 'the players must choose a friendly model to push'; L2239 -> 'If a player leaves, remove their character...'
- Rationale: When one player controls two characters, 'per player' and 'per character' pay different soul rewards.
- Gameplay impact: Soul rewards for invaders in 1-2 player games
- Decision needed: N

### C-119 · voice · Major · REQUIRED
- Location: L1205-1253; L1299-1399; L1445-1479; L1935-1949; L859-887; L931-981; L1604-1658; L2243-2293; L2314-2322; L3040-3094
- Evidence: Rules stated as bullet fragments: Death & Hollowing, Embering, Sparks (1205-1253); Encounter Resolution/Recovery, Souls (1299-1399); Treasure Rewards (1445-1479); Shop Rules (1935-1949); Spells (859-887); Terrain (931-981); Conditions (1604-1658); campaign Soul/Treasure Rewards and Shop (2243-2322); the whole PLAYER VS PLAYER chapter (3040-3094) is 27 bullets with no sentence structure
- Current text: - Encounters are *failed* if either all characters die.
- Proposed fix: Policy: PROCEDURES (setup, turn sequence, defence rolls, encounter start, resting, transposition) = numbered steps; DEFINITIONS and component anatomies (dashboard parts, data-card fields, condition effects, terrain) = bulleted lists of complete sentences; RULES (everything else) = short declarative paragraphs in 'When [trigger], [subject] must/may [action].' form. Rewrite PvP as prose plus a dodge table.
- Rationale: Fragments omit the trigger and subject that lawbook syntax requires ('Encounters are failed if either all characters die' has a dangling 'either').
- Gameplay impact: None
- Decision needed: Y

### F-009 · meta-commentary · Major · CLEAN-UP
- Location: L845 §Equipment › Equipment Cards
- Evidence: Advisory with rationale: 'Players should include all equipment cards from expansions available in their games to increase variety.'
- Current text: Players should include all equipment cards from expansions available in their games to increase variety.
- Proposed fix: REWRITE-IN-VOICE: 'Equipment cards from every expansion in the party's collection are included in the treasure decks (see §6.2).' (Or CUT as a duplicate of L1057.)
- Rationale: 'should … to increase variety' is advice plus rationale. The rule is that expansion cards are included.
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

### A-070 · undefined-state · Minor · OPTIONAL
- Location: EQUIPMENT › Spells (manuscript.md lines 877–887); Character Attacks (line 1846)
- Evidence: manuscript.md:861, 877–887, 1712, 1846
- Current text: Spells stored within their respective catalyst may use their attack options as if equipped.
- Proposed fix: A stored spell provides only its attack options; its block, resist and dodge values are ignored. Using a stored spell's attack option counts as the catalyst's one attack for that turn.
- Rationale: Block and Resist gather dice from 'equipped' cards; 'as if equipped' invites counting stored spells' defence values and a second attack from the same slot.
- Gameplay impact: Prevents a catalyst with three stored spells becoming a multi-attack slot.
- Decision needed: N

### A-071 · undefined-state · Minor · OPTIONAL
- Location: EQUIPMENT › Upgrades (manuscript.md line 851)
- Evidence: manuscript.md:841, 849, 851, 861
- Current text: upgrade spells are attached to a character's equipment as a main action similar to casting an attack spell.
- Proposed fix: Casting an upgrade spell is the caster's one spell attack option for that turn and their major action. An attached upgrade spell does not occupy one of the target card's upgrade slots.
- Rationale: Neither the slot limit nor the one-spell-per-turn limit says whether it covers upgrade spells.
- Gameplay impact: Clarifies buff spells for Cleric and Sorcerer play.
- Decision needed: N

### A-074 · contradiction · Minor · CLEAN-UP
- Location: EQUIPMENT › Upgrades (manuscript.md line 853); Shop Rules (line 1943); COMMUNITY UPDATE PACK (line 3182)
- Evidence: manuscript.md:853, 1941, 1943, 3182–3184
- Current text: Titanite upgrades (i.e.: Titanite Shards) attached to sold weapons are returned to the bottom of the tier one treasure deck.
- Proposed fix: Titanite upgrades attached to a sold weapon are returned, with the weapon, to the bottom of the treasure deck of the weapon's tier.
- Rationale: The Update Pack makes Titanite Chunk a 25/25 (tier two) card; the sell rule sends all titanite to tier one.
- Gameplay impact: Cosmetic deck-composition drift.
- Decision needed: N

### A-120 · undefined-state · Minor · OPTIONAL
- Location: ENEMY TURN › Block & Resist step 4 (manuscript.md line 1722); Equipment Cards (line 843)
- Evidence: manuscript.md:843, 1722
- Current text: Determine the defence total by adding the number of sword pips on the highest two dice results.
- Proposed fix: Fixed modifiers printed on equipment defence values are applied after the two highest dice are summed.
- Rationale: Dice modifiers (843) are defined for attacks; the two-highest-dice defence rule does not say where a defensive modifier applies.
- Gameplay impact: Affects a handful of armour cards.
- Decision needed: N

### C-002 · spelling · Minor · REQUIRED
- Location: L853
- Evidence: 'including the word Titanate (i.e., Titanite Shard)'
- Current text: Titanate
- Proposed fix: Titanite
- Rationale: Misspelled card-family name; 'Titanite' is used correctly at L497, L1943, L2055.
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

### C-022 · hedge · Minor · REQUIRED
- Location: L375; L377; L849; L1263
- Evidence: 'could' x4: L375 'that new players could use'; L377 'any sort of improvement that could be made'; L849 'a character could attach up to two weapon upgrade cards'; L1263 'the characters could skip to the fourth encounter but would all start with 6 stamina expended'
- Current text: could
- Proposed fix: L849: 'a character may attach up to two weapon upgrade cards to a weapon with an upgrade limit of two.' L1263: 'the characters may skip to the fourth encounter; each character begins it with six stamina cubes on their endurance bar.' L375/L377: front matter - cut or move to Foreword.
- Rationale: Permissions use 'may'; examples use the indicative.
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

### C-042 · terminology · Minor · CLEAN-UP
- Location: L771; L849; L1131; L1171; L1179; L1886; L1892; L2195; L2295; L2358ff
- Evidence: 'The Bonfire' capitalised mid-sentence x10 (e.g. 771 'resting at The Bonfire'); '*bonfire*' x35; plain 'the bonfire' x27; 'Bonfire Tile' x48 in campaign lists; 'The Bonfire tile' (1131, 1171, 1179)
- Current text: The Bonfire / Bonfire Tile
- Proposed fix: the *bonfire* (lower-case keyword); 'bonfire tile' for the component; headings may read 'The Bonfire'
- Rationale: Game locations are common nouns (cf. fog gate, shop); capital 'The' mid-sentence is inconsistent with the keyword form.
- Gameplay impact: None
- Decision needed: N

### C-043 · terminology · Minor · CLEAN-UP
- Location: L841; L1025; L1099; L1169; L1888; L1904; L1927; L1929; L2195; L2297; L2310; L2312; L2314; L2340
- Evidence: 'Blacksmith Andre' x7; bare 'Andre' x11 (e.g. 1099 'next to Andre'); 'Andre's Shop' x9; 'the shop' x3; heading 'Blacksmith Andre's Shop' (2310)
- Current text: Andre's Shop / the shop / Andre
- Proposed fix: 'Blacksmith Andre' at first mention in a section, 'Andre' thereafter; 'Andre's shop' (lower-case s) for the shop, 'the shop' acceptable after first mention
- Rationale: One NPC, one shop; choose capitalisation once. Recommend lower-case 'shop' to match other lower-cased game locations (bonfire, fog gate).
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

### C-054 · terminology · Minor · REQUIRED
- Location: L811; L1183; L1880; L1941; L597ff; L809ff
- Evidence: 'treasure card' x40 (deck/reward object) and 'equipment card' x24 (weapons, spells, shields, armour, items) are both legitimate but their relationship is never stated; bare 'item(s)' at 1183 'Shuffle mega-boss Items', 1880 'the equipped item', 1941 'Sold items'; bare 'treasure' x68
- Current text: Items / item / treasure
- Proposed fix: Define once: 'A *treasure card* is any card from a treasure deck. An *equipment card* is a treasure card that may be equipped to a dashboard slot.' Replace bare 'item(s)' with 'treasure card(s)'; allow bare 'treasure' only in reward contexts ('one treasure each').
- Rationale: Three words for overlapping sets; 'item' is also a card type name in the Community Update Pack ('legendary Item').
- Gameplay impact: None
- Decision needed: Y

### C-060 · terminology · Minor · CLEAN-UP
- Location: L801; L1720; L1744; L1780; L1876; L1846; L3194; L763; L805; L1814; L891; L1201; L1908; L373-379; L2225
- Evidence: 'reroll' x8 vs 're-roll' x2 (1846, 3194); 'back-up slot' x2 vs 'backup slot' (891); 'PvP' x10 vs 'player versus player (PvP)' (1201) vs 'player-versus-player (PvP)' (1908); 'rule set'/'ruleset'/'rule-set'; 'rule book'/'rulebook'/'rule-book'
- Current text: (variants)
- Proposed fix: reroll; back-up slot; define 'player versus player (PvP)' once (L1201) then 'PvP'; ruleset; rulebook
- Rationale: One spelling per compound.
- Gameplay impact: None
- Decision needed: N

### C-084 · cross-ref · Minor · CLEAN-UP
- Location: L837; L839; L841; L891; L1057; L1165; L1475; L1485; L1760; L1852; L2045; L2069; L2077; L2099; L2105; L2163; L2195; L2197; L2289; L2297; L2312
- Evidence: 21 prose cross-references resolved correctly but informally: 'explained in detail later on in the section title "Character Attacks"' (837, 'title' for 'titled'); 'section titled "Enemy Attacks"' (839); 'described later in more detail' (841); 'aforementioned effects' (891); 'as above' (1057, 1760); 'as previously described' (1165, 2195); 'later in these rules' (1475); 'detailed later' (1485); 'explained above/previously' (1852); 'per normal treasure chest rules' (2045); 'as described previously' (2069); 'will follow' (2077); 'previously described' (2099, 2163); 'as detailed during the setup chapter' (2105); 'as described earlier' (2197); 'as in the basic rules' (2289, 2297, 2312)
- Current text: (see Evidence)
- Proposed fix: Convert every one to the form '(see §N.N Heading)' once section numbers exist; drop 'later/earlier/previously/aforementioned'. Resolution table in C_report.md Task 6.
- Rationale: Positional words break when sections move; numbered references do not.
- Gameplay impact: None
- Decision needed: N

### C-096 · example · Minor · CLEAN-UP
- Location: L1943; L1945; L2141; L771; L853
- Evidence: '(i.e.: Titanite Shards)' (1943), '(i.e.: gems)' (1945), '(i.e.: *Run*)' (2141) each introduce an example, not a restatement, so 'e.g.' is meant; 771 and 853 use 'i.e.,' correctly; punctuation varies ('i.e.:' vs 'i.e.,').
- Current text: i.e.:
- Proposed fix: Write out: 'for example, Titanite Shards' / 'such as gems' / 'for example by running'; and 'that is,' for the two true restatements. Avoid Latin abbreviations in rules text.
- Rationale: Misused abbreviation changes meaning (Titanite Shards are one kind of Titanite upgrade, not the definition).
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

### C-099 · heading · Minor · REQUIRED
- Location: L855; L857
- Evidence: '## Spells' immediately followed by '### Spells'
- Current text: ## Spells / ### Spells
- Proposed fix: Single '## Spells' heading
- Rationale: Duplicate heading.
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

### C-111 · punctuation · Minor · CLEAN-UP
- Location: L375; L529; L805; L835; L853; L1025; L1529; L1726; L1826; L1904; L1929; L1985; L2310; L2312; L2314; L837; L839; L2047
- Evidence: Mixed quotation marks: curly apostrophe ’ x146 in the body vs straight ' in ~20 lines (e.g. L529 'Executioner's Chariot (Executioner’s Chariot)' has both forms in one line); curly double quotes “ ” at 837, 839, 2047
- Current text: ' / ’ mixed
- Proposed fix: Policy: straight quotes in the Markdown source; the typesetter converts to curly. Until then, make every line consistent (curly).
- Rationale: Mixed glyphs show in print.
- Gameplay impact: None
- Decision needed: N

### C-117 · punctuation · Minor · CLEAN-UP
- Location: L875; L3154; L1806-1834
- Evidence: Pandoc list-separator comments '<!-- -->' (875, 3154) and blockquote '>' markup used for the turn-structure list (1806-1834)
- Current text: <!-- --> / > *Walk*: ...
- Proposed fix: Delete the comments; replace blockquotes with the numbered procedure proposed in the heading row.
- Rationale: Conversion artefacts.
- Gameplay impact: None
- Decision needed: N

### D-033 · underspecified-deviation · Minor · OPTIONAL
- Location: manuscript.md 843 (Equipment Cards) and 1722 (Block & Resist)
- Evidence: Core p.12 modifiers add or subtract from 'the die roll'. HE p.9 'Choose any two rolled dice' is silent on modifiers. Under the manuscript's two-highest-dice rule it is unstated whether a card's fixed block modifier applies after the two dice are selected.
- Current text: Determine the defence total by adding the number of sword pips on the highest two dice results. Additional dice beyond the two with the highest shown face value are ignored.
- Proposed fix: The defence total is the sum of the two highest dice results plus any fixed modifiers on the equipment used.
- Rationale: Closes a gap created by combining the 1E modifier rule with the HE dice cap.
- Gameplay impact: Minor defence maths.
- Decision needed: Y

### D-034 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 851 (Upgrades)
- Evidence: Upgrade spells are attached 'as a main action similar to casting an attack spell'; the Character Turn lists Attack as the only offensive major action, so it is unstated whether attaching an upgrade spell consumes the attack action and whether a stamina cost applies.
- Current text: Instead, upgrade spells are attached to a character's equipment as a main action similar to casting an attack spell.
- Proposed fix: Attaching an upgrade spell is an attack action: the character pays the stamina cost printed on the spell and makes no other attack with that catalyst this turn.
- Rationale: Original mechanic with no official parallel; needs an action cost.
- Gameplay impact: None beyond clarity.
- Decision needed: N

### F-058 · prose-crossref · Minor · CLEAN-UP
- Location: L837 §Equipment › Equipment Cards
- Evidence: Prose cross-reference: 'explained in detail later on in the section title “Character Attacks”'
- Current text: explained in detail later on in the section title “Character Attacks”
- Proposed fix: '(see §10.3)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §10.3 Character Attacks. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-059 · prose-crossref · Minor · CLEAN-UP
- Location: L839 §Equipment › Equipment Cards
- Evidence: Prose cross-reference: 'explained in detail later on in the section titled “Enemy Attacks”'
- Current text: explained in detail later on in the section titled “Enemy Attacks”
- Proposed fix: '(see §9.3)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §9.3 Enemy Attacks. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-060 · prose-crossref · Minor · CLEAN-UP
- Location: L841 §Equipment › Equipment Cards
- Evidence: Prose cross-reference: 'at Blacksmith Andre which is described later in more detail'
- Current text: at Blacksmith Andre which is described later in more detail
- Proposed fix: '(see §11.4)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §11.4 Blacksmith Andre. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-061 · prose-crossref · Minor · CLEAN-UP
- Location: L891 §Equipment › Embers
- Evidence: Prose cross-reference: 'with the aforementioned effects'
- Current text: with the aforementioned effects
- Proposed fix: '(see §7.3)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §3.5 Character Tokens › Ember; §7.3 Embering. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-083 · prose-crossref · Minor · CLEAN-UP
- Location: L1263, L1141, L849, L1914, L2141 (inline 'For example…')
- Evidence: Prose cross-reference: 'For example, if the first three encounters are marked cleared…'
- Current text: For example, if the first three encounters are marked cleared…
- Proposed fix: Set each as a separate *Example.* paragraph per the Voice Guide §7; examples are not rules. — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: n/a — worked examples embedded in rule sentences. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### C-092 · example · Note · OPTIONAL
- Location: L849; L771; L1914; L1918-1923
- Evidence: Upgrade-limit example (849: limit two -> up to two upgrade cards) correct. Stat-tier examples (771 'pay... tier one upgrade, and then the tier two upgrade'; 1914 'two souls to reach tier one before paying four additional souls to reach tier two') match the basic Stat Tier Costs table (2, 4). The campaign table (4, 8) differs; the 1914 example sits in the basic chapter.
- Current text: (verified)
- Proposed fix: Add to §The Bonfire Tile (campaign): 'In campaign play the same example costs four then eight souls.'
- Rationale: Examples verified; one clarifying sentence recommended.
- Gameplay impact: None
- Decision needed: N

### F-098 · copied-prose · Note · OPTIONAL
- Location: L837 §Equipment › Equipment Cards
- Evidence: Matches official text — close paraphrase (14-word run)
- Current text: An equipment card's actions represent an attack or special effect used during an encounter. Each line on the card represents a separate attack option…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.12. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-099 · copied-prose · Note · OPTIONAL
- Location: L843 §Equipment › Equipment Cards
- Evidence: Matches official text — near-verbatim (74% shingle overlap)
- Current text: Some equipment cards have dice modifiers that add a fixed value to the die roll or subtract a fixed value from the die roll.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.12. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-100 · copied-prose · Note · OPTIONAL
- Location: L849 §Equipment › Upgrades
- Evidence: Matches official text — paraphrase (10-word run)
- Current text: Upgrade cards are used to enhance equipment. There are two types of upgrade cards…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: V2 p.10. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (1) — approved at Gate 1

### [CMP-0016] EQUIPMENT › Spells — Duplicate heading — Proposed Completion
- Current state: "## Spells" (line 855) is followed at once by "### Spells" (line 857); the bullet list is split by a stray comment marker (line 875). The second group of bullets concerns catalysts, not spells in general.
- Proposed completion: Delete line 857 and line 875. Retitle the two bullet groups as sub-sections:

  > ## Spells
  >
  > ### Spell Cards
  >
  > (bullets at lines 859–873 unchanged)
  >
  > ### Catalysts
  >
  > - Spells stored in a matching *catalyst* may use their *attack options* as if equipped.
  > - A pyromancer flame stores up to three pyromancies; a staff or catalyst stores up to three sorceries; a talisman or chime stores up to three miracles.
  > - A spell card is stored in the *catalyst* card it is attached to and occupies no equipment slot of its own.
  > - Spells may be transferred between a character's *catalyst* and inventory only between encounters.
- Design rationale: Structural fix with no rule change; the second heading names what the bullets define. "Occupies no equipment slot of its own" states what "as if equipped" implies and answers a question the Equipment Slots section otherwise leaves open.
- Mechanical impact: None.
- Follow-on changes required: Glossary entry Catalyst (CMP-0002). Regenerate TOC.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

