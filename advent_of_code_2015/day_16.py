from dataclasses import dataclass


@dataclass(slots=True)
class Sue:
    number: int
    children: int | None = None
    cats: int | None = None
    samoyeds: int | None = None
    pomeranians: int | None = None
    akitas: int | None = None
    vizslas: int | None = None
    goldfish: int | None = None
    trees: int | None = None
    cars: int | None = None
    perfumes: int | None = None


class Finder:
    def __init__(self):
        self.instructions = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1,
        }
        self.aunties = []

    def process_input(self):
        with open('day_16.txt') as f:
            for line in f:
                words = [word.rstrip(':,.\n') for word in line.split()]
                number = int(words[1])
                sue = Sue(number)
                attributes = {words[2]: words[3], words[4]: words[5], words[6]: words[7]}
                for attribute, value in attributes.items():
                    sue.__setattr__(attribute, int(value))
                self.aunties.append(sue)

    def find_sue(self, part1=True):
        for sue in self.aunties:
            match = 0
            for attribute, value in self.instructions.items():
                sue_value = sue.__getattribute__(attribute)
                if part1:
                    if sue_value == value or sue_value is None:
                        match += 1
                else:
                    if (
                        sue_value is None
                        or (attribute in ('cats', 'trees') and sue_value > value)
                        or (attribute in ('pomeranians', 'goldfish') and sue_value < value)
                        or sue_value == value
                    ):
                        match += 1
                if match == 10:
                    return sue.number


# Results:

# part 1
finder = Finder()
finder.process_input()
result1 = finder.find_sue()
print(f'Result of part 1: "{result1}"')

# part 2
result2 = finder.find_sue(part1=False)
print(f'Result of part 2: "{result2}"')
