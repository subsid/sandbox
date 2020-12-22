def find_anagrams(input_str, pattern):
    freq_window = {}
    freq_pattern = {}
    results = []
    for c in pattern:
        if c not in freq_pattern:
            freq_pattern[c] = 0
        freq_pattern[c] += 1

    remaining_chars = len(freq_pattern.keys())
    start = 0

    for end in range(len(input_str)):
        right_char = input_str[end]
        if right_char not in freq_window:
            freq_window[right_char] = 0
        freq_window[right_char] += 1

        # If char in pattern and matches count, we found 1 char!
        if (right_char in pattern) and (freq_window[right_char] == freq_pattern[right_char]):
            remaining_chars -= 1

        # We found more than required number of chars, shrink window till they are equal.
        if (right_char in pattern) and (freq_window[right_char] > freq_pattern[right_char]):
            while (input_str[start] != right_char):
                remaining_chars += 1
                freq_window[input_str[start]] -= 1
                start += 1
            # Remove the first occurence of right_char so that counts are equal again.
            # No need to update remaining chars, as they will match now.
            start += 1
            freq_window[right_char] -= 1

        # We have a match!
        if (remaining_chars == 0):
            results.append(start)
            # Shrink window and update counts.
            left_char = input_str[start]
            freq_window[left_char] -= 1
            remaining_chars += 1
            start += 1

        # Since the current window includes a out of pattern char, we can move start beyond this char.
        if (right_char not in pattern):
            while (start < end + 1):
                left_char = input_str[start]
                # If this char was matching previously, we need to increment remaining chars.
                if (left_char in pattern) and freq_window[left_char] == freq_pattern[left_char]:
                    remaining_chars += 1
                freq_window[left_char] -= 1
                start += 1

    return results


if __name__ == "__main__":
    print("find_anagrams")

    assert find_anagrams("asabck", "abc") == [2]
    assert find_anagrams("aaaba", "aba") == [1, 2]
    assert find_anagrams("abbcabc", "abc") == [2, 3, 4]
    assert find_anagrams("asabckabsacbjljabc", "bca") == [2, 9, 15]
    assert find_anagrams("asabckabsacbjljabc", "bac") == [2, 9, 15]
    assert find_anagrams("asabckabasacbjljabc", "aab") == [6]
    assert find_anagrams("asabckabsacbjljabc", "zzz") == []
