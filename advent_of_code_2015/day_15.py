import itertools
from dataclasses import dataclass
import numpy as np


@dataclass(slots=False)
class Ingredient:
    name: str
    default_capacity: int
    default_durability: int
    default_flavor: int
    default_texture: int
    default_calories: int
    ratio: int = 1

    @property
    def capacity(self):
        return self.default_capacity * self.ratio

    @property
    def durability(self):
        return self.default_durability * self.ratio

    @property
    def flavor(self):
        return self.default_flavor * self.ratio

    @property
    def texture(self):
        return self.default_texture * self.ratio

    @property
    def calories(self):
        return self.default_calories * self.ratio


class Calculator:
    def __init__(self):
        self.ingredients = []
        self.combinations = []
        self.process_input()
        self.find_all_possible_combinations()

    def process_input(self):
        with open('day_15.txt') as f:
            for line in f:
                words = line.rstrip().rstrip('.').split()[::2]
                name = words[0].rstrip(':').lower()
                capacity, durability, flavor, texture, calories = [int(value.rstrip(',')) for value in words[1:]]
                self.ingredients.append(Ingredient(name, capacity, durability, flavor, texture, calories))

    def find_all_possible_combinations(self):
        """Find all valid combinations - sum of numbers equals to 100."""
        valid_combinations = []
        for a in range(1, 98):
            for b in range(1, 98):
                for c in range(1, 98):
                    for d in range(1, 98):
                        new_combination = [a, b, c, d]
                        if sum(new_combination) == 100:
                            new_combination.sort()
                            valid_combinations.append(new_combination)
        # filter repeated combinations
        self.combinations = set(tuple(sorted(combination)) for combination in valid_combinations)

    def find_best_ratio(self, condition=False):
        """Find a recipe with the highest score. Optionally with calories condition."""
        winning_score = 0
        for combination in self.combinations:
            permutations = list(itertools.permutations(combination))

            for permutation in permutations:
                self.ingredients[0].ratio = permutation[0]
                self.ingredients[1].ratio = permutation[1]
                self.ingredients[2].ratio = permutation[2]
                self.ingredients[3].ratio = permutation[3]
                if condition:
                    permutation_score = self.calculate_score(calories=True)
                else:
                    permutation_score = self.calculate_score()
                if permutation_score > winning_score:
                    winning_score = permutation_score
        return winning_score

    def calculate_score(self, calories=False):
        """
        Calculate score for recipe.
        Optionally check condition which demands 500 calories exactly.
        """
        attributes = ['capacity', 'durability', 'flavor', 'texture']
        if calories:
            attributes.append('calories')
        score = np.array([0] * len(attributes))
        for i, attribute in enumerate(attributes):
            for ingredient in self.ingredients:
                value = ingredient.__getattribute__(attribute)
                score[i] += value
        if calories and score[-1] != 500:
            return 0
        return score[0] * score[1] * score[2] * score[3] if len(score[score >= 0]) == len(attributes) else 0


# Results
calculator = Calculator()
result1 = calculator.find_best_ratio()
print(f'Result of part 1: "{result1}"')
result2 = calculator.find_best_ratio(condition=True)
print(f'Result of part 2: "{result2}"')
