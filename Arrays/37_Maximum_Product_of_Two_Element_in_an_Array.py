"""
Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

class Solution(object):
    def maxProduct(self, nums):
        max1 = 0
        max2 = 0

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)
    
print(Solution().maxProduct([3,4,5,2]))