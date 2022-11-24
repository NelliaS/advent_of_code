import math
from itertools import combinations, pairwise

from line_profiler_pycharm import profile

with open('day_10.txt') as f:
    numbers = [int(number.rstrip()) for number in f.readlines()]
    numbers.extend([0, max(numbers) + 3])
    numbers.sort()


def multiplied_differences(numbers):
    """Return multiplication of 1-jolt and 3-jolt differences"""
    one_jolts = 0
    three_jolts = 0
    for i, number in enumerate(numbers[1:]):
        difference = number - numbers[i]
        if difference == 1:
            one_jolts += 1
        else:
            three_jolts += 1
    return one_jolts * three_jolts


def validate_combination(combination, first, last):
    """Validate combination - difference between numbers is 3 or less."""
    combination = [first, *list(combination), last]
    for number1, number2 in pairwise(combination):
        if number2 - number1 not in (1, 2, 3):
            return False
    return True


def find_chunk_combinations(chunk):
    """
    Find number of combinations for given chunk.
    In case of first chunk make it an option to remove first number as well (otherwise not possible - difference is 3).
    """
    distinct_arrangements = 0
    r = len(chunk) - 1
    chunk_part = chunk[1:-1] if chunk[0] >= 3 else chunk[:-1]
    first, last = (chunk[0], chunk[-1]) if chunk[0] >= 3 else (0, chunk[-1])

    while r >= 0:
        valid_combinations = [c for c in combinations(chunk_part, r=r) if validate_combination(c, first, last)]
        distinct_arrangements += len(valid_combinations)
        r -= 1

    return distinct_arrangements


def calculate_all_combinations(numbers):
    """Calculate all combinations for given list of numbers."""
    combinations = []
    chunk_start = 0
    for i, number in enumerate([n2 - n1 for n1, n2 in pairwise(numbers)]):
        if number == 3:
            combinations.append(find_chunk_combinations(numbers[1:-1][chunk_start:i]))
            chunk_start = i

    return math.prod(filter(lambda x: x != 0, combinations))


print(f'Result of part 1: "{multiplied_differences(numbers)}"')
print(f'Result of part 2: "{calculate_all_combinations(numbers)}"')
