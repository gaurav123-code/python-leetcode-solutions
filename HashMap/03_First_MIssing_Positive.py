"""
Given an unsorted integer array nums. Return the smallest positive integer that is not 
present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        i = 0
        while i < n:
            correct = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

print(Solution().firstMissingPositive([1,3,0]))