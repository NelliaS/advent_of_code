from pytest import mark
from day_11 import parse, identify_neighbours, complete_one_round, main

test_energy_levels = {
    (0, 0): 5, (0, 1): 4, (0, 2): 8, (0, 3): 3, (0, 4): 1, (0, 5): 4,
    (0, 6): 3, (0, 7): 2, (0, 8): 2, (0, 9): 3, (1, 0): 2, (1, 1): 7, 
    (1, 2): 4, (1, 3): 5, (1, 4): 8, (1, 5): 5, (1, 6): 4, (1, 7): 7, 
    (1, 8): 1, (1, 9): 1, (2, 0): 5, (2, 1): 2, (2, 2): 6, (2, 3): 4, 
    (2, 4): 5, (2, 5): 5, (2, 6): 6, (2, 7): 1, (2, 8): 7, (2, 9): 3, 
    (3, 0): 6, (3, 1): 1, (3, 2): 4, (3, 3): 1, (3, 4): 3, (3, 5): 3, 
    (3, 6): 6, (3, 7): 1, (3, 8): 4, (3, 9): 6, (4, 0): 6, (4, 1): 3, 
    (4, 2): 5, (4, 3): 7, (4, 4): 3, (4, 5): 8, (4, 6): 5, (4, 7): 4, 
    (4, 8): 7, (4, 9): 8, (5, 0): 4, (5, 1): 1, (5, 2): 6, (5, 3): 7, 
    (5, 4): 5, (5, 5): 2, (5, 6): 4, (5, 7): 6, (5, 8): 4, (5, 9): 5, 
    (6, 0): 2, (6, 1): 1, (6, 2): 7, (6, 3): 6, (6, 4): 8, (6, 5): 4, 
    (6, 6): 1, (6, 7): 7, (6, 8): 2, (6, 9): 1, (7, 0): 6, (7, 1): 8, 
    (7, 2): 8, (7, 3): 2, (7, 4): 8, (7, 5): 8, (7, 6): 1, (7, 7): 1, 
    (7, 8): 3, (7, 9): 4, (8, 0): 4, (8, 1): 8, (8, 2): 4, (8, 3): 6, 
    (8, 4): 8, (8, 5): 4, (8, 6): 8, (8, 7): 5, (8, 8): 5, (8, 9): 4, 
    (9, 0): 5, (9, 1): 2, (9, 2): 8, (9, 3): 3, (9, 4): 7, (9, 5): 5, 
    (9, 6): 1, (9, 7): 5, (9, 8): 2, (9, 9): 6}


def test_parse() -> None:
    assert parse("day_11_test.txt") == test_energy_levels


@mark.parametrize(
    ["central_position", "area_size", "adjacent_positions"],
    [
        ((4, 9), (10, 10), [(3, 9), (5, 9), (4, 8), (5, 8), (3, 8)]),
        (
            (1, 5),
            (10, 10),
            [(0, 5), (2, 5), (1, 6), (1, 4), (0, 6), (2, 6), (2, 4), (0, 4)],
        ),
        (
            (2, 7),
            (10, 10),
            [(1, 7), (3, 7), (2, 8), (2, 6), (1, 8), (3, 8), (3, 6), (1, 6)],
        ),
    ],
)
def test_identify_neighbours(central_position, area_size, adjacent_positions) -> None:
    assert identify_neighbours(central_position, area_size) == adjacent_positions


@mark.parametrize(
    ["energy_levels", "count_flashes", "area_size", "result"],
    [
        (
            parse("day_11_test.txt"),
            0,
            (10, 10),
            (parse("day_11_test_1_round.txt"), 0, False),
        ),
        (
            parse("day_11_test_1_round.txt"),
            0,
            (10, 10),
            (parse("day_11_test_2_round.txt"), 35, False),
        ),
        (
            parse("day_11_test_2_round.txt"),
            35,
            (10, 10),
            (parse("day_11_test_3_round.txt"), 80, False),
        ),
        (
            parse("day_11_test_3_round.txt"),
            80,
            (10, 10),
            (parse("day_11_test_4_round.txt"), 96, False),
        ),
        (
            parse("day_11_test_4_round.txt"),
            97,
            (10, 10),
            (parse("day_11_test_5_round.txt"), 105, False),
        ),
    ],
)
def test_complete_one_round(energy_levels, count_flashes, area_size, result) -> None:
    assert complete_one_round(energy_levels, count_flashes, area_size) == result


def test_main() -> None:
    assert main("day_11_test.txt", (10, 10), 10) == (204, 195)
    assert main("day_11_test.txt", (10, 10), 100) == (1656, 195)
