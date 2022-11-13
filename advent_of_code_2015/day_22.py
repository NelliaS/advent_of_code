import math
import re
import threading
import time
from copy import deepcopy
from dataclasses import dataclass, field
from itertools import combinations_with_replacement, permutations
from math import inf
from random import choice

from icecream import ic


class GameOver(Exception):
    """Someone health's is 0 or less."""

    ...


class ManaRunOut(Exception):
    """Cannot cast spell"""

    ...


class TooMuchManaSpent(Exception):
    """Too much mana have been spent, there have been better tries."""

    ...


@dataclass
class Spell:
    id: int
    name: str
    mana_cost: int
    target: str
    turns: int = 0
    damage: int = 0
    health: int = 0
    armor: int = 0
    mana: int = 0


@dataclass
class Hero:
    health: int
    mana: int = 0
    effects: list = field(default_factory=list)
    damage: int = 0
    mana_spent: int = 0
    minimum_mana: int = math.inf

    def __post_init__(self):
        self.spells = [
            self.create_spell(0),
            self.create_spell(1),
            self.create_spell(2),
            self.create_spell(3),
            self.create_spell(4),
        ]
        self.default_stats = [self.health, self.mana, self.damage]

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name == 'health' and value <= 0:
            raise GameOver

        if name == 'mana_spent' and value > self.minimum_mana:
            raise TooMuchManaSpent

    def reset_stats(self):
        """Reset object to initial state."""
        self.health, self.mana, self.damage = self.default_stats
        self.mana_spent = 0
        self.effects = []

    def can_use_spells(self):
        """
        Return spells which can be cast - hero has enough mana.
        """
        if self.mana >= 229:
            return [0, 1, 2, 3, 4]
        elif self.mana >= 173:
            return [0, 1, 2, 3]
        elif self.mana >= 113:
            return [0, 1, 2]
        elif self.mana >= 73:
            return [0, 1]
        elif self.mana >= 53:
            return [0]
        else:
            raise ManaRunOut

    @property
    def armor(self):
        """If spell `shield` is in effect, armor is set to its armor value."""
        for spell in self.effects:
            if spell.armor:
                return spell.armor
        return 0

    def create_spell(self, spell_id):
        """Create fresh new spell."""
        if spell_id == 0:
            return Spell(id=0, name='magic_missile', target='opponent', mana_cost=53, damage=4)
        elif spell_id == 1:
            return Spell(id=1, name='drain', target='both', mana_cost=73, damage=2, health=2)
        elif spell_id == 2:
            return Spell(id=2, name='shield', target='oneself', mana_cost=113, armor=7, turns=5)
        elif spell_id == 3:
            return Spell(id=3, name='poison', target='opponent', mana_cost=173, damage=3, turns=5)
        elif spell_id == 4:
            return Spell(id=4, name='recharge', target='oneself', mana_cost=229, mana=101, turns=4)

    def cast_spell(self, spell_id):
        """
        Create fresh new spell. Don't forget to deduct mana and count total spent mana.
        Apply effect to oneself / or return spell to be applied on enemy.
        """
        spell = self.create_spell(spell_id)
        self.mana -= spell.mana_cost
        if self.mana < 0:
            raise ManaRunOut
        self.mana_spent += spell.mana_cost

        if spell.target == 'oneself':
            self.effects.append(spell)
        else:
            self.health += spell.health
            return spell

    def apply_effects(self):
        """Apply effects on oneself, deduct turns. If effect worns out, remove it."""
        new_effects = []
        for spell in self.effects:
            self.health -= spell.damage
            if spell.mana:
                self.mana += spell.mana
            if spell.turns != 0:
                spell.turns -= 1
                new_effects.append(spell)
        self.effects = new_effects

    @property
    def effect_ids(self):
        ids = []
        for effect in self.effects:
            ids.append(effect.id)
        return ids

    def sustain_damage(self, damage):
        """Deduct damage (reduced by armor value). But at least 1 health must be deducted."""
        if (damage - self.armor) <= 0:
            self.health -= 1
        else:
            self.health -= damage - self.armor


class Arena:
    def __init__(self, test_data=None):
        self.wizard, self.boss = self.create_fighters(test_data)
        self.hardmode = False

    def apply_effects(self):
        """Apply effects on wizard and boss and check possible game over."""
        self.boss.apply_effects()
        self.wizard.apply_effects()

    def fight(self, instructions):
        for spell_id in instructions:
            # wizard turn
            if self.hardmode:
                self.lose_one_health()
            self.apply_effects()
            effect = self.wizard.cast_spell(spell_id)
            if effect:
                if effect.turns == 0:
                    self.boss.health -= effect.damage
                else:
                    self.boss.effects.append(effect)
            # boss turn
            if self.hardmode:
                self.lose_one_health()
            self.apply_effects()
            self.wizard.sustain_damage(self.boss.damage)

    def evaluate_winner(self):
        if self.boss.health <= 0:
            return self.wizard
        elif self.wizard.health <= 0:
            return self.boss

    @staticmethod
    def create_fighters(test_data):
        if test_data:
            wizard = test_data[0]
            boss = test_data[1]
        else:
            wizard = Hero(health=50, mana=500)
            with open('day_22.txt') as file:
                health, damage = re.findall('[0-9]+', file.read())
                boss = Hero(health=int(health), damage=int(damage))
        return wizard, boss

    def lose_one_health(self):
        self.wizard.health -= 1

    def find_least_mana_win(self, tries, hard=False):
        self.hardmode = hard
        mana_spent = inf
        for one_fight in range(tries):
            result = self.fight_until_win()
            self.boss.reset_stats()
            self.wizard.reset_stats()
            if result != 0 and result < mana_spent:
                mana_spent = result
                self.wizard.minimum_mana = mana_spent
            # if mana_spent < 1300:
            #     ic(mana_spent)
        return mana_spent

    def fight_until_win(self):
        winner = None
        while not winner:
            try:
                effect_on_boss = self.boss.effect_ids
                spells = self.wizard.can_use_spells()
                for spell_id in effect_on_boss:
                    if spell_id in spells:
                        spells.remove(spell_id)
                self.fight((choice(spells),))
            except ManaRunOut:
                return 0
            except TooMuchManaSpent:
                return 0
            except GameOver:
                winner = self.evaluate_winner()
                return winner.mana_spent

runner = Runner()
state = State(..)
print(runner.round(state))

class Runner:
    dead = []
    won = {}

    def round(self, state):
        if state in self.dead:
            return False
        if state in self.won:
            return self.won

        mana_res = []
        for spell in self.get_spells(state):
            new_state = state.update_state(spell)
            if new_state.health <= 0 or new_state.mana <= 0:
                pass
            elif new_state.boss_health <= 0:
                mana_res.append(spell.mana_cost)
            else:
                res = self.round(new_state)
                if res:
                    mana_res.append(res + spell.mana_cost)

        if mana_res:
            self.won[state] = min(mana_res)
            return mana_res

        self.dead.append(state)
        return False

@dataclass(frozen=True, eq=True)    # bude mít hash
class State:
    mana: int
    health: int
    armor: int
    effects: Effects
    boss_health: int

    def update_state(self, spell):
        state = deepcopy(self)  # ne kopie, ale nový objekt a effect
        state.mana -= spell.mana_cost
        ...
        return state



def paralelize():
    arena = Arena()
    arena.find_least_mana_win(100000, hard=True)


start = time.time()
arena = Arena()
# print(f'Result of part 1: "{arena.find_least_mana_win(100000)}"')


def part_2():
    for i in range(10):
        thread = threading.Thread(target=paralelize)
        thread.start()


ic(time.time() - start)
# mine minimum 1295, true answer 1289
