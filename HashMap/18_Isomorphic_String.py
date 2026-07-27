"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the 
order of characters. No two characters may map to the same character, but a character may map to
itself.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 in mapST:
                if mapST[c1] != c2:
                    return False
            else:
                mapST[c1] = c2

            if c2 in mapTS:
                if mapTS[c2] != c1:
                    return False
            else:
                mapTS[c2] = c1

        return True
    
    
print(Solution().isIsomorphic("egg","add"))    
