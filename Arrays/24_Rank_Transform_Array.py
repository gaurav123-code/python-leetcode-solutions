"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must 
be the same. Rank should be as small as possible.
 
"""

class Solution:
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(set(arr))

        rank = {}
        r = 1

        for num in sorted_arr:
            rank[num] = r
            r += 1

        return [rank[num] for num in arr]
    
print(Solution().arrayRankTransform([78,23,1,90]))