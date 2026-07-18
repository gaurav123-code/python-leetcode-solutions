"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest 
number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""

class Solution:
    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)
        
        a, b = smallest, largest
        while b > 0:
            a, b = b, a % b
            
        return a
print(Solution().findGCD([2,3,4,5,10]))