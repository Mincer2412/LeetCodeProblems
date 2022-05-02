def search(nums, target: int) -> int:
    result = -1

    left, right = 0, len(nums) - 1

    while left <= right:
        print(left, right)
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            break

        if mid == left:
            if nums[right] == target:
                result = right
            break

        if nums[mid] > target:
            right = mid
        else:
            left = mid

    return result


print(search([2, 5, 7, 9, 11, 13, 25], 6))
# print(search([-1, 0, 3, 5, 9, 12], 9))
# print(search([2, 5], 2))
# print(search([2, 5], 3))
# print(search([2, 5], 5))
# print(search([5], 5))
# print(search([5], -5))
