from pytest import mark, raises
from day_1 import (
    count_number_of_sequent_increases,
    count_number_of_sequent_increases_of_triplets,
)

def test_count_number_of_sequent_increases_value_error() -> None:
    with raises(ValueError):
        assert count_number_of_sequent_increases([1])
    with raises(ValueError):
        assert count_number_of_sequent_increases([])


@mark.parametrize(
    ["measurements", "increase"],
    [
        ([1, 2, 3], 2),
        ([7, 6, 2], 0),
        ([1, 2, 3, 4, 5, 6, 7], 6),
        ([1, 2, 1, 2, 1, 2], 3),
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7),
    ],
)
def test_count_number_of_sequent_increases(measurements, increase) -> None:
    assert count_number_of_sequent_increases(measurements) == increase


def test_count_number_of_sequent_increases_of_triplets_value_error() -> None:
    with raises(ValueError):
        assert count_number_of_sequent_increases_of_triplets([])
    with raises(ValueError):
        assert count_number_of_sequent_increases_of_triplets([1, 2, 4])
    with raises(ValueError):
        assert count_number_of_sequent_increases_of_triplets([1, 2, 3, 4, 5])


@mark.parametrize(
    ["measurements", "increase"],
    [
        ([1, 2, 3, 4, 5, 6, 7], 4),
        ([6, 5, 4, 3, 2, 1], 0),
        ([1, 2, 1, 41, 20, 6, 3], 3),
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5),
    ],
)
def test_count_number_of_sequent_increases_of_triplets(
    measurements,
    increase
) -> None:
    assert count_number_of_sequent_increases_of_triplets(measurements) == increase
