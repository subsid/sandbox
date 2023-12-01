from typing import Tuple, Generator


def get_measurements() -> Generator[Tuple[str, int], None, None]:
    # mock = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    with open("./input.txt") as f:
        # for line in mock:
        for line in f:
            v = line.strip().split(" ")

            yield (v[0], int(v[1]))


def part1(measurements):
    d, h_pos = 0, 0

    for cmd, v in measurements:
        if cmd == "up":
            d -= v
        elif cmd == "down":
            d += v
        elif cmd == "forward":
            h_pos += v
        else:
            raise ValueError("Unexpected cmd {cmd}")

    return (h_pos, d, h_pos * d)


def part2(measurements):
    route, d, aim, h_pos = measurements, 0, 0, 0

    for cmd, v in route:
        if cmd == "up":
            aim -= v
        elif cmd == "down":
            aim += v
        elif cmd == "forward":
            h_pos += v
            d = d + (aim * v)
        else:
            raise ValueError("Unexpected cmd {cmd}")

    return (h_pos, d, d * h_pos)


if __name__ == "__main__":
    assert (
        part1(
            [
                ("forward", 5),
                ("down", 5),
                ("forward", 8),
                ("up", 3),
                ("down", 8),
                ("forward", 2),
            ]
        )
        == (15, 10, 150)
    )
    assert (
        part2(
            [
                ("forward", 5),
                ("down", 5),
                ("forward", 8),
                ("up", 3),
                ("down", 8),
                ("forward", 2),
            ]
        )
        == (15, 60, 900)
    )
    print(f"Part1: {part1(get_measurements())}")
    print(f"Part2: {part2(get_measurements())}")
