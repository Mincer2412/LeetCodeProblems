def length_of_longest_substring(s: str) -> int:
    arr = list(s)
    res = []
    step = 1
    start = 0

    for i in range(len(arr) - step + 1):
        if len(set(arr[start: start + step])) == step:
            res = arr[start: start + step]
            step += 1
        else:
            start += 1
            found = False
            for j in range(len(arr) - step + 1):
                if len(set(arr[j: j + step])) == step:
                    found = True
                    res = arr[j: j + step]
                    step += 1
            if found is False:
                break

    return len(res)


# string / hash table / sliding window
print(length_of_longest_substring('dvdf'), 'should return 3')
print(length_of_longest_substring('aab'), 'should return 2')
print(length_of_longest_substring('abcabcbb'), 'should return 3')
print(length_of_longest_substring('pwwkew'), 'should return 3')
print(length_of_longest_substring('bbbb'), 'should return 1')
