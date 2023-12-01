from statistics import median_low


def get_input(mock=False):
    mock_input = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    for line in mock_input if mock else open("./input.txt", "r"):
        yield line.strip()


def analyze_command(command):
    # Returns tuple(error score, missing_chars).
    error_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    open_close = {"[": "]", "(": ")", "{": "}", "<": ">"}

    # Stack of open chars
    opens = []

    for c in command:
        if c in open_close:
            opens.append(c)
        elif c == open_close[opens[-1]]:
            opens.pop()
        else:  # Incorrect char
            return (
                error_scores[c],
                "".join(map(lambda o: open_close[o], reversed(opens))),
            )
    return (0, "".join(map(lambda o: open_close[o], reversed(opens))))


def part1(commands):
    return sum([error_score for error_score, _ in map(analyze_command, commands)])


def part2(commands):
    # Norvig trick!
    close_scores = str.maketrans(")]}>", "1234")
    incompletes = [
        missing_chars
        for e_score, missing_chars in map(analyze_command, commands)
        if e_score == 0
    ]
    score = lambda chars: int(chars.translate(close_scores), base=5)

    total_scores = list(map(score, incompletes))

    return median_low(total_scores)


if __name__ == "__main__":
    assert part1(get_input(mock=True)) == 26397
    assert part2(get_input(mock=True)) == 288957

    print(f"Part1 {part1(get_input(mock=False))}")
    print(f"Part2 {part2(get_input(mock=False))}")
