from collections import defaultdict
from copy import deepcopy
from itertools import product


class Calculator:
    grid: dict[tuple, int]

    @staticmethod
    def make_product(cube, dimensions):
        if dimensions == 3:
            x, y, z = cube
            return product(range(x - 1, x + 2), range(y - 1, y + 2), range(z - 1, z + 2))
        else:
            x, y, z, w = cube
            return product(range(x - 1, x + 2), range(y - 1, y + 2), range(z - 1, z + 2), range(w - 1, w + 2))

    def make_grid(self, dimensions):
        grid = defaultdict(lambda: 0)
        with open('day_17.txt') as f:
            for i_row, line in enumerate(f):
                for i_column, char in enumerate(line):
                    if dimensions == 3:
                        grid[(i_row, i_column, 0)] = 1 if char == '#' else 0
                    else:
                        grid[(i_row, i_column, 0, 0)] = 1 if char == '#' else 0
        self.grid = grid

    def expand_area(self, dimensions):
        """Will add new entries which are -1 to 1 from current considered ones."""
        for cube in list(self.grid.keys()):
            cube_product = (
                self.make_product(cube, dimensions=3) if dimensions == 3 else self.make_product(cube, dimensions=4)
            )
            for neighbour in cube_product:
                _ = self.grid[neighbour]

    def count_active_neighbours(self, cube, cube_product):
        total = 0
        for neighbour in cube_product:
            if neighbour in self.grid and neighbour != cube:
                total += self.grid[neighbour]
        return total

    def do_cycle(self, dimensions):
        self.expand_area(dimensions)
        new_grid = deepcopy(self.grid)

        for cube, state in self.grid.items():
            if dimensions == 3:
                active_neighbours = self.count_active_neighbours(cube, self.make_product(cube, dimensions=3))
            else:
                active_neighbours = self.count_active_neighbours(cube, self.make_product(cube, dimensions=4))
            if active_neighbours == 3 and state == 0:
                new_grid[cube] = 1
            elif active_neighbours not in (2, 3) and state == 1:
                new_grid[cube] = 0
        self.grid = deepcopy(new_grid)

    def count_active_cubes(self):
        return sum(list(self.grid.values()))

    def calculate(self, dimensions):
        self.make_grid(dimensions)
        for i in range(6):
            self.do_cycle(dimensions)
        return self.count_active_cubes()


calculator = Calculator()
print(f'Result of part 1: "{calculator.calculate(dimensions=3)}"')
print(f'Result of part 2: "{calculator.calculate(dimensions=4)}"')
