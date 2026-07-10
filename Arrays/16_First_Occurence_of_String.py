"""
Given two strings needle and haystack, return the index of the 
first occurrence of needle in haystack, or -1 if needle is not part 
of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            match = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1

print(Solution().strStr("Gaurav","aura"))
