"""
Given an array nums of integers, return how many of them 
contain an even number of digits.
"""

class Solution(object):
    
    def findNumbers(self, nums):
        even_count = 0

        for num in nums:
            digits = 0

            while num > 0:
                digits += 1
                num //= 10

            if digits % 2 == 0:
                even_count += 1

        return even_count
    
# print(Solution().findNumbers([22,4,6,8,12,45,2]))