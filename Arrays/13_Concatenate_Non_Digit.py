"""
You are given an integer n.

Form a new integer x by concatenating all the non-zero digits of n in their original order. 
If there are no non-zero digits, x = 0.

Let sum be the sum of digits in x.

Return an integer representing the value of x * sum.
"""


class Solution(object):
    def digitSumProduct(self, n):
        digits = []

        for ch in str(n):
            if ch != '0':
                digits.append(ch)

        if not digits:
            return 0

        x = int("".join(digits))
        digit_sum = sum(int(d) for d in digits)

        return x * digit_sum
    
# print(Solution().digitSumProduct(1230))