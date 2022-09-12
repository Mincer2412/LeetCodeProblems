from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Python way non optimal solution
        # return [sum(nums[:i+1]) for i in range(len(nums))]

        # Use already calculated value on previous step
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
