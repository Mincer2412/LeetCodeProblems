from typing import List


def rotate(nums: List[int], k: int):
    k = k % len(nums)
    j = len(nums) - k
    n = nums.copy()
    nums.clear()
    nums.extend(n[j:])
    nums.extend(n[:j])

    return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 3), 'should [5, 6, 7, 1, 2, 3, 4]')
print(rotate([-1, -100, 3, 99], 2), 'should [3, 99, -1, -100]')
print(rotate([-1, -100, 3, 99], 4), 'should [3, 99, -1, -100]')
print(rotate([1, 2], 5), 'should [2, 1]')
