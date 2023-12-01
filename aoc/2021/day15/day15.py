from math import inf
import heapq


def get_input(mock=False):
    mock_input = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip().split(
        "\n"
    )
    for line in mock_input if mock else open("./input.txt", "r"):
        yield line.strip()


class Grid:
    def __init__(self, lines, expanded=False):
        self.expand = 5 if expanded else 1
        self.grid = [[int(v) for v in line] for line in lines]
        self.n_rows = len(self.grid)
        self.n_cols = len(self.grid[0])
        self.size = self.n_rows * self.expand * self.n_cols * self.expand

    # Norvig trick
    def clock_mod(self, i, m):
        # Like a clock 24 % 12 is 12 instead of 0.
        return (i % m) or m

    def get(self, point):
        r, c = point[0] % self.n_rows, point[1] % self.n_cols
        extra_x = int(point[0] / self.n_rows)
        extra_y = int(point[1] / self.n_cols)

        return self.clock_mod(self.grid[r][c] + extra_x + extra_y, 9)

    def neighbors(self, point):
        r, c = point

        return [
            (i, j)
            for i, j in [(r, c - 1), (r - 1, c), (r, c + 1), (r + 1, c)]
            if i >= 0 and j >= 0 and i < (self.n_rows * self.expand) and j < (self.n_cols * self.expand)
        ]

    def __str__(self):
        return "\n".join([" ".join([str(c) for c in r]) for r in self.grid])


# Slowwww O(edges * nodes), but fun to implement.
def bellman_ford(grid):
    # True for graphs with no negative cycles
    max_path_len = (grid.n_rows * grid.n_cols) - 1
    path_lens = [
        [[inf for _ in range(grid.n_cols)] for _ in range(grid.n_rows)]
        for _ in range(max_path_len + 1)
    ]
    path_lens[0][0][0] = 0

    for i in range(1, max_path_len + 1):
        for r in range(grid.n_rows):
            for c in range(grid.n_cols):
                neighbors = grid.neighbors((r, c))
                path_lens[i][r][c] = min(
                    path_lens[i - 1][r][c],
                    *[
                        path_lens[i - 1][n_i][n_j] + grid.get((r, c))
                        for n_i, n_j in neighbors
                    ]
                )

    return path_lens


def dijkstra(grid):
    start = (0, 0)
    costs = {start: 0}
    frontier_heap = []
    explored = set(start)

    # Init heap with edges from start
    neighbors = grid.neighbors(start)
    for point in neighbors:
        costs[point] = costs[start] + grid.get(point)
        heapq.heappush(frontier_heap, (costs[start] + grid.get(point), point))

    while len(frontier_heap) > 0:
        cost, point = heapq.heappop(frontier_heap)
        explored.add(point)
        neighbors = [n for n in grid.neighbors(point)]

        for n_p in neighbors:
            if n_p not in explored:
                new_cost = cost + grid.get(n_p)
                if new_cost < costs.get(n_p, inf):
                    heapq.heappush(frontier_heap, (new_cost, n_p))
                    costs[n_p] = new_cost

    return costs

def part1(grid):
    # path_lens = bellman_ford(grid)

    # return path_lens[-1][-1][-1]
    costs = dijkstra(grid)

    return costs[((grid.n_rows * grid.expand) - 1, (grid.n_cols * grid.expand) - 1)]

if __name__ == "__main__":
    assert (result := part1(Grid(get_input(mock=True)))) == (expected := 40), f"Expected: {expected}, Got: {result}"
    assert (result := part1(Grid(get_input(mock=True), expanded=True))) == (expected := 315), f"Expected: {expected}, Got: {result}"

    print(f"Shortest path cost: {part1(Grid(get_input(mock=False)))}")
    print(f"Shortest path cost: {part1(Grid(get_input(mock=False), expanded=True))}")
