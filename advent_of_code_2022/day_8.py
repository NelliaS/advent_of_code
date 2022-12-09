import math
from itertools import dropwhile, takewhile

import numpy as np

with open('day_8.txt') as f:
    trees = np.array([list(map(int, list(line))) for line in f.read().splitlines()])


def check_visibility(tree, x, y):
    for numbers in trees[x][:y], trees[x][y + 1 :], trees[:, y][:x], trees[:, y][x + 1 :]:
        if not list(dropwhile(lambda x: x < tree, numbers)):
            return True
    return False


def count_visible_trees(tree, x, y):
    count = []

    for numbers in trees[x][:y][::-1], trees[x][y + 1 :], trees[:, y][:x][::-1], trees[:, y][x + 1 :]:
        view_distance = len(list(takewhile(lambda x: x < tree, numbers)))
        if view_distance != len(numbers):
            view_distance += 1
        count.append(view_distance)
    return math.prod(count)


def count_trees(trees):
    visible = 2 * len(trees[0]) + 2 * len(trees) - 4
    scenic_score = 0
    for i_row, row in enumerate(trees[1:-1], start=1):
        for i_tree, tree in enumerate(row[1:-1], start=1):
            if check_visibility(tree, i_row, i_tree):
                visible += 1
            if (checked_score := count_visible_trees(tree, i_row, i_tree)) > scenic_score:
                scenic_score = checked_score
    return visible, scenic_score


visible, scenic_score = count_trees(trees)
print(f'Result of part 1: "{visible}"')
print(f'Result of part 2: "{scenic_score}"')
