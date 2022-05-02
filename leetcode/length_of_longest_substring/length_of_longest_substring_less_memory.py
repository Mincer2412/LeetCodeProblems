def length_of_longest_substring(s: str) -> int:
    initial_element, search_size = 0, 1

    while initial_element + search_size - 1 < len(s):
        sub_arr = s[initial_element: initial_element + search_size]
        if len(set(sub_arr)) == search_size:
            search_size += 1
        else:
            initial_element += 1

    return search_size - 1


# string / hash table / sliding window
print(length_of_longest_substring('dvdf'), 'should return 3')
print(length_of_longest_substring('aab'), 'should return 2')
print(length_of_longest_substring('abcabcbb'), 'should return 3')
print(length_of_longest_substring('pwwkew'), 'should return 3')
print(length_of_longest_substring('bbbb'), 'should return 1')
