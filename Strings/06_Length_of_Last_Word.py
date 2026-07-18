"""
Given a string s consisting of words and spaces, return the length of the 
last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        i = len(s) - 1

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1

        return count

print(Solution().lengthOfLastWord("Hello World"))