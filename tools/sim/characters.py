#!/usr/bin/env python3
"""Characters, equipment and the bonfire economy for the rules simulator.

A character carries real equipment cards (gear.json, gear_more.json): a right-hand item, a left-hand item and armour,
with upgrade cards fitted to them and spells stored in a catalyst. Its combat profile (block, resist and dodge dice,
attack and support options, the traits its cards' text gives it) is derived from those cards. At the bonfire the
simulated players spend souls by a greedy rule: take whichever purchase or level-up buys the most `power` per soul.
"""
import json, os
from engine import pmf_def, attack_pmf, hit_stats, p_dodge

HERE = os.path.dirname(os.path.abspath(__file__))
GEAR = json.load(open(os.path.join(HERE, 'gear.json')))
ITEMS = GEAR['items']
# The treasure of the other 2017 sets, every boss's treasure and the six other classes (gear_more.json). The treasure is
# used where a ruleset says sets='all'; the classes can be played under any ruleset.
_MORE = json.load(open(os.path.join(HERE, 'gear_more.json')))
MORE = _MORE['items']
CLASSES = dict(GEAR['classes']); CLASSES.update(_MORE['classes'])
# The treasure of the 2022 sets the author owns (gear_2022.json): in the decks where a ruleset says sets='all'.
Y22 = json.load(open(os.path.join(HERE, 'gear_2022.json')))['items']
CARDS = dict(ITEMS); CARDS.update(MORE); CARDS.update(Y22)
# The author's card amendments (the manuscript's appendices A and B; amendments.json): played where a ruleset says
# revised=True, which the manuscript and every ruleset built on its turn rules do. The official presets play the cards as printed.
AMEND = json.load(open(os.path.join(HERE, 'amendments.json')))
_base = lambda k: k.split(' (')[0].split(' [')[0]
for _k, _v in CARDS.items():
    _b = _base(_k)
    if _b in AMEND['req'] and _v['type'] == 'hand': _v['req_ms'] = AMEND['req'][_b]
    if _b in AMEND['cards']:
        for _f, _x in AMEND['cards'][_b].items(): _v[_f + '_ms'] = _x
    if _b in AMEND['traits']: _v['traits_ms'] = tuple(AMEND['traits'][_b])
for _k, _v in Y22.items(): _v['added_ms'] = _base(_k) in AMEND['added'] or _base(_k).replace('Armour', 'Armor') in AMEND['added']


def revised(r): return bool(getattr(r, 'revised', False))
def req_of(it, r): return it['req_ms'] if (revised(r) and 'req_ms' in it) else it['req']
def deck_of(it, r): return it['deck_ms'] if (revised(r) and 'deck_ms' in it) else it['deck']
CORE4 = ['Knight', 'Warrior', 'Herald', 'Assassin']
ALL10 = CORE4 + sorted(_MORE['classes'])
STURDY = ('Knight', 'Warrior')                       # the classes a lone player or a pair is assumed to include
# The heroic action of each class as the engine plays it, and how well its wording is established. The four core
# classes are as printed. Of the six others no printed board could be read: three rest on community transcriptions of
# the 2017 boards, two on the 2022 rulebook's wording for the same class, and the Deprived's could not be found at all.
HEROIC = {
    'Knight': ('after a block roll, one more blue die', 'printed'),
    'Warrior': ('a free step; the next range 0 attack costs no stamina and strikes the node', 'printed'),
    'Herald': ('each character gains 2 stamina', 'printed'),
    'Assassin': ('after a successful dodge, a free attack on the enemy dodged', 'printed'),
    'Mercenary': ('Rapid Strike: one attack costs no stamina', 'community transcription, incomplete'),
    'Sorcerer': ('Spell Fury: a magic attack reaches any distance and costs 3 less', 'community transcription'),
    'Pyromancer': ('Explosive Crit: one attack gains a black die', "inferred from the Great Swamp Ring's text and the 2022 wording"),
    'Cleric': ('this character and each character on the same or an adjacent node heals 2', '2022 rulebook wording'),
    'Thief': ('heals 2 damage and recovers 2 stamina', '2022 rulebook wording, without its luck token'),
    'Deprived': ('none played', 'not found'),
}

# ---------------------------------------------------------------- what a card's text does
# Every text printed on a card of the 2017 sets, and the trait or traits it gives. A trait is a short key that the
# profile below or the engine acts on. A text in NOT_PLAYED is carried on its card and does nothing, for the reason given.
TRAITS = {
    'You cannot dodge': ('no_dodge',),
    'You cannot dodge or walk': ('no_dodge', 'no_walk'),
    'You cannot dodge or run': ('no_dodge', 'no_run'),
    'You can dodge without spending stamina': ('dodge_free',),
    'Dodging costs you 2 Stamina (instead of 1)': ('dodge_dear',),
    'You can dodge attacks from Alonne Knights without spending Stamina': ('alonne',),
    'You gain +1 dodge against Hollows': ('vs_hollow',),
    'You gain 1 dodge against boss arc attacks': ('vs_boss',),
    'You gain 2 dodge if the attacker is 2 or more nodes away': ('vs_far',),
    'When you dodge, you may move 2 nodes (instead of 1)': ('dodge2',),
    'When you walk, you may move 2 nodes (instead of 1)': ('walk2',),
    'When you run, it costs 2 stamina per node (instead of 1)': ('run2',),
    'You are immune to Bleed': ('im_bleed',),
    'You are immune to Poison': ('im_poison',),
    'You are immune to Frostbite': ('im_frost',),
    'You are immune to Bleed and Poison': ('im_bleed', 'im_poison'),
    "Ignore push icons on Enemies' physical and magical attack behaviours": ('im_push',),
    'You can equip this in one hand while you have a two-handed weapon in your other hand': ('offhand',),
    'Reduce the stat requirements of your armour upgrade by 2': ('ring_ease',),
    'When you make an AOE attack, reduce the stamina cost by 1': ('aoe_cheap',),
    'Your highest-stamina one-handed attack costs -1 stamina': ('royal',),
    'Your attacks gain 1 orange die -2': ('hornet',),
    'Your magic attacks gain +1 damage': ('tiara',),
    'Your magic attacks cost -2 Stamina; when you make a magic attack you suffer 1 Damage': ('duskcrown',),
    'Your magic attacks cost +1 Stamina but gain 1 black die': ('manus',),
    'You suffer -1 success on each Block, Resist, and Dodge roll, but gain +1 success on each Attack roll': ('calamity',),
    'Your range 0 attacks gain push': ('minotaur',),
    'You can place a cube here instead of on your endurance bar (remove the cube when an encounter ends)': ('life',),
    'After you suffer damage from an enemy attack, gain 1 stamina': ('tearstone',),
    'Characters in your node gain 3 stamina at the start of their activations (instead of 2)': ('chloranthy',),
    'At the start of your activation, you may gain 1 stamina and 1 health (instead of 2 stamina)': ('tinybeing',),
    'When you end your activation, gain 1 health': ('sunprincess',),
    'When you end your activation, gain 1 health for each enemy on your node': ('lothric',),
    'At the start of your activation, gain 1 health': ('sanctus',),
    'At the end of your activation, if you made two or more attack rolls, gain 1 Health': ('pontiff',),
    'At the end of your activation, if you made two or more attack rolls, gain 1 stamina': ('favour',),
    "After you make an attack that exceeds an enemy's Block or Resist value by 3 or more, gain 1 stamina": ('knightslayer',),
    'At the start of your activation, you may suffer 1 damage to flip your Luck token to the ready side': ('blades',),
    'Your attacks gain +1 damage against enemies that damaged you during the last enemy activation': ('leo',),
    'After you make a block or resist roll against an enemy in your node, it suffers 1 damage': ('thorns',),
    'After a Hollow on your node attacks you, you may push that Hollow': ('sunset',),
    "Once per encounter at the end of another character's activation, you may take the Aggro token": ('faraam',),
    'When you use your heroic ability, gain 1 health': ('hero_hp',),
    'When you use your heroic ability, gain 1 stamina': ('hero_sta',),
    'When you use your heroic ability, you may remove one condition token from a character': ('hero_cleanse',),
    'Encounters reward the party with 1 additional soul': ('serpent',),
    'If the party defeats an encounter and does not open a chest, add 1 card from the treasure deck to the inventory': ('serpent2',),
    'You may roll your dodge dice before you decide whether to dodge of block/resist': ('wolf',),
    "Once per spark, the party may take their first activation before the enemies' first activation": ('mon',),
    'When you use the Spell Fury heroic ability, your attack deals +1 damage': ('dragoncrest',),
    'When you use the Explosive Crit heroic ability, instead of gaining a black die, you gain a blue die': ('swamp',),
    # upgrades fitted to a weapon
    "This weapon's attacks gain +1 damage": ('mod',),
    "This weapon's attacks gain 1 black die": ('die',),
    "This weapon's attacks gain Bleed": ('w_bleed',),
    "This weapon's attacks gain Poison": ('w_poison',),
    "This weapon's attacks gain Magic": ('w_magic',),
    "Reduce the cost of this weapon's highest stamina attack by 1 stamina": ('w_simple',),
    "This weapon's attacks gain +2 damage but cost +2 stamina": ('w_raw',),
    "This weapon's attacks gain +1 damage and magic": ('mod', 'w_magic'),
    "This weapon's 0 range attacks gain 1 range and magic": ('w_flash',),
    "If this weapon's attack deals 0 damage, you may flip your Luck token to the ready side": ('w_hollow',),
    # texts that come with the 2022 sets (wording from a community table of card values)
    "This weapon's attacks gain +1 damage. If this weapon is a boss treasure, reduce the cost of its highest-stamina attack by 1 stamina": ('mod',),
    "This weapon's attacks gain +2 damage against bosses. This upgrade occupies 2 slots": ('w_boss2',),
    "This weapon gains 1 upgrade slot. This weapon's attacks gain Magic": ('w_magic',),
    'This weapon gains +1 damage against Hollows': ('w_vs_hollow',),
    'After you attack with this weapon, you suffer Bleed': ('w_selfbleed',),
    'All of your attacks gain +1 damage while you have four or more damage cubes on your endurance bar': ('redtear',),
    'During your activation, you may permanently discard this card to remove all damage and conditions from your character': ('blessing',),
    'This armor gains 1 physical BLK and 1 magical BLK if it has an equipped ring': ('steel',),
    'When one of your equipment cards allows a character to gain health, they gain +1 health': ('mender',),
    "When you attack an enemy's weak arc, instead of gaining an additional 1 BLK, gain an additional 1 BLU": ('weak_blue',),
    'When you make a magical attack, reduce the stamina cost by 1': ('xanthous',),
    'You may gain 3 stamina at the start of your activation (instead of 2)': ('mask',),
}
NOT_PLAYED = {
    'You gain +1 dodge against traps': 'traps are not played',
    'At the start of each trapped encounter, you may look at 2 trap tokens': 'traps are not played',
    'You can use one-handed magic attacks in your backup slot as if they were equipped': 'the backup slot is not played (the manuscript has catalysts instead)',
    'Tier 3 for each of your stats is 40 while you have this equipped': "a mega boss's treasure: never dealt in a standard game",
    'You may place this character on any entry node (not just entry nodes aligned with the tile you moved from)': "a mega boss's treasure; tile entry is not played",
    'You may look at face-down encounter cards': "a mega boss's treasure; the players do not scout",
    'During your activation, you may discard this card to end an encounter and return to the Bonfire tile': "a mega boss's treasure: never dealt in a standard game",
    'You may discard this card to replace an encounter card with a random encounter card of the same level': "a mega boss's treasure: never dealt in a standard game",
    'Immediately gain an Ember token and discard this card': 'embers are handled by the ruleset, not as a treasure card',
    'Once during each of your activation, you may look at one trap token in this encounter and return it face down': 'traps are not played',
    'When a character in your node would suffer damage, you can suffer the damage instead': 'a choice between characters that the simulated players do not make',
}
# What a trait the dice do not show is worth, in the units of `power` (a judgement; varied in the robustness runs)
TRAIT_VALUE = dict(sunprincess=0.8, sanctus=0.8, lothric=0.4, tinybeing=0.5, tearstone=0.4, chloranthy=0.6, favour=0.3, pontiff=0.4,
                   knightslayer=0.3, blades=0.5, leo=0.4, thorns=0.4, sunset=0.1, faraam=0.2, hero_hp=0.15, hero_sta=0.15, hero_cleanse=0.1,
                   serpent=0.6, serpent2=0.8, wolf=0.5, mon=0.4, life=0.6, im_bleed=0.15, im_poison=0.15, im_frost=0.1, im_push=0.1,
                   dodge2=0.1, walk2=0.3, run2=-0.2, no_walk=-0.5, no_run=-0.3, vs_hollow=0.15, vs_boss=0.2, vs_far=0.2, alonne=0.05,
                   w_hollow=0.2, dragoncrest=0.2, swamp=0.2, redtear=0.3, blessing=0.8, mender=0.2, weak_blue=0.15, mask=0.6,
                   milk=0.5, chlor_ms=0.6, tiny_ms=0.8, wolf_ms=0.4)
FX_VALUE = dict(bleed=0.5, poison=0.6, stagger=0.4, frostbite=0.15)


def text_traits(it, r=None):
    """The traits a card's own text gives (an upgrade card's traits are those it gives the card it is fitted to). Under a
    ruleset that plays the author's amendments, a card whose text the manuscript replaces gives the traits of the new text."""
    if not it: return ()
    if revised(r) and 'traits_ms' in it: return it['traits_ms']
    return TRAITS.get((it.get('text') or '').rstrip('.'), ())


def up_of(it, r):
    """The traits an upgrade card gives the card it is fitted to under ruleset r; None if its text is not played."""
    return (it['traits_ms'] if (revised(r) and 'traits_ms' in it) else it.get('up')) or None


for _i in CARDS.values():
    if _i['type'] == 'upgrade': _i['up'] = text_traits(_i) or None      # None: carried in the decks but never fitted
SPELLS = {k for k, v in CARDS.items() if v.get('spell')}               # sorceries, miracles, pyromancies: never scaled, never two-handed
REF_FOES = ((1, 1, 1), (1, 1, 5), (2, 1, 5), (2, 1, 10))            # (block, resist, health) of reference targets
REF_HITS = ((4, False, 1), (5, False, 1), (5, False, 2), (6, False, 1), (6, False, 2), (4, True, 1), (5, True, 2))   # (damage, magic, dodge difficulty)
EXTRA = ('fx', 'push', 'shift', 'gain_hp', 'gain_sta', 'self_dmg', 'ember_mod', 'area', 'same', 'aggro', 'direct', 'sup', 'guard', 'buff')


def is_shield(it): return it is not None and it['type'] == 'hand' and not it['attacks'] and it['name'] not in SPELLS and not it.get('catalyst')
def has_dice(it): return it is not None and it['type'] == 'hand' and any(a['dice'] for a in it['attacks'])


class Char:
    def __init__(self, cls, rules):
        k = CLASSES[cls]
        self.name, self.r, self.base, self.taunt = cls, rules, k['stats'], k['taunt']
        self.tier = [0, 0, 0, 0]
        kit = [CARDS[x] for x in k['start']] + ([CARDS['Talisman']] if cls == 'Herald' else [])
        self.start = {x['name'] for x in kit}         # starting equipment: it cannot be sold
        self.bag = []; self.plus = {}                 # spare cards; card name -> the traits its fitted upgrades give
        self.up_cards = {}                            # card name -> the upgrade cards fitted to it
        self.spells = []                              # spells kept for a catalyst (the manuscript, 4.3)
        self.souls = 0; self.earned = 0
        self.dmg = self.sta = 0; self.hollow = False; self.alive = True; self.was_hollow = False
        self.estus = self.luck = self.heroic = True; self.ember = False; self.ember_card = False; self.mon = True
        self.node = 0; self.stagger = self.frost = self.bleed = False; self.poison = 0; self.ran = False
        self.guards = []; self.buff = None; self.hurt_by = set(); self.rolls = 0     # guards: defence dice lent for a time (block, resist, until)
        self.bless = True                             # a card that is discarded for good when used has not been used
        self.A = next(x for x in kit if x['type'] == 'armour'); hands = [x for x in kit if x['type'] == 'hand']
        # three hand cards for two hands: the pair that makes the stronger character is carried, the third kept spare
        best = None
        for R in hands:
            if not has_dice(R): continue
            for L in [None] + [x for x in hands if x is not R]:
                if L is not None and R['hands'] == 2 and 'offhand' not in text_traits(L, rules): continue
                if L is not None and L['hands'] == 2: continue
                self.R, self.L = R, L; v = power(self.profile(), rules)
                if best is None or v > best[0] + 1e-9: best = (v, R, L)
        _, self.R, self.L = best
        self.bag = [x for x in hands if x is not self.R and x is not self.L]
        self.refresh()

    # ---------------------------------------------------------------- stats and requirements
    @property
    def cap(self): return (self.r.hollow_bar if self.hollow else self.r.bar) + (1 if 'life' in self.traits else 0)

    def value(self, i, t):
        return self.base[i][min(t, 3)] + (self.r.tier4 if (t >= 4 and self.r.tier4) else 0)

    def max_tier(self): return 4 if self.r.tier4 else 3

    def cost_to_meet(self, req, tiers=None):
        """Souls needed to raise stats until `req` is met, and the resulting tiers; None if it cannot be met."""
        tiers = list(tiers or self.tier); tot = 0
        for i in range(4):
            while self.value(i, tiers[i]) < req[i]:
                if tiers[i] >= self.max_tier(): return None
                tot += self.r.tier_cost[min(tiers[i], len(self.r.tier_cost) - 1)]; tiers[i] += 1
        return tot, tiers

    def meets(self, req, tiers=None):
        tiers = tiers or self.tier
        return all(self.value(i, tiers[i]) >= req[i] for i in range(4))

    # ---------------------------------------------------------------- combat profile
    def profile(self, R=None, L=None, A=None, tiers=None, plus=None, spells=None):
        R = self.R if R is None else R; L = self.L if L is None else L; A = self.A if A is None else A
        if L is False: L = None
        tiers = tiers or self.tier; plus = self.plus if plus is None else plus; r = self.r
        spells = self.spells if spells is None else spells
        worn = [x for x in (A, R, L) if x]
        p = dict(R=R, L=L, A=A, cls=self.name, heavy=getattr(self, 'heavy', (3, 2)))
        traits = set()
        for x in worn: traits.update(text_traits(x, r))
        if A: traits.update(plus.get(A['name'], ()))                  # rings and the like, fitted to the armour
        p['traits'] = traits
        cal = 1 if 'calamity' in traits else 0
        p['blk'] = ''.join(x.get('block', '') for x in worn); p['res'] = ''.join(x.get('resist', '') for x in worn)
        p['arm_blk'] = A.get('block', '') if A else ''; p['arm_res'] = A.get('resist', '') if A else ''
        p['blk_pen'] = cal - sum(x.get('block_mod', 0) for x in worn); p['res_pen'] = cal - sum(x.get('resist_mod', 0) for x in worn)
        p['arm_blk_pen'] = cal - (A.get('block_mod', 0) if A else 0); p['arm_res_pen'] = cal - (A.get('resist_mod', 0) if A else 0)   # the armour's own, for a failed dodge
        if A and 'steel' in traits and plus.get(A['name']):               # an armour that is stronger with a ring fitted
            for k in ('blk', 'res', 'arm_blk', 'arm_res'): p[k] += 'b'
        p['parry_n'] = sum(x.get('dodge', 0) for x in worn)               # a parry rolls the dodge dice printed on the cards, whatever forbids a dodge
        p['dodge'] = 0 if 'no_dodge' in traits else p['parry_n']
        p['dodge_pen'] = cal
        p['two'] = bool(R and R['hands'] == 2)
        opts = {'R': [], 'L': []}; sup = {'R': [], 'L': []}
        for hand, it in (('R', R), ('L', L)):
            if not it: continue
            other = L if hand == 'R' else R
            wt = plus.get(it['name'], ()) if it is not A else ()
            cards = [it]
            if it.get('catalyst') and getattr(r, 'catalyst', False):
                # a catalyst gives the attack options of up to three stored spells of its school, if their requirements are met
                cards += [x for x in spells if x.get('school') == it['catalyst'] and self.meets(req_of(x, r), tiers)][:3]
            mine = []
            for card in cards:
                spell = card['name'] in SPELLS; own = card is it
                bonus = 0
                cr = req_of(card, r)                              # the requirements the ruleset plays: revised where the manuscript revises them
                if getattr(r, 'scaling', False) and has_dice(card) and max(cr) > 0 and not spell:
                    top = max(cr)                                 # where requirements tie for the highest, any of them may be chosen
                    if any(self.value(j, tiers[j]) - top >= 10 for j in range(4) if cr[j] == top):
                        bonus = 1                                 # the manuscript's stat scaling: +1 at ten over the requirement
                for a in card['attacks']:
                    o = dict(name=card['name'], hand=hand, cost=a['cost'], dice=a['dice'], mod=a['mod'], magic=a['magic'], range=a['range'],
                             repeat=a['repeat'], shaft=a['shaft'], ignore=a.get('ignore', False), node=a.get('node', False), spell=spell,
                             reroll=bool(getattr(r, 'grip_reroll', False) and not spell and (card['hands'] == 2 or other is None)))
                    for k in EXTRA:
                        if k in a: o[k] = list(a[k]) if k == 'fx' else a[k]
                    if not (a['dice'] or o.get('fx') or o.get('direct')):
                        if any(k in o for k in ('sup', 'guard', 'buff', 'gain_sta')): sup[hand].append(o)
                        continue                                  # a text that is not played leaves nothing to do
                    if a['dice']:
                        o['mod'] += bonus
                        if own:                                   # upgrades fitted to this weapon
                            o['mod'] += wt.count('mod') + 2 * wt.count('w_raw'); o['dice'] += 'b' * wt.count('die'); o['cost'] += 2 * wt.count('w_raw')
                            if 'w_bleed' in wt: o['fx'] = o.get('fx', []) + ['bleed']
                            if 'w_poison' in wt: o['fx'] = o.get('fx', []) + ['poison']
                            if 'w_magic' in wt: o['magic'] = True
                            if 'w_flash' in wt and o['range'] == 0: o['range'] = 1; o['magic'] = True
                            if 'w_hollow' in wt: o['hollow'] = True
                            if 'w_boss2' in wt: o['vs_boss'] = 2 * wt.count('w_boss2')
                            own_t = text_traits(card, r)              # what the weapon's own text adds to its attacks
                            if 'w_vs_hollow' in own_t: o['vs_hollow'] = 1
                            if 'w_selfbleed' in own_t: o['self_fx'] = ['bleed']
                        if 'hornet' in traits: o['dice'] += 'o'; o['mod'] -= 2
                        if 'calamity' in traits: o['mod'] += 1
                        if o['magic']:
                            if 'tiara' in traits: o['mod'] += 1
                            if 'manus' in traits: o['cost'] += 1; o['dice'] += 'b'
                            if 'duskcrown' in traits: o['cost'] = max(0, o['cost'] - 2); o['self_dmg'] = o.get('self_dmg', 0) + 1
                            if 'xanthous' in traits: o['cost'] = max(0, o['cost'] - 1)
                        if o['range'] == 0 and 'minotaur' in traits: o['push'] = True
                        if o['node'] and 'aoe_cheap' in traits: o['cost'] = max(0, o['cost'] - 1)
                    opts[hand].append(o); mine.append((o, own))
            own_opts = [o for o, own in mine if own and o['dice']]
            if 'w_simple' in wt and own_opts: top = max(own_opts, key=lambda o: o['cost']); top['cost'] = max(0, top['cost'] - 1)
        if 'royal' in traits:
            one = [o for h, it in (('R', R), ('L', L)) if it and it['hands'] == 1 for o in opts[h] if o['dice'] and o['name'] == it['name']]
            if one: top = max(one, key=lambda o: o['cost']); top['cost'] = max(0, top['cost'] - 1)
        p['options'] = opts; p['support'] = sup
        p['mean_blk'] = sum(v * q for v, q in pmf_def(p['blk'], r.block)) - p['blk_pen']
        p['mean_res'] = sum(v * q for v, q in pmf_def(p['res'], r.block)) - p['res_pen']
        p['can_parry'] = bool(r.parry and L and not p['two'] and (is_shield(L) or r.parry == 'any'))
        return p

    def refresh(self):
        p = self.profile()
        for k in ('blk', 'res', 'arm_blk', 'arm_res', 'blk_pen', 'res_pen', 'arm_blk_pen', 'arm_res_pen', 'dodge', 'parry_n', 'dodge_pen', 'options',
                  'support', 'mean_blk', 'mean_res', 'can_parry', 'traits'):
            setattr(self, k, p[k])
        self.two_handed = p['two']; self._power = power(p, self.r)
        best = 0.0
        for o in self.options['R']:
            if o.get('spell'): continue                     # a riposte is never made with a spell
            if o['cost'] <= 2 and o['range'] == 0 or (o['cost'] <= 2 and not o['shaft']):
                best = max(best, sum(x * q for x, q in attack_pmf(o['dice'], o['mod'], 1, o['repeat'])))
        self._rip = best

    def scale_bonus(self, o): return 0                # stat scaling is already folded into each option's modifier

    def rearm(self, block, resist):
        """Before a boss whose block and resist are on its data card, the character takes from its own inventory the hand
        cards that serve best against it (outside an encounter cards move freely between the inventory and the slots:
        the manuscript, 3.2). Returns what to hand back to restore() after the fight, or None if nothing changed."""
        r = self.r
        pool = [x for x in (self.R, self.L) if x is not None] + [i for i in self.bag if i['type'] == 'hand' and self.meets(req_of(i, r))]
        if len(pool) <= (self.R is not None) + (self.L is not None): return None
        now = power(self.profile(), r, vs=(block, resist)); top = (now + 0.05, None)
        for a in pool:
            for b in [None] + [x for x in pool if x is not a]:
                if a['hands'] == 2 and b is not None and 'offhand' not in text_traits(b, r): continue
                if b is not None and b['hands'] == 2: continue
                if (a is self.R and b is self.L): continue
                got = power(self.profile(R=a, L=(b if b is not None else False)), r, vs=(block, resist))
                if got > top[0]: top = (got, (a, b))
        if top[1] is None: return None
        was = (self.R, self.L, list(self.bag))
        a, b = top[1]; held = [x for x in (self.R, self.L) if x is not None]
        self.bag = [i for i in self.bag if i is not a and i is not b] + [x for x in held if x is not a and x is not b]
        self.R, self.L = a, b; self.refresh()
        return was

    def restore(self, was):
        if was is None: return
        self.R, self.L, self.bag = was; self.refresh()
    def riposte_ev(self, foe): return self._rip

    def best_option(self, foe, dist, budget, hand='R', spells=True):
        best = None
        for o in self.options[hand]:
            if o['cost'] + o.get('self_dmg', 0) > budget or o['range'] < dist or (o['shaft'] and dist == 0) or o.get('direct'): continue
            if o.get('spell') and not spells: continue      # a riposte is never made with a spell
            ev = sum(x * q for x, q in attack_pmf(o['dice'], o['mod'], foe.resist if o['magic'] else foe.armor, o['repeat'])) - 0.4 * o['cost']
            if best is None or ev > best[0]: best = (ev, o)
        return best[1] if best else None

    # ---------------------------------------------------------------- the bonfire
    def full_rest(self):
        self.dmg = self.sta = 0; self.hollow = False; self.alive = True; self.estus = self.luck = self.heroic = True; self.mon = True
        self.stagger = self.frost = self.bleed = False; self.poison = 0


def sup_worth(o, n=2):
    """What a support action is worth as a standing option, in the units of `power`: healing most, stamina less."""
    v = 0.0
    if 'sup' in o:
        wide = {'one': 1.0, 'two': 1.3, 'all': 1.5, 'others': 1.2, 'node': 1.3}[o['sup']['who']]
        v = (0.45 * min(4, o['sup']['hp']) + 0.12 * min(4, o['sup']['sta'])) * wide
    elif 'guard' in o: v = 0.35
    elif 'buff' in o: v = 0.3 + 0.2 * o['buff']['mod']
    elif 'gain_sta' in o: v = 0.12 * o['gain_sta']
    return v - 0.12 * o['cost']


def power(p, r, vs=None):
    """A single figure for how strong a loadout is: the damage it deals in a turn against lightly, medium and heavily
    armoured targets, less the damage it lets through from a spread of attacks, plus what its support actions and the
    text of its cards are judged to be worth. Defence counts for more than offence, because a death costs the party
    far more than a slow fight. With vs=(block, resist) the damage is judged against that one target, a boss whose
    data card the players can see, in place of the spread."""
    one_spell = getattr(r, 'one_spell', False)

    def best(block, resist, cap):
        top = 0.0
        for ro in p['options']['R'] or [None]:
            for lo in ([None] + p['options']['L']):
                if one_spell and ro and lo and ro.get('spell') and lo.get('spell'): continue
                tot = 0.0; cost = 0
                for o in (ro, lo):
                    if o is None: continue
                    if o.get('direct'): tot += min(o['direct'], cap) * 0.6; cost += o['cost']; continue
                    pm = attack_pmf(o['dice'], o['mod'], 0 if o['ignore'] else (resist if o['magic'] else block), o['repeat'])
                    hit = sum(min(x, cap) * q for x, q in pm) * (1.3 if o.get('area') else 1.0)
                    hit += sum(FX_VALUE[k] for k in o.get('fx', ())) + 0.1 * bool(o.get('push')) + 0.5 * o.get('gain_hp', 0) - 0.8 * o.get('self_dmg', 0)
                    tot += hit; cost += o['cost']
                if cost <= 5: top = max(top, tot - 0.3 * cost)
        return top
    hv = p.get('heavy', (3, 2))                             # the sturdy target: the boss the party knows it will meet, once it is named
    off = best(vs[0], vs[1], 30) if vs else 0.25 * best(1, 1, 5) + 0.4 * best(2, 1, 10) + 0.35 * best(hv[0], hv[1], 30)
    quick = 0.0                                             # felling a one-health, block-two enemy with a cheap attack
    for hand in 'RL':
        for o in p['options'][hand]:
            if o['cost'] <= 2 and o['dice']:
                quick = max(quick, sum(q for x, q in attack_pmf(o['dice'], o['mod'], 1 if o['magic'] else 2, o['repeat']) if x >= 1))
    if any(o['range'] >= 1 for h in 'RL' for o in p['options'][h]): off += 0.15
    if not any(o['dice'] or o.get('direct') for h in 'RL' for o in p['options'][h]): off -= 3.0     # no way to wound an enemy at all
    for hand in 'RL':                                       # a hand that can heal or steady the party: its best action, and a little for a second
        w = sorted((sup_worth(o) for o in p['support'][hand]), reverse=True)
        if w: off += max(0.0, 0.6 * w[0]) + (max(0.0, 0.2 * w[1]) if len(w) > 1 else 0.0)
    traits = p['traits']
    off += sum(TRAIT_VALUE.get(t, 0.0) for t in traits if not (t == 'dragoncrest' and p['cls'] != 'Sorcerer') and not (t == 'swamp' and p['cls'] != 'Pyromancer'))
    taken = 0.0
    for dmg, magic, k in REF_HITS:
        dice = p['res'] if magic else p['blk']; pen = p['res_pen'] if magic else p['blk_pen']
        blk = sum(d * q for d, q in hit_stats(dice, r.block, dmg, pen))        # a printed bonus counts as a printed penalty does
        if p['dodge'] > 0:
            ps = p_dodge(p['dodge'], k + p['dodge_pen'])
            adice = p['arm_res'] if magic else p['arm_blk']
            fail = sum(d * q for d, q in hit_stats(adice, r.block, dmg, p['arm_res_pen'] if magic else p['arm_blk_pen'])) if r.dodge_fail == 'armour' else dmg
            price = 0.0 if 'dodge_free' in traits else 0.8 if 'dodge_dear' in traits else 0.4
            blk = min(blk, (1 - ps) * fail + price)
        taken += blk / len(REF_HITS)
    return off + (0.0 if vs else 0.8 * quick) - 1.6 * taken


class Economy:
    """The treasure decks, the shop and the spending of souls, for one game."""

    def __init__(self, party, rules, rng):
        self.party, self.r, self.rng = party, rules, rng
        self.pool = 0                                  # the shared soul cache of the official rules
        self.row = []                                  # Andre's face-up cards, where the ruleset has them
        self.embers = len(party)                       # the manuscript's shop: ember cards equal to the number of characters
        self.inv = []                                  # the shared inventory of the official rules
        self.carried = {}                              # upgrades on weapons lying in it: weapon name -> (bonus, upgrade card)
        self.n_found = self.n_bought = self.n_sold = 0  # treasure cards found, bought and sold in this game
        names = {c.name for c in party}
        cards = [i for i in ITEMS.values() for _ in range(i.get('copies', 1))]
        self.boss_loot = []
        sets = getattr(rules, 'sets', 'core')
        if sets in ('2017', 'all'):
            # every owned set: the other sets' common, class, transposed and legendary cards join the core set's, whoever
            # is playing; the treasure of the two bosses of this game is kept apart until the mini-boss falls
            cards += [i for i in MORE.values() if i['deck'] != 'boss']
        if sets == 'all':
            # the 2022 sets' cards. The manuscript adds the cards that are new in those sets (its Additional Treasure)
            # and does not add their reprints of older cards a second time; as printed, every card joins
            cards += [i for i in Y22.values() if deck_of(i, rules) != 'boss' and (i['added_ms'] or not revised(rules))]
        if revised(rules): cards = [dict(i, deck=deck_of(i, rules)) if 'deck_ms' in i else i for i in cards]
        common = [i for i in cards if i['deck'] == 'common']
        legend = rng.sample([i for i in cards if i['deck'] == 'legendary'], 5)
        if rules.treasure == 'author':
            # the manuscript: every common, class and transposed card, split at a requirement of 25; legendaries join tier two
            pool = common + [i for i in cards if i['deck'] in ('class', 'transposed')]
            two = lambda i: max(req_of(i, rules)) >= 25 or i['deck'] == 'transposed'
            split = getattr(rules, 'deck_split', 'req')
            if split in ('type', 'type_all', 'kind'):
                # a split by kind of card, for comparison: common and class treasure in tier one, transposed (and the
                # legendaries, later) in tier two; 'type' keeps only the cards of the classes in play, as the official game does
                mine = (lambda i: True) if split == 'type_all' else (lambda i: i['cls'] in names)
                pool = common + [i for i in cards if i['deck'] in ('class', 'transposed') and mine(i)]
                two = lambda i: i['deck'] == 'transposed'
            elif split == 'mid':
                # between the two: common cards split at a requirement of 25; class cards tier one and transposed cards
                # tier two whatever they ask for
                two = lambda i: i['deck'] == 'transposed' or (i['deck'] == 'common' and max(req_of(i, rules)) >= 25)
            self.t1 = [i for i in pool if not two(i)]; self.t2 = [i for i in pool if two(i)]
            # where a sold card goes: the bottom of the treasure deck of its tier (legendaries are tier two, except
            # where one deck holds everything but the transposed cards)
            self.tier_two = (lambda i: two(i)) if split == 'kind' else (lambda i: two(i) or i['deck'] in ('legendary', 'boss'))
            rng.shuffle(self.t1); rng.shuffle(self.t2); self.legend = legend
            self.shop1 = self.stock(self.t1); self.shop2 = []
        else:
            # official: the commons and the party's own class cards; transposed and five legendaries after the mini-boss
            self.deck = common + [i for i in cards if i['deck'] == 'class' and i['cls'] in names]
            self.later = [i for i in cards if i['deck'] == 'transposed' and i['cls'] in names] + legend
            rng.shuffle(self.deck)

    def boss_named(self, boss, stage):
        """The boss of this half of the game is chosen: with every set in play its treasure cards join tier two (the
        mini-boss's with the legendaries once it falls, the main boss's as soon as it is known, which is then)."""
        if getattr(self.r, 'sets', 'core') not in ('2017', 'all') or not getattr(self.r, 'boss_loot', True): return
        loot = [i for i in MORE.values() if i['deck'] == 'boss' and i['boss'] == boss]
        if getattr(self.r, 'sets', 'core') == 'all':    # a 2022 boss's own treasure (as printed, every card; as amended, the cards the manuscript adds)
            loot += [i for i in Y22.values() if deck_of(i, self.r) == 'boss' and i.get('boss') == boss and (i['added_ms'] or not revised(self.r))]
        if stage == 0: self.boss_loot += loot; return
        deck = (self.t1 if getattr(self.r, 'deck_split', 'req') == 'kind' else self.t2) if self.r.treasure == 'author' else self.deck
        deck += loot; self.rng.shuffle(deck)

    def stock(self, deck):
        """Andre's shop: three weapons, three armour, two shields, two upgrades, two spells (here: five weapons or spells)."""
        want = {'weapon': 5, 'armour': 3, 'shield': 2, 'upgrade': 2}; out = []
        for it in list(deck):
            kind = 'upgrade' if it['type'] == 'upgrade' else 'armour' if it['type'] == 'armour' else 'shield' if is_shield(it) else 'weapon'
            if want[kind] > 0: want[kind] -= 1; out.append(it); deck.remove(it)
        return out

    def renew_row(self):
        if self.r.treasure == 'row' and self.row:
            self.deck = self.row + self.deck; self.row = []          # back under the deck; a new row is laid out

    def after_mini_boss(self):
        if self.r.treasure == 'author' and getattr(self.r, 'deck_split', 'req') == 'kind':
            # three sources by kind of card: one treasure deck (common and class cards, joined now by the legendaries),
            # and the party's transposed cards laid out as the tier-two shop
            self.t1 += self.shop1 + self.legend + self.boss_loot; self.rng.shuffle(self.t1); self.shop1 = self.stock(self.t1)
            self.shop2 = list(self.t2); self.t2 = []
        elif self.r.treasure == 'author':
            self.t1 += self.shop1; self.rng.shuffle(self.t1); self.shop1 = self.stock(self.t1); self.shop2 = self.stock(self.t2)
            self.t2 += self.legend + self.boss_loot; self.rng.shuffle(self.t2)
        else:
            self.deck += self.later + self.boss_loot; self.later = []; self.rng.shuffle(self.deck)

    def sell(self, c, it):
        """Character c sells card `it` from the bag for one soul. Titanite attached to a sold weapon is sold with it
        and adds nothing; any other attached upgrade comes back to the inventory."""
        c.bag.remove(it); c.souls += 1; self.sold(it); self.n_sold += 1
        ups = c.up_cards.pop(it['name'], []); c.plus.pop(it['name'], None)
        for up in ups:
            if 'Titanite' in up['name']: self.sold(up)
            else: c.bag.append(up)

    def sold(self, it):
        """A sold card goes face down to the bottom of the treasure deck it belongs to (cards are drawn from the end)."""
        if self.r.treasure == 'author': (self.t2 if self.tier_two(it) else self.t1).insert(0, it)
        else: self.deck.insert(0, it)

    def draw(self, tier=1):
        if self.r.treasure == 'author' and getattr(self.r, 'deck_split', 'req') == 'kind': tier = 1      # one treasure deck
        deck = (self.t1 if tier == 1 else self.t2) if self.r.treasure == 'author' else self.deck
        return deck.pop() if deck else None

    # ---------------------------------------------------------------- what a card is worth to a character
    def fit(self, c, it):
        """Best use of card `it` by character c: (gain in power, souls of levelling needed, tiers after, slot)."""
        best = None
        if it['type'] == 'upgrade':
            # an upgrade goes on the right-hand weapon or on the armour, while that card has a free upgrade slot
            tgt = self.up_target(c, it)
            if tgt is None: return None
            req = req_of(it, self.r)
            if tgt is c.A and 'ring_ease' in c.traits: req = [max(0, x - 2) for x in req]
            got = c.cost_to_meet(req)
            if got is None: return None
            plus = dict(c.plus); plus[tgt['name']] = plus.get(tgt['name'], ()) + up_of(it, self.r)
            gain = power(c.profile(tiers=got[1], plus=plus), c.r) - c._power
            return (gain, got[0], got[1], 'U')
        req = req_of(it, self.r)
        if it['name'] in self.carried:                  # an upgrade that comes with the card must be met as well as the card
            for up in (self.carried[it['name']][1] or ()): req = [max(x, y) for x, y in zip(req, req_of(up, self.r))]
        got = c.cost_to_meet(req)
        if got is None: return None
        cost, tiers = got
        off = 'offhand' in text_traits(it, self.r)       # a shield that may sit beside a two-handed weapon
        keep = c.L if (c.L is not None and 'offhand' in text_traits(c.L, self.r)) else False
        if it['type'] == 'armour': tries = [('A', dict(A=it))]
        elif it['hands'] == 2: tries = [('R', dict(R=it, L=keep))]
        elif has_dice(it) or (it['attacks'] and not it.get('catalyst')):
            tries = [('R', dict(R=it, L=(False if (c.L is None) else c.L))), ('L', dict(L=it))] if not c.two_handed else [('R', dict(R=it, L=False))]
        else: tries = [('L', dict(L=it))] if (not c.two_handed or off) else []
        if it.get('spell') and getattr(self.r, 'catalyst', False) and it not in c.spells:
            # a spell may be stored in a catalyst of its school that the character carries, taking no hand
            held = [x for x in (c.R, c.L) if x and x.get('catalyst') == it.get('school')]
            if held and sum(1 for x in c.spells if x.get('school') == it.get('school')) < 3:
                gain = power(c.profile(tiers=tiers, spells=c.spells + [it]), c.r) - c._power
                best = (gain, cost, tiers, 'S')
        plus = None
        if it['name'] in self.carried:                  # a weapon in the shared inventory keeps the upgrade fitted to it
            plus = dict(c.plus); plus[it['name']] = self.carried[it['name']][0]
        for slot, kw in tries:
            gain = power(c.profile(tiers=tiers, plus=plus, **kw), c.r) - c._power
            if best is None or gain > best[0]: best = (gain, cost, tiers, slot)
        return best

    def equip(self, c, it, tiers, slot):
        c.tier = list(tiers); out = []
        if slot != 'U' and it['name'] in self.carried:  # the upgrade comes with a weapon taken from the shared inventory
            c.plus[it['name']], c.up_cards[it['name']] = self.carried.pop(it['name'])
        if slot == 'U':
            tgt = self.up_target(c, it)
            c.plus[tgt['name']] = c.plus.get(tgt['name'], ()) + up_of(it, self.r); c.up_cards.setdefault(tgt['name'], []).append(it)
        elif slot == 'S': c.spells.append(it)
        elif slot == 'A': out.append(c.A); c.A = it
        elif slot == 'L': out.append(c.L); c.L = it
        else:
            out.append(c.R); c.R = it
            if it['hands'] == 2 and not (c.L is not None and 'offhand' in text_traits(c.L, self.r)): out.append(c.L); c.L = None
        # a replaced card goes back to the inventory: the shared one of the official rules, or the character's own,
        # where it may be sold (starting equipment cannot be sold, so it is simply set aside)
        for old in out:
            if not old: continue
            if self.r.pool:
                self.inv.append(old)
                if old['name'] in c.plus:               # an upgrade stays on its weapon, whoever takes it up next
                    self.carried[old['name']] = (c.plus.pop(old['name']), c.up_cards.pop(old['name'], None))
            else: c.bag.append(old)                     # starting equipment is kept too: it can be taken up again, never sold
        c.refresh()

    def in_use(self):
        """Treasure cards the party is using: equipped, fitted as upgrades or stored as spells (starting cards apart)."""
        n = 0
        for c in self.party:
            n += sum(1 for x in (c.R, c.L, c.A) if x and x['name'] not in c.start) + len(c.spells)
            n += sum(len(c.up_cards.get(x['name'], ())) for x in (c.R, c.L, c.A) if x)
        return n

    def up_target(self, c, it):
        """The card an upgrade would be fitted to: the armour for an armour upgrade, the right-hand weapon otherwise;
        None when the upgrade is not played, there is no such card, or its upgrade slots are full."""
        if not up_of(it, self.r): return None
        tgt = c.A if it.get('on') == 'armour' else (c.R if has_dice(c.R) else None)
        if tgt is None: return None
        used = sum(x.get('size', 1) for x in c.up_cards.get(tgt['name'], ()))     # an upgrade takes one slot; one card of 2022 takes two
        if tgt.get('slots', 0) - used < it.get('size', 1): return None
        return tgt

    def give(self, cards):
        """Treasure found: each card goes to whoever gains most from it (free to equip if requirements are met)."""
        for it in cards:
            if it is None: continue
            self.n_found += 1
            if self.r.pool: self.inv.append(it); continue
            fits = [(self.fit(c, it), c) for c in self.party]
            fits = [(f, c) for f, c in fits if f]
            if not fits: self.party[self.rng.randrange(len(self.party))].bag.append(it); continue
            f, c = max(fits, key=lambda x: x[0][0] / (1 + x[0][1]))
            c.bag.append(it)
        self.equip_free()

    def equip_free(self):
        """Between encounters cards may be swapped freely; stats cost souls and need the bonfire, and so does the
        fitting of an upgrade card."""
        for c in self.party:
            again = True
            while again:
                again = False
                for it in list(self.inv if self.r.pool else c.bag):
                    f = self.fit(c, it)
                    if f and f[3] != 'U' and f[1] == 0 and f[0] > 0.05:      # an upgrade is fitted by Andre, at the bonfire
                        (self.inv if self.r.pool else c.bag).remove(it); self.equip(c, it, f[2], f[3]); again = True

    def spend(self, levels=True):
        """At the bonfire: spend souls on whatever gains the most power per soul, until nothing is worth buying.
        With levels=False only Andre is visited: cards may be bought and equipped, but no stat is raised."""
        r = self.r
        if r.pool: return self.spend_pool()
        # where the cards for sale come from, with personal souls: the manuscript's two stocked shops, or (to compare
        # them like for like) the official ways of selling treasure: a standing row, four cards a visit, or a blind draw
        shown = None
        if r.treasure == 'row':
            while len(self.row) < r.shop_limit and self.deck: self.row.append(self.draw())
            shops = ((self.row, 1),)
        elif r.treasure == 'shop4':
            shown = [x for x in (self.draw() for _ in range(r.shop_limit)) if x]; shops = ((shown, 1),)
        elif r.treasure == 'draw':
            shops = ()
            for c in self.party:
                for _ in range(int(c.souls * self.DRAW_SHARE + self.rng.random())):
                    if not self.deck or c.souls < r.draw_cost: break
                    c.souls -= r.draw_cost; c.bag.append(self.draw())
        else: shops = ((self.shop1, 2), (self.shop2, 4))
        for c in self.party:
            if getattr(r, 'ember', False) and self.embers > 0 and not c.ember_card and not c.ember and c.souls >= 2:
                c.souls -= 2; c.ember_card = True; self.embers -= 1            # an ember card: one each, tier-one price
            while True:
                cands = []
                for it in c.bag:
                    f = self.fit(c, it)
                    if f and f[0] > 0.05 and f[1] <= c.souls and (levels or f[1] == 0): cands.append((f[0] / (f[1] + 0.5), f, it, 0, c.bag))
                for shop, price in shops:
                    for it in shop:
                        f = self.fit(c, it)
                        if f and f[0] > 0.05 and f[1] + price <= c.souls and (levels or f[1] == 0): cands.append((f[0] / (f[1] + price + 0.5), f, it, price, shop))
                if not cands: break
                _, f, it, price, src = max(cands, key=lambda x: x[0])
                src.remove(it); c.souls -= f[1] + price; self.equip(c, it, f[2], f[3]); self.n_bought += 1 if price else 0
                if r.treasure == 'row' and src is self.row and self.deck: self.row.append(self.draw())
            for it in list(c.bag):                                   # sell what will never be used (never starting equipment)
                if it['name'] in c.start: continue
                f = self.fit(c, it)
                if (not f or f[0] <= 0.05) and it in c.bag: self.sell(c, it)
            # with souls left over and nothing to buy, raise the stat that brings the best card in hand or shop closer
            if levels and c.souls >= 2:
                wants = [(self.fit(c, it), it) for it in c.bag + [x for shop, _ in shops for x in shop]]
                wants = [(f, it) for f, it in wants if f and f[0] > 0.3 and f[1] > 0]
                if wants:
                    f, it = max(wants, key=lambda x: x[0][0] / (x[0][1] + 1))
                    for i in range(4):
                        while c.tier[i] < f[2][i] and c.souls >= r.tier_cost[min(c.tier[i], len(r.tier_cost) - 1)]:
                            c.souls -= r.tier_cost[min(c.tier[i], len(r.tier_cost) - 1)]; c.tier[i] += 1
                    c.refresh()
        if shown is not None: self.deck = shown + self.deck          # the cards not bought go back under the deck

    def spend_pool(self):
        """The shared cache of the official rules: look at some new cards, then put the souls where they add most,
        the weakest character first (any death loses the fight). Souls that buy nothing useful are kept."""
        r = self.r; shown = []
        if r.treasure == 'row':
            # a standing row of face-up cards at Andre's: a bought card is replaced at once, the row is renewed at a rest
            while len(self.row) < r.shop_limit and self.deck: self.row.append(self.draw())
            shown = self.row
        if r.treasure == 'shop4':
            shown = [x for x in (self.draw() for _ in range(r.shop_limit)) if x]
        elif r.treasure == 'draw':
            for _ in range(int(self.pool * self.DRAW_SHARE + self.rng.random())):
                if not self.deck or self.pool < r.draw_cost: break
                self.pool -= r.draw_cost; self.inv.append(self.draw())
        # each character has an equal share of the cache to level and equip with; what a share cannot use goes back
        share = {id(c): self.pool / len(self.party) for c in self.party}
        for final in (False, True):
            while True:
                cands = []
                for c in sorted(self.party, key=lambda c: c._power):
                    limit = self.pool if final else min(self.pool, share[id(c)])
                    for src, price in ((self.inv, 0), (shown, 1)):
                        for it in src:
                            f = self.fit(c, it)
                            if f and f[0] > 0.05 and f[1] + price <= limit:
                                cands.append((f[0] / (f[1] + price + 0.5), f, it, price, c, src))
                    if cands and not final: break               # the weakest character who can use something goes first
                if not cands: break
                _, f, it, price, c, src = max(cands, key=lambda x: x[0])
                src.remove(it); self.pool -= f[1] + price; share[id(c)] -= f[1] + price; self.equip(c, it, f[2], f[3])
                if r.treasure == 'row' and src is shown and self.deck: shown.append(self.draw())
        if r.treasure == 'shop4': self.deck = shown + self.deck

    DRAW_SHARE = 0.3          # share of the cache spent on drawing treasure before levelling for it
