import re
import time
from itertools import combinations_with_replacement, permutations

from icecream import ic
from line_profiler_pycharm import profile


def prepare_data() -> dict[str, list]:
    """
    Return parsed data into dictionary, where key is mask and value is list of tuples - memory adress and number.
        eg.'0000X001100X0001X011X10X010101101011': [(52773, 64752275), (3789, 898152), (12600, 7124813)],
    Data is given to dictionary in order in which should be applied.
    """
    instructions = {}
    with open('day_14.txt') as f:
        for mask_group in [mask_group.split('\n')[:-1] for mask_group in f.read().split('mask = ')[1:]]:
            mask = mask_group[0]
            instructions[mask] = []
            for el in mask_group[1:]:
                memory_address, number = re.findall('[0-9]+', el)
                instructions[mask].append((int(memory_address), int(number)))
    return instructions


def calculate_sum(memory):
    total = 0
    for value in memory.values():
        total += int(value, 2)
    return total


def part1(instructions):
    memory = {}
    for mask, steps in instructions.items():
        for address, value in steps:
            value = bin(value)[2:].zfill(36)
            result = apply_mask(mask, value)
            memory[address] = result
    return calculate_sum(memory)


@profile
def apply_mask(mask, value, part1=True):
    result = ''
    for mask_number, value_number in zip(mask, value):
        if part1:
            result += mask_number if mask_number != 'X' else value_number
        else:
            result += mask_number if mask_number != '0' else value_number
    return result


@profile
def part2(instructions):
    memory = {}
    instructions_reversed = dict(
        zip(list(instructions.keys())[::-1], [el[::-1] for el in (list(instructions.values())[::-1])])
    )
    for mask, steps in instructions_reversed.items():
        for address, value in steps:
            result = apply_mask(mask, bin(address)[2:].zfill(36), part1=False)
            result = result.replace('X', '{}')
            for combination in combinations_with_replacement(['0', '1'], r=result.count('{}')):
                for permutation in permutations(combination):
                    result_permutation = int(result.format(*permutation), 2)
                    if result_permutation not in memory:
                        memory[result_permutation] = value
    return sum(memory.values())


instructions = prepare_data()
print(f'Result of part 1: "{part1(instructions)}"')
print(f'Result of part 2: "{part2(instructions)}"')
