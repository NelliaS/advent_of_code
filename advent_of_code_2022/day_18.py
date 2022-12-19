from itertools import product

from networkx import Graph, has_path


class CubeCalculator:
    def __init__(self):
        cubes = []
        with open('day_18.txt') as f:
            for line in f:
                x, y, z = line.rstrip().split(',')
                cubes.append((int(x), int(y), int(z)))
        assert len(cubes) == len(set(cubes))
        self.cubes = tuple(cubes)

        x_val, y_val, z_val = [x for (x, y, z) in cubes], [y for (x, y, z) in cubes], [z for (x, y, z) in cubes]
        mins = (min(x_val), min(y_val), min(z_val))
        maxes = (max(x_val), max(y_val), max(z_val))

        self.space = {}
        coordinates = product(
            [*range(mins[0] - 1, maxes[0] + 2)],
            [*range(mins[1] - 1, maxes[1] + 2)],
            [*range(mins[2] - 1, maxes[2] + 2)],
        )
        for cube in coordinates:
            self.space[cube] = 'cube' if cube in self.cubes else 'water'

        self.water_mark = (mins[0] + 1, mins[1] + 1, mins[2] + 1)
        self.space[self.water_mark] = 'water'

        self.graph = Graph()
        self.graph.add_nodes_from(self.space)
        for node, content in self.space.items():
            if content == 'water':
                for neighbour_node in self.make_adjacent(node, 'water'):
                    self.graph.add_edge(node, neighbour_node)

    def make_adjacent(self, cube, filter):
        x, y, z = cube
        adjacent_cubes = {
            (x - 1, y, z),
            (x + 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        }
        if filter == 'cube':
            return adjacent_cubes.intersection(self.cubes)
        elif filter == 'water':
            return [cube for cube in adjacent_cubes.intersection(self.space) if self.space[cube] == 'water']

    def part1(self):
        result = 0
        for cube in self.cubes:
            result += 6 - len(self.make_adjacent(cube, 'cube'))
        return result

    def part2(self):
        result = 0
        for cube, content in self.space.items():
            if content == 'cube':
                for adjacent_cube in self.make_adjacent(cube, 'water'):
                    if has_path(self.graph, adjacent_cube, self.water_mark):
                        result += 1
        return result


cube_calculator = CubeCalculator()

print(f'Result of part 1: "{cube_calculator.part1()}"')
print(f'Result of part 2: "{cube_calculator.part2()}"')
