"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'
where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).
"""

class Solution(object):
    def isMatch(self, s, p):
       
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                res = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                res = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = res
            return res

        return dp(0, 0)

print(Solution().isMatch("aa","a"))