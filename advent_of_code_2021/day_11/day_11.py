from typing import List, Dict, Tuple


def parse(file_name: str) -> Dict[Tuple[int, int], int]:
    energy_levels = {}
    with open(file_name) as f:
        for x, line in enumerate(f):
            for y, el in enumerate(line.rstrip()):
                energy_levels.setdefault((x, y), int(el))
    return energy_levels


def identify_neighbours(
    central_position: tuple, area_size: tuple
) -> List[Tuple[int, int]]:
    adjacent_positions = []

    max_x, max_y = area_size

    x, y = central_position
    adjacent_positions_variants = [
        (x - 1, y),
        (x + 1, y),
        (x, y + 1),
        (x, y - 1),
        (x - 1, y + 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y - 1),
    ]

    for position in adjacent_positions_variants:
        x, y = position
        if x >= 0 and y >= 0:
            if x <= (max_x - 1) and y <= (max_y - 1):
                adjacent_positions.append(position)
    return adjacent_positions


def complete_one_round(
    energy_levels: dict, count_flashes: int, area_size: tuple
) -> Tuple[Dict[Tuple[int, int], int], int, bool]:
    flashed_this_round = []
    flashed_positions = []

    # firstly increment values by 1
    for position, octopus_energy in energy_levels.items():
        energy_levels[position] += 1

    # save all positions, where value is > 9
    for position, octopus_energy in energy_levels.items():
        if octopus_energy > 9:
            flashed_positions.append(position)
            flashed_this_round.append(position)

    # while there are neighbours to be flashed, continue
    while flashed_positions:
        new_flashed_positions = []
        # for every flashed position, increment neighbours
        for position in flashed_positions:
            neighbours = identify_neighbours(position, area_size)

            for neighbour in neighbours:
                energy_levels[neighbour] += 1
                # when value > 9, save it to newly flashed position
                if (
                    energy_levels[neighbour] > 9
                    and neighbour not in flashed_this_round
                    and neighbour not in new_flashed_positions
                ):
                    new_flashed_positions.append(neighbour)
                    flashed_this_round.append(neighbour)
        new_flashed_positions = list(set(new_flashed_positions))
        flashed_positions = new_flashed_positions

    # finally count all flashed octopuses and reset them to 0
    for position, octopus_energy in energy_levels.items():
        if octopus_energy > 9:
            energy_levels[position] = 0
            count_flashes += 1

    # check for synchronization
    for value in energy_levels.values():
        if value != 0:
            synchronized = False
            break
        synchronized = True

    return energy_levels, count_flashes, synchronized


def main(file_name: str, area_size: tuple, max_rounds: int) -> Tuple[int, int]:
    energy_levels = parse(file_name)
    count_flashes = 0
    synchronized = False
    rounds = 0
    while not synchronized:
        rounds += 1
        energy_levels, count_flashes, synchronized = complete_one_round(
            energy_levels, count_flashes, area_size
        )
        if rounds == max_rounds:
            part_1 = count_flashes

    part_2 = rounds
    return part_1, rounds


part_1, part_2 = main("day_11.txt", (10, 10), 100)
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
