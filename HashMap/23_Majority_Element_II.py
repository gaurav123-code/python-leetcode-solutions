"""
Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.
"""

class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        result = []
        limit = len(nums) // 3

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            if count > limit:
                result.append(num)

        return result
    
print(Solution().majorityElement([3,2,3]))