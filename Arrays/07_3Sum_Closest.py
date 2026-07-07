"""
Given an integer array nums of length n and an integer target, 
find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

class Solution(object):
    def threeSumClosest(self, nums, target):

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                current = nums[i] + nums[left] + nums[right]

                if abs(current - target) < abs(closest - target):
                    closest = current

                if current < target:
                    left += 1

                elif current > target:
                    right -= 1

                else:
                    return current

        return closest
    
# print(Solution().threeSumClosest([-1,2,1,-4],1))