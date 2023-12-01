from typing import Iterator
from collections import deque
from functools import reduce


def get_measurements() -> Iterator[int]:
    return map(int, open("./input.txt", "r"))


def window_sum(window_size, vals) -> Iterator[int]:
    window = deque()
    running_sum = 0

    for v in vals:
        window.append(v)
        running_sum += v
        if len(window) == window_size:
            yield running_sum
            left_val = window.popleft()
            running_sum -= left_val


def update_acc(acc, v):
    (prev, count) = acc
    return (v, count + 1 if v - prev > 0 else count)


def part1(measurements):
    return reduce(update_acc, window_sum(1, measurements), (next(measurements), 0))[1]


def part2(measurements):
    return reduce(update_acc, window_sum(3, measurements), (next(measurements), 0))[1]


if __name__ == "__main__":
    assert part1(iter([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])) == 7
    assert part2(iter([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])) == 5
    print(f"Part1: {part1(get_measurements())}")
    print(f"Part2: {part2(get_measurements())}")
