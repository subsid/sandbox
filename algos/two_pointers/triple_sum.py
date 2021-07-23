# Given an array of unsorted numbers, find all unique triplets n it that add up to zero.
# O(N*log(n) + N^2)

from .target_sum_pair import target_sum_pair

def triple_sum(arr):
    sorted_arr = sorted(arr)
    triplets = []
    print(sorted_arr)

    return triplets



if __name__ == "__main__":
    assert triple_sum([-5, 2, 1, 4, 3, 5]) == [[-5, 1, 4], [-5, 2, 3]]
    assert triple_sum([1, 1, 2, 1, 3, -3, 4, 5]) == [[1, 2, -3]]
    assert triple_sum([-5, 1, 2]) == []


