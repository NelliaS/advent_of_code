from pytest import mark
from day_9 import (
    parse,
    determine_adjacent_positions,
    main,
    determine_lowest_points,
    is_lowest,
    count_basin,
)

test_area = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]


def test_parse() -> None:
    assert parse("day_9_test.txt") == test_area


@mark.parametrize(
    ["position_of_number", "height", "width", "adjacent_positions"],
    [
        ([4, 9], 5, 10, [[3, 9], [4, 8]]),
        ([0, 3], 5, 10, [[1, 3], [0, 4], [0, 2]]),
    ],
)
def test_determine_adjacent_positions(
    position_of_number, height, width, adjacent_positions
) -> None:
    assert (
        determine_adjacent_positions(position_of_number, height, width)
        == adjacent_positions
    )


@mark.parametrize(
    ["number", "area_width", "area_height", "position_of_number", "result"],
    [
        (5, 5, 10, [2, 2], True),
        (2, 5, 10, [0, 0], False),
        (9, 5, 10, [1, 1], False),
        (5, 5, 10, [4, 6], True),
    ],
)
def test_is_lowest(number, area_width, area_height, position_of_number, result) -> None:
    assert (
        is_lowest(number, test_area, area_width, area_height, position_of_number)
        == result
    )


def test_determine_lowest_points() -> None:
    assert determine_lowest_points(test_area) == (
        [1, 0, 5, 5],
        [[0, 1], [0, 9], [2, 2], [4, 6]],
    )


@mark.parametrize(
    ["position_of_number", "area_height", "area_width", "result"],
    [
        ([0, 1], 5, 10, 3),
        ([4, 6], 5, 10, 9),
    ],
)
def test_count_basin(position_of_number, area_height, area_width, result) -> None:
    assert count_basin(test_area, position_of_number, area_height, area_width) == result


def test_main() -> None:
    assert main("day_9_test.txt") == (15, 1134)
