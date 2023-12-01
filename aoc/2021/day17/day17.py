from collections import defaultdict

# Start = s_x, s_y
# Find which side target is, left or right, up or down.
# For xs range left: velocities =
# For ys range grid_y_min to grid_y_max
# For a range of xs find t at which it will intersect target x.
# For a range of ys find t at which it will intersect target y.
# For each xs, ys with the same t, that is a valid value.

def find_hits(v, target, axis):
    c_v, c_p, t, max_cp = v, 0, 0, 0

    in_range = lambda rng, p: p >= rng[0] and p <= rng[1]
    hits = []
    end_cond = lambda p_i: p_i > target[1] if axis == "x" else p_i < target[0]
    while not end_cond(c_p):
        if in_range(target, c_p):
            hits.append((c_p, c_v, t))
        c_p += c_v
        max_cp = max(c_p, max_cp)
        d_v = 0
        if (axis == "y"):
            d_v = -1
        else:
            if c_v != 0:
                d_v = 1 if v < 0 else -1
        if (d_v == 0):
            break
        t += 1
        c_v += d_v

    return hits, max_cp

# def simulate_throw(velocity, target):
#     v_x, v_y = velocity
#     pass

def add_intersects(xs, ys):
    # Intersecting vals
    return [(max_y, (v_x, v_y)) for v_x, _ in xs for v_y, max_y in ys]

def part1(x_range, y_range):
    x_hits = defaultdict(lambda: [])
    y_hits = defaultdict(lambda: [])
    x_zero_hits = defaultdict(lambda: [])

    for v_x in range(1, x_range[1] + 1):
        if len((hits := find_hits(v_x, x_range, "x"))[0]) > 0:
            for hit in hits[0]:
                _, v, t  = hit
                # x doesn't change anymore.
                # So this can intersect with any v_y at timestep >= t
                if v == 0:
                    x_zero_hits[t].append((v_x, hits[1]))
                else:
                    x_hits[t].append((v_x, hits[1]))

    # 200 is experimental max, which works.
    for v_y in range(y_range[0], 200):
        if len((hits := find_hits(v_y, y_range, "y"))[0]) > 0:
            for hit in hits[0]:
                _, v, t = hit
                y_hits[t].append((v_y, hits[1]))

    intersects = []
    for t in y_hits:
        intersects.extend(add_intersects(x_hits[t], y_hits[t]))

    for t_x in x_zero_hits:
        for t_y in y_hits:
            if t_y >= t_x:
                intersects.extend(add_intersects(x_zero_hits[t_x], y_hits[t_y]))

    return sorted(intersects, key=lambda v: v[0], reverse=True)

def part2(x_range, y_range):
    # Part 1 returns [(max_y, point)].
    # We don't care about max_y in this part.
    init_velocities = set(map(lambda v: v[1], part1(x_range, y_range)))

    return init_velocities

if __name__ == "__main__":
    assert part1((20, 30), (-10, -5))[0][0] == 45
    print(f"Velocity with max_y: {part1((153, 199), (-114, -75))[0]}")
    print(f"Num valid velocities: {len(part2((153, 199), (-114, -75)))}")

