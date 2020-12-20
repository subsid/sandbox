# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.


def length_of_longest_substring(input_str, k):
    max_length = 0
    start = 0
    freq_map = {}
    max_repeat = 0

    for end in range(len(input_str)):
        letter = input_str[end]
        if letter not in freq_map:
            freq_map[letter] = 0
        freq_map[letter] += 1
        max_repeat = max(max_repeat, freq_map[letter])

        window_len = end - start + 1
        if ((window_len - max_repeat) > k):
            freq_map[input_str[start]] -= 1
            start += 1

        new_window_len = end - start + 1
        max_length = max(max_length, new_window_len)

    return max_length

if __name__ == "__main__":
    print("length_of_longest_substring")

    assert(length_of_longest_substring("aabccbb", 2) == 5)
    assert(length_of_longest_substring("abbcb", 1) == 4)
    assert(length_of_longest_substring("abccde", 1) == 3)


