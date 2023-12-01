import operator
from functools import reduce, partial

def get_input():
    return open("./input.txt").read().strip()

def hex_to_bin(v):
    mapping = { "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111" }
    return "".join(map(lambda char: mapping[char], v))

def parse_literal(bin_p, start):
    curr = start
    vals = []
    done = False
    while not done:
        vals.append(bin_p[curr + 1: curr + 5])
        if bin_p[curr] == '0':
            done = True
        curr += 5

    return curr, int("".join(vals), base=2)

def parse_header(bin_p, p_start):
    v_r = p_start, p_start + 3
    t_r = p_start+3, p_start + 6

    return (bin_p[v_r[0]:v_r[1]], bin_p[t_r[0]: t_r[1]])

def parse_packet(bin_p, p_start):
    version, type_id = parse_header(bin_p, p_start)
    is_literal = lambda t_id: int(t_id, base=2) == 4
    curr = p_start + 6

    if is_literal(type_id):
        curr, val = parse_literal(bin_p, curr)
        return (curr, (int(version, base=2), int(type_id, base=2), val))
    # Operator
    else:
        length_type_id = bin_p[curr]
        curr += 1
        if length_type_id == '0':
            total_length = int(bin_p[curr:curr+15], base=2)
            curr += 15
            results = []
            end = curr + total_length

            while (curr < end):
                curr, parsed = parse_packet(bin_p, curr)
                results.append(parsed)

            return curr, (int(version, base=2), int(type_id, base=2), results)
        else:
            num_subpackets = int(bin_p[curr:curr+11], base=2)
            curr += 11
            results = []

            for _ in range(num_subpackets):
                curr, parsed = parse_packet(bin_p, curr)
                results.append(parsed)

            return curr, (int(version, base=2), int(type_id, base=2), results)

def part1(hex_packet):
    _, parsed = parse_packet(hex_to_bin(hex_packet), 0)
    version_sum = 0
    s = [parsed]
    while (len(s) > 0):
        v = s.pop()
        version_sum += v[0]
        if type(v[2]) is list:
            s.extend(v[2])

    return version_sum

def evaluate(parsed):
    type_id, val = parsed[1], parsed[2]
    eval_list = lambda fn, val: reduce(fn, (evaluate(v) for v in val))

    if type_id == 4:
        return parsed[2]
    elif type_id == 0:
        return eval_list(operator.add, val)
    elif type_id == 1:
        return eval_list(operator.mul, val)
    elif type_id == 2:
        return eval_list(min, val)
    elif type_id == 3:
        return eval_list(max, val)
    elif type_id == 5:
        return eval_list(lambda a, b: 1 if a > b else 0, val)
    elif type_id == 6:
        return eval_list(lambda a, b: 1 if a < b else 0, val)
    elif type_id == 7:
        return eval_list(lambda a, b: 1 if a == b else 0, val)

def part2(hex_packet):
    _, parsed = parse_packet(hex_to_bin(hex_packet), 0)

    return evaluate(parsed)

if __name__ == "__main__":
    assert part1("8A004A801A8002F478") == 16
    assert part1("620080001611562C8802118E34") == 12
    assert part1("C0015000016115A2E0802F182340") == 23
    assert part1("A0016C880162017C3686B18A3D4780") == 31
    print(f"Parsed packet version sum: {part1(get_input())}")
    assert part2("C200B40A82") == 3
    assert part2("04005AC33890") == 54
    assert part2("880086C3E88112") == 7
    assert part2("CE00C43D881120") == 9
    assert part2("D8005AC2A8F0") == 1
    assert part2("F600BC2D8F") == 0
    assert part2("9C005AC2F8F0") == 0
    assert part2("9C0141080250320F1802104A08") == 1
    print(f"Evaluated packet: {part2(get_input())}")

