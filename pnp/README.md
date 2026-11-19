# Print-and-play modules

Three modules of the rulebook that are printed at home. None of their cards is ever shuffled with a card of the printed game: each has its own decks and its own card backs.

| Module | Files | Cards | Card size |
|---|---|---|---|
| Events deck | `events/events_deck_letter.pdf`, `events/events_deck_a4.pdf` | 48 event cards (16 of each level), 8 trap cards, 9 item cards | events and traps 63.5 x 88.9 mm (poker); items 41 x 63 mm (mini) |
| Tomb of Giants encounter deck | `encounters/tomb_of_giants_letter.pdf`, `..._a4.pdf` | 27 encounter cards (9 of each level) and a key card | 41 x 63 mm (mini), the size of the printed encounter cards |
| Painted World of Ariamis encounter deck | `encounters/painted_world_letter.pdf`, `..._a4.pdf` | 27 encounter cards (9 of each level) and a key card | 41 x 63 mm (mini) |

## Printing

- Print at 100% (no scaling) on Letter or A4, double-sided, flipping on the long edge. Every sheet of fronts is followed by its sheet of backs.
- Card stock of 200 g/m2 or more, or plain paper in opaque sleeves with a playing card behind each.
- Cut along the grey card edges.

## Rules

- Events deck: §7.5 (Event Cards), §5.5 (trap cards) and §6.5 (setup) of the rulebook. The card texts are in `events/cards.json`; `events/design_notes.md` records how each card differs from the community Events Expansion II it grew out of.
- Encounter decks: §6.5 of the rulebook (the choice of decks), §9.2 and §9.3 (leap and resurrect) and Appendix B (the enemies). The cards are in `encounters/*.json`.
- The Painted World enemies are shown by monograms (BW, CD, EZ, PX, PH, SR) with a key card, because no icon artwork for them is held; the Tomb of Giants cards use the set's own icons.

## Rebuilding

`python3 tools/build_pnp.py` rebuilds every PDF from the JSON files. `python3 tools/sim/encounter_score.py core` and `... FILE.json` score encounters against the printed core set.
