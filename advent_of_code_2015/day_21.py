import re
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Equipment:
    price: int
    damage: int
    defense: int


class Factory:
    @staticmethod
    def create_equipment(equipments_offer: list) -> list:
        equipments = []
        for equipment in equipments_offer:
            _, price, damage, defense = equipment.split()
            equipments.append(Equipment(price=int(price), damage=int(damage), defense=int(defense)))
        return equipments

    @classmethod
    def create_equipment_sets(cls):
        equipments_sets = []
        with open('day_21_item_shop.txt') as f:
            file = [line.strip() for line in f.read().split('-')]
            weapons = cls.create_equipment(file[0].split('\n')[1:])
            armors = cls.create_equipment(file[1].split('\n')[1:])
            rings = cls.create_equipment(file[2].split('\n')[1:])

        for weapon in weapons:
            for armor in [None, *armors]:
                # no ring
                equipments_sets.append([weapon, armor])
                # one ring
                for ring in rings:
                    equipments_sets.append([weapon, armor, ring])
                # 2 rings
                ring_tuples = list(combinations(rings, 2))
                for ring_tuple in ring_tuples:
                    equipments_sets.append([weapon, armor, ring_tuple[0], ring_tuple[1]])
        return equipments_sets


class Warrior:
    def __init__(self, health: int, equipments: list):
        self.health = health
        self.default_health = health
        self.equipments = filter(None, equipments)

        stats = [0, 0, 0]
        for item in self.equipments:
            stats[0] += item.damage
            stats[1] += item.defense
            stats[2] += item.price
        self.damage, self.defense, self.equipment_cost = stats

    def count_dealt_damage(self, opponent):
        if self.damage < opponent.defense:
            return 1
        else:
            return self.damage - opponent.defense

    def __repr__(self):
        return f'Health: {self.health}, damage: {self.damage}, defense: {self.defense}'


class Arena:
    enemy: Warrior

    def __init__(self):
        self.create_enemy()

    def find_cheapest_win_and_expensive_loss(self):
        equipment_sets = Factory.create_equipment_sets()
        win_sets = []
        lost_sets = []

        for equipment_set in equipment_sets:
            warrior = Warrior(health=100, equipments=equipment_set)
            if self.would_win_fight(warrior):
                win_sets.append(warrior.equipment_cost)
            else:
                lost_sets.append(warrior.equipment_cost)
            self.reset_enemy_health()

        return min(win_sets), max(lost_sets)

    def would_win_fight(self, warrior) -> bool:
        while True:

            damage = warrior.count_dealt_damage(self.enemy)
            self.enemy.health -= damage
            if self.enemy.health <= 0:
                return True

            damage = self.enemy.count_dealt_damage(warrior)
            warrior.health -= damage
            if warrior.health <= 0:
                return False

    def create_enemy(self):
        with open('day_21.txt') as file:
            health, damage, defense = re.findall('[0-9]+', file.read())
            self.enemy = Warrior(
                health=int(health), equipments=[Equipment(price=0, damage=int(damage), defense=int(defense))]
            )

    def reset_enemy_health(self):
        self.enemy.health = self.enemy.default_health


arena = Arena()
part_1, part_2 = arena.find_cheapest_win_and_expensive_loss()
print(f'Result of part 1: "{part_1}"')
print(f'Result of part 2: "{part_2}"')
