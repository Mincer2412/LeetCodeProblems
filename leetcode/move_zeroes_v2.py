from typing import List


def move_zeroes(nums: List[int]):
    i, j = 0, 0

    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

        i += 1

    return nums


print(move_zeroes([0, 1, 0, 3, 12]), 'should [1,3,12,0,0]')
print(move_zeroes([0]), 'should [0]')
print(move_zeroes([1]), 'should [1]')
print(move_zeroes([73348, 66106, -85359, 53996, 18849, -6590, -53381, -86613, -41065, 83457, 0]),
      'should \n[73348, 66106, -85359, 53996, 18849, -6590, -53381, -86613, -41065, 83457, 0]')
