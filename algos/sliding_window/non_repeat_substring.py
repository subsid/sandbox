# Given a string, find the length of the longest substring, which has no repeating characters.

def non_repeat_substring(input_str):
    curr_chars = set()
    window_start = 0
    longest = 0
    curr_len = 0

    for j in range(len(input_str)):
        c = input_str[j]
        if c not in curr_chars:
            curr_len += 1
            longest = max(curr_len, longest)
            curr_chars.add(c)
        else:
            while (c in curr_chars):
                curr_chars.remove(input_str[window_start])
                curr_len -= 1
                window_start += 1
            curr_chars.add(c)
            curr_len += 1
            longest = max(curr_len, longest)

    return longest

if __name__ == "__main__":
    assert(non_repeat_substring("aabccbb") == 3)
    assert(non_repeat_substring("abbbb") == 2)
    assert(non_repeat_substring("abccde") == 3)
