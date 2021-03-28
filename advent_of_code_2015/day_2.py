presents = []

with open('day_2.txt') as f:
    for line in f:
        presents.append(line.rstrip())


def calculate_square_feets(presents):
    '''Calculate sum of square feets needed to wrap every present. Presents are rectangular cuboid, defined by length l, width w, and height h (in this order), e.g. 2x3x4
    Used formula is 2*l*w + 2*w*h + 2*h*l plus area of smallest side (either of l*w / w*h / h*l)'''
    total = 0
    for present in presents:
        present = present.split('x')
        present = list(map(int, present))
        # lengths of sides
        w = present[0]
        h = present[1]
        l = present[2]
        # contents of sides
        lw = l * w
        wh = w * h
        hl = h * l
        # find smallest content of side
        smallest = min(lw, wh, hl)
        # use formula to calculate square feets needed for one present, add to total
        total += 2 * lw + 2 * wh + 2 * hl + smallest
    return total


print(calculate_square_feets(presents))


def calculate_ribbons_length(presents):
    ''' Ribbons are calculated from the shortest distance around present's sides, e.g. 2x3x4 requires 2+2+3+3 = 10 feets of ribbons.
        Plus they need some more length for bows, bow is calculated as l * w * h.'''
    total = 0
    for present in presents:
        present = present.split('x')
        present = list(map(int, present))
        # lengths of sides
        w = present[0]
        h = present[1]
        l = present[2]
        # length needed to make a bow
        total += l * w * h
        # ribbon length - sum of two smallest sides * 2
        present.sort()
        total += 2 * present[0] + 2 * present[1]
    return total


print(calculate_ribbons_length(presents))