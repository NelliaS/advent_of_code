from day_5 import (
    parse_data,
    count_overlaps,
    main,
    go_through_coordinates,
)


def test_parse_data() -> None:
    list_of_coordinates = [
        [(0, 9), (5, 9)],
        [(8, 0), (0, 8)],
        [(9, 4), (3, 4)],
        [(2, 2), (2, 1)],
        [(7, 0), (7, 4)],
        [(6, 4), (2, 0)],
        [(0, 9), (2, 9)],
        [(3, 4), (1, 4)],
        [(0, 0), (8, 8)],
        [(5, 5), (8, 2)],
    ]
    assert parse_data("day_5_test.txt") == list_of_coordinates


def test_go_through_coordinates_horizontal_and_vertical() -> None:
    coordinates_row = [
        [(0, 9), (5, 9)],
        [(9, 4), (5, 4)],
        [(0, 9), (2, 9)],
        [(1, 6), (1, 7)]
    ]

    stretched_in_row = [
        (0, 9), (5, 9), (1, 9), (2, 9), (3, 9), (4, 9),
        (9, 4), (5, 4), (8, 4), (7, 4), (6, 4),
        (0, 9), (2, 9), (1, 9),
        (1, 6), (1, 7)
    ]

    coordinates_column = [
        [(3, 5), (3, 2)],
        [(7, 0), (7, 4)],
        [(0, 0), (0, 3)],
        [(2, 2), (2, 1)],
    ]

    stretched_in_column = [
        (3, 5), (3, 2), (3, 4), (3, 3),
        (7, 0), (7, 4), (7, 1), (7, 2), (7, 3),
        (0, 0), (0, 3), (0, 1), (0, 2),
        (2, 2), (2, 1)
    ]

    # stretch in row
    assert go_through_coordinates(coordinates_row, part_2=False) == stretched_in_row

    # stretch in column
    assert go_through_coordinates(coordinates_column, part_2=False) == stretched_in_column


def test_go_through_coordinates_diagonal() -> None:
    # x1 < x2 |+| y1 < y2 |+|
    assert go_through_coordinates([[(1, 1), (3, 3)]], part_2=True) == [
        (1, 1), (3, 3), (2, 2)
        ]

    # x1 > x2 |-| y1 < y2 |+|
    assert go_through_coordinates([[(9, 7), (7, 9)]], part_2=True) == [
        (9, 7), (7, 9), (8, 8)
        ]

    # x1 > x2 |-| y1 > y2 |-|
    assert go_through_coordinates([[(6, 4), (2, 0)]], part_2=True) == [
        (6, 4), (2, 0), (5, 3), (4, 2), (3, 1)
        ]

    # x1 < x2 |+| y1 > y2 |-|
    assert go_through_coordinates([[(3, 4), (5, 2)]], part_2=True) == [
        (3, 4), (5, 2), (4, 3)
        ]


def test_count_overlaps():
    coordinates = [
        (0, 9), (0, 9), (0, 0), (0, 0), (5, 9), (5, 9), (5, 9), (5, 9),
        (1, 7), (1, 7), (3, 5),
        ]
    assert count_overlaps(coordinates) == 4


def test_example_part1():
    part_1, _ = main('day_5_test.txt')
    assert part_1 == 5


def test_example_part2():
    _, part_2 = main('day_5_test.txt')
    assert part_2 == 12
