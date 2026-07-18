"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the 
result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
such as eval().
"""

class Solution:
    def calculate(self, s):
        stack = []
        current_number = 0
        result = 0
        sign = 1 
        
        for char in s:
            if char.isdigit():
                current_number = (current_number * 10) + int(char)
            elif char == '+':
                result = result + (sign * current_number)
                current_number = 0
                sign = 1
            elif char == '-':
                result = result + (sign * current_number)
                current_number = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result = result + (sign * current_number)
                current_number = 0
                
                prev_sign = stack.pop()
                prev_result = stack.pop()
                
                result = result * prev_sign
                result = result + prev_result
                
        result = result + (sign * current_number)
        return result
print(Solution().calculate("1+3"))