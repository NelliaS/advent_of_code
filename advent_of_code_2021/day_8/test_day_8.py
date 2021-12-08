from pytest import mark
from day_8 import (
    parse,
    count_1_4_7_8,
    count_output,
    determine_1_4_7_8,
    decode_signals,
    main,
)


def test_parse_data() -> None:
    parsed_data = parse("day_8_test.txt")
    assert parsed_data[0] == [
        [
            "be",
            "cfbegad",
            "cbdgef",
            "fgaecd",
            "cgeb",
            "fdcge",
            "agebfd",
            "fecdb",
            "fabcd",
            "edb",
        ],
        ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
    ]


def test_count_1_4_7_8() -> None:
    assert count_1_4_7_8(parse("day_8_test.txt")) == 26


@mark.parametrize(
    ["signals", "corresponding"],
    [
        (
            [
                "acedgfb",
                "cdfbe",
                "gcdfa",
                "fbcad",
                "dab",
                "cefabd",
                "cdfgeb",
                "eafb",
                "cagedb",
                "ab",
            ],
            {1: "ab", 4: "abef", 7: "abd", 8: "abcdefg"},
        ),
        (
            [
                "abc",
                "dabc",
                "ba",
                "gabcdef",
            ],
            {8: "abcdefg", 7: "abc", 4: "abcd", 1: "ab"},
        ),
        (
            [
                "bae",
                "ecfd",
                "ga",
                "abcdefg",
            ],
            {8: "abcdefg", 7: "abe", 4: "cdef", 1: "ag"},
        ),
    ],
)
def test_determine_1_4_7_8(signals, corresponding) -> None:
    assert determine_1_4_7_8(signals) == corresponding


@mark.parametrize(
    ["signals", "output_tuple"],
    [
        (
            [
                [
                    "acedgfb",
                    "cdfbe",
                    "gcdfa",
                    "fbcad",
                    "dab",
                    "cefabd",
                    "cdfgeb",
                    "eafb",
                    "cagedb",
                    "ab",
                ],
                ["cdfeb", "fcadb", "cdfeb", "cdbaf"],
            ],
            (
                ["cdfeb", "fcadb", "cdfeb", "cdbaf"],
                {
                    8: "abcdefg",
                    7: "abd",
                    4: "abef",
                    1: "ab",
                    5: "bcdef",
                    2: "acdfg",
                    3: "abcdf",
                    9: "abcdef",
                    6: "bcdefg",
                    0: "abcdeg",
                },
            ),
        ),
    ],
)
def test_decode_signals(signals, output_tuple) -> None:
    assert decode_signals(signals) == output_tuple


@mark.parametrize(
    ["output_signals", "decoded", "result"],
    [
        (
            ["cdfeb", "fcadb", "cdfeb", "cdbaf"],
            {
                8: "acedgfb",
                7: "dab",
                4: "eafb",
                1: "ab",
                5: "bcdef",
                2: "acdfg",
                3: "abcdf",
                9: "abcdef",
                6: "bcdefg",
                0: "abcdeg",
            },
            5353,
        )
    ],
)
def test_count_output(output_signals, decoded, result) -> None:
    assert count_output(output_signals, decoded) == result


def test_main() -> None:
    list_of_signals = parse("day_8_test.txt")
    assert main(list_of_signals) == 61229
