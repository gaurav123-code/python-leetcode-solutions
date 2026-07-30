"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the 
array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_index = {}

        for i in range(len(nums)):
            if nums[i] in last_index:
                if i - last_index[nums[i]] <= k:
                    return True

            last_index[nums[i]] = i

        return False
    
print(Solution().containsNearbyDuplicate([1,2,3,1],3))