"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True
    
print(Solution().isAnagram("anagram","nagaarm"))