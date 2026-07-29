"""
You are given a palindromic string s and an integer k.

Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k 
distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are 
counted once.
"""

class Solution(object):
    def smallestPalindrome(self, s, k):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        mid = ""

        half = [0] * 26
        m = 0

        for i in range(26):
            if cnt[i] % 2:
                mid = chr(i + 97)
            half[i] = cnt[i] // 2
            m += half[i]

        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        denom = 1
        for x in half:
            denom *= fact[x]

        ways = fact[m] // denom

        if ways < k:
            return ""

        ans = []

        rem = m

        while rem:
            for i in range(26):
                if half[i] == 0:
                    continue

                # Number of permutations if this character is fixed
                nxt = ways * half[i] // rem

                if k > nxt:
                    k -= nxt
                else:
                    ans.append(chr(i + 97))
                    ways = nxt
                    half[i] -= 1
                    rem -= 1
                    break

        left = "".join(ans)
        return left + mid + left[::-1]    
    
print(Solution().smallestPalindrome("abba",2))    
