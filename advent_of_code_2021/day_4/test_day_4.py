from day_4 import parse_data, Board, main


def test_parse_data() -> None:
    list_of_draws = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 
                     13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1
                    ]
    boards_data = [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    ]
    assert parse_data("day_4_test.txt") == (list_of_draws, boards_data)


def test_Board_mark_number() -> None:
    board = Board([[22, 13, 17], [8, 2, 23], [21, 9, 14]])
    board.mark_number(2, (1, 1))
    assert board.board == [[22, 13, 17], [8, (2, "d"), 23], [21, 9, 14]]
    assert board.marked == [2]


def test_Board_has_won_row() -> None:
    board = Board(
        [[22, (13, "d"), 17], [8, (2, "d"), 23], [(21, "d"), (9, "d"), (14, "d")]]
    )
    assert board.has_won() == True
    board = Board([[22, (13, "d"), 17], [8, (2, "d"), 23], [(21, "d"), 9, 14]])
    assert board.has_won() == False


def test_Board_has_won_column() -> None:
    board = Board([[22, 13, (17, "d")], [8, 2, (23, "d")], [21, 9, (14, "d")]])
    assert board.has_won() == True
    board = Board([[(22, "d"), 13, 17], [8, 2, (23, "d")], [21, 9, (14, "d")]])
    assert board.has_won() == False


def test_Board_calculate_score() -> None:
    board = Board([[22, 13, (17, "d")], [8, 2, (23, "d")], [21, 9, (14, "d")]])
    board.all_numbers = [22, 13, 17, 8, 2, 23, 21, 9, 14]
    board.marked = [17, 23, 14]
    assert board.calculate_score(14) == 1050


def test_Board_find_number_to_mark() -> None:
    board = Board([[22, 13, (17, "d")], [8, 2, 23]])
    board.find_number_to_mark(2)
    assert board.board == [[22, 13, (17, "d")], [8, (2, "d"), 23]]


def test_main() -> None:
    part_1, part_2 = main("day_4_test.txt")
    assert part_1 == 4512
    assert part_2 == 1924
