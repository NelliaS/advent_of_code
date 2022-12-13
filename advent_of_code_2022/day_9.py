with open('day_9.txt') as f:
    instructions = [(instr.split()[0], int(instr.split()[1])) for instr in f.read().splitlines()]


def move_to_knot(previous_knot, knot):
    x_diff, y_diff = previous_knot[0] - knot[0], previous_knot[1] - knot[1]

    if 2 in (abs(x_diff), abs(y_diff)):
        match (x_diff, y_diff):
            case (0, _):
                knot[1] += 1 if y_diff > 0 else -1
            case (_, 0):
                knot[0] += 1 if x_diff > 0 else -1
            case (1, _) | (-1, _):
                knot[0] += 1 if x_diff > 0 else -1
                knot[1] += 1 if y_diff > 0 else -1
            case (_, 1) | (_, -1):
                knot[0] += 1 if x_diff > 0 else -1
                knot[1] += 1 if y_diff > 0 else -1
            case _:
                knot[0] += 1 if x_diff > 0 else -1
                knot[1] += 1 if y_diff > 0 else -1

    return [knot[0], knot[1]]


def simulate(instructions, middle_knots):
    head = [0, 0]
    tail = [0, 0]
    tail_coordinates = [(0, 0)]

    for direction, number in instructions:
        for _ in range(number):
            match direction:
                case 'R':
                    head[0] += 1
                case 'L':
                    head[0] -= 1
                case 'D':
                    head[1] += 1
                case 'U':
                    head[1] -= 1

            if middle_knots:
                for i in range(len(middle_knots)):
                    previous_knot = head if i == 0 else middle_knots[i - 1]
                    middle_knots[i] = move_to_knot(previous_knot=previous_knot, knot=middle_knots[i])

            previous_to_tail = middle_knots[-1] if middle_knots else head
            tail = move_to_knot(previous_knot=previous_to_tail, knot=tail)
            tail_coordinates.append((tail[0], tail[1]))

    return len(set(tail_coordinates))


print(f'Result of part 1: "{simulate(instructions, middle_knots=[])}"')
print(f'Result of part 1: "{simulate(instructions, middle_knots=[[0, 0]]* 8)}"')
