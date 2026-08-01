"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result 
must be unique and you may return the result in any order.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
    
print(Solution().intersection([1,2,3,4],[3,4,5,6]))

