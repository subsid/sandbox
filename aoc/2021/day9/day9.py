from typing import List
import heapq
import math


def get_input(mock) -> List[List[int]]:
    mock_input = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]

    return [
        [int(line[i]) for i in range(len(line.strip()))]
        for line in (mock_input if mock else open("./input.txt", "r"))
    ]


def is_min(i, j, grid):
    return all(
        [
            grid[i][j] < grid[n_i][n_j]
            for n_i, n_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            if n_i >= 0 and n_i < len(grid) and n_j >= 0 and n_j < len(grid[0])
        ]
    )


def find_basin_points(i, j, grid):
    points = set([(i, j)])
    explored = set()
    start_nodes = [(i, j)]
    valid = lambda i, j: i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

    while len(start_nodes) > 0:
        c_i, c_j = start_nodes.pop()
        if (c_i, c_j) not in explored:
            c_val = grid[c_i][c_j]
            if c_val == 9:
                continue

            for n_i, n_j in [
                (c_i - 1, c_j),
                (c_i + 1, c_j),
                (c_i, c_j - 1),
                (c_i, c_j + 1),
            ]:
                if valid(n_i, n_j):
                    n_val = grid[n_i][n_j]
                    if (n_i, n_j) not in explored and n_val != 9 and n_val > c_val:
                        points.add((n_i, n_j))
                        start_nodes.append((n_i, n_j))

            explored.add((c_i, c_j))

    return points


def part1(grid: List[List[int]]):
    return sum(
        [
            grid[i][j] + 1
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if is_min(i, j, grid)
        ]
    )


def part2(grid: List[List[int]]):
    basin_sizes = []

    min_points = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if is_min(i, j, grid)
    ]

    for i, j in min_points:
        points = find_basin_points(i, j, grid)
        if len(points) > 0:
            heapq.heappush(basin_sizes, len(points))

    return math.prod(heapq.nlargest(3, basin_sizes))


if __name__ == "__main__":
    assert part1(get_input(mock=True)) == 15
    assert part2(get_input(mock=True)) == 1134
    print(f"Risk sum part1: {part1(get_input(mock=False))}")
    print(f"Top 3 basins part2: {part2(get_input(mock=False))}")
