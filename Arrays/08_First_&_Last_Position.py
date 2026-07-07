"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):

    def firstPosition(self, nums, target):

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:

            mid = (left + right) 

            if nums[mid] == target:
                ans = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return ans

    def lastPosition(self, nums, target):

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:

            mid = (left + right) 

            if nums[mid] == target:
                ans = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return ans

    def searchRange(self, nums, target):

        first = self.firstPosition(nums, target)
        last = self.lastPosition(nums, target)

        return [first, last]

print(Solution().searchRange([1,1,2,2,3,3],3))