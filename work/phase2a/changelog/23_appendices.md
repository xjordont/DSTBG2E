# Change log — chapter 23 Appendices

### CH-23-001 · Appendix A Weapon Stat Revisions and Appendix B Card Amendments
- Type: restructure
- Before: "# COMMUNITY UPDATE PACK" with the bold labels "Treasure - Official", "Treasure - Errata/Updated", "Weapons - Updated Stat Requirements", "Enemy Data", "Boss Data & Behaviours"
- After: "# Appendix A. Weapon Stat Revisions" and "# Appendix B. Card Amendments", with the sections Revised Requirements, Treasure Type, Additional Treasure, Revised Treasure, Enemy Data Cards, and Boss Data and Behaviour Cards
- Rationale: The chapter becomes the two appendices fixed at Gate 1. The pack is never named; the text speaks of the revised cards and the cards listed in the appendix.
- Source: Gate 1 — OQ-31; CMP-0004; F-047

### CH-23-002 · Appendix A (lead)
- Type: cut
- Before: "The first edition of DStBG has many nonsensical weapon stat requirements which this edition aims to remedy. Specifically, many high strength requirement weapons from the video game series where given intelligence and/or Faith requirements."
- After: "The *stat requirements* in this appendix replace those printed on the *weapon* cards listed. A weapon not listed keeps its printed requirements."
- Rationale: Design rationale and comparison with another edition are removed; the rule the paragraph carried (the listed values replace the printed ones) is kept, with the tier split at 25 and the scaling rule cited to their owning sections. The CMP-0004 rationale sentence is not adopted for the same reason.
- Source: F-048; CMP-0004

### CH-23-003 · Appendix A, Revised Requirements
- Type: restructure
- Before: "**Weapon Name STR DEX INT FTH**" followed by 60 plain-text lines such as "Avelyn 23 30 0 0"
- After: "| Weapon | STR | DEX | INT | FTH | Tier |" with one row per weapon, sorted alphabetically, digits throughout
- Rationale: Plain-text columns set as a table with a computed Tier column. All 60 rows were checked by script against the source and against CMP-0004: the two agree on every value, and the only differences in the chapter are the ten corrected rows logged in CH-23-004 to CH-23-007. CMP-0004 has no grouping, so the table has none.
- Source: C-072; CMP-0004

### CH-23-004 · Appendix A, Revised Requirements (Falchion)
- Type: correction
- Before: "Falchion 37 30 0 0"
- After: "| Falchion | 17 | 30 | 0 | 0 | 2 |"
- Rationale: Digit transposition corrected. Source and CMP-0004 both print 37; the Gate 1-approved finding governs. The card stays tier two on DEX.
- Source: B-018; Gate 1 (approve all)

### CH-23-005 · Appendix A, Revised Requirements (Carthus Curved Greatsword, Carthus Curved Sword)
- Type: correction
- Before: "Carthus Curved Greatsword 19 30 0 0 / Carthus Curved Sword 25 35 0 0"
- After: "| Carthus Curved Greatsword | 25 | 35 | 0 | 0 | 2 |" and "| Carthus Curved Sword | 19 | 30 | 0 | 0 | 2 |"
- Rationale: The two lines are swapped so that the heavier weapon has the higher requirements. Source and CMP-0004 both print the unswapped values; the approved finding governs. Both stay tier two.
- Source: B-019; Gate 1 (approve all)

### CH-23-006 · Appendix A, Revised Requirements (boundary rows)
- Type: correction
- Before: "Butcher Knife 25 0 0 0 / Dark Silver Tracer 0 25 0 0 / Warden Twinblades 17 25 0 0"
- After: "| Butcher Knife | 24 | 0 | 0 | 0 | 1 |", "| Dark Silver Tracer | 12 | 26 | 0 | 0 | 2 |", "| Warden Twinblades | 17 | 26 | 0 | 0 | 2 |"
- Rationale: The three rows that sat exactly on the split at 25 are moved off it. The finding offers Butcher Knife 24 (tier one) or 28 (tier two); 24 is adopted as the first-listed value and the one that answers the audit's concern (see issues file). Butcher Knife moves from tier two to tier one; the other two stay tier two.
- Source: B-020 (OPTIONAL, applied); Gate 1 (approve all)

### CH-23-007 · Appendix A, Revised Requirements (claws, dagger, Caestus, zero requirements)
- Type: correction
- Before: "Claws 0 20 0 0 / Manikin Claws 24 24 0 0 / Parrying Dagger 14 21 0 0 / Caestus 0 15 0 0"
- After: "Claws 12 20", "Manikin Claws 14 24", "Parrying Dagger 10 18", "Caestus 12 10", and "A weapon shown with 0 STR or 0 DEX has no requirement in that stat, and every character meets it."
- Rationale: Approved value corrections; all four rows remain tier one. The finding's note sentence ("A requirement of 0 is intentional where shown") is restated as a rule, together with the fact that every listed weapon has 0 INT and 0 FTH (C-072).
- Source: B-021; C-072; Gate 1 (approve all)

### CH-23-008 · Appendix A, Revised Requirements (Tier column) and Treasure Type
- Type: correction
- Before: CMP-0004: "A weapon is tier one if every requirement is below 25 and tier two otherwise." with the column values "One" / "Two"
- After: "The Tier column shows 1 for *tier one treasure* and 2 for *tier two treasure*." and "A listed card that is *transposed treasure* or *legendary treasure* is *tier two treasure* whatever its requirements (see §6.2)."
- Rationale: Tier recomputed from the final values: 23 rows are tier one and 37 tier two (CMP-0004's note of nineteen and forty-one did not match its own table). The only tier that differs from CMP-0004 is Butcher Knife (Two to 1). The treasure-type sentences keep the column consistent with §6.2 for transposed, legendary, and boss treasure.
- Source: CMP-0004; B-020; §6.2

### CH-23-009 · Appendix A, Revised Requirements (example)
- Type: clarification
- Before: new text
- After: "*Example.* The Brigand Axe's revised requirements are 19 STR and 16 DEX, so strength is its *relevant stat*. The Knight has 24 STR and 20 DEX, meets both requirements, and equips the Brigand Axe."
- Rationale: One worked example shows a revised requirement used for equipping and for scaling at five over (OQ-19). It introduces no rule.
- Source: CMP-0004; Gate 1 — OQ-19

### CH-23-010 · Appendix B (lead)
- Type: completion
- Before: new text (CMP-0004: "The Community Update Pack is a set of print-and-play cards that accompanies this edition. … Where a card in the pack and a published card disagree, the pack card governs.")
- After: "The *revised cards* replace the printed cards of the same name. Where a card listed here differs from its printed text, the text given here governs. Where only part of a card is amended, every other part of the card is as printed."
- Rationale: The general rule is stated once. The description of the pack as a print-and-play set and its purpose is cut; the precedence rule and the "unchanged parts as printed" rule are kept.
- Source: CMP-0004; F-047; Gate 1 — OQ-31

### CH-23-011 · Appendix B, Additional Treasure
- Type: completion
- Before: "**Treasure - Official**" over 34 bare card names in two lists split by a stray comment marker
- After: "Each card listed in this section is added to the *treasure cards* in play. Each card is sorted during setup by the treasure type marked on it and by its *stat requirements* (see §6.2)." with a table Card | Amendment of 34 rows
- Rationale: The bare list becomes a rule and an alphabetical table. All 34 source names are present (CMP-0004 counts 33 but lists 34). The eight weapons that also appear in Appendix A point to it, and Blue Titanite points to its amendment. CMP-0004's three type groups are not kept: a card's type is read from the card, and the supplied sources do not confirm the grouping (see issues file).
- Source: CMP-0004; F-047; C-117

### CH-23-012 · Appendix B, Revised Treasure (Titanite Chunk and Titanite Slab)
- Type: completion
- Before: "Titanite Chunk (+2 attack, must replace Titanite Shard) \[25/25/0/0 Common\]" and "Titanite Slab (+3 attack, must replace Titanite Chunk) \[25/25/0/0 legendary\]"
- After: "Every *attack option* of the *weapon* adds 2 to its *attack value*. This card may be attached only in place of a Titanite Shard." and "A replaced Titanite Shard is returned to the bottom of the tier one treasure deck, and a replaced Titanite Chunk is returned to the bottom of the tier two treasure deck."
- Rationale: The notes become card text, stat requirements, and treasure type, and the Shard to Chunk to Slab chain is stated in the sub-section Titanite Replacement with its exception to the permanence of Titanite (§4.2). Escaped brackets are replaced by "25 STR, 25 DEX, 0 INT, and 0 FTH".
- Source: CMP-0004; F-047; C-109; A-074

### CH-23-013 · Appendix B, Revised Treasure (Blue Titanite and Demon Titanite)
- Type: completion
- Before: "Demon Titanite" (no note) and "Blue Titanite (legendary Item instead of Boss Drop, increase INT req to 25)"
- After: "Replace the printed treasure type with *legendary treasure*. Replace the printed INT requirement with 25. The rules text is unchanged." and "Replace the printed card with the *revised card*. The rules text, stat requirements, and treasure type are unchanged."
- Rationale: Blue Titanite's two changes are stated as replacements. Demon Titanite carries no note in the manuscript, so the card is listed with no change of rule, as CMP-0004 proposes. Bare "Item" is removed.
- Source: CMP-0004; F-047

### CH-23-014 · Appendix B, Revised Treasure (Tiny Being's Ring and Chloranthy Ring)
- Type: completion
- Before: "Tiny Being’s Ring (remove one damage cube each turn)", "Chloranthy Ring (+1 passive stamina gain each turn to characters on node)", and "Chloranthy Ring (will need custom card to state +1 stamina gain per turn)"
- After: "At the start of each of the wearer's turns, the wearer removes 1 *damage cube* from their *endurance bar*." and "At the start of each of the wearer's turns, the wearer and every other character on the wearer's *node* each recover 1 stamina."
- Rationale: Each note becomes card text with a trigger, an actor, and an outcome. The two Chloranthy Ring entries are merged into one and the working note is cut. The wearer of a ring is defined once in the section lead.
- Source: CMP-0004; F-047

### CH-23-015 · Appendix B, Revised Treasure (dodge cards)
- Type: completion
- Before: "Black Leather Armour (will keep old version with free dodge)", "Wolf Ring (change to allow re-rolling dodge rolls for one stamina)", "Eastern Armour (will keep old version of +1 stamina cost to dodge)", "Carthus Milkring (will use new version of increasing dodge by one)"
- After: "The character who has this card equipped pays no stamina to attempt a *dodge*." / "pays 1 additional stamina to attempt a dodge." / "The wearer adds 1 to the count of dodge icons rolled for a dodge." / "the wearer may pay 1 stamina to reroll any or all of those dice. The wearer may do this once for each dodge."
- Rationale: The "will keep" and "will use" notes are cut and each card's governing text is stated and tied to the numbered steps of a dodge (§9.5). The choice between printings is stated without history: the printing that carries the text is used.
- Source: CMP-0004; F-047; C-060

### CH-23-016 · Appendix B, Revised Treasure (Sellsword Twinblades)
- Type: completion
- Before: "Sellsword Twinblade (will keep old one-handed version)"
- After: "The one-handed card of this name is used. A two-handed card of this name is returned to the game box."
- Rationale: Working note rewritten as a rule. The card name follows CMP-0004 ("Twinblades"), which differs from the source ("Twinblade").
- Source: CMP-0004; F-047; Gate 1 — OQ-17

### CH-23-017 · Appendix B, Revised Treasure (Covetous Silver Serpent Ring)
- Type: completion
- Before: "Covetous Silver Serpent Ring (+1 soul to an equipped character per encounter)"
- After: "When the wearer gains the soul reward for a *cleared* *encounter*, the wearer gains 1 additional soul." The additional soul is gained with the full reward and with the *reduced reward* (see §7.6).
- Rationale: The bonus is tied to the encounter soul reward of §7.6, full or reduced, as CMP-0004 proposes.
- Source: CMP-0004; F-047; Gate 1 — OQ-05

### CH-23-018 · Appendix B, Revised Treasure (Mon Ring)
- Type: completion
- Before: "Mon Ring (one use per floor)"
- After: "This effect may be used only while this card is face up. When the effect is used, turn this card face down." The card is turned face up each time the characters rest at the *bonfire* (see §11.2).
- Rationale: "Floor" is not a term of the book. It is read, as CMP-0004 proposes, as the play between two rests, and the limit is tracked by turning the card.
- Source: CMP-0004; F-047

### CH-23-019 · Appendix B, Enemy Data Cards
- Type: completion
- Before: "**Enemy Data**" over 12 bare enemy names
- After: "Each enemy listed in this section is played from the revised *data card* of the same name, which shows the values of an enemy data card (see §8.2)." with a table Card | Amendment of 12 rows naming each enemy's expansion
- Rationale: The bare list becomes a rule and a table. "Skeleton Beast" is the spelling used, matching §2.2. The values shown on a data card are cited to §8.2 and not repeated.
- Source: CMP-0004; C-007; F-047

### CH-23-020 · Appendix B, Boss Data and Behaviour Cards
- Type: completion
- Before: "**Boss Data & Behaviours**" over four bare boss names
- After: "Each *boss* listed in this section is played from the revised *data card* of the same name and the general boss rules (see §15.4, §16.1). Its *behaviour deck* is built from the revised *behaviour cards* of the same name (see §15.5)."
- Rationale: The bare list becomes a rule and a table that names each boss's type and expansion, consistent with §2.3, §17.7, and §17.10. The printed boss treasure, model, and health dial stay in use. The ampersand is replaced by "and".
- Source: CMP-0004; F-047; Gate 1 — OQ-02

### CH-23-021 · Appendices A and B (style sweep)
- Type: style
- Before: "Onikiri And Ubadachi"; "re-rolling"; "Tiny Being’s Ring"; "\[25/25/0/0 Common\]"; "<!-- -->"; "legendary Item"; "Boss Data & Behaviours"
- After: "Onikiri and Ubadachi"; "reroll"; "Tiny Being's Ring"; "25 STR, 25 DEX, 0 INT, and 0 FTH"; deleted; "legendary treasure"; "Boss Data and Behaviour Cards"
- Rationale: One spelling per compound, straight quotes, no conversion artefacts, no escaped brackets, no bare "item", no ampersand in a heading. "Onikiri and Ubadachi" follows CMP-0004 where it differs from the source.
- Source: C-060; C-109; C-117; CMP-0004; brief §2 and §3

### CH-23-022 · Findings with no text in the appendices
- Type: clarification
- Before: (pack findings whose rule is owned by another chapter)
- After: no statement in the appendices; the appendices are consistent with the owning sections
- Rationale: A-096, C-056, and B-032 (the crystal-lizard reward is a Titanite Scale): owned by §7.7 and §14; Appendix B gives the Titanite Chunk no link to crystal lizards. A-074 (sold Titanite goes to the deck of the weapon's tier): owned by §4.2 and §11.4; Appendix B makes the Titanite Chunk tier two, which that rule accommodates. B-022 (definition of a shield): owned by §4.1; the East-West Shield stays in the weapon table because a shield is a weapon card.
- Source: A-096; C-056; B-032; A-074; B-022

### CH-23-023 · OPTIONAL findings skipped
- Type: clarification
- Before: (not applicable)
- After: (not applied)
- Rationale: A-066 (equipment whose highest requirement is zero cannot be scaled): the rule belongs to §10.5, and no weapon in the table has a highest requirement of zero after the approved corrections, so the appendix needs no statement.
- Source: A-066
