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
        return dict(evade=0.35 * s, read_new=0.1 + 0.2 * s, read_known=0.3 + 0.6 * s)

    def __init__(self, skill=None, **kw):
        if skill is not None: self.__dict__.update(self.at(skill))
        self.__dict__.update(kw)

# ------------------------------------------------------------------ models


class Foe:
    __slots__ = ('name', 'card', 'hp', 'max', 'node', 'stagger', 'frost', 'poison', 'bleed', 'boss', 'deck', 'discard',
                 'heated', 'heat_cards', 'armor', 'resist', 'threat', 'weak', 'atk_bonus', 'seen')

    def __init__(self, name, card, hp, node, boss=False):
        self.name, self.card, self.hp, self.max, self.node, self.boss = name, card, hp, hp, node, boss
        self.stagger = self.frost = False; self.poison = 0; self.bleed = False
        self.armor, self.resist, self.threat = card['armor'], card['resist'], card.get('threat', 10)
        self.deck = self.discard = self.heat_cards = None; self.heated = False; self.weak = False; self.atk_bonus = 0
        self.seen = set()

    @property
    def alive(self): return self.hp > 0


class Fight:
    """One encounter (a list of enemy names) or one boss fight (a boss name)."""
    ARC = 0.35       # chance that a boss attack also catches another character standing within one node of the boss
    WEAK = 0.3       # chance that a character's attack on a boss comes from a weak arc (+1 black die): card not yet seen
    WEAK_KNOWN = 0.6 # the same once the card has been seen (the deck comes round in the same order)

    def __init__(self, party, rules, rng, enemies=None, boss=None, policy=None, log=None, n=None):
        self.party, self.r, self.rng, self.pol, self.log = party, rules, rng, policy or Policy(), log
        self.n = n or len(party);                      # scaling counts every character in the game, present or not
        self.seats = len(party); self.rounds = 0; self.char_turns = 0; self.enemy_acts = 0; self.deaths = 0
        self.is_boss = boss is not None; self.dealt = {}
        r = rules
        ents = list(ENTRY); rng.shuffle(ents)
        for i, c in enumerate(party):
            c.node = ents[i % 3] if self.pol.spread else ents[0]
            c.alive = True; c.stagger = c.frost = False; c.poison = 0; c.bleed = False; c.ran = False
        if boss:
            b = BOSSES[boss]; mul = getattr(r, 'boss_mul', None)
            if mul: b = dict(b, hp=int(round(b['hp'] * mul(self.n))), heatup=int(round(b['heatup'] * mul(self.n))))
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
        """An attack of `dmg` (after scaling) with dodge difficulty k resolves against character c."""
        if not c.alive: return
        r, pol, rng = self.r, self.pol, self.rng
        if not src.boss and rng.random() < pol.evade: return
        free = c.cap - c.dmg - c.sta
        pen = 1 if (c.stagger and r.stagger == 'author') else 0
        dice = c.res if magic else c.blk
        adice = c.arm_res if magic else c.arm_blk
        wd = pol.w_death * (1.6 if (r.death == 'party' or c.hollow or len(self.live()) == 1) else 1.0)

        def cost(pmf, extra_sta):
            lim = free - extra_sta
            e = sum(d * p for d, p in pmf)
            pl = sum(p for d, p in pmf if (d >= lim if r.lethal == 'full' else d > lim) and d > 0)
            # stamina is cheap while the bar is open and dear once it crowds out room for damage
            crowd = sum(1.0 for i in range(extra_sta) if free - i <= 4)
            return e + wd * pl + pol.w_sta * extra_sta + 0.6 * crowd
        opts = [(cost(hit_stats(dice, r.block, dmg, pen), 0), 'block', 0)]
        sta1 = 1 + (1 if (c.frost and r.frost == 'official') else 0)
        room = free - (1 if r.lethal == 'full' else 0)
        nd = c.dodge
        fail = hit_stats(adice, r.block, dmg, pen) if r.dodge_fail == 'armour' else ((dmg, 1.0),)
        tries = [(nd, sta1)]
        if r.dodge_extra:
            tries += [(nd + j, sta1 + 2 * j) for j in (1, 2) if nd + j <= 4]
        for dice_n, sta in tries:
            if sta > room or (dice_n <= 0 and k > 0): continue
            ps = p_dodge(dice_n, k + pen)
            mixed = ((0, ps),) + tuple((d, p * (1 - ps)) for d, p in fail)
            opts.append((cost(mixed, sta), 'dodge', (dice_n, sta)))
        if (r.parry and parryable and not push and c.can_parry and DIST[src.node][c.node] == 0 and sta1 <= room
                and not src.boss):
            ps = p_dodge(nd, k + pen)
            gain = c.riposte_ev(src) + 1.0                       # the riposte, and the stagger on the attacker
            mixed = ((0, ps), (dmg, 1 - ps))
            opts.append((cost(mixed, sta1) - ps * gain + (1 - ps) * 1.0, 'parry', None))
        _, how, arg = min(opts, key=lambda o: o[0])
        hit = True; taken = 0
        if how == 'block':
            v = sum(sorted(roll(dice, rng))[-2:]) if r.block == 'best2' else sum(roll(dice, rng))
            taken = max(0, dmg - max(0, v - pen))
            if c.heroic and c.name == 'Knight' and (self.lethal(c, taken) or taken >= 2):
                c.heroic = False; v += rng.choice(DIE['u']); taken = max(0, dmg - max(0, v - pen))     # Stand Fast
            if c.luck and (self.lethal(c, taken) or taken >= pol.luck_at):
                c.luck = False
                v = sum(sorted(roll(dice, rng))[-2:]) if r.block == 'best2' else sum(roll(dice, rng))
                taken = max(0, dmg - max(0, v - pen))
        else:
            dice_n, sta = arg if how == 'dodge' else (nd, sta1)
            c.sta += sta
            ok = sum(rng.random() < 0.5 for _ in range(dice_n)) >= k + pen
            if not ok and c.luck:
                c.luck = False; ok = sum(rng.random() < 0.5 for _ in range(dice_n)) >= k + pen
            if ok:
                hit = False
                if how == 'parry':
                    src.stagger = True; self.riposte(c, src)
                else:
                    if c.heroic and c.name == 'Assassin' and src.hp > 0:                   # Backstab: a free attack after a dodge
                        o = c.best_option(src, DIST[c.node][src.node], 99, hand='R')
                        if o: c.heroic = False; self.strike(c, src, o)
                if how != 'parry' and r.dodge_move:
                    c.node = step_away(c.node, src.node, rng) if DIST[c.node][src.node] == 0 else c.node
                    if c.node == src.node: c.node = rng.choice(NBR[c.node])
            elif how == 'parry':
                taken = dmg; c.stagger = True
            elif r.dodge_fail == 'armour':
                v = sum(sorted(roll(adice, rng))[-2:]) if r.block == 'best2' else sum(roll(adice, rng))
                taken = max(0, dmg - max(0, v - pen))
            else:
                taken = dmg
        self.say('   ', c.name, how, 'vs', dmg, '->', taken if hit else 'avoided')
        if hit:
            if taken >= 3 and c.ember and r.ember: taken -= 1
            self.wound(c, taken)
            if c.alive:
                for e in effects:
                    if e == 'stagger': c.stagger = True
                    elif e == 'frostbite': c.frost = True
                    elif e == 'poison': c.poison = c.poison + 1 if r.poison == 'stack' else 1
                    elif e == 'bleed':
                        if r.bleed == 'official': c.bleed = True
                        elif c.bleed: c.bleed = False; self.wound(c, 3)
                        else: c.bleed = True
                if push and c.alive: c.node = step_away(c.node, src.node, rng) if c.node != src.node else rng.choice(NBR[c.node])

    def riposte(self, c, f):
        o = c.best_option(f, 0, c.cap - c.dmg - c.sta - 1, hand='R')
        if o: c.sta += o['cost']; self.strike(c, f, o)        # the riposte's stamina is paid like any attack's

    # -------------------------------------------------------------- enemy activation
    def enemy_turn(self, f):
        r, rng = self.r, self.rng
        self.enemy_acts += 1
        for st in f.card['steps']:
            if not self.live() or self.failed(): break
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
                        t = self.target(f, st['tgt'])
                    if t is None or not self.live(): break
                    if f.node == t.node: break
                    origin = f.node; f.node = step_to(f.node, t.node, rng)
                    if st.get('push'):
                        for c in self.live():
                            if c.node != f.node: continue
                            if 'dmg' in st and (c not in struck or not r.push_once):
                                struck.add(c)
                                self.defend(f, c, st['dmg'] + f.atk_bonus - (1 if f.stagger else 0), st['magic'], st['dodge'],
                                            push=True, parryable=False)
                            if c.alive and c.node == f.node:
                                far = [x for x in NBR[c.node] if DIST[x][origin] > DIST[c.node][origin]]
                                c.node = rng.choice(far or NBR[c.node])
            else:
                for _ in range(st.get('repeat', 1) * r.reps(self.n)):
                    t = self.target(f, st['tgt'])
                    if t is None or DIST[f.node][t.node] > st['range']: break
                    node = t.node
                    for c in ([x for x in self.live() if x.node == node] if st.get('node') else [t]):
                        self.defend(f, c, st['dmg'] + f.atk_bonus - (1 if f.stagger else 0), st['magic'], st['dodge'],
                                    push=st.get('push', False), parryable=not st.get('node'))
        f.stagger = f.frost = False

    def boss_turn(self, f):
        r, rng = self.r, self.rng
        self.enemy_acts += 1
        if not f.deck:
            f.deck = f.discard; f.discard = []
            if r.boss_reshuffle: rng.shuffle(f.deck)
        card = f.deck.pop(0); f.discard.append(card)
        known = card['name'] in f.seen; f.seen.add(card['name'])
        f.weak = rng.random() < (self.WEAK_KNOWN if known else self.WEAK)
        for _ in range(card['repeat']):
            for a in card['attacks']:
                live = self.live()
                if not live or self.failed(): break
                t = self.aggro if (self.aggro.alive and rng.random() < 0.5) else self.target(f, 'nearest')
                for _s in range(2):                                 # bosses close on their target before striking
                    f.node = step_to(f.node, t.node, rng)
                victims = [t] + [c for c in live if c is not t and DIST[f.node][c.node] <= 1 and rng.random() < self.ARC]
                for c in victims:
                    if rng.random() < (self.pol.read_known if known else self.pol.read_new): continue    # out of the arc or the reach
                    self.defend(f, c, a['dmg'] - (1 if f.stagger else 0), a['magic'], card['dodge'], push=a['push'],
                                effects=a['effects'], parryable=False)
        f.stagger = f.frost = False

    def check_heat(self, f):
        if f.boss and not f.heated and 0 < f.hp <= f.card['heatup']:
            f.heated = True
            f.deck = f.deck + f.discard + [self.rng.choice(f.heat_cards)]; f.discard = []; self.rng.shuffle(f.deck)
            f.seen = set()                              # the order is new: the pattern has to be learned again

    # -------------------------------------------------------------- character turn
    def incoming(self, c, slack=1):
        """Room this character should keep on the bar for the damage due before its next turn: the mean plus 1.3
        standard deviations of that damage, from the attacks that can reach it and the chance each is aimed at it."""
        r = self.r; n = max(1, len(self.live())); mean = var = 0.0
        phases = n if (r.round == 'alternate' or self.is_boss) else 1       # enemy phases before this character acts again

        def add(share, dmg, magic, times=1):
            nonlocal mean, var
            share = min(1.0, share)
            if share <= 0 or dmg <= 0: return
            st = hit_stats(c.res if magic else c.blk, r.block, dmg, c.res_pen if magic else c.blk_pen)
            e1 = sum(d * p for d, p in st); e2 = sum(d * d * p for d, p in st)
            mean += times * share * e1; var += times * (share * e2 - (share * e1) ** 2)
        for f in self.foes_alive():
            if f.boss:
                cards = f.deck + f.discard
                p_me = (0.5 if self.aggro is c else 0.0) + 0.5 / n
                p_me = (p_me + self.ARC * (1 - p_me)) * (1 - self.pol.read_new)
                for k in cards:
                    for a in k['attacks']: add(p_me, a['dmg'], a['magic'], phases * k['repeat'] / len(cards))
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
        """Character c makes attack option o (already paid for) against foe f; a node attack hits every foe there."""
        rng = self.rng; r = self.r; grand = 0
        targets = [x for x in self.foes_alive() if x.node == f.node] if o.get('node') else [f]
        dice = o['dice'] + ('b' if (f.boss and f.weak and o['range'] <= 1) else '')
        rolls = []
        for _ in range(o['repeat']):
            faces = roll(dice, rng)
            if o.get('reroll') and faces:                            # two-handed grip: one die may be rolled again
                i = min(range(len(faces)), key=lambda j: faces[j] - sum(DIE[dice[j]]) / 6)
                if faces[i] < sum(DIE[dice[i]]) / 6: faces[i] = rng.choice(DIE[dice[i]])
            rolls.append(sum(faces) + o['mod'] - (1 if (c.stagger and r.stagger == 'author') else 0))
        for t in targets:
            total = sum(max(0, v - (0 if o.get('ignore') else t.resist if o['magic'] else t.armor)) for v in rolls)
            if total > 0:
                if t.bleed and r.bleed == 'official': total += 2; t.bleed = False
                t.hp -= total; self.dealt[c] = self.dealt.get(c, 0) + total; grand += total
                if r.aggro == 'last': self.aggro = c
                self.check_heat(t)
            self.say('   ', c.name, 'hits', t.name, 'with', o['name'], 'for', total, '(hp', max(0, t.hp), ')')
        return grand

    def reposition(self, c, budget, walk_free):
        """After acting, step out of the enemies' reach if that saves more damage than it costs in stamina."""
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
            cost = steps - (1 if walk_free else 0)
            if cost > budget: continue
            c.node = node
            gap = max(0, min(DIST[node][f.node] for f in self.foes_alive()) - reach - 1)       # running needed to return
            val = 0.8 * (base - self.incoming(c, 0)) - self.pol.w_sta * (cost + 0.6 * gap) - 0.3 * sum(1 for i in range(cost) if budget - i <= 3)
            if val > best[0]: best = (val, node, cost)
        c.node = best[1]; c.sta += best[2]
        if best[2] or best[1] != here: self.say('   ', c.name, 'steps back to', NODES[c.node])

    def char_turn(self, c):
        r, pol, rng = self.r, self.pol, self.rng
        self.char_turns += 1
        if not (c.frost and r.frost == 'author'): c.sta = max(0, c.sta - r.regen)
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
            c.ember_card = False; c.ember = True; c.dmg = 0; c.hollow = False
            self.say('  ', c.name, 'uses an ember'); self.end_turn(c); return
        # the flask: drunk when death is near; where damage outlasts the encounter (the manuscript) also once badly hurt
        if c.estus and c.dmg >= 3 and (self.risk(free) > pol.estus_risk or (r.recover != 'all' and c.dmg >= pol.estus_at)):
            c.estus = False; c.dmg = 0
            self.say('  ', c.name, 'drinks')
            if r.estus == 'full': c.sta = 0; free = c.cap
            else: self.end_turn(c); return                           # a major action: the turn ends
        if c.heroic and c.name == 'Herald' and (sum(x.sta for x in self.live()) >= 2 * len(self.live())):
            c.heroic = False                                         # Perseverance: each character gains 2 stamina
            for x in self.live(): x.sta = max(0, x.sta - 2)
        attacked = False; moved = False
        used = set()
        wd = pol.w_death * (1.6 if (r.death == 'party' or c.hollow or len(self.live()) == 1) else 1.0)
        for attempt in (0, 1):
            foes = self.foes_alive()
            if not foes: break
            free = c.cap - c.dmg - c.sta
            self.incoming(c); risk0 = self.risk(free)
            best = None
            for f in foes:
                d = DIST[c.node][f.node]
                for hand in ('R', 'L'):
                    if hand in used: continue
                    for o in c.options[hand]:
                        rg = o['range']
                        steps = max(0, d - rg) if attempt == 0 else (0 if d <= rg else 99)
                        if o['shaft'] and d - steps == 0:
                            if attempt: continue
                            steps = 1
                        if steps == 99: continue
                        surge = c.heroic and c.name == 'Warrior' and rg == 0 and o['cost'] >= 2      # free step, free node attack
                        if surge: o = dict(o, cost=0, node=True); steps = max(0, steps - 1)
                        run = max(0, steps - 1) + (steps if (c.frost and r.frost == 'official') else 0)
                        cost = o['cost'] + run + (1 if (c.stagger and r.stagger == 'official') else 0) \
                            + (1 if (f.boss and f.heated and f.name == 'Gargoyle' and d - steps == 0) else 0)
                        room = free - (1 if r.lethal == 'full' else 0)
                        if cost > room: continue
                        pm = attack_pmf(o['dice'], o['mod'] + c.scale_bonus(o), f.resist if o['magic'] else f.armor, o['repeat'])
                        ed = sum(min(x, f.hp) * p for x, p in pm); pk = sum(p for x, p in pm if x >= f.hp)
                        last = len(foes) == 1; vk = self.kill_value(f, last)
                        if o.get('node') and not f.boss:
                            for g in foes:
                                if g is not f and g.node == f.node:
                                    pg = attack_pmf(o['dice'], o['mod'], g.resist if o['magic'] else g.armor, o['repeat'])
                                    vg = self.kill_value(g, False)
                                    ed += (sum(min(x, g.hp) * p for x, p in pg) / g.max * 0.5 * vg + sum(p for x, p in pg if x >= g.hp) * vg) / (0.5 * vk / f.max)
                        # the price of stamina: the added chance of dying before the next turn
                        danger = (self.risk(free - cost) - risk0) * (1 - pk if last else 1.0)
                        score = (ed if f.boss else ed / f.max * 0.5 * vk) + pk * vk - pol.w_sta * cost - wd * danger
                        if best is None or score > best[0]: best = (score, f, hand, o, steps, cost, run, surge)
            if best is None or best[0] <= 0: break
            _, f, hand, o, steps, cost, run, surge = best
            if surge: c.heroic = False
            if steps: moved = True
            for _ in range(steps):
                c.node = step_to(c.node, f.node, rng) if not (o['shaft'] and DIST[c.node][f.node] == 1) else c.node
            if o['shaft'] and c.node == f.node: c.node = rng.choice(NBR[c.node])
            if run: c.ran = True
            c.sta += cost; used.add(hand); attacked = True
            self.strike(c, f, o)
            if c.two_handed or not c.options['L' if hand == 'R' else 'R']: break
        if not attacked:
            foes = self.foes_alive()
            if foes and r.turn == 'major' and c.sta > 0:
                c.sta = 0; self.say('  ', c.name, 'rests')            # the Rest action
            elif foes:
                f = min(foes, key=lambda f: DIST[c.node][f.node])
                if DIST[c.node][f.node] > 1: c.node = step_to(c.node, f.node, rng); moved = True
        # hit and run: official rules allow movement before or after attacking, not both; the manuscript has no such limit
        if pol.kite and self.foes_alive() and not self.is_boss and (r.turn != 'official' or not moved):
            free = c.cap - c.dmg - c.sta
            self.reposition(c, min(2, free - 1 - int(pol.caution * 0.5 * self.incoming(c))), walk_free=not moved)
        self.end_turn(c)

    def end_turn(self, c):
        r = self.r
        if c.poison and c.alive:
            self.wound(c, c.poison if r.poison == 'stack' else 1); c.poison = max(0, c.poison - 1) if r.poison == 'stack' else 0
        c.stagger = False; c.frost = False

    # -------------------------------------------------------------- the fight
    def order(self):
        live = self.live()
        if self.r.order == 'free':                     # the party chooses: the sturdiest acts last and keeps the enemies' eyes
            return sorted(live, key=lambda c: (c.mean_blk + c.dodge * 0.5, c.cap - c.dmg))
        return sorted(live, key=lambda c: -c.taunt)

    def run(self, max_rounds=60):
        r = self.r
        for c in self.party: c.was_hollow = c.hollow
        if self.is_boss or r.round == 'alternate':
            while not self.over() and self.rounds < max_rounds:
                self.rounds += 1
                for _ in range(self.seats):
                    if self.over(): break
                    for f in sorted(self.foes_alive(), key=lambda f: -f.threat):
                        if self.over(): break
                        (self.boss_turn if f.boss else self.enemy_turn)(f)
                    if self.over(): break
                    for _k in range(self.seats):             # the next living character in seat order
                        c = self.party[self.turn_i % self.seats]; self.turn_i += 1
                        if c.alive: break
                    if c.alive: self.char_turn(c)
        else:
            while not self.over() and self.rounds < max_rounds:
                self.rounds += 1; self.dealt = {}
                for f in sorted(self.foes_alive(), key=lambda f: (-f.threat, min(DIST[f.node][c.node] for c in self.live()))):
                    if self.over(): break
                    self.enemy_turn(f)
                if self.over(): break
                for c in self.order():
                    if self.over(): break
                    if c.alive: self.char_turn(c)
                if r.aggro == 'most' and self.dealt:
                    top = max(self.dealt.values()); lead = [c for c, v in self.dealt.items() if v == top and c.alive]
                    if len(lead) == 1: self.aggro = lead[0]
        for c in self.party: c._first = self.turn_i
        return (not self.failed()) and not self.foes_alive()
