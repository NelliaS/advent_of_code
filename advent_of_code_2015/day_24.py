from itertools import combinations
from math import inf, prod


class Calculator:
    def __init__(self):
        with open('day_24.txt') as f:
            self.numbers = [int(number) for number in f.read().splitlines()]

    def calculate(self, group_size):
        sum_of_group = sum(self.numbers) // group_size
        group_1 = []
        r = 1
        while not group_1:
            group_1 = [c for c in combinations(self.numbers, r=r) if sum(c) == sum_of_group]
            r += 1

        smallest_product = inf
        for combination in group_1:
            result = prod(combination)
            if result < smallest_product:
                smallest_product = result

        return smallest_product


calculator = Calculator()
print(f'Result of part 1: "{calculator.calculate(3)}"')
print(f'Result of part 1: "{calculator.calculate(4)}"')
