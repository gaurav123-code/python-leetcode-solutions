"""
Given a string s, return the lexicographically smallest subsequence of s that contains all the
distinct characters of s exactly once.
"""

class Solution:
    def smallestSubsequence(self, s):
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i
            
        stack = []
        seen = []
        
        for i in range(len(s)):
            char = s[i]
            
            if char in seen:
                continue
                
            while stack and stack[-1] > char and last_index[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)
                
            stack.append(char)
            seen.append(char)
            
        result = ""
        for char in stack:
            result += char
            
        return result