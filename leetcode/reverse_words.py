def reverse_words(s: str) -> str:
    result = []
    for word in s.split():
        result.append(word[::-1])

    return ' '.join(result)


print(reverse_words('Let\'s take LeetCode contest'))
