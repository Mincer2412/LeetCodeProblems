def search(nums, target: int) -> int:
    result = -1

    start_index = 0
    end_index = len(nums) - 1

    while True:
        mid = (start_index + end_index) // 2

        if nums[mid] == target:
            result = mid
            break

        if mid == start_index:
            if nums[end_index] == target:
                result = end_index
            break

        if nums[mid] > target:
            end_index = mid
        else:
            start_index = mid

    if result == -1:
        if nums[end_index] < target:
            result = end_index + 1
        elif nums[mid] < target:
            result = mid + 1
        else:
            result = mid

    return result


def search_insert(nums, target: int) -> int:
    return search(nums, target)


print(search_insert([1, 3, 5, 6], 0), 'should be 0')
# print(search_insert([1, 3, 5, 6], 5), 'should be 2')
# print(search_insert([1, 3, 5, 6], 2), 'should be 1')
# print(search_insert([1, 3, 5, 6], 7), 'should be 4')
