"""
You are given a binary string s of length n, where:

'1' represents an active section.
'0' represents an inactive section.
You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
Return the maximum number of active sections in s after making the optimal trade.

Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. 
The augmented '1's do not contribute to the final count.
"""

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = s.count('1')
        t = '1' + s + '1'

        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        best = 0

        for i in range(1, len(runs) - 1):
            if (runs[i][0] == '1' and
                runs[i - 1][0] == '0' and
                runs[i + 1][0] == '0'):
                best = max(best, runs[i - 1][1] + runs[i + 1][1])

        return base + best

print(Solution().maxActiveSectionsAfterTrade("01"))