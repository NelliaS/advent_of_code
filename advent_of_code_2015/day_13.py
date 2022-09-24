import itertools
from copy import copy


class Person:
    def __init__(self, name):
        self.name: str = name
        self.happiness: int = 0
        self.relationships: dict[Person, int] = {}

    def __repr__(self):
        return self.name

    def add_relationship(self, to_whom, unit_change):
        self.relationships[to_whom] = unit_change

    def sit_next_to(self, person):
        """
        Seat a person next to self and increase / decrease happiness accordingly.
        """
        value = self.relationships[person]
        self.happiness += value

    def reset_happiness(self):
        self.happiness = 0


class Arranger:
    def __init__(self):
        self.people: dict[str, Person] = {}

    def add_myself(self):
        nela = Person('Nela')
        for person in self.people.values():
            person.add_relationship(nela, 0)
            nela.add_relationship(person, 0)
        self.people['Nela'] = nela

    def create_new_person_if_nonexistent(self, name: str):
        if name not in self.people:
            self.people[name] = Person(name)

    def process_input(self):
        """
        Create a dictionary of people - Person() objects.
        And save their relationship preferences.
        """
        with open('day_13.txt') as f:
            for line in f:
                words = line.rstrip().rstrip('.').split()
                gain, name, to_whom = int(words[3]), words[0], words[-1]
                self.create_new_person_if_nonexistent(name)
                self.create_new_person_if_nonexistent(to_whom)
                if 'gain' in words:
                    self.people[name].add_relationship(self.people[to_whom], gain)
                elif 'lose' in words:
                    self.people[name].add_relationship(self.people[to_whom], -gain)

    def calculate_people_happiness(self):
        happiness = 0
        for person in self.people.values():
            happiness += person.happiness
        return happiness

    def reset_people_happiness(self):
        for person in self.people.values():
            person.reset_happiness()

    def sit_people_to_circle(self, ordered_people: tuple):
        """
        Seat people according to their order in a given tuple.
        Seating is to the circle, so the first and the last person are neighbours.
        Happiness values of seated people are changed according to their relationships.
        """
        for i, person in enumerate(ordered_people):
            if i == len(ordered_people) - 1:
                to1, to2 = i - 1, 0
            else:
                to1, to2 = i - 1, i + 1
            self.people[person.name].sit_next_to(ordered_people[to1])
            self.people[person.name].sit_next_to(ordered_people[to2])

    @property
    def highest_possible_happiness(self):
        highest_happiness = 0
        for ordered_people in itertools.permutations(self.people.values()):
            self.sit_people_to_circle(ordered_people)
            current_happiness = self.calculate_people_happiness()
            if current_happiness > highest_happiness:
                highest_happiness = current_happiness
            self.reset_people_happiness()
        return highest_happiness


# Results:

# part 1
arranger = Arranger()
arranger.process_input()
print(f'Result of part 1: "{arranger.highest_possible_happiness}"')

# part 2
arranger2 = copy(arranger)
arranger.add_myself()
print(f'Result of part 2: "{arranger.highest_possible_happiness}"')
