from typing import Tuple, Iterator, List


def get_measurements() -> Iterator[str]:
    return map(lambda v: v.strip(), open("./input.txt", "r"))


def part1(measurements) -> Tuple[int, int, int]:
    num_ones_idx: List[int] = []
    num_zeroes_idx: List[int] = []

    for val in measurements:
        if len(num_ones_idx) == 0:
            num_ones_idx = [0 for _ in range(len(val))]
        if len(num_zeroes_idx) == 0:
            num_zeroes_idx = [0 for _ in range(len(val))]

        for idx, c in enumerate(val):
            if c == "1":
                num_ones_idx[idx] += 1
            elif c == "0":
                num_zeroes_idx[idx] += 1
            else:
                raise ValueError(f"Unknown value {c}")

    gamma_rate = ""
    epsilon_rate = ""
    for o, z in zip(num_ones_idx, num_zeroes_idx):
        if o > z:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    gamma_rate = int(gamma_rate, base=2)
    epsilon_rate = int(epsilon_rate, base=2)

    return (gamma_rate, epsilon_rate, gamma_rate * epsilon_rate)


def part2(gen_measurements):
    def get_most_common(vals, pos):
        num_ones = 0
        num_zeroes = 0

        ## Find counts per position
        for val in vals:
            c = val[pos]
            if c == "1":
                num_ones += 1
            elif c == "0":
                num_zeroes += 1
            else:
                raise ValueError(f"Unknown value {c}")

        return "1" if num_ones >= num_zeroes else "0"

    def filter_vals(vals: Iterator[str], bit: str, bit_pos: int) -> List[str]:
        return list(filter(lambda x: x[bit_pos] == bit, vals))

    bit_pos = 0
    most_common_bit = get_most_common(gen_measurements(), bit_pos)
    remaining_vals_oxy = filter_vals(gen_measurements(), most_common_bit, bit_pos)

    while len(remaining_vals_oxy) > 1:
        bit_pos += 1
        most_common_bit = get_most_common(remaining_vals_oxy, bit_pos)
        remaining_vals_oxy = filter_vals(remaining_vals_oxy, most_common_bit, bit_pos)

    bit_pos = 0
    most_common_bit = get_most_common(gen_measurements(), bit_pos)
    remaining_vals_co2 = filter_vals(
        gen_measurements(), "0" if most_common_bit == "1" else "1", bit_pos
    )
    while len(remaining_vals_co2) > 1:
        bit_pos += 1
        least_common_bit = (
            "0" if get_most_common(remaining_vals_co2, bit_pos) == "1" else "1"
        )
        remaining_vals_co2 = filter_vals(remaining_vals_co2, least_common_bit, bit_pos)

    oxy_rating = int(remaining_vals_oxy[0], base=2)
    co2_rating = int(remaining_vals_co2[0], base=2)

    return (oxy_rating, co2_rating, oxy_rating * co2_rating)


if __name__ == "__main__":
    assert (
        part1(
            [
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ]
        )
        == (22, 9, 198)
    )

    assert (
        part2(
            lambda: [
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ]
        )
        == (23, 10, 230)
    )

    print(f"Part 1: (gamma, eps, gamma * epsilon) {part1(get_measurements())}")
    print(
        f"Part 2: (oxy_rating, co2_rating, oxy * co2) {part2(lambda: get_measurements())}"
    )
