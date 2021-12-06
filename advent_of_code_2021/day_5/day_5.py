from typing import Tuple, List
from collections import Counter


def parse_data(file_name: str) -> List[List[Tuple[int, int]]]:
    """
    Read data from a file and save it into a nested list.
    Nested lists consists of two coordinates - 2 tuples, each with 2 digits.
    Eg. line 0,9 -> 5,9 will produce [ [ (0, 9), (5, 9) ] ]

    Args:
        file_name (str): name of file in folder / or absolute path

    Returns:
        List[List[Tuple[int, int]]]: a nested list of coordinates
    """
    list_of_coordinates: list = []

    with open(file_name, encoding="utf-8") as f:
        for line in f:
            el1, el2 = line.rstrip().split("->")
            el1 = tuple(map(int, el1.split(",")))
            el2 = tuple(map(int, el2.split(",")))
            list_of_coordinates.append([el1, el2])

    return list_of_coordinates


def go_through_coordinates(list_of_coordinates: list, part_2: bool) -> List:
    """
    In part 1: for every two boundaries in horizontal or vertical direction
    fill in coordinates between.

    In part 2: for every two boundaries fill in coordinates between.

    The list is being gradually stretched by those coordinates.

    Args:
        list_of_coordinates (list): a nested list of coordinates
        part_2 (bool): True if function is called to solve part 2

    Returns:
        stretched_list (list): list of coordinates as tuples
    """
    stretched_list: list = []
    for two_coordinates in list_of_coordinates:
        (x1, y1), (x2, y2) = two_coordinates
        if (y1 == y2) or (x1 == x2):
            stretched_list = stretch_in_row_or_column(stretched_list, two_coordinates)
        else:
            if part_2:
                stretched_list = stretch_in_diagonal(stretched_list, two_coordinates)
    return stretched_list


def stretch_in_diagonal(
    stretched_list: list, two_coordinates: tuple
) -> List[Tuple[int, int]]:
    """
    Update a list of coordinates by coordinates between two boundaries of a line.
    Form a line in diagonal direction.

    Args:
        stretched_list (list): list of coordinates as tuples
        two_coordinates (tuple): two boundaries (coordinates) of a line

    Returns:
        List[Tuple[int, int]]: updated list of coordinates
    """
    updated_stretched_list: list = stretched_list[::]
    (x1, y1), (x2, y2) = two_coordinates
    updated_stretched_list.extend(two_coordinates)
    difference = abs(x1 - x2)

    if x1 < x2 and y1 < y2:
        for n in range(1, difference):
            updated_stretched_list.append((x1 + n, y1 + n))

    elif x1 > x2 and y1 < y2:
        for n in range(1, difference):
            updated_stretched_list.append((x1 - n, y1 + n))

    elif x1 > x2 and y1 > y2:
        for n in range(1, difference):
            updated_stretched_list.append((x1 - n, y1 - n))

    elif x1 < x2 and y1 > y2:
        for n in range(1, difference):
            updated_stretched_list.append((x1 + n, y1 - n))

    return updated_stretched_list


def stretch_in_row_or_column(
    stretched_list: list, two_coordinates: tuple
) -> List[Tuple[int, int]]:
    """
    Update a list of coordinates by coordinates between two boundaries of a line.
    Form a line in horizontal or vertical direction.

    Args:
        stretched_list (list): list of coordinates as tuples
        two_coordinates (tuple): two boundaries (coordinates) of a line

    Returns:
        List[Tuple[int, int]]: updated list of coordinates
    """
    updated_stretched_list: list = stretched_list[::]
    (x1, y1), (x2, y2) = two_coordinates
    updated_stretched_list.extend(two_coordinates)
    # movement in row
    if y1 == y2 and (abs(x1 - x2) != 1):
        difference = x1 - x2
        if difference < 1:
            for n in range(1, abs(difference)):
                updated_stretched_list.append((x1 + n, y1))
        elif difference > 1:
            for n in range(1, abs(difference)):
                updated_stretched_list.append((x1 - n, y1))

    # movement in column
    elif x1 == x2 and (abs(y1 - y2) != 1):
        difference = y1 - y2
        if difference < 1:
            for n in range(1, abs(difference)):
                updated_stretched_list.append((x1, y1 + n))
        elif difference > 1:
            for n in range(1, abs(difference)):
                updated_stretched_list.append((x1, y1 - n))

    return updated_stretched_list


def count_overlaps(coordinates):
    """
    Count how many coordinates are present more than 1 time.

    Args:
        coordinates (list): list of coordinates as tuples

    Returns:
        int: number of overlaps
    """
    counter = Counter(coordinates)
    overlaps = 0

    for occurence in counter.values():
        if occurence > 1:
            overlaps += 1

    return overlaps


def main(file_name):
    list_of_coordinates = parse_data(file_name)

    coordinates_1 = go_through_coordinates(list_of_coordinates, part_2=False)
    coordinates_2 = go_through_coordinates(list_of_coordinates, part_2=True)

    result_1 = count_overlaps(coordinates_1)
    result_2 = count_overlaps(coordinates_2)

    return result_1, result_2


part_1, part_2 = main("day_5.txt")
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
