def comp(nums, squares):
    if nums is None or squares is None or len(nums) != len(squares):
        return False

    return sorted([x ** 2 for x in nums]) == sorted(squares)


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
print(comp([2, 2, 3], [4, 9, 9]))
