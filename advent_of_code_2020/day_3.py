pattern = []

with open('day_3.txt') as f:
    for line in f:
        pattern.append([line.rstrip()])


def count_trees(pattern, right, down):
    '''Use dictionary to redefine positions outside base pattern,
    count all trees in pattern (#) which we meet, when we follow defined number of moves to right and down'''
    # for making dictionary
    len_line = len(''.join(pattern[0]))
    border_pos = len_line - right - 1           # border positions - need to be translated
    keys = [*range(border_pos, len_line)]       # keys up to length of line
    values = []
    for key in keys:
        values.append(key - border_pos - 1)
    # make dictionary
    dictionary = dict(zip(keys, values))
    # count trees and change current position
    count = 0
    pos = 0
    for index, line in enumerate(pattern):
        if index % down == 0:
            # count met tree
            if line[0][pos] == '#':
                count += 1
            # define new position after move
            if pos > border_pos:        # redefine border position, if needed
                pos = dictionary[pos]
            else:
                pos += right
    return count


def follow_instructions(instructions):
    '''Call function count_trees() for every instruction, return product of multiplication of all trees'''
    for i, instruction in enumerate(instructions):
        right, down = instruction
        if i == 0:
            total = count_trees(pattern, right, down)
        else:
            total *= count_trees(pattern, right, down)
    return total


part1_instructions = [(3, 1)]
part2_instructions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(follow_instructions(part1_instructions))
print(follow_instructions(part2_instructions))
