# Print-and-play modules

Three modules printed at home. None of their cards is ever shuffled with a card of the printed game.

| Module | Files | Cards | Card size |
|---|---|---|---|
| Events Expansion II (a community expansion, laid out here for printing) | `events/events_expansion_letter.pdf`, `events/events_expansion_a4.pdf` | 49 event cards, 8 trap cards, 14 treasure cards | events and traps 63.5 x 88.9 mm; treasure cards 45.3 x 66.2 mm, the trim their maker's crop marks give |
| Tomb of Giants encounter deck | `encounters/tomb_of_giants_letter.pdf`, `..._a4.pdf` | 27 encounter cards (9 of each level) and a key card | 41 x 63 mm |
| Painted World of Ariamis encounter deck | `encounters/painted_world_letter.pdf`, `..._a4.pdf` | 27 encounter cards (9 of each level) and a key card | 41 x 63 mm |

## Printing

- Print at 100% (no scaling) on Letter or A4, double-sided, flipping on the long edge. Every sheet of fronts is followed by its sheet of backs.
- Card stock of 200 g/m2 or more, or plain paper in opaque sleeves with a playing card behind each.
- Cut along the grey card edges.

## Events Expansion II

- The cards are the expansion's own, with its art, frames and backs. Five event cards have changed text, listed with the reasons in `events/edits.json`: Fatal Gaffe, Reinforcements, Undead Settlement, Vitiated Boon and Propitious Cartographer. The other 66 cards are exactly as their maker printed them.
- Rules: §7.5 (Event Cards), §5.5 (trap cards) and §6.5 (setup) of the rulebook. The expansion's own rules insert is not needed.
- The cards carry the work of the expansion's maker and of the artists its insert credits. The author holds the rights to use and publish them (statement of 2026-11-26), so the print files may be passed on with the book.
- Rebuilding needs the maker's two card PDFs in `sources/events_expansion/` (sources are not kept in the repository): `python3 tools/build_pnp.py events`.

## Encounter decks

- Rules: §6.5 of the rulebook (the choice of decks), §9.2 and §9.3 (leap and resurrect) and Appendix B (the enemies). The cards are in `encounters/*.json`.
- The Tomb of Giants cards use the set's own enemy icons. The Painted World icons (`encounters/icons/`) are cut from a community sheet of 2017-style encounter cards.
- `python3 tools/build_pnp.py encounters` rebuilds the PDFs. `python3 tools/sim/encounter_score.py core` and `... FILE.json` score encounters against the printed core set.
