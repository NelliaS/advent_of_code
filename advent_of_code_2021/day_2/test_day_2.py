from pytest import mark, raises
from day_2 import calculate_coordinates_simple, calculate_coordinates_advanced


@mark.parametrize(
    ["directions", "resulting_coordinates"],
    [
        (
            ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"],
            [15, -10],
        ),
        (["forward 1", "down 5"], [1, -5]),
        (["down 3", "up 1", "forward 1"], [1, -2]),
        (["down 4", "forward 2", "up 3"], [2, -1]),
        (["forward 1000", "down 50"], [1000, -50]),
    ],
)
def test_calculate_coordinates_simple(directions, resulting_coordinates) -> None:
    assert calculate_coordinates_simple(directions) == resulting_coordinates


def test_calculate_coordinates_simple_value_errors() -> None:
    with raises(ValueError):
        assert calculate_coordinates_simple([])
    with raises(ValueError):
        assert calculate_coordinates_simple([""])
    with raises(ValueError):
        assert calculate_coordinates_simple(["foo 5"])


@mark.parametrize(
    ["directions", "resulting_coordinates"],
    [
        (
            ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"],
            [15, -60, 10],
        ),
        (["forward 1", "down 5"], [1, 0, 5]),
        (["down 3", "up 1", "forward 1"], [1, -2, 2]),
        (["down 4", "forward 2", "up 3"], [2, -8, 1]),
        (["forward 1000", "down 50"], [1000, 0, 50]),
    ],
)
def test_calculate_coordinates_advanced(directions, resulting_coordinates) -> None:
    assert calculate_coordinates_advanced(directions) == resulting_coordinates


def test_calculate_coordinates_advanced_value_errors() -> None:
    with raises(ValueError):
        assert calculate_coordinates_advanced([])
    with raises(ValueError):
        assert calculate_coordinates_advanced([""])
    with raises(ValueError):
        assert calculate_coordinates_advanced(["foo 5"])
