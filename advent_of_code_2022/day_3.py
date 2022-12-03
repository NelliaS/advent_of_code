with open('day_3.txt') as f:
    items = [line.rstrip() for line in f.readlines()]


def calculate_letter_score(letter):
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38


def part1(items):
    total = 0
    for item in items:
        half = len(item) // 2
        intersection = set(item[:half]).intersection(item[half:]).pop()
        total += calculate_letter_score(intersection)
    return total


def part2(items):
    total = 0
    for i in range(0, len(items), 3):
        intersection = set(items[i]).intersection(items[i + 1], items[i + 2]).pop()
        total += calculate_letter_score(intersection)
    return total


print(f'Result of part 1: "{part1(items)}"')
print(f'Result of part 1: "{part2(items)}"')
