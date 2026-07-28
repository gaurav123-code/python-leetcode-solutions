"""
You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.
"""


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = []
        mid = ""

        for i in range(26):
            if freq[i] % 2 == 1:
                mid = chr(i + ord('a'))
            left.append(chr(i + ord('a')) * (freq[i] // 2))

        left = "".join(left)
        right = left[::-1]

        return left + mid + right
    
print(Solution().smallestPalindrome("bababa"))

    