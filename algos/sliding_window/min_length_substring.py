# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

def min_length_substring(input_str, required_chars):
    # Some const
    min_length = len(input_str) + 1
    freq_window = {}
    freq_required = {}
    min_start = -1
    min_end = -1

    for c in required_chars:
        if c not in freq_required:
            freq_required[c] = 0
        freq_required[c] += 1

    remaining_chars = len(freq_required.keys())
    start = 0

    for end in range(len(input_str)):
        right_char = input_str[end]
        if right_char not in freq_window:
            freq_window[right_char] = 0
        freq_window[right_char] += 1

        # We found a char!
        if ((right_char in freq_required) and
                (freq_window[right_char] == freq_required[right_char])):
                remaining_chars -= 1

        if (remaining_chars == 0):
            if (end - start + 1) < min_length:
                min_length = end - start + 1
                min_start = start
                min_end = end

            # Keep shrinking window till remaining_chars is non-zero
            while remaining_chars == 0:
                left_char = input_str[start]
                start += 1
                freq_window[left_char] -= 1
                if ((left_char in freq_required) and
                        (freq_window[left_char] < freq_required[left_char])):
                    remaining_chars += 1
                else:
                    if (end - start + 1) < min_length:
                        min_length = end - start + 1
                        min_start = start
                        min_end = end

    return input_str[min_start:min_end + 1] if min_start != -1 else ""

if __name__ == "__main__":
    print("min length substring")

    assert min_length_substring("hkhlajkjbcjhy", "abc") == "ajkjbc"
    assert min_length_substring("hayubcjhyjja4cb", "abc") == "a4cb"
    assert min_length_substring("aaayubcjhyjjbba4cb", "abc") == "ba4c"
    assert min_length_substring("aaayubcjhyjjbba4cb", "zzc") == ""

