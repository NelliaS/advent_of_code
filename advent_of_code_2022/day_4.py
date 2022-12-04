import re

with open('day_4.txt') as f:
    pairs = []
    for pair in f.read().splitlines():
        n1, n2, n3, n4 = list(map(int, re.findall('[0-9]+', pair)))
        pairs.append([set(range(n1, n2 + 1)), set(range(n3, n4 + 1))])


def main(pairs: list[list[set, set]]):
    part_1, part_2 = 0, 0

    for set1, set2 in pairs:
        if set1.issubset(set2) or set2.issubset(set1):
            part_1 += 1
        if set1.intersection(set2):
            part_2 += 1
    return part_1, part_2


result1, result2 = main(pairs)
print(f'Result of part 1: "{result1}"')
print(f'Result of part 2: "{result2}"')
