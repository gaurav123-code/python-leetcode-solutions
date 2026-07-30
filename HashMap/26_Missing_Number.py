"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the 
range that is missing from the array.
"""


class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual
    
print(Solution().missingNumber([3,0,1]))