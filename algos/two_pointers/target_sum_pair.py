# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target. Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
# O(N)

def target_sum_pair(arr, target_sum):
    start = 0
    end = len(arr) - 1

    while(start < end):
        curr_sum = arr[start] + arr[end]
        if curr_sum == target_sum:
            return (start, end)
        elif curr_sum > target_sum:
            end -= 1
        elif curr_sum < target_sum:
            start += 1

    return ()

if __name__ == "__main__":
    print("target_sum_pair")

    assert target_sum_pair([1, 3, 7, 8, 9], 15) == (2, 3)
    assert target_sum_pair([1, 1, 3, 3, 4, 7], 6) == (2, 3)
