import heapq

with open('day_1.txt') as f:
    elves_calories = [sum((map(int, items.split()))) for items in f.read().split('\n\n')]


def part1(elves_calories: list[int]) -> int:
    """Return the most calories taken by 1 elf."""
    return max(elves_calories)


def part2(elves_calories: list[int]) -> int:
    """Return sum of the most calories taken by 3 elves."""
    return sum(heapq.nlargest(3, elves_calories))


print(f'Result of part 1: "{part1(elves_calories)}"')
print(f'Result of part 2: "{part2(elves_calories)}"')
