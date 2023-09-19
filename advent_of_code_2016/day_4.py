import re
from collections import Counter
from itertools import cycle
from string import ascii_lowercase


with open('day_4.txt') as f:
    data = []
    lines = [line.strip('\n') for line in f.readlines()]
    for line in lines:
        number_match = re.search('\d+', line)
        number = int(number_match[0])
        name = line[:number_match.span()[0]].strip('-')
        checksum = line[number_match.span()[1]:].lstrip('[').rstrip(']')
        data.append((name, number, checksum))


def part1():
    sum_ids = 0

    for code, number, checksum in data:
        code = ''.join(sorted(code.replace('-', '')))
        most_common = Counter(code).most_common(5)
        expected_result = ''.join([letter for (letter, _) in most_common])
        if checksum == expected_result:
            sum_ids += number

    return sum_ids


def find_in_alphabet(position):
    for i, letter in enumerate(cycle(ascii_lowercase)):
        if i == position:
            return letter


def part2():
    for code, number, checksum in data:
        decrypted = ''
        for char in code:
            if char == '-':
                decrypted += ' '
            else:
                decrypted += find_in_alphabet(ord(char) - 97 + number)
        if 'north' in decrypted:
            return number


print(f'Result of part 1: "{part1()}"')
print(f'Result of part 2: "{part2()}"')
