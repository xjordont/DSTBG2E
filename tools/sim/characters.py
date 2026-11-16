#!/usr/bin/env python3
"""Characters, equipment and the bonfire economy for the rules simulator.

A character carries real equipment cards (gear.json): a right-hand item, a left-hand item and armour. Its combat
profile (block, resist and dodge dice, attack options) is derived from those cards. At the bonfire the simulated
players spend souls by a greedy rule: take whichever purchase or level-up buys the most `power` per soul.
"""
import json, os
from engine import pmf_def, attack_pmf, hit_stats, p_dodge

HERE = os.path.dirname(os.path.abspath(__file__))
GEAR = json.load(open(os.path.join(HERE, 'gear.json')))
ITEMS, CLASSES = GEAR['items'], GEAR['classes']
for _i in ITEMS.values():
    if _i['type'] == 'upgrade':                      # Titanite Shard: +1 damage; four gems: one more black die
        _t = _i.get('text') or ''
        _i['up'] = 'mod' if '+1 damage' in _t else 'die' if 'gain 1 black die' in _t else None
CORE4 = ['Knight', 'Warrior', 'Herald', 'Assassin']
REF_FOES = ((1, 1, 1), (1, 1, 5), (2, 1, 5), (2, 1, 10))            # (block, resist, health) of reference targets
REF_HITS = ((4, False, 1), (5, False, 1), (5, False, 2), (6, False, 1), (6, False, 2), (4, True, 1), (5, True, 2))   # (damage, magic, dodge difficulty)


def is_shield(it): return it is not None and it['type'] == 'hand' and not it['attacks']


# Spell cards (sorceries, miracles, pyromancies). The manuscript never scales a spell with a stat and never counts it
# as wielded two-handed, so it gains neither the +1 at ten over its requirement nor the grip reroll.
SPELLS = {'Fireball', 'Soul Arrow', 'Soulstream', 'Heal', 'Heal Aid', 'Replenishment', 'Bountiful Light',
          'Bountiful Sunlight', 'Force', 'Great Magic Weapon', 'Poison Mist'}


class Char:
    def __init__(self, cls, rules):
        k = CLASSES[cls]
        self.name, self.r, self.base, self.taunt = cls, rules, k['stats'], k['taunt']
        self.tier = [0, 0, 0, 0]
        w, s, a = k['start']
        self.R, self.L, self.A = ITEMS[w], ITEMS[s], ITEMS[a]
        self.start = {w, s, a}                        # starting equipment: it cannot be sold
        self.bag = []; self.plus = {}                 # spare cards; weapon name -> upgrade bonus
        self.up_cards = {}                            # weapon name -> the upgrade card attached to it
        self.souls = 0; self.earned = 0
        self.dmg = self.sta = 0; self.hollow = False; self.alive = True; self.was_hollow = False
        self.estus = self.luck = self.heroic = True; self.ember = False; self.ember_card = False
        self.node = 0; self.stagger = self.frost = self.bleed = False; self.poison = 0; self.ran = False
        self.refresh()

    # ---------------------------------------------------------------- stats and requirements
    @property
    def cap(self): return self.r.hollow_bar if self.hollow else self.r.bar

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

    # ---------------------------------------------------------------- combat profile
    def profile(self, R=None, L=None, A=None, tiers=None, plus=None):
        R = self.R if R is None else R; L = self.L if L is None else L; A = self.A if A is None else A
        if L is False: L = None
        tiers = tiers or self.tier; plus = self.plus if plus is None else plus; r = self.r
        worn = [x for x in (A, R, L) if x]
        p = dict(R=R, L=L, A=A)
        p['blk'] = ''.join(x.get('block', '') for x in worn); p['res'] = ''.join(x.get('resist', '') for x in worn)
        p['arm_blk'] = A.get('block', '') if A else ''; p['arm_res'] = A.get('resist', '') if A else ''
        p['blk_pen'] = -sum(x.get('block_mod', 0) for x in worn); p['res_pen'] = -sum(x.get('resist_mod', 0) for x in worn)
        p['dodge'] = sum(x.get('dodge', 0) for x in worn)
        p['two'] = bool(R and R['hands'] == 2)
        opts = {'R': [], 'L': []}
        for hand, it in (('R', R), ('L', L)):
            if not it: continue
            other = L if hand == 'R' else R
            up = plus.get(it['name']); bonus = 1 if up == 'mod' else 0; more = 'b' if up == 'die' else ''
            spell = it['name'] in SPELLS
            if getattr(r, 'scaling', False) and it['attacks'] and max(it['req']) > 0 and not spell:
                top = max(it['req'])                            # where requirements tie for the highest, any of them may be chosen
                if any(self.value(j, tiers[j]) - top >= 10 for j in range(4) if it['req'][j] == top):
                    bonus += 1                                  # the manuscript's stat scaling: +1 at ten over the requirement
            for a in it['attacks']:
                if not a['dice']: continue                     # support actions (healing, stamina) are not modelled
                opts[hand].append(dict(name=it['name'], cost=a['cost'], dice=a['dice'] + more, mod=a['mod'] + bonus, magic=a['magic'],
                                       range=a['range'], repeat=a['repeat'], shaft=a['shaft'], ignore=a.get('ignore', False),
                                       node=a.get('node', False), spell=spell,
                                       reroll=bool(getattr(r, 'grip_reroll', False) and not spell and (it['hands'] == 2 or other is None))))
        p['options'] = opts
        p['mean_blk'] = sum(v * q for v, q in pmf_def(p['blk'], r.block)) - p['blk_pen']
        p['mean_res'] = sum(v * q for v, q in pmf_def(p['res'], r.block)) - p['res_pen']
        p['can_parry'] = bool(r.parry and L and not p['two'] and (is_shield(L) or r.parry == 'any'))
        return p

    def refresh(self):
        p = self.profile()
        for k in ('blk', 'res', 'arm_blk', 'arm_res', 'blk_pen', 'res_pen', 'dodge', 'options', 'mean_blk', 'mean_res', 'can_parry'):
            setattr(self, k, p[k])
        self.two_handed = p['two']; self._power = power(p, self.r)
        best = 0.0
        for o in self.options['R']:
            if o.get('spell'): continue                     # a riposte is never made with a spell
            if o['cost'] <= 2 and o['range'] == 0 or (o['cost'] <= 2 and not o['shaft']):
                best = max(best, sum(x * q for x, q in attack_pmf(o['dice'], o['mod'], 1, o['repeat'])))
        self._rip = best

    def scale_bonus(self, o): return 0                # stat scaling is already folded into each option's modifier
    def riposte_ev(self, foe): return self._rip

    def best_option(self, foe, dist, budget, hand='R', spells=True):
        best = None
        for o in self.options[hand]:
            if o['cost'] > budget or o['range'] < dist or (o['shaft'] and dist == 0): continue
            if o.get('spell') and not spells: continue      # a riposte is never made with a spell
            ev = sum(x * q for x, q in attack_pmf(o['dice'], o['mod'], foe.resist if o['magic'] else foe.armor, o['repeat'])) - 0.4 * o['cost']
            if best is None or ev > best[0]: best = (ev, o)
        return best[1] if best else None

    # ---------------------------------------------------------------- the bonfire
    def full_rest(self):
        self.dmg = self.sta = 0; self.hollow = False; self.alive = True; self.estus = self.luck = self.heroic = True
        self.stagger = self.frost = self.bleed = False; self.poison = 0


def power(p, r):
    """A single figure for how strong a loadout is: the damage it deals in a turn against lightly, medium and heavily
    armoured targets, less the damage it lets through from a spread of attacks. Defence counts for more than offence,
    because a death costs the party far more than a slow fight."""
    def best(block, resist, cap):
        top = 0.0
        for ro in p['options']['R'] or [None]:
            for lo in ([None] + p['options']['L']):
                tot = 0.0; cost = 0
                for o in (ro, lo):
                    if o is None: continue
                    pm = attack_pmf(o['dice'], o['mod'], 0 if o['ignore'] else (resist if o['magic'] else block), o['repeat'])
                    tot += sum(min(x, cap) * q for x, q in pm); cost += o['cost']
                if cost <= 5: top = max(top, tot - 0.3 * cost)
        return top
    off = 0.25 * best(1, 1, 5) + 0.4 * best(2, 1, 10) + 0.35 * best(3, 2, 30)
    quick = 0.0                                             # felling a one-health, block-two enemy with a cheap attack
    for hand in 'RL':
        for o in p['options'][hand]:
            if o['cost'] <= 2:
                quick = max(quick, sum(q for x, q in attack_pmf(o['dice'], o['mod'], 1 if o['magic'] else 2, o['repeat']) if x >= 1))
    if any(o['range'] >= 1 for h in 'RL' for o in p['options'][h]): off += 0.15
    taken = 0.0
    for dmg, magic, k in REF_HITS:
        dice = p['res'] if magic else p['blk']; pen = p['res_pen'] if magic else p['blk_pen']
        blk = sum(d * q for d, q in hit_stats(dice, r.block, dmg, max(0, pen)))
        if p['dodge'] > 0:
            ps = p_dodge(p['dodge'], k)
            adice = p['arm_res'] if magic else p['arm_blk']
            fail = sum(d * q for d, q in hit_stats(adice, r.block, dmg, 0)) if r.dodge_fail == 'armour' else dmg
            blk = min(blk, (1 - ps) * fail + 0.4)
        taken += blk / len(REF_HITS)
    return off + 0.8 * quick - 1.6 * taken


class Economy:
    """The treasure decks, the shop and the spending of souls, for one game."""

    def __init__(self, party, rules, rng):
        self.party, self.r, self.rng = party, rules, rng
        self.pool = 0                                  # the shared soul cache of the official rules
        self.row = []                                  # Andre's face-up cards, where the ruleset has them
        self.embers = len(party)                       # the manuscript's shop: ember cards equal to the number of characters
        self.inv = []                                  # the shared inventory of the official rules
        self.carried = {}                              # upgrades on weapons lying in it: weapon name -> (bonus, upgrade card)
        names = {c.name for c in party}
        cards = [i for i in ITEMS.values() for _ in range(i.get('copies', 1))]
        common = [i for i in cards if i['deck'] == 'common']
        legend = rng.sample([i for i in cards if i['deck'] == 'legendary'], 5)
        if rules.treasure == 'author':
            # the manuscript: every common, class and transposed card, split at a requirement of 25; legendaries join tier two
            pool = common + [i for i in cards if i['deck'] in ('class', 'transposed')]
            two = lambda i: max(i['req']) >= 25 or i['deck'] == 'transposed'
            split = getattr(rules, 'deck_split', 'req')
            if split in ('type', 'type_all', 'kind'):
                # a split by kind of card, for comparison: common and class treasure in tier one, transposed (and the
                # legendaries, later) in tier two; 'type' keeps only the cards of the classes in play, as the official game does
                mine = (lambda i: True) if split == 'type_all' else (lambda i: i['cls'] in names)
                pool = common + [i for i in cards if i['deck'] in ('class', 'transposed') and mine(i)]
                two = lambda i: i['deck'] == 'transposed'
            self.t1 = [i for i in pool if not two(i)]; self.t2 = [i for i in pool if two(i)]
            # where a sold card goes: the bottom of the treasure deck of its tier (legendaries are tier two, except
            # where one deck holds everything but the transposed cards)
            self.tier_two = (lambda i: two(i)) if split == 'kind' else (lambda i: two(i) or i['deck'] == 'legendary')
            rng.shuffle(self.t1); rng.shuffle(self.t2); self.legend = legend
            self.shop1 = self.stock(self.t1); self.shop2 = []
        else:
            # official: the commons and the party's own class cards; transposed and five legendaries after the mini-boss
            self.deck = common + [i for i in cards if i['deck'] == 'class' and i['cls'] in names]
            self.later = [i for i in cards if i['deck'] == 'transposed' and i['cls'] in names] + legend
            rng.shuffle(self.deck)

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
            self.t1 += self.shop1 + self.legend; self.rng.shuffle(self.t1); self.shop1 = self.stock(self.t1)
            self.shop2 = list(self.t2); self.t2 = []
        elif self.r.treasure == 'author':
            self.t1 += self.shop1; self.rng.shuffle(self.t1); self.shop1 = self.stock(self.t1); self.shop2 = self.stock(self.t2)
            self.t2 += self.legend; self.rng.shuffle(self.t2)
        else:
            self.deck += self.later; self.later = []; self.rng.shuffle(self.deck)

    def sell(self, c, it):
        """Character c sells card `it` from the bag for one soul. Titanite attached to a sold weapon is sold with it
        and adds nothing; any other attached upgrade comes back to the inventory."""
        c.bag.remove(it); c.souls += 1; self.sold(it)
        up = c.up_cards.pop(it['name'], None)
        if c.plus.pop(it['name'], None) is not None and up is not None:
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
            got = c.cost_to_meet(it['req'])
            if got is None or not it.get('up') or not c.R or not c.R['attacks'] or c.R.get('slots', 0) < 1 or c.R['name'] in c.plus: return None
            plus = dict(c.plus); plus[c.R['name']] = it['up']
            gain = power(c.profile(tiers=got[1], plus=plus), c.r) - c._power
            return (gain, got[0], got[1], 'U')
        got = c.cost_to_meet(it['req'])
        if got is None: return None
        cost, tiers = got
        if it['type'] == 'armour': tries = [('A', dict(A=it))]
        elif it['hands'] == 2: tries = [('R', dict(R=it, L=False))]
        elif it['attacks']: tries = [('R', dict(R=it, L=(False if (c.L is None) else c.L))), ('L', dict(L=it))] if not c.two_handed else [('R', dict(R=it, L=False))]
        else: tries = [('L', dict(L=it))] if not c.two_handed else []
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
        if slot == 'U': c.plus[c.R['name']] = it['up']; c.up_cards[c.R['name']] = it
        elif slot == 'A': out.append(c.A); c.A = it
        elif slot == 'L': out.append(c.L); c.L = it
        else:
            out.append(c.R); c.R = it
            if it['hands'] == 2: out.append(c.L); c.L = None
        # a replaced card goes back to the inventory: the shared one of the official rules, or the character's own,
        # where it may be sold (starting equipment cannot be sold, so it is simply set aside)
        for old in out:
            if not old: continue
            if self.r.pool:
                self.inv.append(old)
                if old['name'] in c.plus:               # an upgrade stays on its weapon, whoever takes it up next
                    self.carried[old['name']] = (c.plus.pop(old['name']), c.up_cards.pop(old['name'], None))
            elif old['name'] not in c.start: c.bag.append(old)
        c.refresh()

    def give(self, cards):
        """Treasure found: each card goes to whoever gains most from it (free to equip if requirements are met)."""
        for it in cards:
            if it is None: continue
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
                src.remove(it); c.souls -= f[1] + price; self.equip(c, it, f[2], f[3])
                if r.treasure == 'row' and src is self.row and self.deck: self.row.append(self.draw())
            for it in list(c.bag):                                   # sell what will never be used
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
