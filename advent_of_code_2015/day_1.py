with open('day_1.txt') as f:
    instructions = f.read()

def floor_level(instructions):
    '''Determine in which floor should Santa go.
    Instructions: opening parenthesis "(" stands for level up, closing parenthesis ")" stands for going level down'''
    up = instructions.count('(')
    down = instructions.count(')')
    return up - down


print(floor_level(instructions))


def entering_basement(instructions):
    '''Determine in which floor (numbered from 1) will Santa enter basement ( < 0 )
    Instructions: opening parenthesis "(" stands for level up, closing parenthesis ")" stands for going level down'''
    current_floor = 1
    for index, value in enumerate(instructions):
        if value == '(':
            current_floor += 1
        else:
            current_floor -= 1
        if current_floor < 1:
            return index + 1


print(entering_basement(instructions))