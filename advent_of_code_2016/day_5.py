from hashlib import md5
from itertools import count

with open('day_5.txt') as f:
    password = f.readline().rstrip()


def encode(text):
    return md5(text.encode()).hexdigest()


def part1(password):
    result = ''
    for number in count(start=0, step=1):
        hex_format = encode(f'{password}{number}')
        if hex_format.startswith('0' * 5):
            result += hex_format[5]
            if len(result) == len(password):
                return result


def part2(password):
    data = {}
    for number in count(start=0, step=1):
        hex_format = encode(f'{password}{number}')
        if hex_format.startswith('0' * 5) and hex_format[5].isdigit():
            position = int(hex_format[5])
            if position not in data.keys() and 0 <= position <= 7:
                data[position] = hex_format[6]
                if len(data.keys()) == 8:
                    return ''.join([data[i] for i in range(0, 8)])


print(f'Result of part 1: "{part1(password)}"')
print(f'Result of part 2: "{part2(password)}"')
