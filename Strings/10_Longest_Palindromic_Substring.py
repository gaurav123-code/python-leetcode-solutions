"""
Given a string s, return the longest palindromic substring in s.
"""

class Solution(object):
    def longestPalindrome(self, s):
        
        if not s:
            return ""
            
        start = 0
        end = 0
        n = len(s)
        
        for i in range(n):
            l1 = i
            r1 = i
            while l1 >= 0 and r1 < n and s[l1] == s[r1]:
                l1 -= 1
                r1 += 1
            len1 = r1 - l1 - 1
            
            l2 = i
            r2 = i + 1
            while l2 >= 0 and r2 < n and s[l2] == s[r2]:
                l2 -= 1
                r2 += 1
            len2 = r2 - l2 - 1
            
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]
    
print(Solution().longestPalindrome("babad"))
