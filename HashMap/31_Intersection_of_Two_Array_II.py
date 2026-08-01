"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result 
in any order.
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        freq = {}
        
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        ans = []

        for num in nums2:
            if freq.get(num, 0) > 0:
                ans.append(num)
                freq[num] -= 1

        return ans
    
print(Solution().intersect([1,2,3,4,5],[3,4,5,6]))

