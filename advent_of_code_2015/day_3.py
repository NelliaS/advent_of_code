with open('day_3.txt') as f:
    instructions = list(f.read())


def visited_houses(instructions):
    '''Returns number of houses visited by Santa.
    Instructions are translated to coordinates (x,y) using function translator(instructions).
    Only number of original (non-repeated) coordinates is returned.'''
    coordinates = translator(instructions)
    original_coordinates = set(coordinates)
    return len(original_coordinates)


def translator(instructions):
    '''Returns coordinates.
    Input is array of instructions, where north is ^, south v, < west and > east.
    From instructions an array of tuples as coordinates (x, y) is made.'''
    coordinates = []
    x = 0       # -1 for west, +1 for east
    y = 0       # +1 for north, -1 for south
    for sign in instructions:
        if sign == '<':       # -1 east
            x -= 1
        elif sign == '>':     # +1 west
            x += 1
        elif sign == '^':     # +1 north
            y += 1
        else:                 # -1 south
            y -= 1
        coordinates.append((x,y))
    return coordinates


def visited_houses2(instructions):
    '''Returns number of houses visited by Santa and Robo-Santa.
    Instructions are divided into santa_instructions and robo_santa_instructions strings.
    Two arrays of tuples as coordinates (x,y) are made using function translator(instructions).
    Both arrays are merged and only number of original (non-repeated) coordinates is returned'''
    santa_instructions = ''
    robo_santa_instructions = ''
    for i, sign in enumerate(instructions):    # even instructions are for Santa, odd for Robo-santa
        if i % 2 == 0:
            santa_instructions += sign
        else:
            robo_santa_instructions += sign
    coordinates_santa = translator(santa_instructions)
    coordinates_robo_santa = translator(robo_santa_instructions)
    coordinates_both_original = set(coordinates_santa + coordinates_robo_santa)
    return len(coordinates_both_original)



print(visited_houses(instructions))
print(visited_houses2(instructions))







