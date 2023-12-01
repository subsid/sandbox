from collections import Counter
from functools import lru_cache
from itertools import chain


def get_input(mock=False):
    mock_input = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip().split(
        "\n"
    )
    return mock_input if mock else open("./input.txt", "r").readlines()


def parse_input(lines):
    initial = lines[0].strip()
    mapping = dict([map(lambda x: x.strip(), line.split("->")) for line in lines[2:]])

    return (initial, mapping)


def pair_counts(initial, mapping, steps):
    counts = Counter(map(lambda x: x[0] + x[1], zip(initial, initial[1:])))

    for _ in range(steps):
        new_counts = Counter()
        for pair, v in counts.items():
            start_pair = pair[0] + mapping["".join(pair)]
            end_pair = mapping["".join(pair)] + pair[1]
            new_counts[start_pair] += v
            new_counts[end_pair] += v

        counts = new_counts

    return counts


def part1(initial, mapping, steps):
    char_counter = Counter()
    end_char = initial[-1]

    counts = pair_counts(initial, mapping, steps)
    # Count only first element to avoid double counting
    for k, v in counts.items():
        char_counter[k[0]] += v

    # Add in last element
    char_counter[end_char] += 1
    char_counts = char_counter.most_common()

    return char_counts[0][1] - char_counts[-1][1]


# def part2(initial):

if __name__ == "__main__":
    assert part1(*parse_input(get_input(mock=True)), 10) == 1588
    assert part1(*parse_input(get_input(mock=True)), 40) == 2188189693529
    print(f"Part 1: {part1(*parse_input(get_input(mock=False)), 10)}")
    print(f"Part 2: {part1(*parse_input(get_input(mock=False)), 40)}")
