from pytest import mark, raises
from day_3 import (
    count_vertically_most_common_bits,
    count_gamma_and_epsilon_rate,
    compare_numbers,
    filter_list,
)

numbers = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

bits_in_lines = {
    0: {"0": 5, "1": 7},
    1: {"0": 7, "1": 5},
    2: {"0": 4, "1": 8},
    3: {"0": 5, "1": 7},
    4: {"0": 7, "1": 5},
}


def test_count_vertically_most_common_bits() -> None:
    assert count_vertically_most_common_bits(numbers) == bits_in_lines


def test_count_gamma_and_epsilon_rate() -> None:
    assert count_gamma_and_epsilon_rate(bits_in_lines) == ("10110", "01001")


def test_compare_numbers() -> None:
    assert compare_numbers(8, 9, "most") == "1"
    assert compare_numbers(20, 9, "most") == "0"
    assert compare_numbers(20, 9, "least") == "1"
    assert compare_numbers(2, 9, "least") == "0"


def test_filter_list() -> None:
    assert filter_list(numbers, bits_in_lines, "most") == "10111"
    assert filter_list(numbers, bits_in_lines, "least") == "01010"
