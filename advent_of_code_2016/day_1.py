with open('day_1.txt') as f:
    steps = f.read().splitlines()[0].split(', ')


def calculate_distance(coord):
    return abs(0 - coord[0]) + abs(0 - coord[1])


def main(steps, find_first_repeated=False):
    headings = {
        'N': {'L': 'W', 'R': 'E'},
        'E': {'L': 'N', 'R': 'S'},
        'S': {'L': 'E', 'R': 'W'},
        'W': {'L': 'S', 'R': 'N'},
    }
    coord = [0, 0]
    heading = 'N'
    visited_coordinates = []
    for step in steps:
        count = int(step[1:])
        heading = headings[heading][step[0]]

        for _ in range(count):
            axis = 1 if heading in ('N', 'S') else 0
            coord[axis] += -1 if heading in ('N', 'W') else 1

            if find_first_repeated:
                if coord in visited_coordinates:
                    return calculate_distance(coord)
                visited_coordinates.append([coord[0], coord[1]])

    return calculate_distance(coord)


print(f'Result of part 1: "{main(steps)}"')
print(f'Result of part 2: "{main(steps, find_first_repeated=True)}"')
