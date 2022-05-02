from typing import List


def reverse_string(s: List[str]) -> None:
    s.reverse()  # s = s[::-1]

    return s


print(reverse_string(["h", "e", "l", "l", "o"]))
