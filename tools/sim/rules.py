#!/usr/bin/env python3
"""Rulesets for the simulator. Each field names the rule it stands for; the sources are quoted in
41_rules_workshop.md, section 12.

  OFFICIAL_2017   the 2017 core rulebook (standard game)
  OFFICIAL_2022   the 2022 core rulebook (Tomb of Giants / Painted World), played on the same enemy cards
  MANUSCRIPT      the author's original manuscript, as written
  variants        built with Rules(base, **changes)
"""


class Rules:
    def __init__(self, base=None, **kw):
        if base is not None: self.__dict__.update(base.__dict__)
        self.__dict__.update(kw)

    def but(self, **kw): return Rules(self, **kw)


def plus(k): return lambda h, n: h + k * (n - 1)


_COMMON = dict(
    bar=10,
    sparks=lambda n: 6 - n,                 # five, four, three, two: the same in every ruleset
    tier_cost=(2, 4, 8),                    # souls to raise one stat to tiers one, two, three
    boss_reshuffle=False,                   # a spent behaviour deck is turned over, not shuffled
)

OFFICIAL_2017 = Rules(
    name='Official 2017', **_COMMON,
    # the round: all enemies activate, then one character; and again for the next character
    round='alternate', order='seat', aggro='active', regen=2, turn='official',
    # defence: every block die counts; a failed dodge takes the full damage; no parry
    block='sum', dodge_fail='full', dodge_extra=False, dodge_move=False, parry=False,
    # death: any death defeats the party; a full bar kills; a win clears the whole bar
    death='party', lethal='full', recover='all', hollow_bar=10,
    # no enemy scaling
    hp=lambda h, n: h, atk=lambda n: 0, move2=lambda n: False, reps=lambda n: 1, push_once=False,
    stagger='official', frost='official', poison='single', bleed='official', ember=False, estus='full',
    # economy: one shared soul cache; two souls a character for an encounter; a boss pays a soul a character for
    # each spark left; a treasure card costs one soul, drawn blind; a lone character starts with sixteen souls
    pool=True, souls=lambda level, n, first: 2 * n, boss_souls=lambda n, sparks: n * sparks, solo_souls=16,
    treasure='draw', draw_cost=1, shop_limit=None, free_treasure=lambda level, n: 0.0, tier4=None,
    # the bonfire: a rest costs a spark and resets every encounter; no skipping; the sparks are reset after the mini-boss
    skip_cost=None, fog_gate=False, boss_spark='reset', luck_cost=1, free_visit=True,
)

# 2022: the same combat rules. What changes is the economy and the track (pages 16 to 19 and 26 to 27):
#   rewards are printed on each encounter card (souls, treasure draws); averaged here over the Tomb of Giants deck;
#   Andre shows four cards a visit, one soul each; the spark dial rises by one after the mini-boss.
_R22 = {1: (1.3, 0.3), 2: (3.0, 0.6), 3: (5.0, 1.0)}        # level: (souls beyond one per player, treasure cards)
OFFICIAL_2022 = OFFICIAL_2017.but(
    name='Official 2022',
    souls=lambda level, n, first: n + _R22[level][0], free_treasure=lambda level, n: _R22[level][1],
    boss_souls=lambda n, sparks: 0, treasure='shop4', shop_limit=4, boss_spark='plus1', solo_souls=0, choose_of_two=True,
    free_visit=False,
)

MANUSCRIPT = Rules(
    name="Author's manuscript", **{**_COMMON, 'tier_cost': (2, 4, 8, 8)},
    # the round: every enemy in descending threat, then every character in descending threat
    round='all', order='threat', aggro='most', regen=1, turn='major',
    # defence: the two highest block dice; a failed dodge still rolls the armour; extra dodge dice for stamina;
    # parry with a shield in the left slot
    block='best2', dodge_fail='armour', dodge_extra=True, dodge_move=True, parry='shield',
    # death: the dead are revived hollow if the encounter is cleared; lost if all die or a hollow character dies
    death='hollow', lethal='overflow', recover='sta+1', hollow_bar=8,
    # enemy scaling, as the manuscript's table
    hp=plus(1), atk=lambda n: 1 if n >= 3 else 0, move2=lambda n: n >= 2, reps=lambda n: 2 if n >= 4 else 1, push_once=True,
    stagger='author', frost='author', poison='stack', bleed='author', ember=True, estus='health',
    # economy: souls are personal; three, four, five for Levels 1, 2, 3 and six for a boss; a treasure card each on a
    # first clear; Andre's shop at two souls (tier one) and four (tier two); a lone character starts with six souls
    pool=False, souls=lambda level, n, first: {1: 3, 2: 4, 3: 5}[level] // (1 if first else 2), boss_souls=lambda n, sparks: 6,
    solo_souls=6, treasure='author', draw_cost=None, shop_limit=None, free_treasure=lambda level, n: 1.0, tier4=5,
    # the bonfire: a rest costs a spark; cleared encounters may be skipped for two stamina each; the fog gate is a
    # shortcut once a boss has been reached; one spark is added for each boss
    skip_cost=2, fog_gate=True, boss_spark='plus1', luck_cost=None, free_visit=False,
    grip_reroll=True, scaling=True,
)

# The ruleset settled in the workshop (section 9.6): the manuscript with the party choosing its turn order, aggro to
# the last character to deal damage, parry with anything in the left slot, and the scaling under test.
SETTLED = MANUSCRIPT.but(name='Settled (section 9.6)', order='free', aggro='last', parry='any',
                         hp=lambda h, n: h + 2 * max(0, n - 2), atk=lambda n: n - 1, move2=lambda n: False,
                         reps=lambda n: 1)


# ---------------------------------------------------------------- building variants by name (picklable specs)
BASES = {'official2017': OFFICIAL_2017, 'official2022': OFFICIAL_2022, 'manuscript': MANUSCRIPT, 'settled': SETTLED}


def make(spec):
    """spec: {'base': name, plus any Rules field; scaling may be given as per-party-size lists:
    hp_add=[_, n1, n2, n3, n4] (added health), hp_mul=[...] (health multiplier), atk=[...], reps=[...], move2=[...]}."""
    spec = dict(spec); r = BASES[spec.pop('base')]; kw = {}
    add = spec.pop('hp_add', None); mul = spec.pop('hp_mul', None)
    if add or mul:
        kw['hp'] = lambda h, n, add=add, mul=mul: int(round(h * (mul[n] if mul else 1))) + (add[n] if add else 0)
    for k in ('atk', 'reps', 'move2', 'sparks', 'boss_mul'):
        if k in spec:
            v = spec.pop(k); kw[k] = lambda n, v=v: v[n]
    if 'soul_mul' in spec:
        m = spec.pop('soul_mul'); base_souls = r.souls; base_boss = r.boss_souls
        kw['souls'] = lambda level, n, first: int(round(base_souls(level, n, first) * m))
        kw['boss_souls'] = lambda n, sparks: int(round(base_boss(n, sparks) * m))
    kw.update(spec)
    return r.but(**kw)
