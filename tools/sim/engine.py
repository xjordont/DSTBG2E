#!/usr/bin/env python3
"""Tactical combat engine for the rules simulator.

One encounter or boss fight is played on the real 13-node tile with the printed enemy cards, the real dice, and
characters carrying real equipment cards. The rules that differ between rulesets (round structure, aggro, stamina
recovery, block and dodge procedures, death, enemy scaling) are fields of a Rules object; see rules.py.

The players are a fixed, explicit policy (see `Policy`); its knobs are varied in the robustness runs.
"""
import functools, itertools, json, math, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = json.load(open(os.path.join(HERE, 'cards.json')))
ENEMIES, ENCOUNTERS, BOSSES = CARDS['enemies'], CARDS['encounters'], CARDS['bosses']

# ------------------------------------------------------------------ dice
DIE = {'b': (0, 1, 1, 1, 2, 2), 'u': (1, 1, 2, 2, 2, 3), 'o': (1, 2, 2, 3, 3, 4)}


@functools.lru_cache(None)
def pmf_sum(dice):
    """Distribution of the total of a dice string such as 'bbu', as a tuple of (value, probability)."""
    d = {0: 1.0}
    for ch in dice:
        n = {}
        for s, p in d.items():
            for f in DIE[ch]: n[s + f] = n.get(s + f, 0.0) + p / 6
        d = n
    return tuple(sorted(d.items()))


@functools.lru_cache(None)
def pmf_best2(dice):
    """Distribution of the two highest dice of a dice string."""
    d = {}
    for faces in itertools.product(*(DIE[ch] for ch in dice)):
        v = sum(sorted(faces)[-2:]); d[v] = d.get(v, 0.0) + 6.0 ** -len(dice)
    return tuple(sorted(d.items())) if dice else ((0, 1.0),)


def pmf_def(dice, mode): return pmf_best2(dice) if mode == 'best2' else pmf_sum(dice)


@functools.lru_cache(None)
def p_dodge(n, k):
    """Chance that n dodge dice (three dodge faces in six) show at least k dodges."""
    if k <= 0: return 1.0
    if n < k: return 0.0
    from math import comb
    return sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n


@functools.lru_cache(None)
def hit_stats(dice, mode, dmg, pen):
    """Damage distribution of an attack of `dmg` against a defence roll (minus `pen` for stagger)."""
    out = {}
    for v, p in pmf_def(dice, mode):
        d = max(0, dmg - max(0, v - pen)); out[d] = out.get(d, 0.0) + p
    return tuple(sorted(out.items()))


@functools.lru_cache(None)
def attack_pmf(dice, mod, armor, repeat):
    """Damage distribution of a character attack (dice + mod, repeated) against an armour value."""
    one = {}
    for v, p in pmf_sum(dice):
        d = max(0, v + mod - armor); one[d] = one.get(d, 0.0) + p
    tot = {0: 1.0}
    for _ in range(repeat):
        n = {}
        for a, pa in tot.items():
            for b, pb in one.items(): n[a + b] = n.get(a + b, 0.0) + pa * pb
        tot = n
    return tuple(sorted(tot.items()))


def roll(dice, rng): return [rng.choice(DIE[ch]) for ch in dice]

# ------------------------------------------------------------------ the tile
NODES = [(x, y) for y in range(5) for x in range(5) if (x + y) % 2 == 0]          # 13 nodes, rows of 3-2-3-2-3
IDX = {p: i for i, p in enumerate(NODES)}
NBR = [[IDX[(x + dx, y + dy)] for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), (-2, 0), (0, 2), (0, -2))
        if (x + dx, y + dy) in IDX] for x, y in NODES]
DIST = [[0] * 13 for _ in range(13)]
for _s in range(13):
    seen = {_s: 0}; q = [_s]
    while q:
        a = q.pop(0)
        for b in NBR[a]:
            if b not in seen: seen[b] = seen[a] + 1; q.append(b)
    for b, d in seen.items(): DIST[_s][b] = d
ENTRY = [IDX[(0, 4)], IDX[(2, 4)], IDX[(4, 4)]]
SPAWN = [i for i, (x, y) in enumerate(NODES) if y <= 2]


def step_to(a, b, rng):
    if a == b: return a
    m = min(DIST[n][b] for n in NBR[a]); return rng.choice([n for n in NBR[a] if DIST[n][b] == m])


def step_away(a, b, rng):
    m = max(DIST[n][b] for n in NBR[a])
    return a if m <= DIST[a][b] else rng.choice([n for n in NBR[a] if DIST[n][b] == m])

# ------------------------------------------------------------------ policy


class Policy:
    """How the simulated players decide. Every number here is a judgement, varied in the robustness runs."""
    caution = 1.0        # stamina kept free, as a multiple of the damage expected before the next turn
    w_death = 14.0       # how much a death is feared, in points of damage (raised when a death ends the encounter)
    w_sta = 0.4          # what a point of stamina is worth, in points of damage
    estus_at = 5         # drink when this much damage is on the bar (where damage is not cleared by a win)
    estus_risk = 0.2     # or when the chance of dying before the next turn is above this
    luck_at = 3          # spend luck to re-roll a defence that lets this much damage through (or a lethal one)
    spread = True        # enter on different nodes when possible
    kite = True          # step out of reach after attacking when it pays
    read_new = 0.15      # share of a boss's attacks side-stepped by position alone, card not yet seen
    read_known = 0.45    # the same once the card has been seen
    evade = 0.12         # share of ordinary enemies' attacks avoided by positioning finer than the model plays out

    @staticmethod
    def at(s):
        """One scale for the play the model does not act out move by move: 0 = none of it, 1 = all that seems possible.
        It sets how often an ordinary attack is avoided by position and how well a boss's fixed card order is read."""
        return dict(evade=0.6 * s, read_new=0.1 + 0.3 * s, read_known=min(0.95, 0.3 + 0.65 * s))

    def __init__(self, skill=None, **kw):
        if skill is not None: self.__dict__.update(self.at(skill))
        self.__dict__.update(kw)

# ------------------------------------------------------------------ models


class Foe:
    __slots__ = ('name', 'card', 'hp', 'max', 'node', 'stagger', 'frost', 'poison', 'bleed', 'boss', 'deck', 'discard',
                 'heated', 'heat_cards', 'armor', 'resist', 'threat', 'weak', 'atk_bonus', 'seen', 'fresh', 'heal', 'surges')

    def __init__(self, name, card, hp, node, boss=False):
        self.name, self.card, self.hp, self.max, self.node, self.boss = name, card, hp, hp, node, boss
        self.stagger = self.frost = False; self.poison = 0; self.bleed = False
        self.fresh = False                             # staggered during its own activation (by a parry)
        self.armor, self.resist, self.threat = card['armor'], card['resist'], card.get('threat', 10)
        self.deck = self.discard = self.heat_cards = None; self.heated = False; self.weak = False; self.atk_bonus = 0
        self.seen = set(); self.heal = 0; self.surges = 0

    @property
    def alive(self): return self.hp > 0


class Fight:
    """One encounter (a list of enemy names) or one boss fight (a boss name)."""
    ARC = 0.2        # chance that a boss attack also catches another character standing within one node of the boss
    WEAK = 0.3       # chance that a character's attack on a boss comes from a weak arc (+1 black die): card not yet seen
    WEAK_KNOWN = 0.6 # the same once the card has been seen (the deck comes round in the same order)

    def __init__(self, party, rules, rng, enemies=None, boss=None, policy=None, log=None, n=None):
        self.party, self.r, self.rng, self.pol, self.log = party, rules, rng, policy or Policy(), log
        self.n = n or len(party);                      # scaling counts every character in the game, present or not
        self.seats = len(party); self.rounds = 0; self.char_turns = 0; self.enemy_acts = 0; self.deaths = 0
        self.is_boss = boss is not None; self.dealt = {}; self.dec = {}
        self.boss_atk = rules.boss_atk(self.n) if hasattr(rules, 'boss_atk') else 0
        r = rules
        ents = list(ENTRY); rng.shuffle(ents)
        for i, c in enumerate(party):
            c.node = ents[i % 3] if self.pol.spread else ents[0]
            c.alive = True; c.stagger = c.frost = False; c.poison = 0; c.bleed = False; c.ran = False
            c.guard = ('', ''); c.buff = None; c.hurt_by = set(); c.rolls = 0
        self.faraam = set()                            # who has used "once per encounter" card text
        self.idle = 0; self._hp = None                 # rounds in a row in which no enemy lost health
        self.special = None; self.bdef = None
        if boss:
            b = BOSSES[boss]; mul = getattr(r, 'boss_mul', None); k = mul(self.n) if mul else 1
            self.bdef = b; self.special = b.get('special')
            if self.special == 'pair':
                # one boss fought as two models, each with its own health; one behaviour card a turn, on which both act
                self.foes = []
                for i, m in enumerate(b['models']):
                    card = dict(armor=m['armor'], resist=m['resist'], heatup=0, hp=int(round(m['hp'] * k)))
                    f = Foe(m['name'], card, card['hp'], IDX[(2, 0)] if i == 0 else IDX[(0, 0)], boss=True)
                    f.heat_cards = list(m['heat']); f.heal = int(round(m['heal'] * k)); f.deck = f.discard = None; self.foes.append(f)
                self.pdeck = list(b['cards']); rng.shuffle(self.pdeck); self.pdeck = self.pdeck[:b['deck']]; self.pdiscard = []; self.pair_heat = False
            else:
                if mul: b = dict(b, hp=int(round(b['hp'] * k)), heatup=int(round(b['heatup'] * k)))
                f = Foe(boss, b, b['hp'], IDX[(2, 0)], boss=True)
                std = [c for c in b['cards'] if not c['heatup']]; rng.shuffle(std)
                f.deck = std[:b['deck']]; f.discard = []; f.heat_cards = [c for c in b['cards'] if c['heatup']]
                self.foes = [f]
        else:
            sp = rng.sample(SPAWN, 2); self.foes = []
            for i, name in enumerate(enemies):
                card = ENEMIES[name]
                f = Foe(name, card, r.hp(card['hp'], self.n), sp[0] if i < (len(enemies) + 1) // 2 else sp[1])
                f.atk_bonus = r.atk(self.n); self.foes.append(f)
        self.aggro = max(party, key=lambda c: c.taunt)
        self.turn_i = getattr(party[0], '_first', 0) % self.seats      # official: who activates first carries over

    # -------------------------------------------------------------- helpers
    def live(self): return [c for c in self.party if c.alive]
    def foes_alive(self): return [f for f in self.foes if f.hp > 0]

    def failed(self):
        if self.r.death == 'party': return self.deaths > 0
        if self.r.death == 'lost': return not self.live()        # a hollow character who dies is lost until the next rest
        return not self.live() or any((not c.alive) and c.was_hollow for c in self.party)

    def over(self): return self.failed() or not self.foes_alive()

    def say(self, *a):
        if self.log is not None: self.log.append(' '.join(str(x) for x in a))

    def target(self, f, mode):
        live = self.live()
        if not live: return None
        if mode == 'aggro' and self.aggro.alive: return self.aggro
        m = min(DIST[f.node][c.node] for c in live); tied = [c for c in live if DIST[f.node][c.node] == m]
        return self.aggro if self.aggro in tied else max(tied, key=lambda c: c.taunt)

    def lethal(self, c, d):
        free = c.cap - c.dmg - c.sta
        return d >= free if self.r.lethal == 'full' else d > free

    # -------------------------------------------------------------- damage to a character
    def wound(self, c, d):
        if d <= 0 or not c.alive: return
        if c.bleed and self.r.bleed == 'official': d += 2; c.bleed = False
        if self.lethal(c, d):
            c.alive = False; c.dmg = min(c.cap, c.dmg + d); self.deaths += 1; c.ember = False; self.say('   ', c.name, 'dies')
            if self.aggro is c and self.live(): self.aggro = max(self.live(), key=lambda x: x.taunt)
        else:
            c.dmg += d

    def defend(self, src, c, dmg, magic, k, push=False, effects=(), parryable=True):
        """An attack of `dmg` (after scaling) with dodge difficulty k resolves against character c. Returns whether the
        character was hit (a blocked attack is a hit; a dodged or parried one is not)."""
        if not c.alive or src.hp <= 0: return False    # a riposte or a backstab may have killed the attacker mid-activation
        r, pol, rng = self.r, self.pol, self.rng
        if src.stagger and r.stagger == 'author': k = max(0, k - 1)      # a staggered attacker is easier to dodge and parry
        if not src.boss and rng.random() < pol.evade: return False
        free = c.cap - c.dmg - c.sta
        pen = 1 if (c.stagger and r.stagger == 'author') else 0
        tr = c.traits
        dice = (c.res if magic else c.blk) + c.guard[1 if magic else 0]      # with any die lent by a spell or a shield's action
        adice = c.arm_res if magic else c.arm_blk
        # a block or resist value also takes the modifier printed on the equipment (bpen: everything worn; apen: the
        # armour alone, for the roll after a failed dodge); a dodge roll takes only the stagger
        bpen = pen + (c.res_pen if magic else c.blk_pen); apen = pen + (c.arm_res_pen if magic else c.arm_blk_pen)
        wd = pol.w_death * (1.6 if (r.death == 'party' or c.hollow or len(self.live()) == 1) else 1.0)

        def cost(pmf, extra_sta):
            lim = free - extra_sta
            e = sum(d * p for d, p in pmf)
            pl = sum(p for d, p in pmf if (d >= lim if r.lethal == 'full' else d > lim) and d > 0)
            # stamina is cheap while the bar is open and dear once it crowds out room for damage
            crowd = sum(1.0 for i in range(extra_sta) if free - i <= 4)
            return e + wd * pl + pol.w_sta * extra_sta + 0.6 * crowd
        opts = [(cost(hit_stats(dice, r.block, dmg, bpen), 0), 'block', 0)]
        # the price of a dodge, and the dodge dice, as the cards worn change them
        sta1 = 0 if ('dodge_free' in tr or ('alonne' in tr and 'Alonne' in src.name)) else 2 if 'dodge_dear' in tr else 1
        sta1 += 1 if (c.frost and r.frost == 'official') else 0
        room = free - (1 if r.lethal == 'full' else 0)
        nd = c.dodge
        if 'no_dodge' not in tr:
            nd += (1 if ('vs_hollow' in tr and 'Hollow' in src.name) else 0) + (1 if ('vs_boss' in tr and src.boss) else 0) \
                + (2 if ('vs_far' in tr and DIST[src.node][c.node] >= 2) else 0)
        pen_d = pen + c.dodge_pen                       # what a dodge roll is short by: stagger, and a card that takes a success away
        fail = hit_stats(adice, r.block, dmg, apen) if r.dodge_fail == 'armour' else ((dmg, 1.0),)
        tries = [(nd, sta1)]
        if r.dodge_extra:
            if nd + 1 <= 4: tries.append((nd + 1, sta1 + 2))          # one extra die a dodge, for two more stamina
        for dice_n, sta in tries:
            if sta > room or (dice_n <= 0 and k > 0): continue
            ps = p_dodge(dice_n, k + pen_d)
            mixed = ((0, ps),) + tuple((d, p * (1 - ps)) for d, p in fail)
            opts.append((cost(mixed, sta), 'dodge', (dice_n, sta)))
        if (r.parry and parryable and not push and c.can_parry and DIST[src.node][c.node] == 0 and sta1 <= room
                and not src.boss):
            ps = p_dodge(nd, k + pen_d)
            gain = c.riposte_ev(src) + 1.0                       # the riposte, and the stagger on the attacker
            mixed = ((0, ps), (dmg, 1 - ps))
            opts.append((cost(mixed, sta1) - ps * gain + (1 - ps) * 1.0, 'parry', None))
        _, how, arg = min(opts, key=lambda o: o[0]); pre = None; peek = None
        if 'wolf' in tr and nd > 0 and sta1 <= room and getattr(r, 'defence', 'choice') != 'combined':
            # the dodge dice are rolled before the choice is made: a roll that would dodge is taken, any other is a block
            got = sum(rng.random() < 0.5 for _ in range(nd)); peek = got >= k + pen_d
            how, arg = ('dodge', (nd, sta1)) if peek else ('block', 0)
        if getattr(r, 'defence', 'choice') == 'combined':
            # the 2022 rule: dodge and block dice are rolled together at no cost; enough dodges and the attack misses,
            # otherwise the block or resist pips still count
            need = k + pen_d; got = sum(rng.random() < 0.5 for _ in range(nd)); pre = roll(dice, rng)
            if 0 < need == got + 1 and nd > got and c.luck:
                # one dodge short, with every die on the table: luck may re-roll one die of the defence roll, and a failed
                # dodge die is the one to pick when the block dice would let a telling blow through
                through = max(0, dmg - max(0, (sum(sorted(pre)[-2:]) if r.block == 'best2' else sum(pre)) - bpen))
                if self.lethal(c, through) or through >= pol.luck_at:
                    c.luck = False; got += rng.random() < 0.5
            if need <= 0 or got >= need:
                self.dec['dodge'] = self.dec.get('dodge', 0) + 1
                if c.heroic and c.name == 'Assassin' and src.hp > 0:                       # Backstab: a free attack after a dodge
                    o = c.best_option(src, DIST[c.node][src.node], 99, hand='R')
                    if o: self.hero(c); self.strike(c, src, o)
                if r.dodge_move == 'paid': self.reposition(c, min(1, free), False, count=False)     # 2022: may pay 1 stamina to move a node
                return False
            how, arg = 'block', 0
        hit = True; taken = 0
        if how == 'block':
            faces = pre if pre is not None else roll(dice, rng); bonus = [0]      # the combined roll has its block dice already
            total = lambda: (sum(sorted(faces)[-2:]) if r.block == 'best2' else sum(faces)) + bonus[0]
            v = total(); taken = max(0, dmg - max(0, v - bpen))
            if c.heroic and c.name == 'Knight' and not magic and (self.lethal(c, taken) or taken >= 2):     # a block roll only
                # Stand Fast: one more blue die. Where only the two highest dice count, the author rules that this die is
                # added to them (heroic_die='add'); the other reading puts it in the pool with the rest
                self.hero(c); die = rng.choice(DIE['u'])
                if r.block == 'best2' and getattr(r, 'heroic_die', 'pool') == 'add': bonus[0] = die
                else: faces.append(die); dice = dice + 'u'
                v = total(); taken = max(0, dmg - max(0, v - bpen))
            if c.luck and faces and (self.lethal(c, taken) or taken >= pol.luck_at):
                # luck: the official rules re-roll one die; the manuscript any or all of them, chosen at once
                c.luck = False; worst = sorted(range(len(faces)), key=lambda j: faces[j] - sum(DIE[dice[j]]) / 6)
                again = worst[:1] if getattr(r, 'luck', 'one') == 'one' else [j for j in worst if faces[j] < sum(DIE[dice[j]]) / 6] or worst[:1]
                for j in again: faces[j] = rng.choice(DIE[dice[j]])
                v = total(); taken = max(0, dmg - max(0, v - bpen))
        else:
            dice_n, sta = arg if how == 'dodge' else (nd, sta1)
            c.sta += sta
            # 2017: having paid for the dodge the character can move one node, before the dice are rolled and whatever they show
            if how == 'dodge' and r.dodge_move == 'before': self.reposition(c, 0, True, count=False, frost=False)   # frostbite is charged on the dodge
            got = sum(rng.random() < 0.5 for _ in range(dice_n)); ok = got >= k + pen_d
            if peek: ok = True                              # the roll was seen before the dodge was chosen
            if not ok and c.luck and dice_n > got:
                # luck re-rolls the failed dodge dice: one of them under the official rules, all of them under the manuscript
                c.luck = False; n_again = 1 if getattr(r, 'luck', 'one') == 'one' else dice_n - got
                got += sum(rng.random() < 0.5 for _ in range(n_again)); ok = got >= k + pen_d
            if ok:
                hit = False
                if how == 'parry':
                    src.stagger = True; src.fresh = True; self.riposte(c, src)     # placed during the attacker's own turn
                else:
                    if c.heroic and c.name == 'Assassin' and src.hp > 0:                   # Backstab: a free attack after a dodge
                        o = c.best_option(src, DIST[c.node][src.node], 99, hand='R')
                        if o: self.hero(c); self.strike(c, src, o)
                if how != 'parry' and r.dodge_move is True:
                    # the manuscript: a successful dodge always moves the character one node. Off the attacker's own
                    # node if it is there; otherwise sideways, keeping its distance where the tile allows
                    d0 = DIST[c.node][src.node]
                    same = [x for x in NBR[c.node] if DIST[x][src.node] == max(1, d0)]
                    c.node = rng.choice(same or [x for x in NBR[c.node] if x != src.node] or NBR[c.node])
                    if 'dodge2' in tr: c.node = step_away(c.node, src.node, rng)       # a card that lets the dodge carry two nodes
            elif how == 'parry':
                taken = dmg; c.stagger = True
            elif r.dodge_fail == 'armour':
                v = sum(sorted(roll(adice, rng))[-2:]) if r.block == 'best2' else sum(roll(adice, rng))
                taken = max(0, dmg - max(0, v - apen))
            else:
                taken = dmg
        self.dec[how] = self.dec.get(how, 0) + 1
        self.say('   ', c.name, how, 'vs', dmg, '->', taken if hit else 'avoided')
        if hit:
            if taken >= 3 and c.ember and r.ember: taken -= 1
            self.wound(c, taken)
            if taken > 0: c.hurt_by.add(src)
            if c.alive:
                if taken > 0 and 'tearstone' in tr: c.sta = max(0, c.sta - 1)
                for e in effects:
                    if e == 'stagger': c.stagger = True
                    elif e == 'frostbite' and 'im_frost' not in tr: c.frost = True
                    elif e == 'poison' and 'im_poison' not in tr: c.poison = c.poison + 1 if r.poison == 'stack' else 1
                    elif e == 'bleed' and 'im_bleed' not in tr:
                        if r.bleed == 'official': c.bleed = True
                        elif c.bleed: c.bleed = False; self.wound(c, 3)
                        else: c.bleed = True
                if push and c.alive and 'im_push' not in tr:
                    c.node = step_away(c.node, src.node, rng) if c.node != src.node else rng.choice(NBR[c.node])
            if src.hp > 0 and src.node == c.node:
                if 'thorns' in tr: self.hurt(src, 1)                 # after a block or resist roll against an enemy in the node
                if 'sunset' in tr and 'Hollow' in src.name and src.hp > 0 and c.alive: src.node = rng.choice(NBR[src.node])
        return hit

    def hurt(self, f, d):
        """Damage to an enemy or boss that is not an attack roll (a condition, a card's text)."""
        if d <= 0 or f.hp <= 0: return
        f.hp -= d; self.check_heat(f)

    def afflict(self, t, fx):
        """Conditions placed on an enemy or boss by a character's attack that hit it, under the ruleset's condition rules."""
        r = self.r
        for e in fx:
            if t.hp <= 0: return
            if e == 'bleed':
                if r.bleed == 'official': t.bleed = True             # the next damage it suffers is two higher
                elif t.bleed: t.bleed = False; self.hurt(t, 3)       # the manuscript: a second token deals three damage at once
                else: t.bleed = True
            elif e == 'poison': t.poison = t.poison + 1 if r.poison == 'stack' else 1
            elif e == 'frostbite': t.frost = True
            elif e == 'stagger': t.stagger = True; t.fresh = False

    def hero(self, c):
        """The heroic action token is spent; cards that answer to it take effect."""
        c.heroic = False; tr = c.traits
        if 'hero_hp' in tr: c.dmg = max(0, c.dmg - 1)
        if 'hero_sta' in tr and not (c.frost and self.r.frost == 'author'): c.sta = max(0, c.sta - 1)
        if 'hero_cleanse' in tr:
            for x in sorted(self.live(), key=lambda x: -(x.poison * 2 + x.bleed + x.frost + x.stagger)):
                if x.poison: x.poison = 0
                elif x.bleed: x.bleed = False
                elif x.frost: x.frost = False
                elif x.stagger: x.stagger = False
                break

    def can_reach(self, f, c, slack=1):
        """Whether foe f has an attack that could land on character c in its coming activation."""
        closing = sum(s['n'] for s in f.card['steps'] if s['k'] == 'move' and s['dir'] == 'to')
        return any('dmg' in s and s.get('range', 0) + closing + slack >= DIST[f.node][c.node] for s in f.card['steps'])

    def p_kill(self, c, f, o):
        """Chance that attack option o by character c kills foe f outright."""
        guard = 0 if o.get('ignore') else f.resist if o['magic'] else f.armor
        mod = o['mod']
        if self.r.stagger == 'author': guard = max(0, guard - (1 if f.stagger else 0)); mod -= 1 if c.stagger else 0
        return sum(q for x, q in attack_pmf(o['dice'], mod, guard, o['repeat']) if x >= f.hp)

    def riposte(self, c, f):
        """The riposte after a parry, paid for like any attack. A player keeps one space of the bar back, since the
        riposte comes in the middle of the enemies' turn and a full bar means the next point of damage kills. The
        player fills the bar all the same (the author's ruling on how it is played) when the enemy is the last of the
        encounter, or when the riposte will probably kill it and no enemy still to act this turn can reach the
        character. Keeping a space back is the player's caution, not a rule."""
        room = c.cap - c.dmg - c.sta
        o = c.best_option(f, 0, room - 1, hand='R', spells=False)
        if self.r.lethal != 'full':                           # where a full bar kills, the last space is never spent
            full = c.best_option(f, 0, room, hand='R', spells=False)
            if full is not None and full is not o:
                others = [x for x in self.foes_alive() if x is not f]
                waiting = [x for x in others if x in getattr(self, 'to_act', others)]
                if not others or (self.p_kill(c, f, full) >= 0.5 and not any(self.can_reach(x, c) for x in waiting)):
                    o = full
        if o: c.sta += o['cost']; self.strike(c, f, o)

    # -------------------------------------------------------------- enemy activation
    def enemy_turn(self, f):
        r, rng = self.r, self.rng
        self.enemy_acts += 1
        for st in f.card['steps']:
            if not self.live() or self.failed() or f.hp <= 0: break
            if st['k'] == 'move':
                n = st['n'] - (1 if f.frost else 0)
                if st['n'] == 1 and r.move2(self.n): n += 1
                t = self.target(f, st['tgt'])
                if t is None: break
                struck = set()
                for _ in range(max(0, n)):
                    if st['dir'] == 'away':
                        f.node = step_away(f.node, t.node, rng); continue
                    if st.get('push'):
                        for c in self.live():
                            if c.node == f.node: c.node = rng.choice(NBR[c.node])       # shoved off the enemy's own node
                    # the target was fixed when the icon began; the enemy follows it wherever a push has sent it
                    if t is None or not t.alive or not self.live(): break
                    if f.node == t.node: break
                    origin = f.node; f.node = step_to(f.node, t.node, rng)
                    if st.get('push'):
                        for c in self.live():
                            if c.node != f.node: continue
                            was_hit = True                                   # a push-move with no damage pushes everyone
                            if 'dmg' in st and (c not in struck or not r.push_once):
                                struck.add(c)
                                # the push itself is resolved below, away from the node the enemy left. A character
                                # who dodges is not hit and is not pushed, whether or not the dodge moved it
                                was_hit = self.defend(f, c, st['dmg'] + f.atk_bonus - (1 if f.stagger else 0), st['magic'], st['dodge'],
                                                      push=False, effects=st.get('effects', ()), parryable=False)
                            if was_hit and c.alive and c.node == f.node:
                                far = [x for x in NBR[c.node] if DIST[x][origin] > DIST[c.node][origin]]
                                c.node = rng.choice(far or NBR[c.node])
            else:
                for _ in range(st.get('repeat', 1) * r.reps(self.n)):
                    t = self.target(f, st['tgt'])
                    if t is None or DIST[f.node][t.node] > st['range']: break
                    node = t.node
                    for c in ([x for x in self.live() if x.node == node] if st.get('node') else [t]):
                        self.defend(f, c, st['dmg'] + f.atk_bonus - (1 if f.stagger else 0), st['magic'], st['dodge'],
                                    push=st.get('push', False), effects=st.get('effects', ()), parryable=not st.get('node'))
        self.end_activation(f)

    def end_activation(self, f):
        """Tokens come off at the end of a model's turn. Where the ruleset says so (the workshop's ruling, section 9.6), a
        stagger token placed during the model's own turn stays until the end of its next one; under the manuscript as
        written and the official rules it comes off at once."""
        if f.fresh and getattr(self.r, 'stagger_hold', False): f.fresh = False
        else: f.stagger = False; f.fresh = False
        f.frost = False
        if f.poison and f.hp > 0 and self.live():
            # poison: one damage and the token comes off (official); a damage a token, one token off (the workshop's ruling)
            stack = self.r.poison == 'stack'
            self.hurt(f, f.poison if stack else 1); f.poison = max(0, f.poison - 1) if stack else 0

    def boss_cards(self, f):
        """The behaviours this boss model may still show: its part of each card in the deck and the discard pile."""
        cards = (self.pdeck + self.pdiscard) if self.special == 'pair' else (f.deck + f.discard)
        return [c['parts'][f.name] if 'parts' in c else c for c in cards]

    def boss_turn(self, f):
        r, rng = self.r, self.rng
        if self.special == 'pair': return self.pair_turn(f)
        self.enemy_acts += 1
        for _ in range(2 if self.special == 'pursuer' else 1):       # the Pursuer draws and resolves two cards a turn
            if not self.live() or self.failed() or f.hp <= 0: break
            if not f.deck:
                f.deck = f.discard; f.discard = []
                if r.boss_reshuffle: rng.shuffle(f.deck)
            card = f.deck.pop(0); f.discard.append(card)
            known = card['name'] in f.seen; f.seen.add(card['name'])
            f.weak = rng.random() < (self.WEAK_KNOWN if known else self.WEAK)
            self.resolve(f, card, known)
        self.end_activation(f)

    def pair_turn(self, f):
        """Ornstein and Smough: one card is drawn and each living model acts on its own part of it. When the first of
        them falls the survivor heats up at the start of the next turn: its own heat-up cards become the deck and it
        regains health (10 for Ornstein, 15 for Smough), to no more than it began with."""
        rng = self.rng; models = [m for m in self.foes if m.hp > 0]
        if not models or f is not models[0]: return                  # the turn is taken once, when the first living model comes up
        self.enemy_acts += 1
        if len(models) == 1 and not self.pair_heat:
            m = models[0]; self.pair_heat = True; m.heated = True
            self.pdeck = list(m.heat_cards); rng.shuffle(self.pdeck); self.pdiscard = []; m.seen = set()
            m.hp = min(m.max, m.hp + m.heal)
        if not self.pdeck:
            self.pdeck = self.pdiscard; self.pdiscard = []
            if self.r.boss_reshuffle: rng.shuffle(self.pdeck)
        card = self.pdeck.pop(0); self.pdiscard.append(card)
        for m in models:
            if m.hp <= 0 or not self.live() or self.failed(): continue
            known = card['name'] in m.seen; m.seen.add(card['name'])
            m.weak = rng.random() < (self.WEAK_KNOWN if known else self.WEAK)
            self.resolve(m, card['parts'][m.name] if 'parts' in card else card, known)
            self.end_activation(m)

    def resolve(self, f, card, known):
        """A boss model resolves the attacks of one behaviour card."""
        rng = self.rng
        bonus = self.boss_atk + (1 if (self.special == 'pursuer' and f.heated) else 0)      # the Pursuer hits one harder once heated up
        for _ in range(card['repeat']):
            for a in card['attacks']:
                live = self.live()
                if not live or self.failed() or f.hp <= 0: break
                t = self.aggro if (self.aggro.alive and rng.random() < 0.5) else self.target(f, 'nearest')
                for _s in range(2):                                 # bosses close on their target before striking
                    f.node = step_to(f.node, t.node, rng)
                victims = [t] + [c for c in live if c is not t and DIST[f.node][c.node] <= 1 and rng.random() < self.ARC]
                for c in victims:
                    if rng.random() < (self.pol.read_known if known else self.pol.read_new): continue    # out of the arc or the reach
                    self.defend(f, c, a['dmg'] + bonus - (1 if f.stagger else 0), a['magic'], card['dodge'], push=a['push'],
                                effects=a['effects'], parryable=False)

    def check_heat(self, f):
        """A boss heats up when its health reaches the point on its card: one heat-up card joins the deck, which is
        shuffled. Some bosses do it their own way (the manuscript, chapter 17)."""
        if not f.boss or f.hp <= 0 or self.special == 'pair': return
        rng = self.rng; sp = self.special
        if sp == 'sif' and f.hp <= 3 and not f.surges:
            f.surges = 1; f.deck = list(self.bdef['cool']); f.discard = []; f.seen = set(); return     # Sif, near death: one weak card from now on
        if f.heated or not f.card.get('heatup') or f.hp > f.card['heatup']: return
        f.heated = True
        if sp == 'artorias':                                         # two cards go at random; all his heat-up cards come in
            pool = f.deck + f.discard; rng.shuffle(pool); pool = pool[2:] + list(f.heat_cards)
        elif sp == 'smelter': pool = rng.sample(f.heat_cards, min(5, len(f.heat_cards)))     # a new deck of five heat-up cards
        else: pool = f.deck + f.discard + ([rng.choice(f.heat_cards)] if f.heat_cards else [])
        f.deck = pool; f.discard = []; rng.shuffle(f.deck)
        f.seen = set()                              # the order is new: the pattern has to be learned again

    # -------------------------------------------------------------- character turn
    def incoming(self, c, slack=1):
        """Room this character should keep on the bar for the damage due before its next turn: the mean plus 1.3
        standard deviations of that damage, from the attacks that can reach it and the chance each is aimed at it."""
        r = self.r; n = max(1, len(self.live())); mean = var = 0.0
        once = self.is_boss and getattr(r, 'boss_round', 'alternate') == 'once'
        phases = n if ((r.round == 'alternate' and not self.is_boss) or (self.is_boss and not once)) else 1   # enemy phases before this character acts again

        def add(share, dmg, magic, times=1):
            nonlocal mean, var
            share = min(1.0, share)
            if share <= 0 or dmg <= 0: return
            st = hit_stats(c.res if magic else c.blk, r.block, dmg, c.res_pen if magic else c.blk_pen)
            e1 = sum(d * p for d, p in st); e2 = sum(d * d * p for d, p in st)
            mean += times * share * e1; var += times * (share * e2 - (share * e1) ** 2)
        for f in self.foes_alive():
            if f.boss:
                cards = self.boss_cards(f)
                p_me = (0.5 if self.aggro is c else 0.0) + 0.5 / n
                p_me = (p_me + self.ARC * (1 - p_me)) * (1 - self.pol.read_new)
                draws = 2 if self.special == 'pursuer' else 1
                for k in cards:
                    for a in k['attacks']: add(p_me, a['dmg'] + self.boss_atk, a['magic'], draws * phases * k['repeat'] / len(cards))
                continue
            closing = sum(s['n'] for s in f.card['steps'] if s['k'] == 'move' and s['dir'] == 'to')
            nearest = self.target(f, 'nearest') is c
            for st in f.card['steps']:
                if 'dmg' not in st: continue
                if st.get('range', 0) + closing + slack < DIST[f.node][c.node]: continue
                if st['tgt'] == 'aggro': share = 1.0 if self.aggro is c else (1.0 / n if r.aggro == 'active' else 0.0)
                else: share = (0.6 if nearest else 0.4 / n) * (phases if r.round == 'alternate' else 1)
                add(share, st['dmg'] + f.atk_bonus, st['magic'], st.get('repeat', 1) * r.reps(self.n))
        self._ms = (mean, max(0.05, var) ** 0.5)
        return mean + 1.3 * max(0.0, var) ** 0.5

    def risk(self, room):
        """Chance (normal approximation) that the damage due before the next turn exceeds `room` on the bar."""
        m, s = self._ms
        return 0.5 * math.erfc((room + 0.5 - m) / (s * 1.4142))

    def kill_value(self, f, last):
        """What removing a foe is worth, in points of damage: what it would deal over the next three rounds, and the
        fight itself if it is the last one standing."""
        if f.boss: return 12.0
        blk = sum(c.mean_blk for c in self.live()) / max(1, len(self.live()))
        per = sum(max(0.5, s['dmg'] + f.atk_bonus - blk) * s.get('repeat', 1) * self.r.reps(self.n) for s in f.card['steps'] if 'dmg' in s)
        phases = len(self.live()) if self.r.round == 'alternate' else 1
        return 3.0 * per * phases + (6.0 if last else 0.0)

    def strike(self, c, f, o):
        """Character c makes attack option o (already paid for) against foe f; a node attack hits every foe there. An
        attack that repeats is resolved once for each repetition, and when its target has fallen the next repetition
        may take another enemy within the attack's reach. Conditions and the other things printed on the attack follow."""
        rng = self.rng; r = self.r; grand = 0; tr = c.traits
        if c.buff and o['dice'] and not o.get('spell'): o = dict(o, magic=True, mod=o['mod'] + c.buff['mod'])   # a weapon made magical this turn
        mod = o['mod'] + (o.get('ember_mod', 0) if c.ember else 0) - (1 if (c.stagger and r.stagger == 'author') else 0)
        if 'redtear' in tr and c.dmg >= 4 and o['dice']: mod += 1     # a ring that rewards fighting on while badly hurt
        if o.get('direct'):                                          # a fixed amount of damage, no roll: only on an enemy that shares its node
            if any(g is not f and g.node == f.node for g in self.foes_alive()):
                self.hurt(f, o['direct']); self.dealt[c] = self.dealt.get(c, 0) + o['direct']; grand = o['direct']
            return grand
        node0 = f.node
        for _ in range(o['repeat']):
            if f.hp <= 0:
                if o.get('same') == 'enemy': break                   # every repetition is aimed at the one enemy
                near = [g for g in self.foes_alive() if DIST[c.node][g.node] <= o['range'] and not (o.get('shaft') and g.node == c.node)]
                if o.get('same') == 'node': near = [g for g in near if g.node == node0]
                if not near: break
                f = min(near, key=lambda g: (g.hp, -g.threat))       # the one most likely to fall to what is left
            if o.get('area'): targets = [x for x in self.foes_alive() if DIST[c.node][x.node] <= o['area'] and not (o.get('shaft') and x.node == c.node)]
            elif o.get('node'): targets = [x for x in self.foes_alive() if x.node == f.node]
            else: targets = [f]
            dice = o['dice'] + (('u' if 'weak_blue' in tr else 'b') if (f.boss and f.weak and o['range'] <= 1 and o['dice']) else '')
            faces = roll(dice, rng); c.rolls += 1
            if o.get('reroll') and faces:                            # two-handed grip: one die may be rolled again
                i = min(range(len(faces)), key=lambda j: faces[j] - sum(DIE[dice[j]]) / 6)
                if faces[i] < sum(DIE[dice[i]]) / 6: faces[i] = rng.choice(DIE[dice[i]])
            v = sum(faces) + mod
            for t in targets:
                guard = 0 if o.get('ignore') else t.resist if o['magic'] else t.armor
                if t.stagger and r.stagger == 'author': guard = max(0, guard - 1)      # a staggered model blocks and resists one less
                lead = v + (1 if ('leo' in tr and t in c.hurt_by) else 0) + (o.get('vs_boss', 0) if t.boss else 0) \
                    + (o.get('vs_hollow', 0) if 'Hollow' in t.name else 0)
                total = max(0, lead - guard)
                if 'knightslayer' in tr and o['dice'] and lead - guard >= 3 and not (c.frost and r.frost == 'author'): c.sta = max(0, c.sta - 1)
                if total > 0:
                    if t.bleed and r.bleed == 'official': total += 2; t.bleed = False
                    t.hp -= total; self.dealt[c] = self.dealt.get(c, 0) + total; grand += total
                    # the manuscript: against a boss the token goes to whoever damaged it since its last turn
                    if r.aggro == 'last' or (r.aggro == 'most' and self.is_boss): self.aggro = c
                    if self.special == 'dragonslayer' and t.boss and total >= 4 and t.surges < 3 and t.hp > 0:
                        t.surges += 1; t.deck.insert(0, rng.choice(t.heat_cards))      # a heavy blow brings a heat-up card to the top of its deck
                    self.check_heat(t)
                elif o.get('hollow'): c.luck = True                  # a gem that readies luck when the blow does nothing
                self.say('   ', c.name, 'hits', t.name, 'with', o['name'], 'for', total, '(hp', max(0, t.hp), ')')
                if o.get('fx'): self.afflict(t, o['fx'])             # a condition is placed by a hit, whatever damage it did
                if o.get('push') and not t.boss and t.hp > 0:        # a boss is never pushed by a character
                    t.node = step_away(t.node, c.node, rng) if t.node != c.node else rng.choice(NBR[t.node])
        if o.get('gain_hp'): c.dmg = max(0, c.dmg - o['gain_hp'])
        if o.get('gain_sta') and not (c.frost and r.frost == 'author'): c.sta = max(0, c.sta - o['gain_sta'])
        if o.get('aggro') and self.live():                           # the token may be handed to another: the sturdiest takes it
            self.aggro = max(self.live(), key=lambda x: (x.mean_blk + 0.5 * x.dodge, x.cap - x.dmg - x.sta))
        if o.get('self_dmg'): self.wound(c, o['self_dmg'])
        if 'bleed' in o.get('self_fx', ()) and c.alive and 'im_bleed' not in tr:      # a weapon that makes its wielder bleed
            if r.bleed == 'official' or not c.bleed: c.bleed = True
            else: c.bleed = False; self.wound(c, 3)
        return grand

    # -------------------------------------------------------------- support actions
    def sup_plan(self, c, o):
        """What a support action would do now: (worth in points of damage, who receives it)."""
        r = self.r; live = [x for x in self.live() if DIST[c.node][x.node] <= o['range']]
        barred = lambda x: x.frost and r.frost == 'author'           # frostbite bars any recovery of stamina
        if 'sup' in o:
            s = o['sup']

            def need(x):
                hp = min(s['hp'], x.dmg); st = 0 if barred(x) else min(s['sta'], x.sta)
                return hp * (1.8 if x.cap - x.dmg - x.sta <= 3 else 1.0) + 1.2 * self.pol.w_sta * st
            who = s['who']
            if who == 'one': pick = sorted(live, key=need)[-1:]
            elif who == 'two': pick = sorted(live, key=need)[-2:]
            elif who == 'others': pick = [x for x in live if x is not c]
            elif who == 'node':
                nodes = {x.node for x in live}
                pick = max(([x for x in live if x.node == nd] for nd in nodes), key=lambda g: sum(need(x) for x in g)) if nodes else []
            else: pick = live
            return sum(need(x) for x in pick), pick
        if 'guard' in o:
            g = o['guard']; pick = [c] if g['who'] == 'self' else (self.live() if g['who'] == 'party' else live)
            return 0.45 * len(pick) * (0.6 if g['blk'] == '' or g['res'] == '' else 1.0), pick
        if 'gain_sta' in o: return (0.0 if barred(c) else 1.2 * self.pol.w_sta * min(o['gain_sta'], c.sta)), [c]
        if 'buff' in o:
            # an attack with the other hand becomes magical (and stronger): worth the block it gets past
            foes = self.foes_alive(); other = c.options['L' if o['hand'] == 'R' else 'R']
            if not foes or not [x for x in other if x['dice'] and not x['magic'] and not x.get('spell')]: return 0.0, [c]
            f = min(foes, key=lambda f: DIST[c.node][f.node])
            return 0.9 * max(0, f.armor - f.resist + o['buff']['mod']), [c]
        return 0.0, []

    def support(self, c, o, pick):
        r = self.r
        if 'sup' in o:
            more = 1 if ('mender' in c.traits and o['sup']['hp']) else 0      # an armour that adds one to any healing its wearer gives
            for x in pick:
                x.dmg = max(0, x.dmg - o['sup']['hp'] - more)
                if not (x.frost and r.frost == 'author'): x.sta = max(0, x.sta - o['sup']['sta'])
        elif 'guard' in o:
            for x in pick: x.guard = (x.guard[0] + o['guard']['blk'], x.guard[1] + o['guard']['res'])
        elif 'gain_sta' in o: c.sta = max(0, c.sta - o['gain_sta'])
        elif 'buff' in o: c.buff = o['buff']
        self.say('   ', c.name, 'uses', o['name'], 'on', [x.name for x in pick])

    def walk(self, c, steps, free=0):
        """What moving `steps` nodes costs character c: (stamina, whether it ran), or None if its cards forbid it.
        One node is the free Walk, unless a card says none or two; `free` adds nodes given by a heroic action or a shift."""
        tr = c.traits
        free += 0 if 'no_walk' in tr else 2 if 'walk2' in tr else 1
        run = max(0, steps - free)
        if run and 'no_run' in tr: return None
        return run * (2 if 'run2' in tr else 1) + (steps if (c.frost and self.r.frost == 'official') else 0), bool(run)

    def reposition(self, c, budget, walk_free, count=True, frost=True):
        """After acting, step out of the enemies' reach if that saves more damage than it costs in stamina. Also used for
        the optional step of an official dodge (count=False keeps it out of the tally of turns ending with a step)."""
        if not self.foes_alive() or budget < 0: return
        here = c.node; base = self.incoming(c, 0); best = (0.25, here, 0)
        reach = max([o['range'] for h in 'RL' for o in c.options[h]] or [0])
        seen = {here: 0}; frontier = [here]
        for depth in (1, 2):
            nxt = []
            for a in frontier:
                for b in NBR[a]:
                    if b not in seen: seen[b] = depth; nxt.append(b)
            frontier = nxt
        for node, steps in seen.items():
            if steps == 0: continue
            tr = c.traits
            run = max(0, steps - ((0 if 'no_walk' in tr else 2 if 'walk2' in tr else 1) if walk_free else 0))
            if run and 'no_run' in tr: continue
            cost = run * (2 if 'run2' in tr else 1)
            if frost and c.frost and self.r.frost == 'official': cost += steps          # 2017 frostbite: one more for each walk or run
            if cost > budget: continue
            c.node = node
            gap = max(0, min(DIST[node][f.node] for f in self.foes_alive()) - reach - 1)       # running needed to return
            val = 0.8 * (base - self.incoming(c, 0)) - self.pol.w_sta * (cost + 0.6 * gap) - 0.3 * sum(1 for i in range(cost) if budget - i <= 3)
            if val > best[0]: best = (val, node, cost)
        c.node = best[1]; c.sta += best[2]
        if (best[2] or best[1] != here) and count:
            self.dec['step'] = self.dec.get('step', 0) + 1; self.say('   ', c.name, 'steps back to', NODES[c.node])

    def char_turn(self, c):
        r, pol, rng = self.r, self.pol, self.rng
        self.char_turns += 1; tr = c.traits
        c.guard = ('', ''); c.buff = None; c.rolls = 0
        # stamina at the start of the turn: none under the manuscript's frostbite, one less under the 2022 rules
        barred = c.frost and r.frost == 'author'
        if not barred:
            regen = max(0, r.regen - (1 if (c.frost and r.frost == '2022') else 0))
            if any('chloranthy' in x.traits for x in self.live() if x.node == c.node): regen += 1
            if 'mask' in tr: regen += 1
            if 'tinybeing' in tr and regen >= 1 and c.dmg > 0: regen -= 1; c.dmg -= 1      # one of the stamina traded for health
            c.sta = max(0, c.sta - regen)
        if 'sanctus' in tr: c.dmg = max(0, c.dmg - 1)
        if 'blessing' in tr and c.bless and c.dmg >= pol.estus_at + 1 and not c.estus:
            c.bless = False; c.dmg = 0; c.poison = 0; c.bleed = c.frost = c.stagger = False     # discarded for good: all damage and conditions off
        if 'blades' in tr and not c.luck and c.cap - c.dmg - c.sta >= 4: c.dmg += 1; c.luck = True
        if r.aggro == 'active': self.aggro = c
        c.ran = False
        foes = self.foes_alive()
        need = pol.caution * self.incoming(c)
        if self.log is not None:
            self.say('  ', c.name, 'turn: dmg', c.dmg, 'sta', c.sta, 'at', NODES[c.node], 'need %.1f' % need,
                     [(f.name[:8], NODES[f.node], f.hp) for f in foes])
        free = c.cap - c.dmg - c.sta
        # an ember card (the manuscript): an action that clears all damage and the hollow state and leaves the character embered
        if c.ember_card and (c.dmg >= pol.estus_at + 1 or (c.hollow and c.dmg >= 3)) and not c.estus:
            c.ember_card = False; c.ember = True; c.dmg = 0; c.hollow = False; c.was_hollow = False    # no longer hollow if it dies
            self.say('  ', c.name, 'uses an ember'); self.end_turn(c); return
        # heroic actions that mend: the Thief's own wounds and stamina, the Cleric's and its neighbours' wounds
        if c.heroic and c.name == 'Thief' and c.dmg >= 2 and (c.sta >= 2 or c.dmg >= 4):
            self.hero(c); c.dmg = max(0, c.dmg - 2)
            if not barred: c.sta = max(0, c.sta - 2)
        if c.heroic and c.name == 'Cleric':
            near = [x for x in self.live() if DIST[c.node][x.node] <= 1]
            if sum(min(2, x.dmg) for x in near) >= min(3, 2 * len(self.live())):
                self.hero(c)
                for x in near: x.dmg = max(0, x.dmg - 2)
        free = c.cap - c.dmg - c.sta
        # the flask: drunk when death is near; where damage outlasts the encounter (the manuscript) also once badly hurt
        if c.estus and c.dmg >= 3 and (self.risk(free) > pol.estus_risk or (r.recover != 'all' and c.dmg >= pol.estus_at)):
            c.estus = False; c.dmg = 0
            self.say('  ', c.name, 'drinks')
            if r.estus == 'full': c.sta = 0; free = c.cap
            else: self.end_turn(c); return                           # a major action: the turn ends
        if c.heroic and c.name == 'Herald' and (sum(x.sta for x in self.live()) >= 2 * len(self.live())):
            self.hero(c)                                             # Perseverance: each character gains 2 stamina
            for x in self.live():
                if not (x.frost and r.frost == 'author'): x.sta = max(0, x.sta - 2)      # frostbite bars any recovery
        attacked = False; moved = False; rested = False
        cast = False                                   # a spell has been used this turn (the manuscript allows one)
        used = set()
        wd = pol.w_death * (1.6 if (r.death == 'party' or c.hollow or len(self.live()) == 1) else 1.0)
        one_spell = getattr(r, 'one_spell', False)
        for attempt in (0, 1):
            foes = self.foes_alive()
            if not foes: break
            free = c.cap - c.dmg - c.sta
            self.incoming(c); risk0 = self.risk(free)
            room = free - (1 if r.lethal == 'full' else 0)
            best = None
            for f in foes:
                d = DIST[c.node][f.node]
                for hand in ('R', 'L'):
                    if hand in used: continue
                    for base in c.options[hand]:
                        if cast and base.get('spell') and one_spell: continue
                        for o, hero, hstep in self.variants(c, base, d):
                            rg = o['range']
                            steps = max(0, d - rg) if attempt == 0 else (0 if d <= rg else 99)
                            if o['shaft'] and d - steps == 0:
                                if attempt: continue
                                steps = 1
                            if steps == 99: continue
                            if o.get('direct') and not any(g is not f and g.node == f.node for g in foes): continue
                            # one step is the free Walk; a heroic action or a shift printed on the attack may give more
                            w = self.walk(c, steps, hstep + o.get('shift', 0))
                            if w is None: continue
                            run, ran = w
                            cost = o['cost'] + run + (1 if (c.stagger and r.stagger == 'official') else 0) \
                                + (1 if (f.boss and f.heated and f.name == 'Gargoyle' and d - steps == 0) else 0)
                            if cost + o.get('self_dmg', 0) > room: continue
                            last = len(foes) == 1; vk = self.kill_value(f, last)
                            if o.get('direct'): ed = min(o['direct'], f.hp); pk = 1.0 if o['direct'] >= f.hp else 0.0
                            else:
                                guard = 0 if o.get('ignore') else (f.resist if o['magic'] else f.armor)
                                pm = attack_pmf(o['dice'], o['mod'] + c.scale_bonus(o), guard, o['repeat'])
                                ed = sum(min(x, f.hp) * p for x, p in pm); pk = sum(p for x, p in pm if x >= f.hp)
                                # what a condition adds while the enemy lives: bleed and poison as damage to come
                                fx = o.get('fx', ())
                                if fx and pk < 0.9:
                                    more = (3.0 if (f.bleed and r.bleed != 'official') else 1.0) * ('bleed' in fx) + 1.0 * ('poison' in fx) \
                                        + 0.6 * ('stagger' in fx) + 0.2 * ('frostbite' in fx)
                                    ed += (1 - pk) * min(more, max(0.0, f.hp - ed) + 0.6)
                                if o.get('gain_hp') and c.dmg: ed += 0.8 * min(o['gain_hp'], c.dmg)
                            others = [g for g in foes if g is not f and ((o.get('area') and DIST[c.node][g.node] <= o['area'])
                                                                         or (o.get('node') and g.node == f.node and not o.get('area')))]
                            if others and not f.boss and not o.get('direct'):
                                for g in others:
                                    pg = attack_pmf(o['dice'], o['mod'], g.resist if o['magic'] else g.armor, o['repeat'])
                                    vg = self.kill_value(g, False)
                                    ed += (sum(min(x, g.hp) * p for x, p in pg) / g.max * 0.5 * vg + sum(p for x, p in pg if x >= g.hp) * vg) / (0.5 * vk / f.max)
                            # the price of stamina: the added chance of dying before the next turn
                            danger = (self.risk(free - cost - o.get('self_dmg', 0)) - risk0) * (1 - pk if last else 1.0)
                            score = (ed if f.boss else ed / f.max * 0.5 * vk) + pk * vk - pol.w_sta * cost - wd * danger - 1.0 * o.get('self_dmg', 0)
                            if cost == 0 and ed > 0: score = max(score, 0.01)          # a free blow is never passed up
                            if self.idle >= 2 and ed > 0: score += 50.0                # nothing is being done: the fight must be forced, whatever the risk
                            if best is None or score > best[0]: best = (score, f, hand, o, steps, cost, ran, hero)
            for hand in ('R', 'L'):                                  # a hand that heals, steadies or lends stamina instead
                if hand in used: continue
                for o in c.support[hand]:
                    if (cast and o.get('spell') and one_spell) or o['cost'] > room: continue
                    if 'buff' in o and attacked: continue
                    val, pick = self.sup_plan(c, o)
                    if val <= 0.5 and not ('buff' in o and val > 0): continue
                    score = val - pol.w_sta * o['cost'] - wd * (self.risk(free - o['cost']) - risk0) + (2.0 if 'buff' in o else 0.0)
                    if best is None or score > best[0]: best = (score, pick, hand, o, 0, o['cost'], False, False)
            if best is None or best[0] <= 0: break
            _, f, hand, o, steps, cost, ran, hero = best
            c.sta += cost; used.add(hand); cast = cast or bool(o.get('spell'))
            if isinstance(f, list):                                  # a support action
                self.support(c, o, f); self.dec['support'] = self.dec.get('support', 0) + 1
                continue
            if hero: self.hero(c)
            if steps: moved = True
            for _ in range(steps):
                c.node = step_to(c.node, f.node, rng) if not (o['shaft'] and DIST[c.node][f.node] == 1) else c.node
            if o['shaft'] and c.node == f.node: c.node = rng.choice(NBR[c.node])
            if ran: c.ran = True
            attacked = True
            self.dec['heavy' if o['cost'] >= 2 else 'light'] = self.dec.get('heavy' if o['cost'] >= 2 else 'light', 0) + 1
            self.strike(c, f, o)
            if not c.alive: self.end_turn(c); return                 # an attack that costs health can be the last
            other = 'L' if hand == 'R' else 'R'
            if not (c.options[other] or c.support[other]): break
        if not attacked:
            foes = self.foes_alive()
            if foes and r.turn == 'major' and c.sta > 0 and not used and not (c.frost and r.frost == 'author'):      # frostbite bars any recovery
                c.sta = 0; rested = True; self.dec['rest'] = self.dec.get('rest', 0) + 1; self.say('  ', c.name, 'rests')            # the Rest action
            elif foes:
                f = min(foes, key=lambda f: DIST[c.node][f.node])
                # the approach is the free Walk; under the 2017 rules a frostbitten character pays one stamina for it,
                # and stays where it is if the bar has no room for that
                w = self.walk(c, 1)
                if DIST[c.node][f.node] > 1 and w is not None and w[0] <= c.cap - c.dmg - c.sta - (1 if r.lethal == 'full' else 0):
                    c.sta += w[0]; c.node = step_to(c.node, f.node, rng); moved = True
        # hit and run: official rules allow movement before or after attacking, not both; the manuscript has no such limit
        if pol.kite and self.foes_alive() and not self.is_boss and (r.turn != 'official' or not moved):
            free = c.cap - c.dmg - c.sta
            budget = min(2, free - 1 - int(pol.caution * 0.5 * self.incoming(c)))
            if rested: budget = min(budget, 0)               # Rest and Run cannot share a turn: only the free Walk is left
            self.reposition(c, budget, walk_free=not moved)
        self.end_turn(c)

    def variants(self, c, o, d):
        """An attack option as it stands, and as a heroic action would change it: (option, heroic action used, free nodes)."""
        yield o, False, 0
        if not c.heroic or not o['dice']: return
        n = c.name
        if n == 'Warrior' and o['range'] == 0 and o['cost'] >= 2:
            yield dict(o, cost=0, node=True), True, 1                # a free step; the attack costs nothing and strikes the node
        elif n == 'Mercenary' and o['cost'] >= 2:
            yield dict(o, cost=0), True, 0                           # Rapid Strike: an attack that costs no stamina
        elif n == 'Sorcerer' and o['magic'] and (o['cost'] >= 3 or d > o['range']):
            # Spell Fury: a magic attack reaches any distance and costs three less
            yield dict(o, cost=max(0, o['cost'] - 3), range=9, mod=o['mod'] + (1 if 'dragoncrest' in c.traits else 0)), True, 0
        elif n == 'Pyromancer' and o['cost'] >= 2:
            yield dict(o, dice=o['dice'] + ('u' if 'swamp' in c.traits else 'b')), True, 0       # Explosive Crit: one more die

    def end_turn(self, c):
        r = self.r; tr = c.traits
        if c.alive:
            if 'sunprincess' in tr: c.dmg = max(0, c.dmg - 1)
            if 'lothric' in tr: c.dmg = max(0, c.dmg - sum(1 for f in self.foes_alive() if f.node == c.node))
            if c.rolls >= 2:
                if 'pontiff' in tr: c.dmg = max(0, c.dmg - 1)
                if 'favour' in tr and not (c.frost and r.frost == 'author'): c.sta = max(0, c.sta - 1)
        # the encounter is cleared the moment the last enemy falls: conditions then come off without being resolved
        if c.poison and c.alive and self.foes_alive():
            self.wound(c, c.poison if r.poison == 'stack' else 1); c.poison = max(0, c.poison - 1) if r.poison == 'stack' else 0
        c.stagger = False; c.frost = False; c.hurt_by = set()
        # a card that lets its wearer take the aggro token, once an encounter, when another character's turn ends
        for x in self.live():
            if x is not c and 'faraam' in x.traits and id(x) not in self.faraam and self.aggro is not x and self.aggro.alive \
                    and x.mean_blk + 0.5 * x.dodge > self.aggro.mean_blk + 0.5 * self.aggro.dodge + 0.3:
                self.faraam.add(id(x)); self.aggro = x; break

    # -------------------------------------------------------------- the fight
    def order(self):
        live = self.live()
        if self.r.order == 'free':                     # the party chooses: the sturdiest acts last and keeps the enemies' eyes
            return sorted(live, key=lambda c: (c.mean_blk + c.dodge * 0.5, c.cap - c.dmg))
        return sorted(live, key=lambda c: -c.taunt)

    def stalled(self):
        """Kept at the end of each round: how many rounds have passed with no enemy losing health. A party that only
        backs away from enemies it finds hard to hurt has to close and strike all the same."""
        hp = sum(f.hp for f in self.foes_alive())
        self.idle = self.idle + 1 if hp == self._hp else 0
        self._hp = hp

    def run(self, max_rounds=60):
        r = self.r
        for c in self.party: c.was_hollow = c.hollow
        first = next((c for c in self.party if 'mon' in c.traits and c.mon), None)      # a card that lets the party act first, once a spark
        if first is not None: first.mon = False
        if (self.is_boss and getattr(r, 'boss_round', 'alternate') == 'alternate') or (not self.is_boss and r.round == 'alternate'):
            while not self.over() and self.rounds < max_rounds:
                self.rounds += 1
                for _ in range(self.seats):
                    if self.over(): break
                    self.to_act = set(self.foes_alive())
                    for f in ([] if first is not None else sorted(self.foes_alive(), key=lambda f: -f.threat)):
                        self.to_act.discard(f)
                        if self.over(): break
                        if f.hp <= 0: continue               # killed during another enemy's activation
                        (self.boss_turn if f.boss else self.enemy_turn)(f)
                    if self.over(): break
                    for _k in range(self.seats):             # the next living character in seat order
                        c = self.party[self.turn_i % self.seats]; self.turn_i += 1
                        if c.alive: break
                    if c.alive: self.char_turn(c)
                    if first is not None and self.turn_i % self.seats == 0: first = None      # every character has had the free turn
                self.stalled()
        else:
            while not self.over() and self.rounds < max_rounds:
                self.rounds += 1; self.dealt = {}
                self.to_act = set(self.foes_alive())
                for f in ([] if first is not None else sorted(self.foes_alive(), key=lambda f: (-f.threat, min(DIST[f.node][c.node] for c in self.live())))):
                    self.to_act.discard(f)
                    if self.over(): break
                    if f.hp <= 0: continue                   # killed during another enemy's activation
                    (self.boss_turn if f.boss else self.enemy_turn)(f)
                if self.over(): break
                for c in self.order():
                    if self.over(): break
                    if c.alive: self.char_turn(c)
                first = None; self.stalled()
                if r.aggro == 'most' and self.dealt:
                    top = max(self.dealt.values()); lead = [c for c, v in self.dealt.items() if v == top and c.alive]
                    if len(lead) == 1: self.aggro = lead[0]
        for c in self.party: c._first = self.turn_i
        return (not self.failed()) and not self.foes_alive()
