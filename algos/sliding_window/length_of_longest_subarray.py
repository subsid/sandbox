# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

def length_of_longest_subarray(arr, k):
    freq_ones = 0
    max_length = 0
    max_length_ones = 0
    start = 0

    for end in range(len(arr)):
        if arr[end] == 1:
            freq_ones += 1
            max_length_ones = max(max_length_ones, freq_ones)
        while (end - start + 1 - max_length_ones > k):
            if arr[start] == 1:
                freq_ones -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

if __name__ == "__main__":
    print("length_of_longest_subarray")

    assert length_of_longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6
    assert length_of_longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9
