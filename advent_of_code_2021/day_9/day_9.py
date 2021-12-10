from typing import List, Any, Tuple
from functools import reduce


def parse(file_name: str) -> List[Any]:
    area = []
    with open(file_name) as f:
        for line in f:
            area.append(list(map(int, list(line.rstrip()))))
    return area


def determine_lowest_points(area: List[Any]) -> Tuple[List[int], List[Any]]:
    lowest_numbers = []
    lowest_numbers_positions = []
    area_width = len(area[0])
    area_height = len(area)

    for x, row in enumerate(area):
        for y, number in enumerate(row):
            if is_lowest(number, area, area_width, area_height, [x, y]):
                lowest_numbers.append(number)
                lowest_numbers_positions.append([x, y])

    return lowest_numbers, lowest_numbers_positions


def determine_adjacent_positions(
    position_of_number: List[int], area_height: int, area_width: int
) -> List[Any]:
    adjacent_positions = []

    x, y = position_of_number
    adjacent_positions_variants = [
        [x - 1, y],
        [x + 1, y],
        [x, y + 1],
        [x, y - 1],
    ]

    for position in adjacent_positions_variants:
        x, y = position
        if x >= 0 and y >= 0:
            if x <= (area_height - 1) and y <= (area_width - 1):
                adjacent_positions.append(position)

    return adjacent_positions


def is_lowest(
    number: int,
    area: List[int],
    area_width: int,
    area_height: int,
    position_of_number: List[int],
) -> bool:

    adjacent_positions = determine_adjacent_positions(
        position_of_number, area_height, area_width
    )
    adjacent_numbers = []

    for position in adjacent_positions:
        tested_x, tested_y = position
        adjacent_numbers.append(area[tested_x][tested_y])

    for adjacent_number in adjacent_numbers:
        if adjacent_number <= number:
            return False
    return True


def count_basin(
    area: List[Any], position_of_number: List[int], area_height: int, area_width: int
) -> int:
    basin_size = 0
    adjacent_positions = [position_of_number]

    while len(adjacent_positions) >= 1:
        position = adjacent_positions.pop()
        x, y = position
        if area[x][y] < 9:
            basin_size += 1
            adjacent_positions.extend(
                determine_adjacent_positions(position, area_height, area_width)
            )
            area[x][y] = 9

    return basin_size


def three_biggest_basins(
    area: List[Any], lowest_numbers_positions: List[Any]
) -> List[int]:
    area_width = len(area[0])
    area_height = len(area)
    size_all_basins = []

    for position in lowest_numbers_positions:
        basin_size = count_basin(area, position, area_height, area_width)
        size_all_basins.append(basin_size)

    size_all_basins.sort(reverse=True)

    return size_all_basins[:3]


def main(file_name) -> Tuple[int, int]:
    area = parse(file_name)
    lowest_numbers, lowest_numbers_positions = determine_lowest_points(area)
    part_1 = sum(lowest_numbers) + len(lowest_numbers)

    size_basins = three_biggest_basins(area, lowest_numbers_positions)
    part_2 = reduce(lambda x, y: x * y, size_basins)
    return part_1, part_2


part_1, part_2 = main("day_9.txt")
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
