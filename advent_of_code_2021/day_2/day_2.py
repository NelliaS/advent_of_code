from typing import List

list_of_directions = []

with open("day_2.txt", encoding="utf-8") as f:
    for line in f:
        list_of_directions.append(line.rstrip())


def calculate_coordinates_simple(directions) -> List[int]:
    """
    Apply directions to submarine coordinates, starting as [0, 0]
    Directions are "forward", "down" and "up".
    Where:
        "down X" decreases the vertical position by X units
        "up X" increases the vertical position by X units
        "forward X" increases the horizontal position by X units

    Eg. apply directions ["down 2", "up 1", "forward 2"]

     o - - -             - - - -           - - - -                - - - -
     - - - -  down 2 ->  - - - -  up 1 ->  o - - -  forward 2 ->  - - o -
     - - - -             o - - -           - - - -                - - - -
     [0, 0]              [0, -2]           [0, -1]                [2, -1]

    Args:
        directions (List[str]): list of directions

    Returns:
        list: resulting coordinates [x, y]
    """
    coordinates = [0, 0]

    if not directions:
        raise ValueError("Empty list of directions")

    for direction_tuple in directions:
        direction, number = direction_tuple.split()
        number = int(number)

        if direction == "forward":
            coordinates[0] += number
        elif direction == "down":
            coordinates[1] -= number
        elif direction == "up":
            coordinates[1] += number
        else:
            raise ValueError("Invalid direction")

    return coordinates


def calculate_coordinates_advanced(directions) -> List[int]:
    """
    Apply directions to submarine coordinates, starting as [0, 0, 0]
    Third value is "aim" with special consenquences to submarine movement.

    Directions are "forward", "down" and "up".
    Where:
        "down X" increases "aim" by X units
        "up X" decreases "aim" by X units
        "forward X"
            - increases the horizontal position by X units
            - decreases the vertical position by "aim" * X

    Eg. apply directions ["down 2", "up 1", "forward 2"]

     o - - -             o - - -           o - - -                - - - -
     - - - -  down 2 ->  - - - -  up 1 ->  - - - -  forward 2 ->  - - - -
     - - - -             - - - -           - - - -                - - o -
    [0, 0, 0]           [0, 0, 2]          [0, 0, 1]             [2, -2, 0]


    Args:
        directions (List[str]): list of directions

    Returns:
        list: resulting coordinates [x, y, z]
    """
    coordinates = [0, 0, 0]

    if not directions:
        raise ValueError("Empty list of directions")

    for direction_tuple in directions:
        direction, number = direction_tuple.split()
        number = int(number)

        if direction == "forward":
            # increases the horizontal position by X units
            coordinates[0] += number
            # decreases the vertical position by "aim" * X
            coordinates[1] -= coordinates[2] * number
        elif direction == "down":
            # increase "aim"
            coordinates[2] += number
        elif direction == "up":
            # decrease "aim"
            coordinates[2] -= number
        else:
            raise ValueError("Invalid direction")

    return coordinates


# part 1
x, y = calculate_coordinates_simple(list_of_directions)
print(x * abs(y))


# part 1
x, y, z = calculate_coordinates_advanced(list_of_directions)
print(x * abs(y))
