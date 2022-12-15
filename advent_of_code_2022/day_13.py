from copy import deepcopy
from functools import cmp_to_key
from itertools import zip_longest

RIGHT_ORDER = 1
NOT_RIGHT_ORDER = -1

with open('day_13.txt') as f:
    packages = []
    for pair in f.read().split('\n\n'):
        left, right = pair.split()
        left = [el for el in eval(left.rstrip())]
        right = [el for el in eval(right.rstrip())]
        packages.extend([left, right])


def compare(first, second):
    for left, right in zip_longest(first, second, fillvalue='RUN_OUT'):
        if left == 'RUN_OUT':
            return RIGHT_ORDER
        elif right == 'RUN_OUT':
            return NOT_RIGHT_ORDER
        elif isinstance(left, int) and isinstance(right, int):
            if left == right:
                pass
            elif left < right:
                return RIGHT_ORDER
            else:
                return NOT_RIGHT_ORDER
        else:
            left = [left] if isinstance(left, int) else left
            right = [right] if isinstance(right, int) else right
            comparison_result = compare(left, right)
            if comparison_result in (RIGHT_ORDER, NOT_RIGHT_ORDER):
                return comparison_result


def part1(packages):
    result = 0
    pair_index = 1
    for i in range(0, len(packages), 2):
        right_order = compare(packages[i], packages[i + 1])
        if right_order == 1:
            result += pair_index
        pair_index += 1
    return result


def part2(packages):
    additional_packages = [[[2]], [[6]]]
    packages.extend(additional_packages)
    packages.sort(key=cmp_to_key(compare), reverse=True)
    return (packages.index(additional_packages[0]) + 1) * (packages.index(additional_packages[1]) + 1)


print(f'Result of part 1: "{part1(deepcopy(packages))}"')
print(f'Result of part 2: "{part2(deepcopy(packages))}"')
