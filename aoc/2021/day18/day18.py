import math
from ast import literal_eval
from copy import deepcopy
from functools import reduce
from itertools import permutations

def get_input(mock=False):
    mock_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".split("\n")

    for line in mock_input if mock else open("./input.txt", "r"):
        yield literal_eval(line.strip())

def get_element(pair, idxs):
    curr = pair
    for idx in idxs:
        curr = curr[idx]

    return curr

def is_type(t, v):
    return type(v) == t

def increase_rightmost(pair, val):
    if is_type(int, pair[1]):
        pair[1] += val
        return pair
    else:
        return increase_rightmost(pair[1], val)

def increase_leftmost(pair, val):
    if is_type(int, pair[0]):
        pair[0] += val
    else:
        increase_leftmost(pair[0], val)

    return pair

def increase_left(pair, idxs, val):
    while (len(idxs) > 0):
        idx = idxs.pop()
        curr = get_element(pair, idxs)
        if idx == 1:
            if is_type(int, curr[0]):
                curr[0] += val
            else:
                increase_rightmost(curr[0], val)
            break

    return pair

def increase_right(pair, idxs, val):
    while (len(idxs) > 0):
        idx = idxs.pop()
        curr = get_element(pair, idxs)
        if idx == 0:
            if is_type(int, curr[1]):
                curr[1] += val
            else:
                increase_leftmost(curr[1], val)
            break

    return pair

def explode_pair(pair, idxs):
    curr = get_element(pair, idxs)
    left, right = curr

    # Check left first
    if is_type(list, left):
        # Explode and return.
        if len(idxs) >= 3:
            increase_left(pair, idxs + [0], left[0])
            increase_right(pair, idxs + [0], left[1])
            curr[0] = 0
            return True, pair

        # Try exploding left
        exploded, pair = explode_pair(pair, idxs + [0])
        if exploded:
            return exploded, pair

    # Check right next
    if is_type(list, right):
        # Explode and return.
        if len(idxs) >= 3:
            increase_left(pair, idxs + [1], right[0])
            increase_right(pair, idxs + [1], right[1])
            curr[1] = 0
            return True, pair

        exploded, pair = explode_pair(pair, idxs + [1])
        if exploded:
            return exploded, pair

    # No explosion
    return False, pair

def split_pair(pair, idxs):
    curr = get_element(pair, idxs)
    left, right = curr

    if is_type(int, left):
        # Split and return
        if left >= 10:
            curr[0] = [int(left/2), math.ceil(left/2)]
            return True, pair
    else:
        split, pair = split_pair(pair, idxs + [0])
        if split:
            return split, pair

    if is_type(int, right):
        # Split and return
        if right >= 10:
            curr[1] = [int(right/2), math.ceil(right/2)]
            return True, pair
    else:
        split, pair = split_pair(pair, idxs + [1])
        if split:
            return split, pair

    return False, pair

def reduce_pair(pair, idxs):
    # Try to explode, if not possible try to split.
    # Return after one action.
    exploded, pair = explode_pair(pair, idxs)

    if exploded:
        return exploded, pair

    split, pair = split_pair(pair, idxs)

    if split:
        return split, pair

    return False, pair

def reduce_fn(left, right):
    reduced = True
    pair = [left, right]

    while (reduced):
        reduced, pair = reduce_pair(pair, [])

    return pair

def magnitude(reduced_val):
    left, right = reduced_val

    if is_type(int, left):
        if is_type(int, right):
            return 3 * left + 2 * right
        else:
            return 3 * left + 2 * magnitude(right)
    else:
        if is_type(int, right):
            return 3 * magnitude(left) + 2 * right
        else:
            return 3 * magnitude(left) + 2 * magnitude(right)

def part1(nums):
    reduced_val = reduce(reduce_fn, nums)
    return reduced_val

def part2(nums):
    magnitudes = []
    for left, right in permutations(nums, 2):
        result = magnitude(reduce_fn(deepcopy(left), deepcopy(right)))
        magnitudes.append(result)

    return max(magnitudes)

if __name__ == "__main__":
    assert increase_left([[1, -3], 3], [1], 3) == [[1, 0], 3]
    assert increase_left([[1, [-3, [4, 6]]], 3], [0, 1, 1], 3) == [[1, [0, [4, 6]]], 3]
    assert increase_right([[1, 3], -3], [0, 1], 3) == [[1, 3], 0]
    assert increase_right([[1, [3, [-3, 6]]], 3], [0, 1, 0], 3) == [[1, [3, [0, 6]]], 3]

    assert reduce_pair([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [])[1] == [[3,[2,[8,0]]],[9,[5,[7,0]]]]
    assert reduce_pair([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [])[1] == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
    assert reduce_pair([[1, 10], 2], [])[1] == [[1, [5, 5]], 2]
    assert reduce_pair([[[[[9,8],1],2],3],4], [])[1] == [[[[0,9],2],3],4]
    assert reduce_pair([7,[6,[5,[4,[3,2]]]]], [])[1] == [7,[6,[5,[7,0]]]]
    assert reduce_pair([[6,[5,[4,[3,2]]]],1], [])[1] == [[6,[5,[7,0]]],3]
    assert part1([[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]]) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]

    assert part1([[1, 1], [2, 2], [3, 3], [4, 4]]) == [[[[1,1],[2,2]],[3,3]],[4,4]]
    assert part1([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [[[[3,0],[5,3]],[4,4]],[5,5]]
    assert part1([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == [[[[5,0],[7,4]],[5,5]],[6,6]]

    a = [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    b = [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
    c = [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
    assert part1([a, b]) == c

    assert magnitude([9, 1]) == 29
    assert magnitude([[9, 1], [1, 9]]) == 129
    assert magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488

    assert magnitude(part1(get_input(mock=True))) == 4140
    print(f"Part1 Magnitude {magnitude(part1(get_input(mock=False)))}")

    assert part2(get_input(mock=True)) == 3993
    print(f"Part2 Max Magnitude {part2(get_input(mock=False))}")
