import re


def find_number(line, backwards=False):
    substring = ''
    if backwards:
        line = line[::-1]

    for char in line:
        substring += char
        if number := search_string(substring if not backwards else substring[::-1]):
            return number


def search_string(string):
    translation = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    if string.startswith(tuple(translation.values())):
        return string[0]
    elif string.endswith(tuple(translation.values())):
        return string[-1]
    else:
        for word in translation.keys():
            if string.startswith(word) or string.endswith(word):
                return translation[word]


def main():
    part_1 = 0
    part_2 = 0

    with open('day_1.txt') as f:
        for line in f.readlines():
            numbers = re.findall('\d', line)
            part_1 += int(numbers[0] + numbers[-1])

            first_number = find_number(line)
            second_number = find_number(line, backwards=True)
            part_2 += int(first_number + second_number)

    return part_1, part_2


print(f'Result of part 1: "{main()[0]}"')
print(f'Result of part 2: "{main()[1]}"')
