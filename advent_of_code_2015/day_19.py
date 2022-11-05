import re
from collections import defaultdict
from random import choice


class Calculator:
    def __init__(self, source: str):
        self.translation_table = defaultdict(list)
        self.default_molecule = ''
        self.process_input(source)

    def process_input(self, from_file: str):
        with open(from_file) as f:
            for line in f:
                if '=>' in line:
                    translated_element, translation = line.rstrip().split('=>')
                    self.translation_table[translated_element.strip()].append(translation.strip())
                elif line != '\n':
                    self.default_molecule = line.strip()

    def find_occurences_in_molecule(self, element: str, molecule: str) -> list[tuple[int, int]]:
        """
        Find all occurences of a given element in a given molecule. Case sensitive.
        Eg. 'ab' in 'IOPabclaeERabcAB' -> [(3, 5), (11, 13)]
        """
        positions = []
        for match in re.finditer(element, molecule):
            index_start, index_end = match.span()
            positions.append((index_start, index_end))
        return positions

    def replace_elements(self, molecule: str, element: str, position: tuple) -> str:
        """
        Insert given element on specified position in a given molecule string.
        """
        return molecule[: position[0]] + element + molecule[position[1] :]

    def apply_calibration(self) -> int:
        """
        Count how many unique molecules can be made in 1 translation step.
        """
        new_molecules = []
        for key, values in self.translation_table.items():
            positions = self.find_occurences_in_molecule(key, self.default_molecule)
            for translation in values:
                for position in positions:
                    new_molecules.append(self.replace_elements(self.default_molecule, translation, position))
        return len(set(new_molecules))

    def has_any_match(self, molecule: str) -> bool:
        """
        Check that any replacement can be done according to translation_table.
        """
        for values in self.translation_table.values():
            for value in values:
                if value in molecule:
                    return True
        return False

    def apply_one_change(self, molecule: str) -> tuple[str, int]:
        """
        Randomly choose one translation on a molecule and proceed if possible.
        Return new (or old) molecule and number indicating change was made or not (1 / 0)
        """
        random_item = choice(list(self.translation_table.items()))
        key = random_item[0]
        value = choice(random_item[1])
        positions = self.find_occurences_in_molecule(value, molecule)
        if positions:
            return self.replace_elements(molecule, key, choice(positions)), 1
        else:
            return molecule, 0

    def decontruct_molecule(self):
        """
        Deconstruct molecule into target molecule with randomly applying translations.
        If no translation can be applied, start over.
        """
        steps = 0
        target_molecule = 'e'
        molecule = self.default_molecule
        while True:
            molecule, molecule_change = self.apply_one_change(molecule)
            steps += molecule_change
            if molecule == target_molecule:
                break
            if molecule_change:
                if not self.has_any_match(molecule):  # dead end, try again
                    molecule = self.default_molecule
                    steps = 0
        return steps


calculator = Calculator('day_19.txt')
print(f'Result of part 1: "{calculator.apply_calibration()}"')
print(f'Result of part 2: "{calculator.decontruct_molecule()}"')
