import math
from copy import deepcopy

from icecream import ic


class GoalFinder:
    def __init__(self):
        maze = {}
        maze_picture = []
        with open('day_12.txt') as f:
            for y, line in enumerate(f):
                maze_picture.append([ord(letter) - 96 for letter in line.rstrip()])
                for x, number in enumerate([ord(letter) - 96 for letter in line.rstrip()]):
                    if number == -13:
                        self.start_point = (x, y)
                        number = 1
                    elif number == -27:
                        self.goal_point = (x, y)
                        number = 26
                    maze[(x, y)] = number
        self.maze = maze
        self.maze_measures = (len(maze_picture[0]) - 1, len(maze_picture) - 1)
        self.steps_to_field = {k: math.inf for k in self.maze}
        # ic(self.steps_to_field)
        # ic(maze_picture)
        # ic(maze)
        # ic(self.maze_measures)
        self.shortest_route = math.inf

    def find_possible_steps(self, coord, last_step):
        x0, y0 = coord
        possible_steps = []
        for x1, y1 in [(x0 + 1, y0), (x0 - 1, y0), (x0, y0 - 1), (x0, y0 + 1)]:
            if 0 <= x1 <= self.maze_measures[0] and 0 <= y1 <= self.maze_measures[1]:
                if self.maze[(x1, y1)] - self.maze[(x0, y0)] <= 1 and (x1, y1) != last_step:
                    possible_steps.append((x1, y1))
        return possible_steps

    def part1(self):
        self.one_route(self.start_point, 0, [])

    def one_route(self, coord: tuple, count_steps: int, steps: list):
        steps = deepcopy(steps)
        steps.append(coord)
        self.steps_to_field[coord] = len(steps)

        possible_steps = self.find_possible_steps(coord=coord, last_step=steps[-1] if steps else None)

        if self.goal_point in possible_steps:
            # ic(f'goal visible after {steps} and {count_steps}')
            if (count_steps + 1) < self.shortest_route:
                self.shortest_route = count_steps + 1
                # ic(self.shortest_route)
                return
        elif count_steps > self.shortest_route or not possible_steps:
            return
        else:
            count_steps += 1
            for new_coord in possible_steps:
                if len(steps) <= self.steps_to_field[new_coord]:
                    self.one_route(coord=new_coord, count_steps=count_steps, steps=steps)


goal_finder = GoalFinder()
goal_finder.part1()
ic(goal_finder.shortest_route)
# ic(goal_finder.steps_to_field)
