import turtle

instructions = []
with open('day_12.txt') as f:
    for line in f:
        line = line.rstrip().lower()
        instructions.append(line.rstrip())


# PART 1
def move_ship(instructions):
    '''
    Input is array of instructions - letter and number.
    Letters stand for:  n - north, s - south, e - east, w - west, l - left, r - right, f - forward.
    Make appropriate moves with turtle - named ship.
    Return ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position).
    '''
    ship = turtle.Turtle()
    ship.speed(0)
    for move in instructions:
        number = int(move[1:])
        letter = move[0]
        if letter in 'nsew':
            x = ship.xcor()
            y = ship.ycor()
            if letter == 'n':
                y += number
            elif letter == 's':
                y -= number
            elif letter == 'e':
                x += number
            else:
                x -= number
            ship.goto(x,y)
        elif letter == 'r':
            ship.rt(number)
        elif letter == 'l':
            ship.lt(number)
        else:       # f
            ship.fd(number)
    return abs(ship.xcor()) + abs(ship.ycor())



# PART 2

def rotate(instr, number, x_r, y_r):
    '''Do rotations of relative distance between ship and waypoint'''
    if number in (90, 270):
        if number == 90 and instr == 'r' or number == 270 and instr == 'l':
            x_r, y_r = y_r, -x_r
        else:
            x_r, y_r = -y_r, x_r
    else:               # 180
        x_r, y_r = -x_r, -y_r
    return x_r, y_r


def move_ship_and_waypoint(instructions):
    '''
    There are two turtles - named ship and waypoint.
    With ship waypoint moves too, the waypoint starts 10 units east and 1 unit north relative to the ship.
    Input is array of instructions - letter and number.
    Letters stand for:
        f - move ship in direction of waypoint (in number given times),
        n - north / s - south / e - east / w - west - moves waypoint in number given,
        r - right / l - left - rotates waypoint around ship
    Return ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position).
    '''
    ship = turtle.Turtle()
    waypoint = turtle.Turtle()
    ship.speed(0)
    waypoint.speed(0), waypoint.goto(10, 1)       # origin => x = 10, y = 1
    for move in instructions:
        number = int(move[1:])
        instr = move[0]
        x_w = int(waypoint.xcor())          # waypoint coordinates
        y_w = int(waypoint.ycor())
        x_s = int(ship.xcor())              # ship coordinates
        y_s = int(ship.ycor())
        x_r = x_w - x_s                     # distance between ship and waypoint
        y_r = y_w - y_s
        if instr == 'f':
            x_s += x_r * number
            y_s += y_r * number
            ship.goto(x_s, y_s)
            x_w = x_s + x_r
            y_w = y_s + y_r
            waypoint.goto(x_w, y_w)
        elif instr in 'nsew':
            if instr == 'n':
                y_w += number
            elif instr == 's':
                y_w -= number
            elif instr == 'e':
                x_w += number
            else:
                x_w -= number
            waypoint.goto(x_w, y_w)
        else:
            x_r, y_r = rotate(instr, number, x_r, y_r)
            x_w = x_s + x_r
            y_w = y_s + y_r
            waypoint.goto(x_w, y_w)
    return abs(ship.xcor()) + abs(ship.ycor())


print(move_ship(instructions))                # part 1
print(move_ship_and_waypoint(instructions))   # part 2
