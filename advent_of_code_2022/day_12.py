import math
from collections import defaultdict

import networkx as nx
from icecream import ic


class GoalFinder:
    def __init__(self):
        maze = {}
        with open('day_12.txt') as f:
            for y, line in enumerate(f):
                for x, number in enumerate([ord(letter) - 96 for letter in line.rstrip()]):
                    if number == -13:
                        self.start_point = (x, y)
                        number = 1
                    elif number == -27:
                        self.goal_point = (x, y)
                        number = 26
                    maze[(x, y)] = number
        self.maze = maze
        self.maze_measures = (len(line.rstrip()) - 1, y)

        neighbours = defaultdict(list)
        for x0, y0 in self.maze:
            for x1, y1 in [(x0 + 1, y0), (x0 - 1, y0), (x0, y0 - 1), (x0, y0 + 1)]:
                if 0 <= x1 <= self.maze_measures[0] and 0 <= y1 <= self.maze_measures[1]:
                    if self.maze[(x1, y1)] - self.maze[(x0, y0)] <= 1:
                        neighbours[(x0, y0)].append((x1, y1))

        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(neighbours.keys())
        for node, neighbours in neighbours.items():
            for neighbour_node in neighbours:
                self.graph.add_edge(node, neighbour_node)

    def part1(self):
        return nx.shortest_path_length(self.graph, source=self.start_point, target=self.goal_point)

    def part2(self):
        shortest_route = math.inf
        possible_starts = [key for key, value in self.maze.items() if value == 1]
        for start in possible_starts:
            try:
                steps = nx.shortest_path_length(self.graph, source=start, target=self.goal_point)
                if steps < shortest_route:
                    shortest_route = steps
            except nx.exception.NetworkXNoPath:
                ...
        return shortest_route


goal_finder = GoalFinder()
print(f'Result of part 1: "{goal_finder.part1()}"')
print(f'Result of part 1: "{goal_finder.part2()}"')
