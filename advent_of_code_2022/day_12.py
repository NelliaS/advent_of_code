import math
from collections import defaultdict

from line_profiler_pycharm import profile
from icecream import ic

import networkx as nx


class GoalFinder:
    # @profile
    def __init__(self):
        maze = {}
        maze_raw = []
        with open('day_12_example.txt') as f:
            for y, line in enumerate(f):
                maze_raw.append([ord(letter) - 96 for letter in line.rstrip()])
                for x, number in enumerate([ord(letter) - 96 for letter in line.rstrip()]):
                    if number == -13:
                        self.start_point = (x, y)
                        number = 1
                    elif number == -27:
                        self.goal_point = (x, y)
                        number = 26
                    maze[(x, y)] = number
        self.maze = maze
        self.maze_measures = (len(maze_raw[0]) - 1, len(maze_raw) - 1)
        self.steps_to_field = {k: math.inf for k in self.maze}
        self.neighbours = defaultdict(list)
        for x0, y0 in self.maze:
            for x1, y1 in [(x0 + 1, y0), (x0 - 1, y0), (x0, y0 - 1), (x0, y0 + 1)]:
                if 0 <= x1 <= self.maze_measures[0] and 0 <= y1 <= self.maze_measures[1]:
                    if self.maze[(x1, y1)] - self.maze[(x0, y0)] <= 1:
                        self.neighbours[(x0, y0)].append((x1, y1))
        ic(self.neighbours)
        # ic(self.steps_to_field)
        # ic(maze_raw)
        # ic(maze)
        # ic(self.maze_measures)
        self.shortest_route = math.inf

    # @profile
    def part1(self):
        self.one_route(self.start_point, 0, ())

    # @profile
    def one_route(self, coord: tuple, count_steps: int, steps: tuple):
        steps = steps + (coord,)
        self.steps_to_field[coord] = len(steps)

        possible_steps = [
            neighbour for neighbour in self.neighbours[coord] if count_steps < self.steps_to_field[neighbour]
        ]

        if self.goal_point in possible_steps:
            # ic(f'goal visible after {steps} and {count_steps}')
            if (count_steps + 1) < self.shortest_route:
                self.shortest_route = count_steps + 1
                return
        elif count_steps > self.shortest_route or not possible_steps:
            return
        else:
            count_steps += 1
            if count_steps > 500:
                return

            for new_coord in possible_steps:
                self.one_route(coord=new_coord, count_steps=count_steps, steps=steps)


goal_finder = GoalFinder()
goal_finder.part1()
ic(goal_finder.shortest_route)
