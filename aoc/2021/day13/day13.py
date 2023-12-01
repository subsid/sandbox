from typing import List, Tuple, Set, Dict
from matplotlib import pyplot as plt


def get_input(mock=False):
    mock_input = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".strip().split(
        "\n"
    )

    return mock_input if mock else open("./input.txt", "r").readlines()


def parse_input(lines):
    grid = set()
    folds = []
    max_y = 0
    max_x = 0
    for line in lines:
        if line.strip().startswith("fold along"):
            axis, v = line.strip().replace("fold along ", "").split("=")
            folds.append([axis, int(v)])

        elif line.strip() != "":
            x, y = tuple(map(int, line.strip().split(",")))
            max_x = max(x, max_x)
            max_y = max(y, max_y)

            grid.add(tuple((x, y)))

    return grid, folds


def fold_axis(axis, val, grid):
    # Horizontal fold
    if axis == "y":
        return set({k if k[1] < val else (k[0], val - (k[1] - val)) for k in grid})
    # Vertical fold
    else:
        return set({k if k[0] < val else (val - (k[0] - val), k[1]) for k in grid})

def plot_grid(grid):
    plt.scatter(*zip(*grid), marker='s')
    plt.axis('equal')
    plt.gca().invert_yaxis()
    plt.show()

def part1(grid: Set[Tuple[int, int]], folds: List[Tuple[str, int]]):
    for coord, val in folds[:1]:
        grid = fold_axis(coord, val, grid)

    return len(grid)


def part2(grid: Set[Tuple[int, int]], folds: List[Tuple[str, int]]):
    for coord, val in folds:
        grid = fold_axis(coord, val, grid)

    plot_grid(grid)

    return len(grid)


if __name__ == "__main__":
    assert part1(*parse_input(get_input(mock=True))) == 17
    # part2(*parse_input(get_input(mock=True)))
    print(f"Dots after first fold: {part1(*parse_input(get_input(mock=False)))}")
    part2(*parse_input(get_input(mock=False)))
