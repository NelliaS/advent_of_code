from collections import defaultdict
from itertools import count, pairwise


class SandSimulator:
    def __init__(self):
        self.grid: defaultdict[(int, int), int] = defaultdict(lambda: 0)
        with open('day_14.txt') as f:
            for line in f:
                for (x1, y1), (x2, y2) in pairwise(
                    [[int(n) for n in el.split(',')] for el in line.rstrip().split(' -> ')]
                ):
                    constant, constant_pos, scope = (x1, 0, [y1, y2]) if x1 == x2 else (y1, 1, [x1, x2])
                    scope.sort()
                    for number in range(scope[0], scope[1] + 1):
                        point = (constant, number) if constant_pos == 0 else (number, constant)
                        self.grid[point] = 1
        self.lowest_floor = max([y for (x, y) in self.grid.keys()])
        self.just_above_bedrock = self.lowest_floor + 1
        self.part1, self.part2 = None, None

    def simulate_movement(self, n, x, y):
        while True:
            # sand goes from abyss - part1 result
            if y == self.lowest_floor and self.part1 is None:
                self.part1 = n - 1
            # sand hits bedrock and stops
            if y == self.just_above_bedrock:
                self.grid[x, y] = 1
                return
            # sand goes down
            elif not self.grid[x, y + 1]:
                y += 1
            # sand goes down - left
            elif not self.grid[x - 1, y + 1]:
                x -= 1
                y += 1
            # sand goes down - right
            elif not self.grid[x + 1, y + 1]:
                x += 1
                y += 1
            # sand stopped
            else:
                self.grid[x, y] = 1
                return

    def release_sand(self):
        x, y = 500, 0
        for n in count(start=1):
            if self.grid[x, y]:  # equilibrium reached
                self.part2 = n - 1
                return
            else:
                self.simulate_movement(n, x, y)


sandsimulator = SandSimulator()
sandsimulator.release_sand()
print(f'Result of part 1: "{sandsimulator.part1}"')
print(f'Result of part 1: "{sandsimulator.part2}"')
