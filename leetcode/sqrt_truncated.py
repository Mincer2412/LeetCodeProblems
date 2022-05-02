def my_sqrt(x: int) -> int:
    left, right = 0, x

    while left <= right:
        mid = (right + left) // 2

        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return left - 1


print('- 0 should return 0. result - ', my_sqrt(0))
print('- 1 should return 1. result - ', my_sqrt(1))
print('- 2 should return 1. result - ', my_sqrt(2))
print('- 3 should return 1. result - ', my_sqrt(3))
print('- 4 should return 2. result - ', my_sqrt(4))
print('- 5 should return 2. result - ', my_sqrt(5))
print('- 6 should return 2. result - ', my_sqrt(6))
print('- 7 should return 2. result - ', my_sqrt(7))
print('- 8 should return 2. result - ', my_sqrt(8))
print('- 9 should return 3. result - ', my_sqrt(9))
print('- 10 should return 3. result - ', my_sqrt(10))
