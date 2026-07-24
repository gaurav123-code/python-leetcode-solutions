"""
You are given an integer array nums.

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).
"""

class Solution(object):
    def uniqueXorTriplets(self, nums):
        values = set(nums)

        first = set(values)

        second = set()

        for x in first:
            for y in values:
                second.add(x ^ y)

        third = set()

        for x in second:
            for y in values:
                third.add(x ^ y)

        return len(third)

print(Solution().uniqueXorTriplets([1,3]))