from typing import Tuple, List
import re


class Board:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n_row = len(grid)
        self.n_col = len(grid[0])
        self.marked = [[False for _ in range(self.n_col)] for _ in range(self.n_row)]

    def has_complete_row(self):
        for row in range(self.n_row):
            if all(self.marked[row]):
                return True
        return False

    def has_complete_col(self):
        for col in range(self.n_col):
            flag = True
            for row in range(self.n_row):
                if not self.marked[row][col]:
                    flag = False
                    break
            if flag:
                return True
        return False

    def update_marked(self, num):
        updated = False

        for row in range(self.n_row):
            for col in range(self.n_col):
                if self.grid[row][col] == num:
                    self.marked[row][col] = True
                    updated = True

        return updated

    def __str__(self) -> str:
        return (
            "\nGrid\n"
            + "\n".join(map(str, self.grid))
            + "\nMark\n"
            + "\n".join(map(str, self.marked))
        )

    def sum_unmarked(self):
        s = 0

        for row in range(self.n_row):
            for col in range(self.n_col):
                if not self.marked[row][col]:
                    s += self.grid[row][col]
        return s


def read_input(mock=False):
    mock_input = [
        "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n",
        "\n",
        "22 13 17 11  0\n",
        " 8  2 23  4 24\n",
        "21  9 14 16  7\n",
        " 6 10  3 18  5\n",
        " 1 12 20 15 19\n",
        "\n",
        " 3 15  0  2 22\n",
        " 9 18 13 17  5\n",
        "19  8  7 25 23\n",
        "20 11 10 24  4\n",
        "14 21 16 12  6\n",
        "\n",
        "14 21 17 24  4\n",
        "10 16 15  9 19\n",
        "18  8 23 26 20\n",
        "22 11 13  6  5\n",
        " 2  0 12  3  7",
    ]

    return mock_input if mock else open("./input.txt", "r")


def parse_input(read_input) -> Tuple[List[int], List[Board]]:
    boards: List[Board] = []
    numbers: List[int] = None

    grid: List[List[int]] = []
    for line in read_input:
        if numbers is None:
            # first line
            numbers = list(map(int, line.strip().split(",")))
        else:
            # Current board ends
            # Append it to result and start a new board.
            if line.startswith("\n"):
                if len(grid) != 0:
                    boards.append(Board(grid))
                    grid = []
            else:
                row = list(map(int, re.split(r"\s+", line.strip())))
                grid.append(row)
    # Add last board
    boards.append(Board(grid))

    return (numbers, boards)


def part1(numbers, boards: List[Board]):
    for num in numbers:
        for board in boards:
            updated = board.update_marked(num)
            # We have to check for winner only if there was an update
            if updated and (board.has_complete_col() or board.has_complete_row()):
                s = board.sum_unmarked()
                return (s, num, s * num)


def part2(numbers, boards: List[Board]):
    winning_boards = []
    winners = set()

    for num in numbers:
        for i, board in enumerate(boards):
            # Ignore boards that already won.
            if i in winners:
                continue
            updated = board.update_marked(num)
            # We have to check for winner only if there was an update
            if updated and (board.has_complete_col() or board.has_complete_row()):
                winning_boards.append((i, num))
                winners.add(i)

        # No need to continue with the winner checking. Everyone has won!
        if len(winning_boards) == len(boards):
            break

    i, num = winning_boards[-1]
    s = boards[i].sum_unmarked()
    return (s, num, s * num)


if __name__ == "__main__":
    assert part1(*parse_input(read_input(mock=True))) == (188, 24, 4512)
    assert part2(*parse_input(read_input(mock=True))) == (148, 13, 1924)
    print(f"sum, win_num, sum * win_num: {part1(*parse_input(read_input(mock=False)))}")
    print(f"sum, win_num, sum * win_num: {part2(*parse_input(read_input(mock=False)))}")
