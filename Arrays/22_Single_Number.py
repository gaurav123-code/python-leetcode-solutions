class Solution(object):
    def singleNumber(self, nums):
        ans = 0

        for num in nums:
            ans ^= num

        return ans

print(Solution().singleNumber([1,2,2,1,3,4,3]))
