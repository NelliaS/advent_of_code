with open('day_3.txt') as f:
    triples = [line.split() for line in f.read().splitlines()]


def determine_triangle(triple):
    x, y, z = [int(number) for number in triple]
    if x + y > z:
        if y + z > x:
            if z + x > y:
                return True
    return False


def part1():
    count = 0
    for triple in triples:
        if determine_triangle(triple):
            count += 1
    return count


def part2():
    count = 0
    for row in range(0, len(triples), 3):
        for column in 0, 1, 2:
            x, y, z = triples[row][column], triples[row + 1][column], triples[row + 2][column]
            if determine_triangle([x, y, z]):
                count += 1
    return count


print(f'Result of part 1: "{part1()}"')
print(f'Result of part 2: "{part2()}"')
