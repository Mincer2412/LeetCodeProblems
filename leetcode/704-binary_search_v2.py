# Here used approach when processed mid element no longer processed in further iterations
# That approach applied by me in first_bad_version_v2

def search(nums, target: int) -> int:
    left, right = 0, len(nums) - 1

# It goes out from while when left/right comes over another. Like one making a step over the other
    while left <= right:
        print(left, right)
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


print(search([-1, 0, 3, 5, 9, 12], 6), 'should -1')
# print(search([-1, 0, 3, 5, 9, 12], 9), 'should 4')
# print(search([2, 5], 2), 'should 0')
# print(search([2, 5], 3), 'should -1')
# print(search([2, 5], 5), 'should 1')
# print(search([5], 5), 'should 0')
# print(search([5], -5), 'should -1')
