from typing import Tuple, List, Any


def parse_data(file_name: str) -> Tuple[List[int], List[List[Any]]]:
    """
    Read data from a file and save it to 2 variables:
    - list_of_draws is a list of integers (numbers to be drawn)
    - list_of_boards is a list of boards, each nested list is one row of a board

    Args:
        file_name (str): name of file in folder / or absolute path

    Returns:
        Tuple[List[int], List[List[Any]]]: (list_of_draws, boards_data)
    """
    with open(file_name, encoding="utf-8") as f:
        lines = f.readlines()

        # make a list of draws
        list_of_draws = list(map(int, lines[0].rstrip().split(",")))

        # make a nested list of boards' numbers
        list_of_boards = []
        one_board_data: list = []
        for line in lines[2:]:
            if line == "\n":
                list_of_boards.append(one_board_data)
                one_board_data = []
            else:
                one_row = line.rstrip().split()
                one_row = list(map(int, one_row))
                one_board_data.append(one_row)
        # append last board
        list_of_boards.append(one_board_data)

    return list_of_draws, list_of_boards


class Board:
    """
    Every board starts as a list, where an each nested list represents one row.
    A "board" variable can eg. look like:
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ]
    """

    def __init__(self, one_board_data: list):
        self.marked: list = []
        self.all_numbers = []
        self.board = one_board_data

        for row in self.board:
            for number in row:
                self.all_numbers.append(number)

    def mark_number(self, number: int, position: tuple) -> None:
        """
        Mark drawn number in list "board"
        Marked number will be transformed into tuple, with 'd' as second element
        Eg. to mark 9 in row [21, 9, 14] will modify board to [21, (9, 'd'), 14]
        Also add drawn number into a list "marked"

        Args:
            number (int): number which has been drawn
            position (tuple): number of row and position in list "board"
        """
        row, column = position
        self.board[row][column] = (number, "d")
        self.marked.append(number)

    def find_number_to_mark(self, drawn_number: int) -> None:
        """
        Search board for a drawn number.
        If there is any, mark it with a method mark_number()

        Args:
            drawn_number (int): number which have been drawn
        """
        for index_row, row in enumerate(self.board):
            for index_column, number in enumerate(row):
                if drawn_number == number:
                    self.mark_number(drawn_number, (index_row, index_column))
                    return

    def has_won(self):
        """
        Determine if board have won "bingo" in one of the rows or columns.
        That means all numbers in specific row or column have been marked.

        Returns:
            bool: True/False
        """
        # win in row
        count_marks = 0
        marks_to_win = len(self.board)

        for row in self.board:
            for el in row:
                if type(el) != int:
                    count_marks += 1
            if count_marks == marks_to_win:
                return True
            count_marks = 0

        # win in column
        count_marks = 0
        marks_to_win = len(self.board[0])
        for position in range(len(self.board[0])):
            for row_number in range(len(self.board)):
                if type(self.board[row_number][position]) != int:
                    count_marks += 1
            if count_marks == marks_to_win:
                return True
            count_marks = 0

        return False

    def calculate_score(self, last_number_drawn: int):
        """
        Calculate score of board, sum all unmarked numbers and multiply by
        last number drawn.

        Args:
            last_number_drawn (int): last number drawn

        Returns:
            int: score of board
        """
        unmarked = list(set(self.all_numbers) - set(self.marked))
        sum_unmarked = sum(unmarked)
        return sum_unmarked * last_number_drawn


def apply_one_round(winning: list, game_boards: list, drawn_number: int):
    remaining_boards = game_boards[::]

    for board in game_boards:
        board.find_number_to_mark(drawn_number)
        if board.has_won():
            winning.append(board.calculate_score(drawn_number))
            remaining_boards.remove(board)

    return winning, remaining_boards


def main(file_name: str):
    list_of_draws, list_of_boards = parse_data(file_name)
    game_boards: list = []
    winning: list = []

    for board_data in list_of_boards:
        game_boards.append(Board(board_data))

    for drawn_number in list_of_draws:
        winning, game_boards = apply_one_round(winning, game_boards, drawn_number)

    return winning[0], winning[-1]


# part 1 + 2
part_1, part_2 = main("day_4.txt")
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
