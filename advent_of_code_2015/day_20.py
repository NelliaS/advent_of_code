import math
from collections import defaultdict


class Calculator:
    def __init__(self, source):
        if type(source) == str:
            self.process_input(source)
        else:
            self.desired_presents = source
        self.elves_log = defaultdict(lambda: 0)

    def process_input(self, from_file):
        with open(from_file) as f:
            for line in f:
                self.desired_presents = int(line.rstrip())

    def find_divisors(self, current_house: int, special_rule=False):
        """Find divisors to a number and return them in list (including 1 and itself)."""
        house_divisors = []
        for number in range(1, int(math.sqrt(current_house) + 1)):
            if current_house % number == 0:
                result = int(current_house / number)
                set_elves = {number, result}
                if special_rule:
                    for elf in set_elves:
                        if self.elves_log[elf] < 50:
                            house_divisors.append(elf)
                            self.elves_log[elf] += 1
                else:
                    for elf in set_elves:
                        house_divisors.append(elf)
        return house_divisors

    def find_lowest_house(self, number_of_presents, special_rule=False):
        result_for_house = 0
        current_house = 0
        while result_for_house < self.desired_presents:
            current_house += 1
            result_for_house = sum([x * number_of_presents for x in self.find_divisors(current_house, special_rule)])
        return current_house


calculator = Calculator('day_20.txt')
print(f'Result of part 1: "{calculator.find_lowest_house(number_of_presents=10)}"')
print(f'Result of part 2: "{calculator.find_lowest_house(number_of_presents=11, special_rule=True)}"')
