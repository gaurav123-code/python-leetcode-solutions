"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements 
sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        st = set(nums)

        longest = 0

        for num in st:

            if num - 1 not in st:

                current = num
                length = 1

                while current + 1 in st:
                    current += 1
                    length += 1

                if length > longest:
                    longest = length

        return longest

print(Solution().longestConsecutive([100,4,200,1,3,2]))