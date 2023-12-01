import math

def get_input(mock=False):
    mock_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    if mock:
        return mock_input
    return list(map(int, open("./input.txt", "r").readline().strip().split(",")))

def align_to_n_cost(n, vals):
    cost = 0
    for val in vals:
        cost += abs(val - n)

    return cost

def align_to_n_cost_2(n, vals):
    cost = 0

    for val in vals:
        n_steps = abs(val - n)
        cost += int((n_steps * (n_steps + 1)) / 2)

    return cost

def compute_cost(horizontal_vals, cost_fn):
    optimal_cost = math.inf

    min_pos = min(horizontal_vals)
    max_pos = max(horizontal_vals)

    for pos in range(min_pos, max_pos + 1):
        cost = cost_fn(pos, horizontal_vals)
        if cost < optimal_cost:
            optimal_cost = cost

    return optimal_cost

if __name__ == "__main__":
    assert compute_cost(get_input(True), align_to_n_cost) == 37
    assert compute_cost(get_input(True), align_to_n_cost_2) == 168

    print(f"Cost part 1: {compute_cost(get_input(False), align_to_n_cost)}")
    print(f"Cost part 2: {compute_cost(get_input(False), align_to_n_cost_2)}")
