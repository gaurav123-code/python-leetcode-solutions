"""
You are given an integer array nums of length n.

Construct an array prefixGcd where for each index i:

Let mxi = max(nums[0], nums[1], ..., nums[i]).
prefixGcd[i] = gcd(nums[i], mxi).
After constructing prefixGcd:

Sort prefixGcd in non-decreasing order.
Form pairs by taking the smallest unpaired element and the largest unpaired element.
Repeat this process until no more pairs can be formed.
For each formed pair, compute the gcd of the two elements.
If n is odd, the middle element in the prefixGcd array remains unpaired and should be ignored.
Return an integer denoting the sum of the GCD values of all formed pairs.

The term gcd(a, b) denotes the greatest common divisor of a and b.
"""
class Solution(object):
    def gcdSum(self, nums):
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        if n < 2:
            return 0

        prefixGcd = []
        current_max = nums[0]
        
        for x in nums:
            if x > current_max:
                current_max = x
            prefixGcd.append(get_gcd(x, current_max))
        
        prefixGcd.sort()
        
        total_gcd_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            pair_gcd = get_gcd(prefixGcd[left], prefixGcd[right])
            total_gcd_sum += pair_gcd
            left += 1
            right -= 1
            
        return total_gcd_sum
    
print(Solution().gcdSum([2,6,4]))