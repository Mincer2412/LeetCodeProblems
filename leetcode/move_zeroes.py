from typing import List


def move_zeroes(nums: List[int]) -> None:
    first_zero_index = get_zero_index(nums, 0)

    while True:
        j = get_non_zero_index(nums, first_zero_index)
        if j == -1:
            break
        nums[first_zero_index], nums[j] = nums[j], nums[first_zero_index]
        first_zero_index = get_zero_index(nums, first_zero_index)

    return nums


def get_non_zero_index(nums: List[int], i: int):
    for k in range(i, len(nums)):
        if nums[k] != 0:
            return k

    return -1


def get_zero_index(nums: List[int], i: int):
    for k in range(i, len(nums)):
        if nums[k] == 0:
            return k
    return -1


# print(move_zeroes([0, 1, 0, 3, 12]), 'should [1,3,12,0,0]')
# print(move_zeroes([0]), 'should [0]')
print(move_zeroes([1]), 'should [1]')
