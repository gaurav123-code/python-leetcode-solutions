"""
Given two integers representing the numerator and denominator of a fraction, 
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given 
inputs.

Note that if the fraction can be represented as a finite length string, you must return it.
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        ans = ""

        # Handle sign
        if (numerator < 0) != (denominator < 0):
            ans += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        ans += str(numerator // denominator)

        remainder = numerator % denominator

        if remainder == 0:
            return ans

        ans += "."

        seen = {}

        while remainder != 0:
            if remainder in seen:
                index = seen[remainder]
                ans = ans[:index] + "(" + ans[index:] + ")"
                return ans

            seen[remainder] = len(ans)

            remainder *= 10
            ans += str(remainder // denominator)
            remainder %= denominator

        return ans
    
print(Solution().fractionToDecimal(2,1))

