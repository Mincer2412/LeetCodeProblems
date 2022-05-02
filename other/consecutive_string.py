def longest_consec(words, n):
    max_word = ''

    if n > 0:
        for i in range(len(words) - n + 1):
            tmp = ''.join(words[i: i + n])
            if len(tmp) > len(max_word):
                max_word = tmp

    return max_word


max()

print(longest_consec(["zone", "abigail", "theta", "foam", "libe", "zas"], 3))
