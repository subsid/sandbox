def get_input(mock=False):
    mock_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip().split("\n")

    for line in mock_input if mock else open("./input.txt", "r"):
        yield line.strip()

class Grid:
    def __init__(self, lines) -> None:
        self.n_rows = len(lines)
        self.n_cols = len(lines[0])
        self.grid = [[int(v) for v in line] for line in lines]

    def get(self, point):
        return self.grid[point[0]][point[1]]

    def neighbors(self, point):
        r, c = point
        return [ (n_r, n_c)
            for n_r, n_c in [(r, c-1), (r-1, c-1), (r-1, c), (r-1, c+1), (r, c+1), (r+1, c+1), (r+1, c), (r+1, c-1)]
            if all([n_r >= 0, n_r < self.n_rows, n_c >= 0, n_c < self.n_cols])]

    def increment(self):
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                self.grid[r][c] += 1

    def increment_points(self, points):
        for r, c in points:
            self.grid[r][c] += 1

    def drain_points(self, points):
        for r, c in points:
            self.grid[r][c] = 0

def flash_from_source(grid, point, flashed):
    start_nodes = [point]
    while (len(start_nodes) > 0):
        n_point = start_nodes.pop()

        if n_point not in flashed:
            if grid.get(n_point) > 9:
                flashed.add(n_point)
                neighbors = grid.neighbors(n_point)
                grid.increment_points(neighbors)
                start_nodes.extend(neighbors)

    return flashed

def flash_available(grid):
    flashed = set()

    for r in range(grid.n_rows):
        for c in range(grid.n_cols):
            flashed = flash_from_source(grid, (r, c), flashed)

    return flashed

def part1(lines, steps):
    grid = Grid(list(lines))
    num_flashes = 0

    for _ in range(steps):
        grid.increment()
        flashed = flash_available(grid)
        grid.drain_points(flashed)

        num_flashes += len(flashed)

    return num_flashes

def part2(lines, max_steps=10000):
    grid = Grid(list(lines))

    step = 0
    while(step < max_steps):
        step += 1
        grid.increment()
        flashed = flash_available(grid)
        # flashed = flash_due_to_adjacent(grid, flashed)
        grid.drain_points(flashed)

        if len(flashed) == (grid.n_rows * grid.n_cols):
            return step

    return 0

if __name__ == "__main__":
    assert part1(get_input(mock=True), 10) == 204
    assert part1(get_input(mock=True), 100) == 1656
    assert part2(get_input(mock=True)) == 195
    print(f"{part1(get_input(mock=False), 100)}")
    print(f"{part2(get_input(mock=False))}")
