# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.
# O(N*M*L)
# N: Number of chars in input string
# M: Number of words
# L: Length of word

def word_concatenation(input_str, words):
    if len(words) == 0:
        return []

    freq_words = {}
    result = []
    word_len  = len(words[0])
    total_len = word_len * len(words)
    for w in words:
        if w not in freq_words:
            freq_words[w] = 0
        freq_words[w] += 1

    # For each window start, can we find a match?
    for window_start in range(0, len(input_str) - total_len + 1):
        start = window_start
        freq_input = {}
        remaining_words = len(freq_words.keys())

        while (start < start + total_len):
            word = input_str[start:start + word_len]
            if word in freq_words:
                if word not in freq_input:
                    freq_input[word] = 0
                freq_input[word] += 1

                if freq_input[word] == freq_words[word]:
                    remaining_words -= 1

                if freq_input[word] > freq_words[word]:
                    break
            else:
                break
            start += word_len

        if remaining_words == 0:
            result.append(window_start)

    return result

if __name__ == "__main__":
    print("word_concatenation")

    assert word_concatenation("obarfoo", ["foo", "bar"]) == [1]
    assert word_concatenation("foobarfoooofoo", ["foo", "oof"]) == [6]
    assert word_concatenation("wholetwhofoo", ["who", "let"]) == [0, 3]
    assert word_concatenation("wholetletwhowhofoo", ["who", "let", "who"]) == [6]
    assert word_concatenation("wholetwhofoowhobooletwhooo", ["who", "let"]) == [0, 3, 18]
    assert word_concatenation("wholetletwho", ["boo"]) == []


