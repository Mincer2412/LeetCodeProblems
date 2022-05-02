def guess(answer: int, pick: int):
    if pick > answer:
        return 1
    if pick < answer:
        return -1
    return 0


def guess_number(n: int, pick) -> int:
    left, right = 1, n

    while True:
        mid = left + (right - left) // 2

        check = guess(mid, pick)

        if check == 0:
            return mid
        if check == 1:
            left = mid + 1
        else:
            right = mid - 1


print(guess_number(10, 6))
# print(guess_number(1, 1))
# print(guess_number(2, 1))
