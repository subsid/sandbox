from typing import List
from functools import lru_cache
from collections import Counter

def get_input(mock=False) -> List[int]:
    mock_input = [3, 4, 3, 1, 2]
    return mock_input if mock else list(map(int, open("./input.txt").readline().strip().split(",")))

def part1_topdown(initial_list, days):
    new_fish_timer = 8
    reset_timer = 6

    @lru_cache(maxsize=None)
    def memoized(timer, curr_days):
        if (curr_days < 0):
            return 0
        if (timer == -1):
            return 1 + memoized(new_fish_timer - 1, curr_days - 1) + memoized(reset_timer - 1, curr_days - 1)
        return memoized(timer - 1, curr_days - 1)

    result = 0
    for i in initial_list:
        result += 1 + memoized(i, days)

    return result

def part1_bottomup(initial_list, days):
    fish_counts = Counter(initial_list)

    for _ in range(days):
        fish_counts = Counter({timer - 1: v for timer, v in fish_counts.items()})

        # Births
        fish_counts[8] = fish_counts[-1]
        fish_counts[6] += fish_counts[-1]
        del fish_counts[-1]

    return sum(fish_counts.values())

if __name__ == "__main__":
    assert part1_bottomup(get_input(mock=True), 18) == 26
    assert part1_bottomup(get_input(mock=True), 80) == 5934
    assert part1_bottomup(get_input(mock=True), 256) == 26984457539
    assert part1_topdown(get_input(mock=True), 18) == 26
    assert part1_topdown(get_input(mock=True), 80) == 5934
    assert part1_topdown(get_input(mock=True), 256) == 26984457539
    print(f"Total fishes after 80 days: {part1_topdown(get_input(mock=False), 80)}")
    print(f"Total fishes after 256 days: {part1_topdown(get_input(mock=False), 256)}")

