from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1

    while i <= j:
        res = numbers[i] + numbers[j]
        if res == target:
            return [i + 1, j + 1]
        if res > target:
            j -= 1
        else:
            i += 1


print(two_sum([2, 7, 11, 15], 9), 'should return [1, 2]')
print(two_sum([2, 3, 4], 6), 'should return [1, 3]')
print(two_sum([-1, 0], -1), 'should return [1, 2]')
