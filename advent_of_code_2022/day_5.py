import re
from collections import defaultdict


def process_input():
    with open('day_5.txt') as f:
        cargo, instructions = f.read().split('\n\n')

        stacks = defaultdict(list)
        for line in cargo.replace('    ', ' x ').split('\n')[::-1][1:]:
            for i, el in enumerate(line.split(), start=1):
                if el != 'x':
                    stacks[i].append(el[1:-1])

        moves = []
        for instruction in instructions.split('\n'):
            numbers = re.findall('[0-9]+', instruction)
            if numbers:
                moves.append([int(number) for number in numbers])
        return stacks, moves


def main(reverse=True):
    stacks, moves = process_input()
    for move in moves:
        number, wherefrom, to = move
        if reverse:
            stacks[to].extend(stacks[wherefrom][-number:][::-1])
        else:
            stacks[to].extend(stacks[wherefrom][-number:])
        del stacks[wherefrom][-number:]

    return ''.join([ls[-1] for ls in stacks.values()])


print(f'Result of part 1: "{main()}"')
print(f'Result of part 2: "{main(reverse=False)}"')
