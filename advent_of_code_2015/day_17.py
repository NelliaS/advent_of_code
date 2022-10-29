import itertools


class Calculator:
    def __init__(self):
        self.containers = []
        self.combinations = []
        self.minimal_combinations = []
        self.process_input()
        self.calculate()

    @property
    def valid_combinations(self):
        return len(self.combinations)

    @property
    def minimalistic_combinations(self):
        return len(self.minimal_combinations)

    def process_input(self):
        with open('day_17.txt') as f:
            for line in f:
                self.containers.append(int(line.rstrip()))

    def calculate(self):
        mimimal_len = None
        for i in range(1, len(self.containers)):
            all_combinations = list(itertools.combinations(self.containers, i))
            for combination in all_combinations:
                if sum(combination) == 150:
                    self.combinations.append(combination)
                    if mimimal_len is None:
                        mimimal_len = i
                    if mimimal_len == i:
                        self.minimal_combinations.append(combination)


calculator = Calculator()
print(f'Result of part 1: "{calculator.valid_combinations}"')
print(f'Result of part 2: "{calculator.minimalistic_combinations}"')
