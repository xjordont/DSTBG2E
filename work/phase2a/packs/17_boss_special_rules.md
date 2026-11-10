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
- Current state: Lines 2199–2213 cover only "Asylum Demon & Stray Demon" (Pillar Smasher, Wind Up). Setup After the main-boss step 11 (line 1195) defers to "any special rules described in the mega-boss rule booklet" — an external reference. No rules exist for the Core bosses, Darkroot, Iron Keep, Explorers, Tomb of Giants or any other mega-boss, although all are listed in Game Components and used in CAMPAIGNS. Booklets supplied: Core, Tomb of Giants (V2), Darkroot, Iron Keep, Explorers, Phantoms, Black Dragon Kalameet, Executioner's Chariot. Not supplied: Asylum Demon, Four Kings, Gaping Dragon, Guardian Dragon, Manus, Old Iron King, Vordt, The Last Giant, Painted World of Ariamis.
- Proposed completion (full chapter replacement; the existing Asylum/Stray Demon text is retained and re-ordered; BLOCKED placeholders are given in the structure the finished entries use):

  > # BOSS SPECIAL RULES
  >
  > Every boss's data card carries a special ability that applies throughout its encounter. This chapter gives the further rules that particular bosses require. A boss that is not listed here has no rules beyond its data card and the general boss rules.
  >
  > Where this chapter and a data card disagree, this chapter governs.
  >
  > ## Rules Common to Several Bosses
  >
  > **Zero dodge difficulty.** When a behaviour card shows a dodge difficulty of 0, a character may pay one stamina to *dodge* the attack without rolling, even with no dodge dice, as the Dodge rules describe. The character may instead block or resist as usual.
  >
  > **Two boss models in one encounter.** When an encounter contains two boss models, the boss node limit applies to each model separately: a node may hold one boss model, and a boss model that moves onto a node containing the other pushes it. Characters sharing a node with a boss model are placed in that model's arcs.
  >
  > ## Core Set
  >
  > **Gargoyle, Titanite Demon, Boreal Outrider Knight, Winged Knight, Dancer of the Boreal Valley.** No rules beyond the data card.
  >
  > **Twin Gargoyles.** Some campaign sections list the Gargoyle twice. The two Gargoyle encounters form one boss encounter in two parts. When the first Gargoyle is slain, the encounter does not end: at once place the second Gargoyle on the boss spawn node facing the centre of the tile, set its health dial to its starting health, and build a new behaviour deck for it. The characters remain where they are, recover nothing, and characters who died remain dead. *Souls*, boss treasure, the *spark* and the *ember* tokens are awarded once, when the second Gargoyle is slain. If the characters are defeated by either Gargoyle, the boss encounter is *failed* and both Gargoyles must be fought again. [PROPOSED adaptation of the Core campaign footnote]
  >
  > **Dragonslayer Ornstein & Executioner Smough.** Ornstein & Smough are one boss: one data card, one health dial, one behaviour deck, one heat-up. Place both models on the main-boss tile as the data card directs; each behaviour card states which model acts and which model's arcs its attack uses. A character attacking either model attacks the boss; the weak-arc bonus is judged against the arcs of the model attacked. The rule for two boss models in one encounter applies. The placement of the second model, the behaviour cards' model markings and the effect of heat-up on the pair are printed on the data card and behaviour cards. [Editor: BLOCKED — the data card is the only source for the pairing and is not supplied; the Core rulebook prose contains no dual-boss rule.]
  >
  > ## Asylum Demon Expansion — Asylum Demon and Stray Demon
  >
  > ### Pillar Smasher
  >
  > During the boss encounter setup, place one pillar token on each of the four pillar nodes found on the mega-boss game board. Pillars block movement.
  >
  > When the Asylum Demon or Stray Demon makes a physical attack with an *area* icon, check whether any pillar token lies within the affected arcs and range. Each character within one node of such a pillar token immediately suffers one damage and the *stagger* condition; then remove that pillar token from the tile. Resolve the *area* attack itself (including any pushes or dodges) after every pillar's destruction is resolved. A single attack may destroy several pillars, and a model may be hit by several shattering pillars at once.
  >
  > Once a pillar is destroyed, its node is a basic node for the rest of the encounter. When the characters rest at the *bonfire*, return every destroyed pillar to its pillar node.
  >
  > ### Wind Up
  >
  > When a Wind Up behaviour icon is resolved, each character may spend one stamina to move their model to an adjacent node. This movement counts as a *Run*.
  >
  > [Editor: BLOCKED — Asylum Demon booklet not supplied. The two rules above are the manuscript's own text, retained unchanged; any further rule the booklet defines (game board layout, Level 4 encounter cards, treasure) cannot be drafted.]
  >
  > ## Darkroot Expansion
  >
  > **Great Grey Wolf Sif (main-boss).** Several of Sif's behaviour cards have dodge difficulty 0. Sif's behaviour deck includes cool-down cards that show Sif weakened near death; they are used exactly as the data card directs. No other rules beyond the data card.
  >
  > **Artorias (main-boss).** Several of Artorias's behaviour cards have dodge difficulty 0. *Heat-up:* when Artorias's health is reduced to or below his heat-up point, do not shuffle in one heat-up card. Instead remove two random cards from his behaviour deck and return them to the box, then shuffle all three of his heat-up cards into the behaviour deck.
  >
  > ## Iron Keep Expansion
  >
  > **Smelter Demon (main-boss).** *Heat-up:* when the Smelter Demon's health is reduced to or below its heat-up point, do not shuffle in one heat-up card. Instead return the whole five-card behaviour deck and its discard pile to the box, and replace them with a new behaviour deck of five random heat-up cards, shuffled.
  >
  > **Sir Alonne (main-boss).** No rules beyond the data card.
  >
  > ## Explorers Expansion
  >
  > **Old Dragonslayer (mini-boss).** The Old Dragonslayer uses the Ornstein miniature with its own health dial, data card, eight behaviour cards and treasure cards. *Corrupted Dragonslayer:* the first three times the Old Dragonslayer loses four or more health from a single attack, place one random heat-up card face down on top of his behaviour deck. This is in addition to the ordinary heat-up at his heat-up point.
  >
  > **Pursuer (main-boss).** Several of the Pursuer's behaviour cards have dodge difficulty 0. *Ceaseless Pursuit:* on each of his turns the Pursuer draws and resolves two behaviour cards, one after the other; the second card's weak arcs apply to character attacks until his next turn. *Heat-up:* shuffle one random heat-up card into his behaviour deck as usual; from then on every attack value on his behaviour cards is increased by one.
  >
  > **Hungry Mimic and Voracious Mimic (mini-boss).** Mimics are fought as mini-boss encounters with these differences. Mimics have no arcs; their behaviour cards show no attack arcs or weak arcs and the weak-arc bonus is never gained. Mimics have no heat-up cards; when a mimic's health is reduced to or below its heat-up point, shuffle one random unused behaviour card into its behaviour deck. *Loot the Body:* when a mimic is slain, the characters receive two treasure cards of the current tier instead of the single card the chest held. See Mimics.
  >
  > ## Tomb of Giants Set
  >
  > **Black Knight (mini-boss) and Gravelord Nito (main-boss).** Use the data and behaviour cards from the Community Update Pack. No rules beyond the data card.
  >
  > ## Black Dragon Kalameet Expansion (mega-boss)
  >
  > **Components.** Kalameet's data card, health dial, thirteen behaviour cards (ten standard, two signature — *Mark of Calamity* and *Hellfire Blast* — and one heat-up card, *Hellfire Barrage*), eight strafe cards, two treasure cards, four *calamity* tokens, four Level 4 encounter cards and the mega-boss game board.
  >
  > **Setup.** Place the characters on the entry nodes beside the doorway, no more than three to a node, and give the aggro token to the character with the highest *threat*. Place Kalameet on the mega-boss spawn node with its front arc facing the centre of the game board. Build the behaviour deck: take four random standard behaviour cards, add the two signature cards, and shuffle these six together face down. Set the heat-up card aside. Shuffle the eight strafe cards and place them face down beside the behaviour deck.
  >
  > **Special ability — Calamity & Ruin.** Kalameet's behaviour deck always contains *Mark of Calamity* and *Hellfire Blast*. Attacks marked with the *calamity* icon place a *calamity* token on each character hit; the token's effect is given in Combat Basics › Conditions.
  >
  > **Heat-up.** When Kalameet's health is reduced to or below its heat-up point, shuffle *Hellfire Barrage* into the behaviour deck.
  >
  > **Strafe attacks.** The strafe icon is a magical attack that targets particular nodes instead of arcs. To resolve it: remove Kalameet from the game board, leaving any models that shared its node where they are; reveal the top strafe card; resolve the attack, at the value shown on the behaviour card, against every character on the nodes marked on the strafe card, each defending separately; discard the strafe card; then place Kalameet on the landing node shown on the strafe card, keeping its previous facing. Any character on the landing node is pushed to an adjacent node of that player's choice. If the strafe deck is empty when a strafe icon is resolved, turn its discard pile face down without shuffling to form the new strafe deck, then continue.
  >
  > ## Executioner's Chariot Expansion (mega-boss)
  >
  > **Components.** The Chariot's data card (two-sided), health dial, two models (the skeletal horse and the chariot), four track behaviour cards numbered 1 to 4, nine standard behaviour cards, three heat-up cards, a mega-boss setup card, two treasure cards, two Black Hollow Mages and four Falchion Skeletons with their data cards, four Level 4 encounter cards, six Level 1–3 encounter cards and the mega-boss game board.
  >
  > **The game board.** The centre of the Chariot's game board is not a node, and nodes are not adjacent across it. Treat the centre as a node containing a gravestone.
  >
  > **Setup.** Place the characters on the entry nodes beside the doorway, no more than three to a node, and give the aggro token to the character with the highest *threat*. Place both Chariot models together on the mega-boss spawn node and place the Black Hollow Mages and Falchion Skeletons on the enemy spawn nodes shown on the mega-boss setup card. Build two decks. The track deck: the four track behaviour cards in numerical order, card 1 on top, face down, not shuffled. The heat-up deck: four random standard behaviour cards and one random heat-up card, shuffled together face down and set aside.
  >
  > **Before heat-up — Death Race.** The Chariot's data card shows no starting health, block or resist on its front side. The Chariot cannot be attacked or damaged. After each character's turn, the Chariot and every other enemy on the board take a turn in descending *threat* order; the Chariot's turn is the top card of the track deck. To resolve a track behaviour card: move both Chariot models to the node shown, with the front arc facing away from the node they left; then make the card's physical attack against every character on the nodes marked on the card, including the node the Chariot left and the node it moved to, each defending separately; then push each character hit onto an adjacent node that is not marked on the card. Enemy models on marked nodes are pushed in the same way but suffer no damage. When the track deck is empty at the start of the Chariot's turn, turn its discard pile face down without shuffling to form the new track deck.
  >
  > **Raise Skeleton.** When a Black Hollow Mage resolves the Raise Skeleton icon, if fewer enemies with "Skeleton" in their name are on the board than there were at the start of the encounter, choose one defeated skeleton and place it, with no wound tokens, on the enemy spawn node closest to the Mage; if several spawn nodes are equally close, the players choose.
  >
  > **Heat-up — Chariot Crash.** When every Black Hollow Mage and Falchion Skeleton has been defeated, the Chariot heats up at once: remove the chariot model from the board, leaving the skeletal horse; flip the data card to its heat-up side, which shows the horse's starting health, block and resist; set the health dial to that starting health; and replace the track deck and its discard pile with the heat-up deck. The encounter continues as an ordinary boss encounter against the skeletal horse. The horse does not heat up again.
  >
  > **Special ability after heat-up — Crush.** When a character's block or resist roll prevents all of the damage of an attack from one of the horse's behaviour cards, that character suffers one damage.
  >
  > ## Mega-bosses Without Supplied Rules
  >
  > [Editor: the following entries are BLOCKED — source booklet not supplied. Each is to be drafted in the structure used above (Components · Setup · Special ability · Heat-up · Unique icons) once its booklet is available.] A boss whose rules are not yet given here is played from its data card and the general boss rules.
  >
  > **The Four Kings (mega-boss, The Four Kings expansion).** BLOCKED. Known requirement: multiple boss models; the rule for two boss models in one encounter applies.
  >
  > **Gaping Dragon (mega-boss, Gaping Dragon expansion).** BLOCKED. Known requirement: *corrosion* condition (Combat Basics › Conditions).
  >
  > **Guardian Dragon (mega-boss, Guardian Dragon expansion).** BLOCKED.
  >
  > **Manus, Father of the Abyss (mega-boss, Manus expansion).** BLOCKED.
  >
  > **Old Iron King (mega-boss, Old Iron King expansion).** BLOCKED.
  >
  > **Vordt of the Boreal Valley (mega-boss, Vordt expansion).** BLOCKED. Known requirement: *frostbite* condition.
  >
  > **The Last Giant (mega-boss, The Last Giant expansion).** BLOCKED. Not listed in Game Components › Mega-bosses; see CMP-0008.
  >
  > **Crossbreed Priscilla (main-boss) and Heavy Knight (mini-boss), Painted World of Ariamis.** BLOCKED. Use the data and behaviour cards from the Community Update Pack; no further rules are available.

  Consequential edit to Setup › Setup After the main-boss step 11 (line 1195): replace "employing any special rules described in the mega-boss rule booklet" with "employing the rules for that mega-boss given in Boss Special Rules".
- Design rationale: Every drafted rule is taken from a supplied booklet and recast in the manuscript's turn structure (the Chariot's "enemy activation" becomes the enemy turn that follows each character's turn; the aggro token goes to the highest-threat character as the manuscript requires rather than to "one of the characters"). Two official steps are deliberately dropped because the manuscript's own design supersedes them: the per-gravestone reveal of behaviour cards at boss setup (the manuscript's Gravestones rule awards a scry on clearing instead) and the official Calamity removal-on-damage (the manuscript's Conditions chapter keeps Calamity to the end of the encounter). Artorias, Smelter Demon, Old Dragonslayer, Pursuer and the Mimics are drafted from explicit booklet or card text. Sif's cool-down and O&S's pairing live on data cards that were not supplied, so the entries state the boundary rather than invent. The Twin Gargoyles rule is an adaptation of the Core campaign footnote to the manuscript's boss-death sequence and is tagged.
- Mechanical impact: Kalameet and the Chariot become playable from this book alone. The Pursuer's double activation and the Chariot's unattackable first phase are significant difficulty rules now stated. The "two boss models" rule generalises the manuscript's existing boss-pushes-boss text.
- Follow-on changes required: Add strafe cards, track behaviour cards, mega-boss setup card, pillar tokens and Level 4 encounter cards to Game Components (CMP-0012). Add "The Last Giant" to Game Components › Mega-bosses or remove it from Big Game Hunting (CMP-0008). Obtain the missing booklets to unblock nine entries. Delete the empty heading at line 2215.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0017] BOSS SPECIAL RULES › Wind Up — Scope — Proposed Completion
- Current state: "Wind Up" (lines 2211–2213) is a sub-section under "Asylum Demon & Stray Demon", but its text describes a behaviour icon generically ("When the Wind Up behaviour icon is resolved…"). Whether any other boss uses the icon cannot be verified: the Asylum Demon booklet was not supplied.
- Proposed completion: Keep the rule under Asylum Demon & Stray Demon (as in CMP-0005) and add one sentence: "The Wind Up icon appears on the Asylum Demon's and Stray Demon's behaviour cards. If it appears on any other behaviour card, resolve it in the same way." Add the Glossary entry "Wind Up" (CMP-0002).
- Design rationale: The rule is written as an icon rule and is harmless if generalised; the added sentence keeps it findable under the only bosses known to use it while covering any other card.
- Mechanical impact: None.
- Follow-on changes required: None. BLOCKED only for confirming other users of the icon (Asylum Demon booklet).
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

