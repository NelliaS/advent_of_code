codes = []

with open('day_5.txt') as f:
    for line in f:
        codes.append(line.rstrip())


def decypher(code, range_of_seats):
    ''' Each letter in code tells which half of region the searched seat is,
    "F" / "L" stands for lower half, "B" / "R" stands for upper half.'''
    for letter in code:
        half = len(range_of_seats) // 2
        if len(range_of_seats) == 1:   # only one number is left in given range
            if letter in 'FL':
                return range_of_seats[0]
            else:
                return range_of_seats[0] + 1
        elif letter in 'FL':                            # lower half
            range_of_seats = range_of_seats[:half]
        else:                                           # upper half
            range_of_seats = range_of_seats[half + 1:]


def determine_seat_id(code):
    '''First 7 letters in code determine row, last 3 determine column.
    Seat ID is multiplication of row, column and number 8.'''
    row = decypher(code[0:7], range(0,127))
    column = decypher(code[7:10], range(0,7))
    seat_id = row * 8 + column
    return seat_id


def return_seats(codes):
    '''Boarding pass is represented by code.
    From all ID seats return highest ID seat,
    and only missing seat in range of seats (my seat)'''
    seats = []
    for code in codes:
        seat_id = determine_seat_id(code)
        seats.append(seat_id)
    seats = sorted(seats)
    for number in range(seats[1], seats[-1]): # first and last seats shouldn't be included
        if number not in seats:               # my seat is only one missing in given range
            my_seat = number
    return seats[-1], my_seat                 # highest seat and my seat


highest_seat, my_seat = return_seats(codes)
print(highest_seat)     # part 1
print(my_seat)          # part 2
