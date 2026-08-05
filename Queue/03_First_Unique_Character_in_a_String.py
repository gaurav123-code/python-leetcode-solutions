"""
Given a string s, find the first non-repeating character in it and return its index. If it does 
not exist, return -1.
"""

class Solution(object):
    def firstUniqChar(self, s):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1

print(Solution().firstUniqChar("aabb"))
