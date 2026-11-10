# Drafting pack — chapter 18 (campaign_play) — manuscript chapter "CAMPAIGN PLAY"

Source text: `work/phase2a/source/18_campaign_play.md` (manuscript.md lines 2217–2349).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 2217.
- **Setup** · present — contradiction · line 2219. Claims "three campaigns, all three sections long"; body has 13 campaigns, 3–6 sections.
- **The Fog Gate** · present — to audit · line 2227.
- **Sparks** · present — to audit · line 2231.
- **Adding & Dropping Players** · present — to audit · line 2237.
- **Encounter Soul Rewards** · present — TOC mismatch · line 2241. TOC calls it "Encounter Rewards".
- **Campaign Soul Reward Table** · present — to audit · line 2247.
- **Encounter Treasure Rewards** · present — TOC mismatch · line 2287. Not in TOC.
- **The Bonfire Tile** · present — to audit · line 2295.
- **Stat Tier Costs** · present — to audit · line 2299.
- **(empty heading)** · ORPHAN — delete · line 2308: empty H3 used as page break
- **Blacksmith Andre's Shop** · present — to audit · line 2310.
- **(empty heading)** · ORPHAN — delete · line 2324: empty H3 used as page break
- **Shop Price Table** · present — to audit · line 2326.
- **(empty heading)** · ORPHAN — delete · line 2336: empty H3 used as page break
- **Bonfire Ascetic** · present — TOC mismatch · line 2338. Not in TOC.
- **Transposition** · present — to audit · line 2344.

## Audit findings mapped to this chapter (59)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-053 · undefined-state · Blocker · REQUIRED
- Location: GAMEPLAY › Souls (manuscript.md line 1391); Soul Reward Table (lines 1401–1439); Encounter Resolution (line 1327); Campaign Soul Reward Table (lines 2247–2285)
- Evidence: manuscript.md:1321–1327, 1389–1391, 1401–1439, 2245, 2247–2285
- Current text: Upon successfully clearing an encounter that has been previously cleared, reward the reduced soul reward to each character.
- Proposed fix: The reduced soul reward is half of the full soul reward, rounded up. Add a 'Reduced reward' column to both soul reward tables: basic 2 / 2 / 3 / 3 (Level 1–4), campaign 1 / 2 / 2 / 3.
- Rationale: The tables have a single column; 'reduced' is never quantified, so repeated encounters (a core loop the manuscript explicitly allows at 1321 and 2245) have no payout. Alternative: full reward minus two, minimum one (basic 1/2/3/4, campaign 1/1/2/3).
- Gameplay impact: Every repeated encounter is unresolvable.
- Decision needed: Y

### B-031 · scaling · Blocker · REQUIRED
- Location: L2342-2344 (Bonfire Ascetic) with L1527-1529 (Enemy Scaling)
- Evidence: 'This effect is cumulative with stat scaling for character count.' Hollow Soldier (Core p.20, attack 4) in a 4-character campaign after the Ascetic: attack 6 with Repeat 2. Expected damage per activation vs 2 black block dice = 2 x 3.67 = 7.33 of an 8-box bar; P(kill a full-health character in one activation) = 0.444; P(kill a hollow character) = 0.914. An icon-key 5-attack enemy (Core p.25) becomes 7 x2 = 9.33 expected, lethal to a full bar on average. At 3 characters: attack 6, 3.67 per activation.
- Current text: After the bonfire ascetic has been burnt, all non-boss enemies increase their attack damage by one for the remainder of the campaign. This effect is cumulative with stat scaling for character count.
- Proposed fix: "After the bonfire ascetic has been burnt, all non-boss enemies increase their base health by two for the remainder of the campaign. This increase is cumulative with the health scaling for character count. Enemy attack values are not changed."
- Rationale: A second +1 attack on top of player-count scaling pushes every ordinary enemy past what the two-highest-dice block cap can absorb; a health increase lengthens fights without making single activations lethal and matches the 'stronger enemies' flavour.
- Gameplay impact: 4-player post-Ascetic Hollow Soldier: health 6 instead of 4, expected damage per activation 2.67 (if B-003 is adopted) instead of 7.33.
- Decision needed: Y

### C-068 · table-text · Blocker · REQUIRED
- Location: L1389; L1391; L1401-1439; L2243
- Evidence: Souls: 'reward the full *soul* reward' for a first clear (1389) and 'the reduced *soul* reward' for a repeat clear (1391); the Soul Reward Table has a single column (3/4/5/6) and no reduced value; Campaign table is simply basic minus one (2/3/4/5) and L2245 says repeats reward souls 'just as in the basic game'
- Current text: the reduced *soul* reward
- Proposed fix: Either add a 'Repeat clear' column to both tables (author decision on values) or delete 'reduced' and pay the full reward on repeats; then rewrite L1391 and L2245 to match.
- Rationale: A rule references a value that exists nowhere.
- Gameplay impact: Soul income on every repeated encounter is undefined
- Decision needed: Y

### A-001 · undefined-state · Major · REQUIRED
- Location: RETURNING TO THE BONFIRE › Resting at The Bonfire (manuscript.md line 1906)
- Evidence: manuscript.md:1890, 1906, 1223, 1305, 2235
- Current text: Resting at the bonfire also revives lost characters who have been removed from play due to dying while hollow.
- Proposed fix: A character who dies while hollow is lost. A lost character's model is placed on its side beside the bonfire tile and takes no further part in the encounter. When a character is lost, the encounter is failed immediately and the characters must rest at the bonfire. Resting at the bonfire revives all dead and lost characters.
- Rationale: The term 'lost' appears at lines 1890, 1906 and 2235 but is never defined. Death & Hollowing (1223) already forces an immediate rest when a hollow character dies, so 'lost' is a transient state that must be named once and added to the glossary.
- Gameplay impact: Players cannot tell whether a lost character differs from a dead one or whether lost characters return after a free (post-boss) rest.
- Decision needed: N

### A-028 · undefined-state · Major · REQUIRED
- Location: SUMMONS › Invader Encounter Setup step 3 (manuscript.md line 2019); CRYSTAL LIZARDS (line 2055); Enemy Scaling (line 1521)
- Evidence: manuscript.md:1521–1529, 2019, 2055, 2342; DS-Phantoms-Rules-lores.txt p.12; DS-IronKeep-Rules-Web.txt p.5
- Current text: Invaders do not multiply their health by the number of characters like other enemy models.
- Proposed fix: Invaders and crystal lizards are never modified by enemy scaling or by the bonfire ascetic.
- Rationale: Both exemptions cover health only; invaders are 'non-boss enemies' and would otherwise gain +1 attack and Repeat 2, and crystal lizards would gain movement 1→2, which defeats the chase. The bonfire ascetic (2342) already exempts invaders from +1 attack, which shows the intent. Alternative: invaders receive attack scaling but not health scaling.
- Gameplay impact: A Repeat-2 invader with +1 attack acting after every character turn is lethal at four players.
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

### A-057 · contradiction · Major · REQUIRED
- Location: SETUP › Encounter cards step 4 (manuscript.md line 1135) and Setup After the mini-boss step 8 (line 1163) vs Treasure Rewards (line 1451)
- Evidence: manuscript.md:1135, 1163, 1313, 1445–1451, 2291–2293, 2340
- Current text: Deal one tier one treasure per character face-down to each encounter tile. / Draw cards from the Tier one treasure deck before defeating the mini-boss, and Tier two treasure deck thereafter.
- Proposed fix: The treasure cards dealt face-down to an encounter tile during setup are that encounter's treasure reward. When the encounter is cleared for the first time, each character takes one of those cards; the cards are not drawn from the deck at that time. In campaign play, treasure cards already dealt to tiles are not replaced when the bonfire ascetic is burnt.
- Rationale: Setup pre-deals one card per character to every tile, yet Treasure Rewards says to draw from the deck on clearing; a party would collect both. The pre-deal is the only reading under which 'Characters receive their treasure card reward even if they died' and the campaign tier rules (2291) are mechanical. Alternative: delete the pre-deal steps and draw on clearing.
- Gameplay impact: Doubles treasure income if both are applied.
- Decision needed: Y

### B-007 · arithmetic · Major · REQUIRED
- Location: L1923 (Stat Tier Costs, basic)
- Evidence: Tier Three 8 and Tier Four 8 are equal; every other cost progression is strictly increasing. The campaign table (L2303-2306) is exactly double the basic row for Tiers One-Three (4/8/16) and gives Tier Four 20, implying basic Tier Four = 10. Cumulative basic cost one stat: 2/6/14/22 as written, 2/6/14/24 with 10.
- Current text: | Tier Four  | **8**           |
- Proposed fix: | Tier Four  | **10**          |
- Rationale: Preserves the author's own 1:2:4:5 ratio between the basic and campaign tables; 16 (doubling) would cost 30 cumulative, 68% of a character's whole-game income (44 souls), and would never be bought.
- Gameplay impact: Tier Four costs 24 cumulative (55% of basic income) instead of 22; reaching it remains a deliberate end-game choice.
- Decision needed: Y

### B-011 · economy · Major · PROPOSED
- Location: L2301-2306 with L2247-2280 (Campaign Stat Tier Costs and Campaign Soul Reward Table)
- Evidence: First Journey (Core p.35 structure) under the campaign table yields about 55 souls per character over three sections; one stat to Tier Three costs 28 (51% of all income), Tier Four 48 (87%), four stats to Tier Three 112 (204%). The campaign both halves the per-encounter reward relative to level (2/3/4/5 vs 3/4/5/6) and doubles level costs.
- Current text: | Tier Three | **16** | / | Tier Four | **20** | (campaign) and campaign rewards 2/3/4/5
- Proposed fix: Keep the campaign reward table at the basic values (3 / 4 / 5 / 6) and retain the doubled stat costs; or keep 2 / 3 / 4 / 5 and set campaign Tier Three to 12 and Tier Four to 16.
- Rationale: Two simultaneous halvings make a three-session campaign end with most characters at Tier Two in one stat, below where the basic game ends after one session; one lever is enough to slow progression.
- Gameplay impact: With basic rewards the campaign total rises to about 73 per character: one stat to Tier Three plus a second to Tier Two plus two tier-two cards, i.e. one full tier beyond the basic game across three sessions.
- Decision needed: Y

### B-013 · balance · Major · PROPOSED
- Location: L2233-2239 (Campaign Sparks; Adding & Dropping Players)
- Evidence: Campaign maximum = starting sparks (4 players: 2). A boss defeated at a full dial gives nothing. Adding a fourth player to a three-player party holding 1 spark leaves 0 sparks with a maximum of 2. Official 1E campaign (Core p.33) allowed buying a spark for 2 souls per character up to the maximum; the manuscript forbids any purchase.
- Current text: The starting number of sparks also serves as the maximum number of sparks. ... Sparks cannot be purchased or gained otherwise. ... New players can join a campaign that is in progress at the cost of one spark each.
- Proposed fix: "The maximum number of sparks is the starting number plus one. While resting at the bonfire the characters may buy one spark for four souls per character, up to the maximum. A new player may join only while the spark dial shows at least two."
- Rationale: Restores the official pressure valve at double the official price (consistent with the manuscript's doubled prices) and removes the two degenerate states.
- Gameplay impact: A four-player campaign can hold up to 3 sparks and can convert about 16 souls into a rest when a section goes badly.
- Decision needed: Y

### C-033 · italics · Major · REQUIRED
- Location: L1399; L1890; L1906; L2235; L1397; L1277; L3056; L2175; L2017; L1985
- Evidence: Undefined keywords: '*lost*' used at 1890/1906/2235 ('lost to the hollow', 'revives lost characters who have been removed from play due to dying while hollow') but never defined and conflicts with L1223 (hollow death forces a rest, no removal) and L1195 (mega-boss death = permanent removal); 'mastering the encounter' (1397) undefined; '*first player* token' (1277) placed but never used and not a component; 'First turn token' (3056) different name for same thing; boss '*leaps*' (2175) icon undefined; 'Heat Up value' for invaders (2017) undefined on invader cards; 'entrance node' (1985)
- Current text: lost / mastering / first player token / leaps
- Proposed fix: Define *lost* once (proposed: 'A character who dies while *hollow* is *lost*: remove the model from play until the party next rests at the *bonfire*'), then make L1223, L1906 and L1195 agree; delete 'mastering'; either define the first player token's effect or delete L1277 and use 'first player' in PvP only; define *leap*; use 'entry node'.
- Rationale: A term used as a keyword must be defined once.
- Gameplay impact: Whether a hollow character's death removes it from play or ends the encounter
- Decision needed: Y

### C-048 · terminology · Major · REQUIRED
- Location: L1393; L805; L891; L919; L2239; L989; L1095
- Evidence: 'Successfully defeated invaders provide additional *souls* per player' (1393) vs Soul Reward Table 'per character' (1411); 'when that player discards an ember card' (805); 'stored in a player's inventory' (891); 'characters must choose a friendly model to push' (919 - a decision); 'If a player character leaves the characters' (2239). Note L989 'character dashboard(s)' and L1095 'character model(s)' allow one player to control several characters.
- Current text: per player / that player / player's inventory / characters must choose
- Proposed fix: Rule of use: PLAYERS decide, agree, choose and roll; CHARACTERS act, hold tokens, own cards and inventories, gain souls and die; MODELS occupy nodes, move and are pushed. L1393 -> 'per character'; L805 -> 'when that character discards'; L891 -> 'a character's inventory'; L919 -> 'the players must choose a friendly model to push'; L2239 -> 'If a player leaves, remove their character...'
- Rationale: When one player controls two characters, 'per player' and 'per character' pay different soul rewards.
- Gameplay impact: Soul rewards for invaders in 1-2 player games
- Decision needed: N

### C-070 · table-text · Major · REQUIRED
- Location: L1951-1957; L2326-2334; L2348; L1025; L2322
- Evidence: Basic Shop Price Table: Boss Treasure purchase 'N/A', sell 6. Campaign table: Boss Treasure purchase '-', sell 4; extra rows 'Legendary Shop: 4 + Boss Treasure / sell 4' and 'Bonfire Ascetic 16 / -'. Prose: transposition costs a boss treasure + four souls (2348, matches); bonfire ascetic 16 souls (2293/2316/2340, matches); L2322 'Legendary Treasures are now only available through transposition' but the table calls it a 'Shop'; legendary sell value 4 appears nowhere in prose.
- Current text: Boss Treasure sell 6 (basic) vs 4 (campaign); 'N/A' vs '-'; 'Legendary Shop'
- Proposed fix: Confirm whether the campaign boss-treasure sell value (4) is a deliberate change; if so state it in §Blacksmith Andre's Shop (campaign); use one null marker ('-') in both tables; rename row 'Legendary (transposition)'; add a prose line for selling legendary treasure or delete the sell value.
- Rationale: Tables must agree with prose and with each other except where a change is stated.
- Gameplay impact: Boss treasure sale income differs by 2 souls between modes
- Decision needed: Y

### C-071 · table-text · Major · REQUIRED
- Location: L1918-1923; L2301-2306; L1914
- Evidence: Basic Stat Tier Costs: 2 / 4 / 8 / 8 (Tier Four = Tier Three). Campaign: 4 / 8 / 16 / 20. Prose example L1914 'pay two souls to reach tier one before paying four additional souls to reach tier two' matches the basic table.
- Current text: Tier Four **8**
- Proposed fix: Probable error: Tier Four 16 (doubling pattern), or state explicitly that tier four costs the same as tier three. Author decision.
- Rationale: Repeated value breaks the progression and differs in shape from the campaign table.
- Gameplay impact: Cost of the final stat tier
- Decision needed: Y

### C-074 · table-text · Major · REQUIRED
- Location: L2223; L2225; L2350-3034
- Evidence: L2223 'the included campaigns are all three sections long'; L2225 'This rule-set includes three campaigns which require only the components available in the core set' vs CAMPAIGNS chapter: 13 campaigns, 3 to 6 sections each, of which 2 are core-only (The First Journey, The Coiled Sword)
- Current text: all three sections long; three campaigns which require only the... core set
- Proposed fix: 'The included campaigns are three to six sections long.' / 'Two campaigns require only the core set; the others require the expansions listed in each campaign's requirements line.'
- Rationale: Introductory prose contradicts the chapter it introduces.
- Gameplay impact: None
- Decision needed: N

### C-119 · voice · Major · REQUIRED
- Location: L1205-1253; L1299-1399; L1445-1479; L1935-1949; L859-887; L931-981; L1604-1658; L2243-2293; L2314-2322; L3040-3094
- Evidence: Rules stated as bullet fragments: Death & Hollowing, Embering, Sparks (1205-1253); Encounter Resolution/Recovery, Souls (1299-1399); Treasure Rewards (1445-1479); Shop Rules (1935-1949); Spells (859-887); Terrain (931-981); Conditions (1604-1658); campaign Soul/Treasure Rewards and Shop (2243-2322); the whole PLAYER VS PLAYER chapter (3040-3094) is 27 bullets with no sentence structure
- Current text: - Encounters are *failed* if either all characters die.
- Proposed fix: Policy: PROCEDURES (setup, turn sequence, defence rolls, encounter start, resting, transposition) = numbered steps; DEFINITIONS and component anatomies (dashboard parts, data-card fields, condition effects, terrain) = bulleted lists of complete sentences; RULES (everything else) = short declarative paragraphs in 'When [trigger], [subject] must/may [action].' form. Rewrite PvP as prose plus a dodge table.
- Rationale: Fragments omit the trigger and subject that lawbook syntax requires ('Encounters are failed if either all characters die' has a dangling 'either').
- Gameplay impact: None
- Decision needed: Y

### F-036 · tone · Major · CLEAN-UP
- Location: L2221 §Campaign Play › Setup ¶1
- Evidence: Advisory sentence: 'Campaigns provide a more challenging and longer play experience suitable for players who have played the basic game at least a few times..'
- Current text: Campaigns provide a more challenging and longer play experience suitable for players who have played the basic game at least a few times..
- Proposed fix: CUT (or move to the chapter intro as: 'A campaign is a longer adventure of several sections, each ending in a boss.')
- Rationale: Audience advice; double full stop.
- Gameplay impact: none
- Decision needed: N

### F-037 · meta-commentary · Major · CLEAN-UP
- Location: L2223 §Campaign Play › Setup ¶2
- Evidence: Session advice and an inaccurate statement: 'Players might expect to meet over multiple play sessions… the included campaigns are all three sections long.' (Campaigns in §19 run three to six sections.)
- Current text: Players might expect to meet over multiple play sessions to complete a campaign. A single section of a campaign might serve as a convenient amount of content to cover in a session. While campaigns can vary in length, the included campaigns are all three sections long.
- Proposed fix: CUT
- Rationale: Logistics advice; the factual claim is also wrong (Demon Hunting has five sections, The Undead Colosseum six).
- Gameplay impact: none
- Decision needed: N

### F-038 · external-reference · Major · CLEAN-UP
- Location: L2225 §Campaign Play › Setup ¶3
- Evidence: Self-reference to 'this rule-set' and reference to expansion campaign content: 'This rule-set includes three campaigns which require only the components available in the core set. Many of the game's expansions also add additional campaigns for selection.'
- Current text: When starting a campaign, the players must first choose one of the available campaigns. This rule-set includes three campaigns which require only the components available in the core set. Many of the game's expansions also add additional campaigns for selection.
- Proposed fix: REWRITE-IN-VOICE: 'The party chooses a campaign from §19. Each campaign lists the components it requires.'
- Rationale: Expansion rulebooks are not a source in this book; §19 already lists twelve campaigns, so 'three' is also stale.
- Gameplay impact: none
- Decision needed: N

### F-040 · meta-commentary · Major · CLEAN-UP
- Location: L2297 §Campaign Play › The Bonfire Tile
- Evidence: Design rationale: 'essentially unchanged from the basic rules… The cost to level up stats at the Firekeeper is increased in Campaign play to slow the characters' progression to scale better across a longer journey.'
- Current text: The rules for returning to the *bonfire* are essentially unchanged from the basic rules… The cost to level up stats at the Firekeeper is increased in Campaign play to slow the characters' progression to scale better across a longer journey. Characters may now also transpose boss items and burn bonfire ascetic.
- Proposed fix: REWRITE-IN-VOICE: 'The *bonfire* rules of §11 apply in a campaign with the following changes. Stat tier costs are those in the table below. Characters may also transpose boss treasure (§18.8) and burn a bonfire ascetic (§18.7).'
- Rationale: 'to slow progression … scale better' is rationale; 'essentially' is a hedge.
- Gameplay impact: none
- Decision needed: N

### F-041 · meta-commentary · Major · CLEAN-UP
- Location: L2312 §Campaign Play › Blacksmith Andre's Shop
- Evidence: Design rationale: 'functions similarly to the basic rules with some changes to how the shop is stocked to better suit the progression of the campaign.'
- Current text: Andre's Shop functions similarly to the basic rules with some changes to how the shop is stocked to better suit the progression of the campaign. Use the basic rules for Andre's Shop with the following modifications.
- Proposed fix: REWRITE-IN-VOICE: 'The shop rules of §11.4 apply in a campaign with the following changes.'
- Rationale: Rationale removed; one sentence.
- Gameplay impact: none
- Decision needed: N

### F-086 · register-shift · Major · CLEAN-UP
- Location: L919, L1461, L1479, L2043, L1245 vs L2233, L1201, L1107
- Evidence: Actor shifts between 'players' and 'characters' for the same kind of decision: 'the players must push one of the three models… characters must choose a friendly model' (L919); 'Players decide which character should receive' (L1461) vs 'Characters must collectively decide' (L2043); 'Players begin sparks equal to' (L1245) vs 'The characters start a campaign with the same number of sparks' (L2233).
- Current text: Multiple models can share the same node… the players must push one of the three models already on the node. characters must choose a friendly model to push…
- Proposed fix: Apply the actor policy (Voice Guide §3): characters act in the game world (move, attack, spend, die); players make rules decisions where the game asks for a human choice; 'the party' for a collective decision. E.g. L919: 'If a fourth model enters a node, the party chooses a friendly model to push; an enemy pushes another enemy if able.'
- Rationale: Clarity of who acts; also removes the lower-case sentence starts ('characters must…' L919, L1931, L2069, L2155, L2185, L2207).
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

### A-025 · undefined-state · Minor · OPTIONAL
- Location: COMBAT BASICS › Enemy Scaling (manuscript.md line 1527); CAMPAIGN PLAY › Bonfire Ascetic (line 2342)
- Evidence: manuscript.md:1527, 1594, 1702, 2342
- Current text: If playing with three or more characters, increase all non-boss attack values by one.
- Proposed fix: Attack value increases from scaling and from the bonfire ascetic apply to every attack icon and to the damage value of push-movements.
- Rationale: Push-movement damage (1702) is a number inside a movement icon, not an 'attack value'; the scaling text does not say whether it is increased. Alternative: push-movement damage is never modified.
- Gameplay impact: Trampling enemies (Sentinel, Smelter-type) are the ones where the +1 matters most.
- Decision needed: Y

### A-027 · undefined-state · Minor · OPTIONAL
- Location: CAMPAIGN PLAY › Adding & Dropping Players (manuscript.md line 2239) vs Enemy Scaling (line 1523)
- Evidence: manuscript.md:1523, 2239; DS-Core-Rules-lores.txt p.33
- Current text: If a player character leaves the characters, the characters gain one spark, the character's equipment is added to the inventory, and the maximum number of sparks is changed...
- Proposed fix: A character who has left the campaign is not counted for enemy scaling, per-character rewards, shop ember cards or the spark maximum from the moment the player leaves. A new character is counted from the moment the player joins.
- Rationale: Scaling counts 'dead characters' but nothing addresses departed ones; per-character treasure already dealt to tiles also changes count.
- Gameplay impact: Prevents a dropped player inflating enemy health for the rest of the section.
- Decision needed: N

### A-047 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Sparks (manuscript.md lines 1247–1253); Boss Death (line 2195)
- Evidence: manuscript.md:715, 1093, 1249, 2195, 2233; DS-Core-Rules-lores.txt p.33 (campaign maximum = starting sparks)
- Current text: Defeating a mini-boss or main-boss provides one additional spark.
- Proposed fix: The spark dial never shows more sparks than the characters' starting number; a spark gained beyond that maximum is lost.
- Rationale: The campaign chapter sets this maximum (2233) but the basic game does not; a solo character would reach six or seven, beyond the physical dial. Alternative: no maximum, track overflow with a token.
- Gameplay impact: Solo and two-character basic games only.
- Decision needed: Y

### A-051 · contradiction · Minor · REQUIRED
- Location: CAMPAIGN PLAY › Transposition (manuscript.md line 2346)
- Evidence: manuscript.md:1169, 2235, 2346
- Current text: Transposition is only available after the characters spend a spark to rest at the bonfire.
- Proposed fix: Transposition is available whenever the characters rest at the bonfire after the final boss of the first section has been defeated, whether or not a spark was spent for that rest.
- Rationale: The rest that immediately follows a section's final boss is free (2235, 1169), so the literal text denies transposition at the first moment it is unlocked.
- Gameplay impact: Delays the first legendary purchase by one spark for no evident reason.
- Decision needed: N

### A-064 · terminology · Minor · CLEAN-UP
- Location: CAMPAIGN PLAY › Bonfire Ascetic (manuscript.md line 2342)
- Evidence: manuscript.md:1519, 1878, 2342
- Current text: This effect is cumulative with stat scaling for character count.
- Proposed fix: This effect is cumulative with enemy scaling for character count.
- Rationale: 'Stat scaling' is the weapon rule at line 1878; the intended cross-reference is Enemy Scaling.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-067 · arithmetic · Minor · REQUIRED
- Location: RETURNING TO THE BONFIRE › Stat Tier Costs (manuscript.md lines 1918–1923) vs Campaign Stat Tier Costs (lines 2301–2306)
- Evidence: manuscript.md:1914, 1918–1923, 2301–2306; DS-Core-Rules-lores.txt p.15 (2/4/8), p.33 (campaign 4/8/16/20); Hollowed_Edition_v1.3.txt p.3 (2/4/6/8)
- Current text: Tier Three 8 / Tier Four 8
- Proposed fix: Tier Four: 16 souls.
- Rationale: Tier four costing the same as tier three breaks the doubling pattern that the campaign table (4/8/16/20) follows. Alternative: 2/4/6/8 as in Hollowed Edition.
- Gameplay impact: Tier four is the strongest upgrade; mispricing it drives stat inflation.
- Decision needed: Y

### A-077 · undefined-state · Minor · OPTIONAL
- Location: RETURNING TO THE BONFIRE › Shop Rules (manuscript.md line 1941)
- Evidence: manuscript.md:1937, 1941, 1957, 2332
- Current text: Sold items are placed at the bottom of their respective treasure deck.
- Proposed fix: Sold boss treasure and legendary treasure cards are returned to the game box; all other sold cards go to the bottom of the treasure deck of their tier.
- Rationale: Boss and legendary cards have no 'respective' deck.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-103 · contradiction · Minor · REQUIRED
- Location: CAMPAIGN PLAY › Setup (manuscript.md lines 2223–2225)
- Evidence: manuscript.md:2223, 2225, 2352–3034
- Current text: the included campaigns are all three sections long. ... This rule-set includes three campaigns which require only the components available in the core set.
- Proposed fix: This rule-set includes thirteen campaigns, of which two require only the core set; the others list their required expansions. Campaigns are between three and six sections long.
- Rationale: Thirteen campaigns are listed; two are core-only; lengths run from three to six sections.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-105 · undefined-state · Minor · OPTIONAL
- Location: CAMPAIGN PLAY › Adding & Dropping Players (manuscript.md line 2239)
- Evidence: manuscript.md:765, 1385–1387, 2239; DS-Core-Rules-lores.txt p.33
- Current text: New players can join a campaign that is in progress at the cost of one spark each. ... the character's equipment is added to the inventory
- Proposed fix: A new player may join only while the spark dial shows at least one spark. When a character leaves, their equipment cards are distributed among the remaining characters' inventories as the players choose, and their souls are returned to the supply.
- Rationale: The manuscript has personal inventories and personal souls (765, 1387), so the official communal-inventory sentence no longer resolves; joining at zero sparks is unaddressed.
- Gameplay impact: Rare.
- Decision needed: N

### B-034 · economy · Minor · PROPOSED
- Location: L2316, L2334, L2338-2340 (Bonfire Ascetic cost 16 shared)
- Evidence: 16 souls shared by 3 characters = 5.3 each, about 10% of the First Journey campaign income of ~55 per character; the party can burn the Ascetic during section 1 (17 souls per character earned) before any equipment upgrade, immediately triggering +1 enemy attack for the rest of the campaign.
- Current text: Characters may pay a communal one time fee to burn the bonfire ascetic to gain access to tier two treasures. A total of sixteen souls may be paid from any combination of character contributions while resting at the bonfire.
- Proposed fix: "Characters may pay a communal one-time fee of eight souls per character to burn the bonfire ascetic and gain access to tier two treasures. The ascetic may be burnt only after the final boss of the first section has been defeated."
- Rationale: Scales the fee to party size (a fixed 16 is 16 for a solo character but 4 each for four) and prevents the difficulty increase arriving before the party can use tier-two cards.
- Gameplay impact: Solo campaign pays 8 instead of 16; four-player campaign pays 32 instead of 16.
- Decision needed: Y

### C-023 · hedge · Minor · REQUIRED
- Location: L1017; L1021; L2223
- Evidence: 'might' x4: L1017/L1021 'to suggest which class might benefit most from its use'; L2223 'Players might expect to meet over multiple play sessions... A single section of a campaign might serve as a convenient amount of content'
- Current text: might
- Proposed fix: L1017/L1021: 'The emblem indicates the class for which the card is designed; it has no rules effect.' L2223: 'A campaign is designed for several sessions; one section is a convenient session.' (or delete as advice).
- Rationale: Speculation is not a rule; the only rule content is 'no gameplay difference'.
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

### C-045 · terminology · Minor · REQUIRED
- Location: L771; L1451; L2314; L2316; L1920-1923; L1955-1956; L2303-2306; L2330-2331; L689; L1914; L2299
- Evidence: 'tier one/two' lower-case x60 in prose; 'Tier One/Two' x10 in table and heading labels; 'Tier one/two' mid-sentence (1451, 2314, 2316). Separately, 'tier' has two senses: stat tier (771 'from base tier to tier two', 1914) and treasure tier (1013 'tier two treasure deck').
- Current text: Tier one treasure deck (mid-sentence); 'tier two' (stat sense) unqualified
- Proposed fix: Lower-case 'tier one/two' in prose; Title Case only in headings and table row labels. Always qualify the stat sense as 'stat tier' ('stat tier two') and the treasure sense as 'tier two' ('tier two treasure', 'tier two shop').
- Rationale: Ambiguity: L771 'tier two' means a stat tier while L1013 'tier two' means a treasure deck.
- Gameplay impact: Misreading stat tiers as treasure tiers
- Decision needed: Y

### C-053 · terminology · Minor · CLEAN-UP
- Location: L2221
- Evidence: 'each section of a scenario has varying numbers of exploration tiles' vs 'encounter tile' x47; also 'scenario' vs 'campaign'
- Current text: exploration tiles; scenario
- Proposed fix: encounter tiles; campaign
- Rationale: Official V1 term 'exploration tile' is not used anywhere else in the manuscript.
- Gameplay impact: None
- Decision needed: N

### C-058 · terminology · Minor · CLEAN-UP
- Location: L719; L1151; L1179; L2063; L2065; L2227; L2229
- Evidence: 'Fog Gate token' (719), 'fog-gate' (1151, 1179), 'fog gate' x11, 'the fog gate tile should be removed' (2065) vs 'fog gate token' (719, 2229)
- Current text: fog-gate / Fog Gate / fog gate tile
- Proposed fix: fog gate (lower-case, no hyphen); the component is the 'fog gate token'
- Rationale: One component, one name; it is a token not a tile.
- Gameplay impact: None
- Decision needed: N

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

### C-106 · punctuation · Minor · REQUIRED
- Location: L793; L2221; L2748; L2047
- Evidence: Double full stops: 'at the start of the game..' (793); 'at least a few times..' (2221); 'during encounter set-up..' (2748); '*cleared.*.' (2047)
- Current text: ..
- Proposed fix: Single full stop.
- Rationale: Typo.
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

### C-112 · punctuation · Minor · CLEAN-UP
- Location: L679; L895; L1199; L1203; L1710; L1766; L2161; L2201; L2237; L449; L2398
- Evidence: '&' in nine headings and in list items 'Mushroom Child & Parent' (449), 'Ornstein & Smough' (2398, 2500, 2660, 2934)
- Current text: &
- Proposed fix: 'and' in headings and prose; '&' only inside an official product or card name
- Rationale: Ampersand is a logo/label device, not prose.
- Gameplay impact: None
- Decision needed: N

### C-116 · punctuation · Minor · CLEAN-UP
- Location: L925; L1069; L1079; L1085; L1093; L1263; L1860; L1880; L1914; L2177; L2179; L2293; L2316; L2340; L1261
- Evidence: Numerals vs words mixed in prose: 'Range 0 / Range 1 / Range 2' (925); '3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells' (1069, 1079, 1085) vs 'two stamina cubes' (1261) and '6 stamina' (1263); 'six minus the number of characters' (1093); 'costs 0 Stamina' (1860); '5 greater' (1914); '90 degrees', '180 degrees' (2177-2179); '16 *souls*' (2293, 2316) vs 'sixteen souls' (2340). Number words in body: one x155, two x79, four x30, three x27, six x6, five x5, ten x3.
- Current text: 3 weapons ... 6 stamina ... sixteen souls ... 5 greater
- Proposed fix: Policy: words for zero to nine in running prose ('two stamina', 'three weapons'); numerals for 10 and above ('16 souls'), for every value in a table, for values with a sign or symbol ('+1', '≥ 25', '90°'), for dice counts beside icons, and for printed labels ('Level 1', 'Range 0'). Violations under this policy: 1069/1079/1085 (3, 3, 2, 2, 2 -> words), 1263 (6 -> six), 1860 (0 -> no), 1914 (5 -> five), 2340 (sixteen -> 16).
- Rationale: One policy; approximately 8 prose lines currently violate it.
- Gameplay impact: None
- Decision needed: Y

### C-120 · voice · Minor · REQUIRED
- Location: L1963; L2043-2047; L2055-2057; L2065; L2125; L2340; L2348; L1592-1594
- Evidence: Procedures written as long prose paragraphs: Resuming Exploration (1963); mimic chest procedure (2043-2047); crystal lizard spawn/escape (2055-2057); fog gate (2065); behaviour deck construction (2125); bonfire ascetic (2340); transposition 'First, ... Second, ... Third, ... Fourth, ...' (2348); push resolution (1592-1594)
- Current text: First, players gather all available legendary treasure cards... Second, ... Third, ... Fourth, ...
- Proposed fix: Numbered steps, one action per step.
- Rationale: Multi-step procedures are read at the table mid-game; numbered steps are scannable.
- Gameplay impact: None
- Decision needed: N

### F-039 · tone · Minor · CLEAN-UP
- Location: L2239 §Campaign Play › Adding & Dropping Players
- Evidence: Conversational lead-in (copied Core p.33): 'During campaign play, sometimes a new player would like to join the characters part way through or an existing player is required to leave.'
- Current text: During campaign play, sometimes a new player would like to join the characters part way through or an existing player is required to leave. New players can join a campaign that is in progress at the cost of one spark each…
- Proposed fix: REWRITE-IN-VOICE: 'A new character may join a campaign in progress while the party rests at the *bonfire*. The party spends one *spark* per character added. The new character begins with starting stats and equipment. A character who leaves returns one *spark* to the dial and adds their equipment to the party inventory. In either case the maximum number of *sparks* is recalculated.'
- Rationale: Narrative framing; procedure wanted.
- Gameplay impact: none
- Decision needed: N

### F-042 · tone · Minor · CLEAN-UP
- Location: L2304 §Campaign Play › Bonfire Ascetic ¶1
- Evidence: Advice: 'They must decide at what point their need for better equipment outweighs the cost of increased difficulty.'
- Current text: In campaign play, characters do not gain access to tier two treasures freely after defeating a boss. They must decide at what point their need for better equipment outweighs the cost of increased difficulty.
- Proposed fix: CUT second sentence.
- Rationale: Decision advice; the rule follows in the paragraph.
- Gameplay impact: none
- Decision needed: N

### F-043 · tone · Minor · OPTIONAL
- Location: L2306 §Campaign Play › Bonfire Ascetic ¶2
- Evidence: Flavour lead-in: 'However, burning the bonfire ascetic invites stronger enemies.'
- Current text: However, burning the bonfire ascetic invites stronger enemies. After the bonfire ascetic has been burnt, all non-boss enemies increase their attack damage by one for the remainder of the campaign.
- Proposed fix: CUT first sentence; begin: 'After the bonfire ascetic is burnt, every non-boss enemy adds one to its attack values for the rest of the campaign.'
- Rationale: Flavour inside a rule.
- Gameplay impact: none
- Decision needed: N

### F-053 · prose-crossref · Minor · CLEAN-UP
- Location: L2221, L2229, L2233, L2235, L2243, L2245, L2289, L2297, L2312, L3060
- Evidence: 'the basic game' / 'the basic rules' used ten times as if naming another book.
- Current text: …largely the same as the basic game… as it does in the basic game… just as in the basic game… as in the basic rules… essentially unchanged from the basic rules… Use the basic rules for Andre's Shop… unchanged from basic rules.
- Proposed fix: Adopt one term, 'the standard game', defined once in §18 intro: 'A campaign uses the rules of the standard game (§6–§17) except as stated in this chapter.' Then each occurrence becomes '(see §x.y)' or is deleted.
- Rationale: Consistent internal term plus § references; no implied second rulebook.
- Gameplay impact: none
- Decision needed: N

### C-044 · terminology · Note · CLEAN-UP
- Location: L1169; L1187; L1888; L1902; L1912; L2195; L2297
- Evidence: 'Firekeeper' x8, no variants; matches Core/TG rulebooks ('Firekeeper' x16)
- Current text: Firekeeper
- Proposed fix: No change
- Rationale: Consistent; record in style sheet.
- Gameplay impact: None
- Decision needed: N

### C-069 · table-text · Note · CLEAN-UP
- Location: L1401-1439; L2247-2285; L1411-1412; L2257-2258
- Evidence: Campaign Soul Reward Table (2/3/4/5) equals basic table (3/4/5/6) minus one, matching L2243 'reduced by one compared to the basic game'. Header text differs: 'per characteri' (1412, stray i) vs 'per character' (2258).
- Current text: per characteri
- Proposed fix: per character
- Rationale: Arithmetic verified consistent; header defect only.
- Gameplay impact: None
- Decision needed: N

### F-134 · copied-prose · Note · OPTIONAL
- Location: L2219–2221, L2233–2239 §Campaign Play › Setup / Sparks / Adding & Dropping Players
- Evidence: Matches official text — near-verbatim (L2239 68%, 34-word run; L2221 opening sentence)
- Current text: The setup for a campaign is largely the same as the basic game. However, each section of a scenario has varying numbers of exploration tiles… / Each time a mini-boss, main-boss, or mega-boss is defeated, the characters gain one spark… / During campaign play, sometimes a new player would like to join the characters part way through or an existing player is required to leave. New players can join a campaign that is in progress at the cost of one spark each…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.33. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (3) — approved at Gate 1

### [CMP-0006] Gameplay › Death & Hollowing — "Lost" state — Proposed Completion
- Current state: "Lost" is used but never defined: "keeping them from being *lost* to the *hollow*" (line 1890); "Resting at the *bonfire* also revives *lost* characters who have been removed from play due to dying while *hollow*" (line 1906); "The players lose the campaign if all characters are lost to the hollow without a *spark* to revive them" (line 2235). Death & Hollowing (line 1223) and Encounter Resolution (line 1305) say that when a *hollow* character dies the encounter is *failed* and the characters must spend a *spark* and rest. Setup After the main-boss step 11 (line 1195) says that in the mega-boss encounter "If a character dies they are permanently removed from play." Objective & Loss Conditions (line 1201) defines loss only as "all characters are dead and there are no remaining sparks".
- Proposed completion:

  New bullet group appended to Death & Hollowing (after line 1223):

  > - A *hollow* character who dies is *lost*.
  >
  >   - A *lost* character is removed from play: place the model on its side beside the *bonfire* tile, drop its *souls* on the encounter tile and discard its *ember* token as for any death.
  >
  >   - A *lost* character is not revived by *clearing* an encounter. A *lost* character is revived only when the characters rest at the *bonfire*; resting removes the *hollow* markers as usual.
  >
  >   - When a character becomes *lost*, the current encounter is *failed* at once and the characters must rest at the *bonfire* (see Encounter Resolution). If the *spark* dial shows zero, the players lose the game (see Objective & Loss Conditions).
  >
  >   - In a mega-boss encounter no rest follows: a character who dies or is *lost* in a mega-boss encounter is removed from play for the rest of the game.

  Replacement for the Encounter Resolution bullet at line 1305: "Encounters are *failed* if any *hollow* character dies; that character is *lost*."

  Replacement sentence for Returning to the Bonfire line 1906: "Resting at the *bonfire* also revives *lost* characters: characters who died while *hollow* and were removed from play."

  Addition to Objective & Loss Conditions (line 1201), as a second paragraph: "The players also lose if the characters are required to rest at the *bonfire* when the *spark* dial shows zero, and if every character is removed from play during a mega-boss encounter."
- Design rationale: The definition takes the three uses of "lost" as given and makes them one state. It keeps the manuscript's rule that a *hollow* death fails the encounter, so "lost" is a label for the interval between that death and the forced rest, and for permanent removal in the mega-boss fight. The zero-spark case is the one gap the body leaves (the forced rest cannot be paid); the ruling follows the manuscript's own loss condition rather than letting survivors continue without the lost character.
- Mechanical impact: None where sparks remain. With zero sparks, a hollow death now ends the game explicitly; previously the outcome was undefined.
- Follow-on changes required: Glossary entry "Lost" (CMP-0002) loses its [PROPOSED] tag on approval. F.A.Q. entries on forced rest and mega-boss death (CMP-0003) align. CMP-0020 carries the zero-spark rule into Encounter Recovery.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0008] Campaign Play › Setup and CAMPAIGNS list corrections — Proposed Completion
- Current state: Campaign Play › Setup (lines 2221–2225) says "the included campaigns are all three sections long" and "This rule-set includes three campaigns which require only the components available in the core set"; CAMPAIGNS (lines 2352–3034) lists thirteen campaigns of three to six sections, two of which need only the core set. "Facing the Abyss" appears twice (lines 2548 and 2764) with different preambles and a different Section Two (the first copy matches the Darkroot booklet; the second has Level 2 where Level 3 belongs). "A Hollow Pursuit" (line 2720) repeats Demon Hunting's requirements line ("core set and Asylum Demon expansion") although it is the Explorers campaign. Spellings: "Andor Londo" (2384, 2486, 2646; official: Anor Londo), "Earthern" (2736; the game location is Earthen Peak), "Jeramiah" (557) against "Jeremiah" (2492, 2528; the Phantoms booklet uses Jeremiah), "Do no place" (2456, 2504), "Old Dragon Slayer" (2734), "Bonfire Tiles" (2830), "Gaping Dragon(Mega Boss)" (2944), "Section Four- " and "Section Five Dark Champion" (2854, 2864). The Gauntlet's Section Three is titled "Invader Ruins" (2534) but the Phantoms booklet names it "Invader Spire". "Gargoyle (Mini-Boss)" is listed twice in three campaigns (2366–2368, 2468–2470, 2616–2618): the Core rulebook (p. 35) and the Phantoms booklet (p. 17) list the Gargoyle twice deliberately, with a footnote rule. "The Last Giant (Mega Boss)" (line 3018) is not in Game Components › Mega-bosses; The Last Giant is a published mega-boss expansion whose booklet was not supplied. The Undead Colosseum's Section Six (lines 2874–2880) omits the "Level 4 Encounter" that the Executioner's Chariot booklet (p. 19) lists before Vordt. "Ornstein & Smough (main-boss)" is listed as one boss (correct; see CMP-0005). Boss-rank labels vary ("Mini-Boss", "Mini Boss", "main-boss", "Main Boss", "Mega Boss").
- Proposed completion:

  Replacement for Campaign Play › Setup (lines 2219–2225):

  > ## Setup
  >
  > The setup for a campaign is the same as for the basic game except as stated in this chapter. A campaign is divided into sections. Each section lists, in order outward from the *bonfire* tile, the tiles to lay out: the *bonfire* tile, a number of encounter tiles with their encounter levels, and one or more bosses. Sections vary in length. The campaigns in this book are between three and six sections long, and some sections contain more than one boss or an encounter with special rules.
  >
  > When starting a campaign, the players choose one of the thirteen campaigns in CAMPAIGNS. Two of them, The First Journey and The Coiled Sword, require only the core set; each of the others states the expansions it requires.
  >
  > Lay out each section as Encounter Setup describes, using the number of encounter tiles the section lists and dealing encounter cards of the levels listed, in order from the *bonfire* tile. Where a section names an encounter, use that encounter card for that tile. Where a section lists a boss twice, see Boss Special Rules › Twin Gargoyles.
  >
  > A section is completed when its final boss is defeated or, for a section that ends in a named encounter instead of a boss, when that encounter is *cleared*. Completing a section restocks the shops and allows the characters to rest at the *bonfire* without spending a *spark*. A *spark* is gained only for a boss defeated. When a section is completed, perform Setup After the mini-boss for the next section, taking the next section's list in place of steps 4 and 6; for a section ending in a mega-boss, perform Setup After the main-boss instead. [PROPOSED — the section-completion sentence is inferred from Campaign Play › Sparks and › Blacksmith Andre's Shop]
  >
  > Players may expect to meet over several play sessions. One section is a convenient amount of play for a session.

  Merged entry replacing both "Facing the Abyss" entries (delete lines 2764–2808; replace lines 2548–2550 with):

  > ### Facing the Abyss - Dark Souls (Darkroot)
  >
  > This campaign requires the core set and the Darkroot expansion. Use encounters from the Darkroot expansion when setting up each section; players may add the Explorers and Characters expansions if available. Section One ends with the named Level 3 encounter Hydra Lake; the section is completed when that encounter is *cleared*.

  (Section lists as at lines 2552–2592: Section Two is Bonfire Tile, Level 1, Level 2, Level 3, Level 3, Great Grey Wolf Sif (main-boss).)

  Replacement for A Hollow Pursuit requirements (line 2720): "This campaign requires the core set and the Explorers expansion; players may add the Characters expansion if available." Replacement for line 2748: "Gallery of the Hidden Warrior — do not place an *ambush* card beside this tile; its chest is a Voracious Mimic. The section is completed when the mimic is slain."

  Footnote to attach to each doubled Gargoyle line (The First Journey, Ambush Lies Ahead, Demon Hunting): "* The two Gargoyle encounters are fought back-to-back as one boss encounter; see Boss Special Rules › Twin Gargoyles."

  The Undead Colosseum, Section Six (lines 2874–2880), corrected list: Bonfire Tile · Level 3 Encounter - Desolate Cemetery · Level 4 Encounter · Vordt of the Boreal Valley (mega-boss). Section Two, line 2830: "Bonfire Tile".

  Big Game Hunting, line 3018: retain "The Last Giant (mega-boss)" and add "The Last Giant (The Last Giant)" to Game Components › Mega-bosses (after line 535). Boss Special Rules entry for The Last Giant: BLOCKED — source booklet not supplied (CMP-0005).

  Spelling and label corrections, applied throughout CAMPAIGNS and Game Components: Anor Londo; Lower Earthen Peak; Xanthous King Jeremiah (line 557 and all campaign lines); "Do not place invader tokens"; Old Dragonslayer; Invader Spire (The Gauntlet, Section Three); "Section Four - Haunting Warrior"; "Section Five - Dark Champion"; "Gaping Dragon (mega-boss)"; boss-rank labels normalised to "(mini-boss)", "(main-boss)", "(mega-boss)" in every list; "Great Grey Wolf Sif" used in every list.
- Design rationale: The Setup paragraph is rewritten to describe what the CAMPAIGNS chapter actually contains and to state the one procedure the chapter never gives: how a section is laid out and ended. The first Facing the Abyss copy is kept because its section lists match the Darkroot booklet; the two preambles are merged so neither requirement nor encounter-source statement is lost. The doubled Gargoyle is confirmed deliberate by the Core rulebook and is kept, with the back-to-back rule made explicit in CMP-0005. The Last Giant is a published mega-boss and is kept in the campaign; adding it to the component list is the smaller change. Official spellings are taken from the Core and Phantoms booklets; "Earthen" follows the game location, since the Explorers booklet itself prints the typo.
- Mechanical impact: Section completion now explicitly grants a free rest and restock but no spark when a section ends in a named encounter (Facing the Abyss Section One, Playing with Fire Section One, A Hollow Pursuit Section Two). The Undead Colosseum gains its missing Level 4 encounter before Vordt.
- Follow-on changes required: Delete the empty headings at lines 2400 and 3036. Regenerate TOC (seven campaigns are missing from it). CMP-0022 adds The Undead Colosseum's special rules; CMP-0021 adds Kalameet's campaign section. Demon Hunting Section One deliberately has no Bonfire Tile (line 2608 explains); confirm with the author.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0010] Gameplay › Souls / Campaign Play › Encounter Soul Rewards — Reduced soul reward — Proposed Completion
- Current state: Souls (line 1391): "Upon successfully *clearing* an encounter that has been previously *cleared*, reward the reduced *soul* reward to each character." Encounter Resolution (line 1327): "Characters gain *soul* rewards but not treasure." Campaign Play (line 2245): "repeated for *souls* rewards but not treasure rewards, just as in the basic game." Neither Soul Reward Table (lines 1401–1439) nor the Campaign Soul Reward Table (lines 2247–2285) has a reduced column; no value is ever given.
- Proposed completion:

  Replacement for line 1391: "Upon successfully *clearing* an encounter that has been previously *cleared*, reward the reduced *soul* reward to each character. The reduced reward is half the full reward, rounded down."

  Replacement for the Soul Reward Table:

  > ### Soul Reward Table
  >
  > | Encounter | Full reward per character | Reduced reward per character (already *cleared*) |
  > |---|---|---|
  > | Level 1 Encounter and Standard Invaders | 3 | 1 |
  > | Level 2 Encounter and Advanced Invaders | 4 | 2 |
  > | Level 3 Encounter | 5 | 2 |
  > | Level 4 Encounter and Bosses | 6 | 3 |
  >
  > Invaders and bosses are never *cleared* twice; their reduced reward is never used.

  Replacement for the Campaign Soul Reward Table:

  > ### Campaign Soul Reward Table
  >
  > | Encounter | Full reward per character | Reduced reward per character (already *cleared*) |
  > |---|---|---|
  > | Level 1 Encounter and Standard Invaders | 2 | 1 |
  > | Level 2 Encounter and Advanced Invaders | 3 | 1 |
  > | Level 3 Encounter | 4 | 2 |
  > | Level 4 Encounter and Bosses | 5 | 2 |

  Replacement for Encounter Resolution line 1327: "Characters gain the reduced *soul* reward but no treasure."
- Design rationale: Half rounded down is chosen over "one fewer" because the manuscript's stated aim is to remove grinding: at one fewer, repeating a Level 3 encounter would pay 4 souls per character, barely less than clearing it. Half makes repeats worth taking only when a character must retrieve dropped souls or wants a safe route to the boss. Rounding down keeps every value a whole number and never reduces a reward to zero. The alternative (one fewer: 2/3/4/5 and 1/2/3/4) is recorded here for the editor's decision.
- Mechanical impact: Repeat clears pay 1–3 souls (basic) or 1–2 souls (campaign) per character. Dropped-soul recovery is unaffected.
- Follow-on changes required: F.A.Q. answer on reduced rewards (CMP-0003) matches. Line 2243 ("reduced by one compared to the basic game") stands and refers to the full reward only; add "The reduced reward is half the campaign full reward, rounded down" after it.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

