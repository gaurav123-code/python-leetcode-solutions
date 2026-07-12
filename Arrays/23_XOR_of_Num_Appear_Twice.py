class Solution(object):
    def duplicateNumbersXOR(self, nums):
        seen = set()
        ans = 0

        for num in nums:
            if num in seen:
                ans ^= num
            else:
                seen.add(num)

        return ans

print(Solution().duplicateNumbersXOR([1,2,2,1]))