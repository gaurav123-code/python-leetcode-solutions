"""
Given an integer array nums where every element appears three times except for one, 
which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity 
and use only constant extra space.

"""
class Solution:
    def singleNumber(self, nums):
        ans = 0

        for i in range(32):
            bit_count = 0

            for num in nums:
                if (num >> i) & 1:
                    bit_count += 1

            if bit_count % 3:
                if i == 31:          
                    ans -= (1 << 31)
                else:
                    ans |= (1 << i)

        return ans
    
print(Solution().singleNumber([2,56,1,2,333,98]))