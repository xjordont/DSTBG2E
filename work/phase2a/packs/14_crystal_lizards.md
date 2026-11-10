# Drafting pack — chapter 14 (crystal_lizards) — manuscript chapter "CRYSTAL LIZARDS"

Source text: `work/phase2a/source/14_crystal_lizards.md` (manuscript.md lines 2051–2060).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 2051.
- **(empty heading)** · ORPHAN — delete · line 2059: empty H1 used as page break

## Audit findings mapped to this chapter (22)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-028 · undefined-state · Major · REQUIRED
- Location: SUMMONS › Invader Encounter Setup step 3 (manuscript.md line 2019); CRYSTAL LIZARDS (line 2055); Enemy Scaling (line 1521)
- Evidence: manuscript.md:1521–1529, 2019, 2055, 2342; DS-Phantoms-Rules-lores.txt p.12; DS-IronKeep-Rules-Web.txt p.5
- Current text: Invaders do not multiply their health by the number of characters like other enemy models.
- Proposed fix: Invaders and crystal lizards are never modified by enemy scaling or by the bonfire ascetic.
- Rationale: Both exemptions cover health only; invaders are 'non-boss enemies' and would otherwise gain +1 attack and Repeat 2, and crystal lizards would gain movement 1→2, which defeats the chase. The bonfire ascetic (2342) already exempts invaders from +1 attack, which shows the intent. Alternative: invaders receive attack scaling but not health scaling.
- Gameplay impact: A Repeat-2 invader with +1 attack acting after every character turn is lethal at four players.
- Decision needed: Y

### A-096 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Treasure Rewards (manuscript.md line 1477) vs CRYSTAL LIZARDS (line 2055)
- Evidence: manuscript.md:1477, 2055, 3182; DS-IronKeep-Rules-Web.txt p.3 (3x Titanite Scale Cards), p.5
- Current text: award a Titanite Chunk card to any character who killed a crystal lizard during the encounter. / Whenever a character kills a crystal lizard, they immediately place one Titanite Scale card into their inventory.
- Proposed fix: Whenever a character kills a crystal lizard, that character immediately places one Titanite Scale card in their inventory. (Delete the Titanite Chunk bullet at line 1477.)
- Rationale: Two names and two timings for the same reward. The Iron Keep expansion supplies Titanite Scale cards for exactly this purpose; the Update Pack's Titanite Chunk is a separate common card. Alternative: award a Titanite Chunk and treat the three Scale cards as extra Chunks.
- Gameplay impact: Different cards with different stat requirements and bonuses.
- Decision needed: Y

### C-018 · hedge · Major · REQUIRED
- Location: L845; L1057; L1141; L2041; L2053; L2596; L2664; L2720; L2766; L2812; L2884; L2948; L2994
- Evidence: 14 'should' in optional-content advice, e.g. L845 'Players should include all equipment cards from expansions'; L1141 'players should include only the encounter cards from the same set'; L2041 'Groups with new players should default to leaving mimics out... Experienced players should include mimics'; L2596ff 'players should add the Explorers and Characters expansions if available' (x8)
- Current text: Players should include / should add / should default to
- Proposed fix: Rewrite as permissions or labelled recommendations: 'Players may include equipment cards from every expansion they own.' / 'By default, build each encounter deck only from cards of the next boss's set.' / 'Mimics are an optional rule; the players decide during setup whether to use them.' / campaign lines: 'Recommended: Explorers and Characters expansions.' Full per-line rewrites in C_report.md Task 2.
- Rationale: 'Should' leaves it unclear whether expansions are required, optional or recommended. Lawbook voice uses must/may or a labelled 'Recommended' line.
- Gameplay impact: Which components a group must own to play a campaign
- Decision needed: Y

### C-056 · terminology · Major · REQUIRED
- Location: L1477; L2055; L3182
- Evidence: 'award a Titanite Chunk card to any character who killed a *crystal lizard*' (1477) vs 'they immediately place one Titanite Scale card into their inventory' (2055). Iron Keep booklet: '3x Titanite Scale Cards', 'add one Titanite Scale card to the inventory'. Community Update Pack (3182) defines Titanite Chunk as a common +2 upgrade replacing Titanite Shard.
- Current text: Titanite Chunk (L1477)
- Proposed fix: Titanite Scale
- Rationale: Two different cards named for the same reward; official component is the Titanite Scale.
- Gameplay impact: Which card a crystal-lizard kill awards
- Decision needed: N

### D-028 · underspecified-deviation · Major · REQUIRED
- Location: manuscript.md 1477 (Treasure Rewards) vs 2055 (Crystal Lizards)
- Evidence: IK p.3: 3x Titanite Scale cards; IK p.5: one Titanite Scale is added to the inventory only when every lizard in an encounter is killed before the encounter is cleared, and the icon is ignored once the three cards are gone. The manuscript awards a card per lizard killed, names it 'Titanite Chunk' at 1477 and 'Titanite Scale' at 2055, and does not say what happens when the three cards are exhausted.
- Current text: award a Titanite Chunk card to any character who killed a crystal lizard during the encounter … they immediately place one Titanite Scale card into their inventory
- Proposed fix: Whenever a character kills a crystal lizard, that character takes one Titanite Scale card from the supply. When no Titanite Scale cards remain, crystal lizards are no longer placed during encounter setup.
- Rationale: Unifies the name with the printed card and closes the supply gap created by the per-kill award.
- Gameplay impact: Upgrade economy with Iron Keep.
- Decision needed: Y

### F-025 · meta-commentary · Major · CLEAN-UP
- Location: L2053 §Crystal Lizards ¶1
- Evidence: Intro flavour followed by advice and a scope disclaimer: 'Players should include crystal lizards as an optional game component if they own the Iron Keep expansion set. The following rules are assuming the players are playing with…'
- Current text: Crystal lizards are strange and glimmering reptiles that offer character's powerful rewards if the lizard is slain before it can escape. Players should include crystal lizards as an optional game component if they own the Iron Keep expansion set. The following rules are assuming the players are playing with the Iron Keep expansion set and the included crystal lizards.
- Proposed fix: KEEP first sentence as intro, trimmed: 'Crystal lizards are glimmering reptiles that yield rare materials if slain before they escape.' REWRITE rest: 'Crystal lizards are an optional rule. They require the Iron Keep expansion. The party decides during setup whether crystal lizards are in play.'
- Rationale: Same pattern as Mimics; align both optional-rule openers.
- Gameplay impact: none
- Decision needed: N

### A-062 · loop/exploit · Minor · OPTIONAL
- Location: GAMEPLAY › Encounter Resolution (manuscript.md lines 1321–1327)
- Evidence: manuscript.md:1267, 1321–1327, 1391, 2057
- Current text: Encounters cleared that have already been cleared resolve as follows: ... Characters gain soul rewards but not treasure.
- Proposed fix: A cleared encounter may be repeated at most once between two rests at the bonfire.
- Rationale: Nothing limits re-fighting a cleared tile; with only one damage healed per clear the loop is self-limiting but still permits indefinite soul farming of a weak encounter. Alternative: no limit (risk-based self-limiting).
- Gameplay impact: Prevents grinding, which the Second Edition Notes name as a design goal.
- Decision needed: Y

### A-097 · omission · Minor · OPTIONAL
- Location: CRYSTAL LIZARDS (manuscript.md line 2055)
- Evidence: manuscript.md:2055–2057; DS-IronKeep-Rules-Web.txt p.5 ('Once the party has defeated three different encounters with Crystal Lizards, there will be no Titanite Scale cards remaining. Ignore all Crystal Lizard icons')
- Current text: Some encounters contain multiple crystal lizards.
- Proposed fix: If no Titanite Scale cards remain in the supply, crystal lizards are not placed during encounter setup.
- Rationale: Only three Scale cards exist; the manuscript lets lizards keep spawning after they are exhausted.
- Gameplay impact: Rare; long campaigns.
- Decision needed: N

### B-032 · table-text-mismatch · Minor · REQUIRED
- Location: L1477 (Treasure Rewards, crystal lizards) vs L2057 (Crystal Lizards)
- Evidence: L1477 awards 'a Titanite Chunk card' for killing a crystal lizard; L2057 awards 'one Titanite Scale card'. Official Iron Keep rules (text lines 125-131) award a Titanite Scale; the manuscript's own errata list (L3126) redefines Titanite Chunk as a +2 upgrade that must replace a Shard.
- Current text: If playing with the option of *crystal lizards*, award a Titanite Chunk card to any character who killed a *crystal lizard* during the encounter.
- Proposed fix: "If playing with the option of crystal lizards, award one Titanite Scale card to any character who killed a crystal lizard during the encounter."
- Rationale: One reward name across both sections, matching the component list of the Iron Keep expansion (3x Titanite Scale cards).
- Gameplay impact: Prevents the +2 Chunk (a stronger upgrade) being handed out for an optional side-kill.
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

### C-059 · terminology · Minor · CLEAN-UP
- Location: L969; L1017; L1021; L1025; L1029; L1201; L2055; L2748; L1473
- Evidence: 'set-up' x8 (noun), 'setup' x21 (noun), 'set up' (1473, verb)
- Current text: set-up
- Proposed fix: Noun 'setup' (and 'Setup' in headings); verb 'set up'
- Rationale: Standard British usage distinguishes noun and phrasal verb.
- Gameplay impact: None
- Decision needed: N

### C-061 · terminology · Minor · REQUIRED
- Location: L1517; L1850; L1295; L1301; L2053; L2195; L1223; L1305
- Evidence: Enemy death verbs vary: 'considered killed and removed from the tile' (1517); 'that enemy dies and is removed from play' (1850); 'all enemy models are defeated' (1295, 1301); 'the lizard is slain' (2053); 'the boss is slain' (2195). Characters 'die' (1223, 1305).
- Current text: killed / dies / defeated / slain
- Proposed fix: Characters 'die'; non-boss enemy models are 'killed' (and removed); bosses and encounters are 'defeated'/'cleared'. Replace 'slain' and enemy 'dies'.
- Rationale: Distinct verbs let rules refer unambiguously to character death (which has consequences) versus enemy removal.
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

### C-120 · voice · Minor · REQUIRED
- Location: L1963; L2043-2047; L2055-2057; L2065; L2125; L2340; L2348; L1592-1594
- Evidence: Procedures written as long prose paragraphs: Resuming Exploration (1963); mimic chest procedure (2043-2047); crystal lizard spawn/escape (2055-2057); fog gate (2065); behaviour deck construction (2125); bonfire ascetic (2340); transposition 'First, ... Second, ... Third, ... Fourth, ...' (2348); push resolution (1592-1594)
- Current text: First, players gather all available legendary treasure cards... Second, ... Third, ... Fourth, ...
- Proposed fix: Numbered steps, one action per step.
- Rationale: Multi-step procedures are read at the table mid-game; numbered steps are scannable.
- Gameplay impact: None
- Decision needed: N

### C-121 · voice · Minor · OPTIONAL
- Location: L1888; L1890; L2069; L2159; L2197; L2041; L2053; L1876; L1872; L1107; L1109
- Evidence: Flavour and advice inside rules paragraphs: Firekeeper/Andre description (1888); 'Sparks are the most precious resource in this game and the players must carefully weigh the timing' (1890); 'targets of their bloodlust... characters can expect to die often' (2069); 'Players can gain an advantage over a boss by memorising the order' (2159); session-break advice (2197); 'quite punishing' (2041); 'strange and glimmering reptiles' (2053); 'decidedly on the offensive' (1876); 'rapid flurry of attacks' (1872); 'if they like' (1107); 'For added challenge' (1109)
- Current text: (flavour)
- Proposed fix: Move to clearly styled sidebars/flavour boxes or cut; rules paragraphs carry rules only.
- Rationale: Mixing flavour and rules obscures what is binding.
- Gameplay impact: None
- Decision needed: Y

### C-122 · voice · Minor · CLEAN-UP
- Location: L1115; L1141; L1241; L1461; L1479; L2027; L2047; L2055; L2057; L1171; L2996
- Evidence: Future tense for rules: 'This will create a linear route' (1115); 'they would use only the encounters' (1141); 'Invaders will attempt to kill the characters' (1241); 'the treasure will be awarded' (1461, 1479); 'the invader will take many more turns' (2027); 'The mimic will take its turn first' (2047); 'the crystal lizards will respawn' (2055); 'no further crystal lizards will spawn' (2057); 'When all three section two options are complete, the players win' (2996, ok)
- Current text: will be awarded / will take / will respawn
- Proposed fix: Present indicative: 'is awarded', 'takes its turn first', 'respawn'.
- Rationale: Rules are timeless statements.
- Gameplay impact: None
- Decision needed: N

### C-124 · voice · Minor · REQUIRED
- Location: L1107; L1109; L1137; L1141; L2041; L2053; L1201; L3040
- Evidence: Optional rules are introduced inconsistently: 'if they wish... if they like' (1107); 'For added challenge the players may forgo choice' (1109); 'If playing with optional mimics for increased challenge' (1137); 'if they prefer more variety' (1141); 'may choose whether they wish to include mimics' (2041); 'as an optional game component' (2053); 'Players should agree on whether they will include a mega-boss and/or PvP' (1201); 'Decide during setup if PvP rules will be used' (3040)
- Current text: (eight phrasings)
- Proposed fix: One pattern: a boxed 'Optional rule: <name>' heading, then 'If the players choose this option during setup, ...'. List all options (random bosses, all-expansion decks, mimics, crystal lizards, mega-boss, PvP) once in §Setup.
- Rationale: Options are rules too; they need a fixed form.
- Gameplay impact: None
- Decision needed: N

### F-026 · second-person · Minor · CLEAN-UP
- Location: L2057 §Crystal Lizards ¶3
- Evidence: Reader address: 'Note that an encounter is still considered cleared regardless of any surviving crystal lizards.'
- Current text: Note that an encounter is still considered *cleared* regardless of any surviving crystal lizards.
- Proposed fix: REWRITE-IN-VOICE: 'Surviving crystal lizards do not prevent an encounter from being *cleared*.'
- Rationale: 'Note that' addresses the reader.
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

## Completion entries that apply (1) — approved at Gate 1

### [CMP-0015] CRYSTAL LIZARDS / Treasure Rewards — Reward card name — Proposed Completion
- Read `04_completion_backlog.md` lines 1061–1070 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

