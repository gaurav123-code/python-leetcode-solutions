"""
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.
"""

class Solution(object):
    def maxProduct(self, n):
        digits = []

        while n > 0:
            digits.append(n % 10)
            n = n // 10

        maximum = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                product = digits[i] * digits[j]
                if product > maximum:
                    maximum = product

        return maximum


print(Solution().maxProduct(12))
print(Solution().maxProduct(731))
print(Solution().maxProduct(882))
