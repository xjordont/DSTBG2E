# Events Expansion II, redesign notes

Companion to `cards.json` and `rules.md`. Nothing here has been run through `tools/sim`; every balance statement below is reasoning from the house economy, not a measured result.

## Frame decisions

- **Keywords.** *Lingering* (17 cards) is a property of the place: the card stays beside its encounter card and applies at every fight there. *Once* (31 cards) is an incident: it is discarded when the party leaves the tile, unless its text lays it beside the bonfire tile.
- **Reset.** A reset no longer gathers, sets aside or deals anything. The point of the old handling was that a one-off reward is not repeated on a refight; a Once card being gone does that. No Lingering card gives souls, treasure or items, so a reset encounter cannot be farmed through one.
- **Boss.** All discarded cards and all cards on tiles return to their decks when a boss is defeated, which the rulebook's stage setup already does (§6.6 step 2).
- **Wares.** The nine item cards lie face up beside the bonfire tile from setup. They are bought from a visitor or handed over by an event card, never sold to Andre, and return to the wares when discarded. No module card touches a printed deck.
- **Trap cards** hit every model on a marked node, enemies included, as trap tokens do in §5.5. Enemies subtract block or resist. Values are not scaled for party size: more characters already means more models standing in the pattern.
- **Hollowing** uses only the house hollow state: two hollow cubes, lost characters, and the rest, ember or Purging Stone that cures them.
- **Shorthand.** "The treasure deck" on a card is the deck of the current tier (one line in `rules.md`), which saved four words on eleven cards.

## Original event cards (49)

| # | Original | L | Became | Status | Reason |
|---|---|---|---|---|---|
| 1 | Sunken Bog | 1 | E1-01 Sunken Bog | rebalanced | "Cannot walk" turned every step into a run, and a run bars the rest action; a walk now costs one stamina and stays a walk. |
| 2 | Dreadful Gloom | 1 | E1-06 Dreadful Gloom | reworded | Covers attacks and effects on both sides; infinite range stated. |
| 3 | Stagnate Pools | 1 | E1-02 Stagnant Pools | reworded | Trigger is now "ended the turn where it began", checked on the board with no counting; token timing stated; spelling. |
| 4 | Lost Antiquities | 1 | E1-11 Lost Antiquities | rebalanced | One card in all, taken for 4 stamina during the fight; three free cards was worth a whole encounter. |
| 5 | Perilous Impediment | 1 | E1-09 Perilous Impediment | rebalanced | The invader needs the Phantoms expansion. The ember stays and is paid for with stronger enemies; with Phantoms the ember provokes an invader by §12.2 anyway. |
| 6 | Unsure Footing | 1 | E1-07 Unsure Footing | rebalanced | Node diagram, spawn-node exception and instant death replaced by one named ledge (the far edge) and 2 damage, for both sides. |
| 7 | Fatal Gaffe | 1 | E1-03 Fatal Gaffe | reworded | Says who is pushed, by whom and in which direction. |
| 8 | Hollowing I | 1 | E1-05 Hollowing I | rebalanced | A stamina cap was a second kind of hollowing. Now: after a death here, the next rest cures no hollow cubes. |
| 9 | Exploration I | 1 | E1-12 Exploration I | reworded | The soul is paid by one character; the look covers the encounter card and its event card. |
| 10 | Loyal Swindler | 1 | E1-15 Loyal Swindler | rebalanced | Visiting cost nothing, so Greirat paid out about five treasure cards. Now 1 soul an outing, three outings at most. |
| 11 | Royal Atheneum | 1 | E1-08 Royal Atheneum | rebalanced | "INT 15 or greater" was blank for most parties. The highest INT searches, by choice, for a spell. |
| 12 | Sinking Slog | 2 | E2-01 Sinking Slog | rebalanced | +1 stamina on five actions is crippling at one stamina a turn, and block has no cost here. Walk, dodge and parry only. |
| 13 | Lacerations | 2 | E2-02 Lacerations | rebalanced | Threshold 3, not 2: scaled attacks nearly always deal 2, and every second bleed token is 3 damage. |
| 14 | Rootless Foothold | 2 | E1-10 Cramped Quarters (new) | replaced | A second drop-hazard diagram. Replaced by another terrain twist that needs no diagram: a node model limit of two. |
| 15 | Hollowing II | 2 | E2-05 Hollowing II | rebalanced | As Hollowing I, but it lasts until a boss is defeated. |
| 16 | Rebirth | 2 | E2-15 Rebirth | rebalanced | Happens during a rest, costs 3 souls, refunds exactly what the tiers cost. |
| 17 | Reinforcements | 2 | E2-10 Reinforcements | replaced | Two tiles cannot be fought as one. Same spirit on one tile: an optional second wave of the same models for a second reward. |
| 18 | Combat's Blight | 2 | E2-03 Combat's Blight | reworded | The unnamed green icon is read as poison; capped at one token because poison stacks here. |
| 19 | Draw Out True Strength | 2 | E1-16 Draw Out True Strength | rebalanced | A spark for one stat tier is absurd in this economy. Yoel now raises a stat for nothing and the character leaves hollow. Moved to Level 1. |
| 20 | Undead Settlement | 2 | E2-14 Thinned Ranks (new) | replaced | Five Hollow Soldiers exceed the three models printed. The garrison now changes the other way: its weakest enemy is absent. |
| 21 | Maiden of the Sable Church | 2 | E2-16 Maiden of the Sable Church | rebalanced | Purging Stone 1 soul (an ember is 2 and does more). The Morion Blade can be bought by a hollow character, so Yuria works without Yoel. |
| 22 | Judgement | 2 | E1-13 Judgement | reworded | Kills are tracked with the dead models; "cower" is spelt out. Moved to Level 1, where threat 6 covers most enemies. |
| 23 | Exploration II | 2 | E2-11 Exploration II | rebalanced | As Exploration I, and the party may swap the event card it saw for an unseen one. |
| 24 | Lunar Reflection | 2 | E3-04 Lunar Reflection | reworded | Moved to Level 3 to even the decks. |
| 25 | Veiled Figure | 2 | E2-06 Veiled Figure | rebalanced | The invader on a 0 needs Phantoms; it is 3 damage. One attempt in the encounter. |
| 26 | Vitiated Boon | 2 | E2-13 Vitiated Boon | rebalanced | "Stave off death" with a lasting damage tick becomes the house state: the first death is an immediate return hollow. |
| 27 | Divine Endowment | 2 | E3-08 Divine Endowment | rebalanced | Highest FTH searches by choice; "healing reduced by 2" becomes estus removing 4 cubes. Moved to Level 3. |
| 28 | Tribute of Might | 2 | E2-07 Tribute of Might | rebalanced | Highest STR searches by choice; no stat threshold on the character. |
| 29 | Skilled Relief | 2 | E2-08 Skilled Relief | rebalanced | Highest DEX searches by choice; no stat threshold on the character. |
| 30 | Propitious Cartographer | 2 | E2-12 Propitious Cartographer | rebalanced | Moving to "any other tile" and discarding encounter cards breaks the single road. The party may slip past this one encounter, unrewarded and uncleared. |
| 31 | Morbid Enkindling | 2 | E2-04 Morbid Enkindling | rebalanced | An enemy returning every round never ends. The first two killed rise once each, on their own spawn nodes. |
| 32 | Looming Tribulations | 2 | E2-09 Looming Tribulations | rebalanced | "Until the party next perishes" needed tracking across tiles. It is now two events on this tile. |
| 33 | Ameliorated Resolve | 2 | E1-04 Ameliorated Resolve | kept | Wording only. Moved to Level 1, where it is a mild hindrance. |
| 34 | The Great Deceiver | 2 | E3-15 The Great Deceiver | rebalanced | Stealing chest treasure put printed cards in a module display. Patches now kicks the party (1 damage each) and sells four item cards. Moved to Level 3. |
| 35 | Wintry Bite | 3 | E3-01 Wintry Bite | reworded | Same trigger as Stagnant Pools; duration of the token stated. |
| 36 | Waning Grit | 3 | E3-02 Waning Grit | rebalanced | "Twice from the same enemy" needed bookkeeping. The trigger is now read off the endurance bar: eight or more cubes after a hit. |
| 37 | Impending Struggle | 3 | E3-09 Impending Struggle | rebalanced | As Perilous Impediment at Level 3 stakes, with 2 extra souls each. |
| 38 | Reparations | 3 | E3-14 Contest of Arms (new) | replaced | Characters never fight each other outside §20. The rivalry is kept as a race for kills. |
| 39 | Perilous Perch | 3 | E3-06 Perilous Perch | rebalanced | The far edge is a sheer drop: a push there kills, characters and enemies alike. No diagram. |
| 40 | Avaricious Outfit | 3 | E3-07 Avaricious Outfit | rebalanced | Each character chooses; the extra damage applies to enemy attacks only. |
| 41 | Enduring Ambition | 3 | E3-11 Enduring Ambition | rebalanced | The spark comes only at 0 sparks and only on a clear; otherwise 1 soul a spark, not 2. |
| 42 | Transposition | 3 | E3-16 Transposition | rebalanced | Boss treasure is rarely in hand in the standard game. Ludleth trades any treasure card and 6 souls for one of three legendary cards. |
| 43 | Hollowing III | 3 | E3-05 Hollowing III | rebalanced | A death in this encounter leaves the character lost until the next rest. |
| 44 | Wrong Turn | 3 | E3-10 Champion of Ash (new) | replaced | A mini-boss cannot stand in an encounter and no card may grant a spark so cheaply. The strongest enemy becomes a champion with a bounty. |
| 45 | Exploration III | 3 | E3-12 Exploration III | rebalanced | At Level 3 the next thing worth scouting is the boss: the top three behaviour cards. |
| 46 | Forgotten Bridge | 3 | E3-06 Perilous Perch | merged | A second Level 3 drop-hazard diagram; one card covers it. This is the one card cut to reach 48. |
| 47 | Hidden Wall | 3 | E3-13 Illusory Wall (new) | replaced | No spare tile and no Explorers chests are assumed. Two hidden chests are opened with a green die: treasure or a bite. |
| 48 | Wastes | 3 | E1-14 Purging Monument (new) | replaced | Removing every encounter card skips the game. Its slot goes to a small mercy that puts a Purging Stone in play without Yuria. |
| 49 | Emboldened Regiment | 3 | E3-03 Emboldened Regiment | kept | The repeat icon written out in words. |

Each level holds 4 hindrances, 1 curse, 5 twists, 4 boons and 2 visitors.

## Original trap cards (8)

Node rows are now listed from the doorway side upwards, so each diagram is the printed one read from the foot of the card.

| Original | Became | Status | Reason |
|---|---|---|---|
| Rolling Boulder | T-01 Rolling Boulder | kept | Values as printed. |
| Toxic Vapor | T-02 Toxic Vapour | kept | Values as printed; British spelling; the droplet icon is poison. |
| Enveloping Slag | T-03 Enveloping Slag | kept | Values as printed. |
| Collapsed Ceiling | T-04 Collapsed Ceiling | kept | Values as printed. |
| Sandworm Ambush | T-05 Sandworm Ambush | rebalanced | Printed damage fell from 4 to 3 between Levels 1 and 2. Now 3 / 3 / 4, with bleed so that every condition appears once. |
| Blazing Pyres | T-06 Blazing Pyres | kept | Values as printed. |
| Howling Tempest | T-07 Howling Tempest | rebalanced | Printed damage fell from 3 to 2 at Level 3. Now 1 / 2 / 2. |
| Noxious Sanctum | T-08 Noxious Sanctum | rebalanced | Printed damage fell at Level 3 and dodge difficulty 3 is beyond most armour. The unnamed icon becomes stagger and the fumes do magical damage. |

## Original item cards (9)

| Original | Became | Status | Reason |
|---|---|---|---|
| Purging Stone x6 | I-01 Purging Stone x4 | rebalanced | Removes hollow cubes anywhere outside an encounter. No copy enters the treasure deck any more. |
| Irreverent Morion Blade | I-02 Irreverent Morion Blade | rebalanced | Requirements 17 / 30 / 0 / 12 took three stats to tier two. Now 16 / 21 / 0 / 12, and being hollow counts towards the bonus. |
| Red Tearstone Ring | none | dropped | It was common treasure, which the separation rule forbids, and a printed card of the same name is already in the game (Appendix B). Its effect lives on in the Morion Blade. |
| Great Heal Excerpt | I-04 Great Heal Excerpt | rebalanced | A spell is never two-handed here. One cast between rests (the card is turned face down), FTH 13, range 1. |
| Divine Blesing | none | dropped | A printed Divine Blessing is already in the game (Appendix B); a second card of that name with another text would confuse. |
| Horsehoof Ring | I-03 Horsehoof Ring | rebalanced | "Highest stamina attack" and a movement penalty with no token. Now a stagger token on an enemy the wearer hits for no damage. |
| Mask of the Mother | I-05 Mask of the Mother | reworded | "Lowest taunt value" removed; any other character on the same or an adjacent node will do. |
| Mask of the Father | I-06 Mask of the Father | rebalanced | Shield beside a two-handed weapon kept; the wearer cannot dodge but may walk. |
| Mask of the Child | none | dropped | A printed Mask of the Child with a different text is in Appendix B. |

## House rulebook: what needs changing

No mechanism of the rulebook changes. The passages that describe the old deck are replaced, and four sentences are overridden by a card through the first line of `rules.md`.

Passages to replace or delete:

- §7.5, "Event Cards": replace the whole sub-section with `rules.md`.
- §5.5, last bullet of "Traps": delete; the trap card rule is in `rules.md`.
- §6.2, second bullet (two Purging Stones and the Red Tearstone Ring as common treasure): delete. It breaks the separation rule.
- §6.5 step 4: add "lay the item cards face up beside the bonfire tile".
- §11.5 step 5: delete. A reset changes no event card.
- §6.6 step 2 and §6.7 step 2: "every event card" becomes "every event card that is not beside the bonfire tile". In a campaign this happens when a section ends.
- §2.6: the component line becomes 48 event cards, 8 trap cards and 9 item cards.
- Glossary: "Event card" stands; Lingering, Once and wares are new headwords if wanted.

Sentences a card overrides, which the book may leave as they are:

- §7.4 "Sparks cannot be gained by any other means": Enduring Ambition, at 0 sparks only. Adding "except by an event card" to §7.4 is the one edit recommended.
- §7.5 step 1, the encounters are fought in order: Propitious Cartographer.
- §3.2, the other weapon slot stays empty beside a two-handed weapon: Mask of the Father.
- §11.4, every card sells for one soul and goes to the bottom of its treasure deck: item cards are never sold.

"Stats are raised only during a rest" (§11.3) is respected: Yoel and Rosaria act during a rest and say so.

## Balance reasoning

Anchors: a first clear pays 3 / 4 / 5 souls each; a chosen shop card costs 2 or 4 and any card sells for 1, so a random treasure card is worth roughly 1 to 2 souls before the mini-boss and 2 to 4 after; an ember costs 2. A standard game deals eight event cards of the 48, so a given card is seen in about one game in six: fewer for a level the chosen bosses use once, up to one in four for a level they use four times.

Worth more than 3 souls a character:

- **Reinforcements (E2-10).** A second Level 2 reward (4 each) for a second Level 2 fight begun with the damage and stamina cubes of the first. The pay matches the work, and losing the second wave fails the whole encounter, first reward included.
- **Avaricious Outfit (E3-07).** After the mini-boss a card each is up to 4 souls of value. The price is 1 more damage from every damaging enemy attack in a Level 3 encounter, where damage is not healed afterwards. Each character decides alone, so a wounded character declines.
- **Impending Struggle (E3-09).** An ember (2 souls, and scarce) for one character and 2 souls each, against +2 health and +1 damage on every enemy: a little more than the scaling step of one extra character.
- **Champion of Ash (E3-10).** 2 souls each and one card for the party, for 3 more health and 1 more damage on a single model. Not optional, hence a twist.
- **Contest of Arms (E3-14).** 4 souls, to one character only; less than one Level 3 reward.
- **Draw Out True Strength (E1-16).** A free tier two is worth 4 souls, three times in all across the party. Each use leaves the character hollow: eight spaces, and lost on the next death. Curing it at once costs an ember or a Purging Stone, so the net gain is 3 souls a use at most.
- **Rebirth (E2-15).** Refunds only what was paid; the 3 souls are a pure cost.
- **Loyal Swindler (E1-15).** On average 2.5 outings and 2.1 random cards for 2.5 souls. A bargain, not a windfall.
- **The stat searches (E1-08, E2-07, E2-08, E3-08).** One fitting card for one character, 2 to 4 souls of value, against a penalty on the whole encounter.
- **Illusory Wall (E3-13).** Each chest is an even chance of one card for the party or 2 damage on every character.
- **Transposition (E3-16).** 6 souls and a card for a chosen legendary card; the campaign's own transposition asks 4 souls and a boss treasure card (§18.8).
- **The Great Deceiver (E3-15).** 4 souls a card is the tier two shop price.

Touching sparks:

- **Enduring Ambition (E3-11)** is the only card that touches the spark dial. It adds a spark only when the dial shows 0 and only once the encounter is cleared, so it can never be banked by a party that still has a rest in hand. One to four Level 3 cards are dealt in a game, so the card is seen in roughly one game in six, and it finds the dial at 0 in a fraction of those. Otherwise it pays 1 soul a spark: at most 5 for a lone character after the mini-boss, 1 or 2 each for four.
- The original's other spark effects are gone: Wrong Turn (a spark for a mini-boss), Wastes (a shortcut at 0 sparks) and Yoel's price of a spark.
- **Hollowing I and II** make a rest worth less (it cures no hollow cubes) without costing a spark; a Purging Stone at 1 soul or an ember at 2 is the way out.

Average difficulty. Per level, five cards make the fight harder, five cut both ways and six help, and the helpful ones are small or paid for. The Lingering hindrances are the ones a party meets again after a rest; a cleared encounter can be skipped for one damage each (§7.5), which bounds what they cost.
