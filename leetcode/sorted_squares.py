#Not workjing on leetcode because of problems with list indexing
def search(nums: tuple, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if left - 1 >= 0 and nums[left - 1] < 0:
        return left - 1

    return -1


def sorted_squares(nums):
    zero_or_less_index = search(nums, 0)
    negative_arr = nums[:zero_or_less_index + 1]
    nums = nums[zero_or_less_index + 1:]
    negative_arr = negative_arr[::-1]
    negative_arr = [-x for x in negative_arr]

    i, i_max = 0, len(negative_arr)
    j, j_max = 0, len(nums)
    result_arr = []

    if i_max == 0:
        return [x ** 2 for x in nums]
    if j_max == 0:
        return [x ** 2 for x in negative_arr]

    while True:
        if negative_arr[i] < nums[j]:
            result_arr.append(negative_arr[i])
            i += 1
        else:
            result_arr.append(nums[j])
            j += 1

        if i == i_max:
            for x in nums[j:]:
                result_arr.append(x)
            break

        if j == j_max:
            for x in negative_arr[i:]:
                result_arr.append(x)
            break

    return [x ** 2 for x in result_arr]


# print(sorted_squares([-7, -3, 2, 3, 11]), 'should return [4, 9, 9, 49, 121]')
# print(sorted_squares([-4, -1, 0, 3, 10]), 'should return [0, 1, 9, 16, 100]')
# print(sorted_squares([0, 1, 2, 3, 10]), 'should return [0, 1, 4, 9, 100]')
print(sorted_squares([1, 2, 3, 10]), 'should return [1, 4, 9, 100]')
# print(sorted_squares([-5, -4, -3, -3, -1]), 'should return [1, 9, 9, 16, 25]')
# print(sorted_squares([-5, -4, -3, -3, -1]), 'should return [1, 9, 9, 16, 25]')

# найти индекс 0
# взять все элементы до нуля и вынести в отдельный массив
# сменить знак и развернуть массив(позже можно не разворачивать)
# собрать через 2 указателя новый итоговый массив
