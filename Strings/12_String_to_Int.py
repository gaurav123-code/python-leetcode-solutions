"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity 
if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered 
or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer 
to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater 
than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
"""

class Solution(object):
    def myAtoi(self, s):
        
        n = len(s)
        i = 0
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        res = 0
        
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
            if sign * res < INT_MIN:
                return INT_MIN
            if sign * res > INT_MAX:
                return INT_MAX
                
        return sign * res
    
print(Solution().myAtoi("42"))