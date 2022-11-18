import re
from copy import deepcopy
from dataclasses import dataclass, field
from math import inf


class GameOver(Exception):
    """Bos won."""

    pass


class WizardWon(Exception):
    """Wizard won."""

    pass


@dataclass
class Spell:
    id: int
    mana_cost: int
    self_target: bool = False
    turns: int | float = 0
    damage: int = 0
    health: int = 0
    armor: int = 0
    mana: int = 0


@dataclass
class Hero:
    health: int
    mana: int = 0
    effects: list = field(default_factory=list)
    mana_spent: int = 0
    damage: int = 0
    cast_spells: list = field(default_factory=list)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name == 'health' and value <= 0:
            if self.damage:
                raise WizardWon
            else:
                raise GameOver

    def allowed_spells(self, boss) -> list | GameOver:
        """
        Return spells which can be cast - hero has enough mana.
        """
        spells = [
            Spell(id=0, mana_cost=53, damage=4),
            Spell(id=1, mana_cost=73, damage=2, health=2),
            Spell(id=2, self_target=True, mana_cost=113, armor=7, turns=5),
            Spell(id=3, mana_cost=173, damage=3, turns=5),
            Spell(id=4, self_target=True, mana_cost=229, mana=101, turns=4),
        ]
        next_mana_turn = sum([spell.mana for spell in self.effects]) + self.mana

        if next_mana_turn >= 229:
            spells = spells
        elif next_mana_turn >= 173:
            spells = spells[:4]
        elif next_mana_turn >= 113:
            spells = spells[:3]
        elif next_mana_turn >= 73:
            spells = spells[:2]
        elif next_mana_turn >= 53:
            spells = [spells[0]]
        else:
            raise GameOver

        effects_on_boss = [spell.id for spell in boss.effects if spell.turns != 0]
        effect_on_wizard = [spell.id for spell in self.effects if spell.turns != 0]
        effects_in_use = effects_on_boss + effect_on_wizard
        return [spell for spell in spells if spell.id not in effects_in_use][::-1]

    @property
    def armor(self):
        """If spell `shield` is in effect, armor is set to its armor value."""
        for spell in self.effects:
            if spell.armor:
                return spell.armor
        return 0

    def cast_spell(self, spell):
        self.cast_spells.append(spell.id)
        self.mana -= spell.mana_cost
        if self.mana < 0:
            raise GameOver
        self.mana_spent += spell.mana_cost

        if spell.self_target:
            self.effects.append(spell)
        else:
            self.health += spell.health
            return spell

    def apply_effects(self, on_move='boss'):
        """Apply effects on oneself, deduct turns. If effect worns out, remove it."""
        new_effects = []
        for spell in self.effects:
            if spell.damage:
                if spell.id == 5:
                    if on_move == 'wizard':
                        self.health -= spell.damage
                else:
                    self.health -= spell.damage
            if spell.mana:
                self.mana += spell.mana
            if spell.turns != 0:
                if spell.turns != inf:
                    spell.turns -= 1
                new_effects.append(spell)
        self.effects = new_effects

    def sustain_damage(self, damage):
        """Deduct damage (reduced by armor value). But at least 1 health must be deducted."""
        if (damage - self.armor) <= 0:
            self.health -= 1
        else:
            self.health -= damage - self.armor


class Arena:
    @staticmethod
    def create_fighters(hardmode=False) -> tuple[Hero, Hero]:
        wizard = Hero(health=50, mana=500)
        if hardmode:
            wizard.effects.append(Spell(id=5, turns=inf, damage=1, self_target=True, mana_cost=0))
        with open('day_22.txt') as file:
            health, damage = re.findall('[0-9]+', file.read())
            boss = Hero(health=int(health), damage=int(damage))
        return wizard, boss

    @staticmethod
    def fight(spell, wizard, boss) -> tuple:
        try:
            # wizard turn
            wizard.apply_effects(on_move='wizard')
            boss.apply_effects()
            effect = wizard.cast_spell(spell)
            if effect:
                if effect.turns == 0:
                    boss.health -= effect.damage
                else:
                    boss.effects.append(effect)
            # boss turn
            wizard.apply_effects()
            boss.apply_effects()
            wizard.sustain_damage(boss.damage)
            return wizard, boss, None
        except WizardWon:
            return wizard, boss, True
        except GameOver:
            return wizard, boss, False


class Simulator:
    least_win_mana = inf
    tried = []

    def round(self, state):
        wizard, boss = state
        try:
            possible_spells = wizard.allowed_spells(boss)
        except GameOver:
            return False

        for spell in possible_spells:
            if wizard.mana_spent + spell.mana_cost < self.least_win_mana:
                new_wizard, new_boss, win = Arena.fight(spell, deepcopy(wizard), deepcopy(boss))
                if win:
                    self.least_win_mana = new_wizard.mana_spent
                elif win is None and new_wizard.mana_spent < self.least_win_mana:
                    self.round((new_wizard, new_boss))


simulator1, simulator2 = Simulator(), Simulator()
simulator1.round(Arena.create_fighters())
simulator2.round(Arena.create_fighters(hardmode=True))
print(f'Result of part 1: "{simulator1.least_win_mana}"')
print(f'Result of part 2: "{simulator2.least_win_mana}"')
