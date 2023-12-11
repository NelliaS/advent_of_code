import re


def main():
    part_1 = 0
    part_2 = 0

    with open('day_3.txt') as f:
        lines = ['.' + line.rstrip() + '.' for line in f.readlines()]
        lines = [len(lines[0]) * '.'] + lines + [len(lines[0]) * '.']

    for line_index, line in enumerate(lines[:-1]):
        if line_index == 0:
            continue

        # part 1
        for match in list(re.finditer('\d+', line)):
            start, end = match.span()
            neighbours = set()
            for index in range(start - 1, end + 1):
                neighbours.add(lines[line_index - 1][index])
                neighbours.add(lines[line_index + 1][index])
            neighbours.add(line[start - 1])
            neighbours.add(line[end])
            if len(neighbours) > 1:
                part_1 += int(match[0])

        # part 2
        for asterisk_match in list(re.finditer('\*', line)):
            numbers = []
            for number_match in (
                list(re.finditer('\d+', lines[line_index - 1]))
                + list(re.finditer('\d+', lines[line_index + 1]))
                + list(re.finditer('\d+', line))
            ):
                start, end = number_match.span()
                if asterisk_match.span()[0] in range(start - 1, end + 1):
                    numbers.append(int(number_match[0]))
            if len(numbers) == 2:
                part_2 += numbers[0] * numbers[1]

    return part_1, part_2


part_1, part_2 = main()
print(f'Result of part 1: "{part_1}"')
print(f'Result of part 2: "{part_2}"')
