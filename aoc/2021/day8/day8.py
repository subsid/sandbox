from typing import Set, Dict, Iterator
import itertools

##########################################
#     0:      1:      2:      3:      4:
#    aaaa    ....    aaaa    aaaa    ....
#   b    c  .    c  .    c  .    c  b    c
#   b    c  .    c  .    c  .    c  b    c
#    ....    ....    dddd    dddd    dddd
#   e    f  .    f  e    .  .    f  .    f
#   e    f  .    f  e    .  .    f  .    f
#    gggg    ....    gggg    gggg    ....
#
#     5:      6:      7:      8:      9:
#    aaaa    aaaa    aaaa    aaaa    aaaa
#   b    .  b    .  .    c  b    c  b    c
#   b    .  b    .  .    c  b    c  b    c
#    dddd    dddd    ....    dddd    dddd
#   .    f  e    f  .    f  e    f  .    f
#   .    f  e    f  .    f  e    f  .    f
#    gggg    gggg    ....    gggg    gggg
##########################################


def get_input(mock=False):
    mock_input = [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ]
    for entry in mock_input if mock else open("./input.txt", "r"):
        yield tuple(map(lambda xs: xs.strip().split(" "), entry.strip().split("|")))


def part1(entries):
    num_seg_to_digit = {2: 1, 4: 4, 3: 7, 7: 8}
    count = 0

    # Count number of unique segment digits in output
    for _, outputs in entries:
        for output in outputs:
            if len(output) in num_seg_to_digit:
                count += 1

    return count


def gen_mapping() -> Iterator[Dict[int, Set[str]]]:
    all_digits = "abcdefg"

    for mapping in itertools.permutations(all_digits):
        yield {c: all_digits[i] for i, c in enumerate(mapping)}


# Converts the given pattern to its true representation.
def apply_mapping(pattern, mapping) -> str:
    return "".join(sorted([mapping[c] for c in pattern]))


def satifies_constraints(patterns, mapping, true_mapping):
    for pattern in patterns:
        if apply_mapping(pattern, mapping) not in true_mapping:
            return False

    return True


def part2(entries):
    true_mapping = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }

    final_score = 0

    for patterns, result in entries:
        for mapping in gen_mapping():
            if satifies_constraints(patterns, mapping, true_mapping):
                final_score += int(
                    "".join([true_mapping[apply_mapping(r, mapping)] for r in result])
                )
                break

    return final_score


if __name__ == "__main__":
    assert part1(get_input(mock=True)) == 26
    print(f"Count of 1, 4, 3, 7 in output: {part1(get_input(False))}")

    assert part2(get_input(mock=True)) == 61229
    print(f"Count of final result: {part2(get_input(mock=False))}")
