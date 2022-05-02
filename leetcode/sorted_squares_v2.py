from typing import List


class Solution:
    def sortedSquares(nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        result = []

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                result.append(nums[i] ** 2)
                i += 1
            else:
                result.append(nums[j] ** 2)
                j -= 1

        return [x for x in result[::-1]]


print(Solution.sortedSquares([-7, -3, 2, 3, 11]), 'should return [4, 9, 9, 49, 121]')
print(Solution.sortedSquares([-4, -1, 0, 3, 10]), 'should return [0, 1, 9, 16, 100]')
print(Solution.sortedSquares([0, 1, 2, 3, 10]), 'should return [0, 1, 4, 9, 100]')
print(Solution.sortedSquares([1, 2, 3, 4, 10]), 'should return [1, 4, 9, 16, 100]')
print(Solution.sortedSquares([-5, -4, -3, -3, -1]), 'should return [1, 9, 9, 16, 25]')
print(Solution.sortedSquares([-5, -4, -3, -3, -1]), 'should return [1, 9, 9, 16, 25]')
