"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of 
[-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
such as eval().
"""

class Solution:
    def calculate(self, s):
        stack = []
        current_number = 0
        sign = '+'
        
        for i in range(len(s)):
            char = s[i]
            
            if char.isdigit():
                current_number = (current_number * 10) + int(char)
                
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(current_number)
                elif sign == '-':
                    stack.append(-current_number)
                elif sign == '*':
                    prev_number = stack.pop()
                    stack.append(prev_number * current_number)
                elif sign == '/':
                    prev_number = stack.pop()
                    stack.append(int(prev_number / current_number))
                    
                sign = char
                current_number = 0
                
        total = 0
        for num in stack:
            total = total + num
            
        return total
print(Solution().calculate("3+5 / 2"))