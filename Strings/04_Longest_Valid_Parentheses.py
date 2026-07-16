"""
Given a string containing just the characters '(' and ')', return the length of the longest
valid (well-formed) parentheses substring.
"""
class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        ans = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans


print(Solution().longestValidParentheses("(()"))
print(Solution().longestValidParentheses(")()())"))