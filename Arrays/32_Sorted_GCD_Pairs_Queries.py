"""
You are given an integer array nums of length n and an integer array queries.

Let gcdPairs denote an array obtained by calculating the GCD of all possible pairs (nums[i], nums[j]), 
where 0 <= i < j < n, and then sorting these values in ascending order.

For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

The term gcd(a, b) denotes the greatest common divisor of a and b.
"""

class Solution(object):
    def gcdValues(self, nums, queries):
        
        max_val = max(nums)
        counts = [0] * (max_val + 1)
        for x in nums:
            counts[x] += 1
            
        gcd_counts = [0] * (max_val + 1)
        
        for g in range(max_val, 0, -1):
            total_multiples = 0
            for m in range(g, max_val + 1, g):
                total_multiples += counts[m]
                
            pairs_with_common_divisor = (total_multiples * (total_multiples - 1)) // 2
            
            subtracted_pairs = 0
            for m in range(2 * g, max_val + 1, g):
                subtracted_pairs += gcd_counts[m]
                
            gcd_counts[g] = pairs_with_common_divisor - subtracted_pairs
            
        prefix_sums = []
        gcd_values = []
        running_sum = 0
        
        for g in range(1, max_val + 1):
            if gcd_counts[g] > 0:
                running_sum += gcd_counts[g]
                prefix_sums.append(running_sum)
                gcd_values.append(g)
                
        ans = []
        for q in queries:
            target = q + 1
            left = 0
            right = len(prefix_sums) - 1
            idx = right
            
            while left <= right:
                mid = (left + right) // 2
                if prefix_sums[mid] >= target:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
                    
            ans.append(gcd_values[idx])
            
        return ans
 
print(Solution().gcdValues([2,3,4],[0,2,2]))