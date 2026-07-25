"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        window = {}

        have = 0
        need_count = len(need)

        left = 0

        min_len = float("inf")
        res_left = 0
        res_right = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:

                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res_left = left
                    res_right = right

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[res_left:res_right + 1]

print(Solution().minWindow("ADOBECODEBANC","ABC"))