
seats = []

with open('day_11.txt') as f:
    for line in f:
        line = list(line.rstrip())
        seats.append(line)


# PART 1

def occupy_seats(seats):
    '''
    Procedure:
    People occupy seats ('L') in rounds. There is also floor ('.') which never becomes occupied.
    If there are no occupied seats ('#') in 8 adjacent tiles, certain seat becomes occupied,
    then if there are 4 or more seats occupied in 8 adjacent tiles to certain seat, the seat becomes empty
    and this repeats until no more seats are changing their state.

    Return number of occupied seats after stabilization.
    '''
    total_rows = len(seats)
    while True:
        seats_new = []
        for i_row, row in enumerate(seats):
            row_new = []
            for i_seat, seat in enumerate(row):
                row_new.append(apply_rules_part1(i_row, i_seat, seat, seats, len(row), total_rows))
            seats_new.append(row_new)
        if seats_new != seats:      # equlibrium not reached
            seats = seats_new
        else:                       # stabilization
            break
    occupied_seats = 0              # count occupied seats
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied_seats += 1
    return occupied_seats


def determine_shifts(i_row, i_seat, length_row, total_rows):
    '''
    shifts_row = -1, 0, 1 (previous, current, next)
    shifts_pos = -1, 0, 1 (previous, current, next)
    '''
    if i_row == 0:                     # shifting row
        shifts_row = 0, 1
    elif i_row == total_rows - 1:
        shifts_row = -1, 0
    else:
        shifts_row = -1, 0, 1
    if i_seat == 0:
        shifts_pos = 0, 1              # shift positions
    elif i_seat == length_row - 1:
        shifts_pos = -1, 0
    else:
        shifts_pos = -1, 0, 1
    return shifts_row, shifts_pos


def apply_rules_part1(i_row, i_seat, seat, seats, length_row, total_rows):
    '''Apply rules for occupying seats'''
    if seat == '.':         # (.) floor
        return '.'
    adjacents = ''
    shifts_row, shifts_pos = determine_shifts(i_row, i_seat, length_row, total_rows)
    for row_shift in shifts_row:
        for pos_shift in shifts_pos:
            if row_shift == 0 and pos_shift == 0:
                pass
            else:
                adjacents += seats[i_row + row_shift][i_seat + pos_shift]
    if seat == 'L':         # empty
        if '#' not in adjacents:
            return '#'     # becomes occupied (no occupied seats in 8 adjacent fields)
        else:
            return 'L'
    else:                  # occupied
        if adjacents.count('#') >= 4:      # 4 or more occupied, seat becomes empty
            return 'L'
        else:
            return '#'



# PART 2

def apply_directions(r, c, course):
    directions = {
        'right': [r,c+1],
        'left': [r,c-1],
        'up': [r-1,c],
        'up-right': [r-1,c+1],
        'up-left': [r-1,c-1],
        'down': [r+1,c],
        'down-right': [r+1,c+1],
        'down-left': [r+1,c-1]}
    r, c = directions[course]       # make appropriate opperation
    return (r, c)


def seats_in_sight(coord, coord_max, seat, seats):
    '''Return seats in sight to certain seat (8 directions)'''
    r_d, c_d = coord        # default
    r_max, c_max = coord_max
    in_sight = ''           # seats in sight to certain seat
    for course in 'right', 'left', 'up', 'up-right', 'up-left', 'down', 'down-right', 'down-left':
        r_n, c_n = apply_directions(r_d, c_d, course)       # new
        if r_n <= r_max and c_n <= c_max and r_n >= 0 and c_n >= 0:       # if checked position exists, add it to seats in sight
            see = seats[r_n][c_n]
            while see == '.':             # if it is empty seat, check again
                r_n, c_n = apply_directions(r_n, c_n, course)   # new
                if r_n <= r_max and c_n <= c_max and r_n >= 0 and c_n >= 0:
                    see = seats[r_n][c_n]
                else:
                    break
            in_sight += see
    return in_sight


def apply_rules_part2(coord, coord_max, seat, seats):
    '''Apply rules for occupying seats'''
    in_sight = seats_in_sight(coord, coord_max, seat, seats)
    if seat == '.':         # (.) floor
        return '.'
    if seat == 'L':         # empty
        if '#' not in in_sight:
            return '#'     # becomes occupied (no occupied seats in 8 fields on sight
        else:
            return 'L'
    else:                  # occupied
        if in_sight.count('#') >= 5:      # 5 or more occupied also, becomes empty
            return 'L'
        else:
            return '#'


def occupy_seats2(seats):
    '''
    Procedure:
    As long as it is needed for chaos to reach equlibrium call functions for applying rules for seats.
    Rules for occupied seats changed - relevant is first seat, which can be seen in eight directions,
    apply rules until no more seats are changing their state.

    Return number of occupied seats after stabilization.
    '''
    while True:
        seats_new = []
        for i_row, row in enumerate(seats):
            coord_max = (len(seats) - 1, len(row)-1)    # max number of rows, max number of columns
            row_new = []
            for i_seat, seat in enumerate(row):
                coord = (i_row, i_seat)         # which row, which column
                row_new.append(apply_rules_part2(coord, coord_max, seat, seats))
            seats_new.append(row_new)
        if seats_new != seats:          # equlibrium not reached
            seats = seats_new
        else:                           # equlibrium reached
            break
    occupied_seats = 0                           # count occupied seats (#) in seats
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied_seats += 1
    return occupied_seats


print(occupy_seats(seats))               # part 1
print(occupy_seats2(seats))              # part 2