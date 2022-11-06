import re
from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Equipment:
    type: str
    name: str
    price: int
    damage: int
    defense: int


@dataclass
class EquipmentSet:
    weapon: Equipment
    armor: Equipment | None = None
    ring_left: Equipment | None = None
    ring_right: Equipment | None = None

    def __post_init__(self):
        self.items = []
        for item in self.weapon, self.armor, self.ring_left, self.ring_right:
            if item:
                self.items.append(item)


class Factory:
    def __init__(self):
        self.equipments_sets = []
        self.process_input()

    def create_equipment(self, equipments_offer: list, kind: str) -> list:
        equipments = []
        for equipment in equipments_offer:
            name, price, damage, defense = equipment.split()
            equipments.append(
                Equipment(type=kind, name=name, price=int(price), damage=int(damage), defense=int(defense))
            )
        return equipments

    def process_input(self):
        with open('day_21_item_shop.txt') as f:
            file = [line.strip() for line in f.read().split('-')]
            weapons = self.create_equipment(file[0].split('\n')[1:], 'weapon')
            armors = self.create_equipment(file[1].split('\n')[1:], 'armor')
            rings = self.create_equipment(file[2].split('\n')[1:], 'ring')

        for weapon in weapons:
            for armor in [None, *armors]:
                # no ring
                self.equipments_sets.append(EquipmentSet(weapon=weapon, armor=armor))
                # one ring
                for ring in rings:
                    self.equipments_sets.append(EquipmentSet(weapon=weapon, armor=armor, ring_left=ring))
                # 2 rings
                ring_tuples = list(combinations(rings, 2))
                for ring_tuple in ring_tuples:
                    self.equipments_sets.append(
                        EquipmentSet(weapon=weapon, armor=armor, ring_left=ring_tuple[0], ring_right=ring_tuple[1])
                    )


class Warrior:
    def __init__(self, name: str, health: int, equipment_set: EquipmentSet = None):
        self.name = name
        self.health = health
        self.default_health = health
        self.equipment_set = equipment_set
        if equipment_set:
            self.give_stats()

    def give_stats(self):
        stats = [0, 0, 0]
        for item in self.equipment_set.items:
            for i, attribute in enumerate(['damage', 'defense', 'price']):
                stats[i] += getattr(item, attribute)
        self.damage, self.defense, self.equipment_cost = stats

    def attack(self, opponent):
        if self.damage < opponent.defense:
            opponent.health -= 1
        else:
            opponent.health -= self.damage - opponent.defense
        if opponent.health <= 0:
            raise ValueError(self.name)
        return opponent

    def __repr__(self):
        return f'{self.name} - health: {self.health}, damage: {self.damage}, defense: {self.defense}'


class Arena:
    def __init__(self):
        factory = Factory()
        self.equipment_sets = factory.equipments_sets
        with open('day_21.txt') as file:
            health, damage, defense = re.findall('[0-9]+', file.read())
            self.enemy = Warrior(
                name='Sauron',
                health=int(health),
                equipment_set=EquipmentSet(
                    Equipment(type='ring', name='the_one', price=0, damage=int(damage), defense=int(defense))
                ),
            )

    def find_cheapest_win_and_expensive_loose(self, special_rule=False):
        winner_sets = []
        lose_sets = []
        warrior = Warrior(name='Nellia', health=100)
        for equipment_set in self.equipment_sets:
            warrior.equipment_set = equipment_set
            warrior.give_stats()
            winner = self.fight(warrior)
            if winner:
                winner_sets.append(warrior.equipment_cost)
            else:
                lose_sets.append(warrior.equipment_cost)
            self.enemy.health = self.enemy.default_health
            warrior.health = warrior.default_health
        winner_sets.sort()
        lose_sets.sort()
        return winner_sets[0], lose_sets[-1]

    def fight(self, warrior) -> bool:
        while True:
            try:
                self.enemy = warrior.attack(self.enemy)
                warrior = self.enemy.attack(warrior)
            except ValueError:
                return True if self.enemy.health <= 0 else False


arena = Arena()
cheapest_win, most_expensive_lose = arena.find_cheapest_win_and_expensive_loose()
print(f'Result of part 1: "{cheapest_win}"')
print(f'Result of part 2: "{most_expensive_lose}"')
