class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        positions = [i for i, ch in enumerate(s) if ch == '1']

        if len(positions) < k:
            return ""

        min_len = float('inf')
        ans = ""

        for i in range(len(positions) - k + 1):
            start = positions[i]
            end = positions[i + k - 1]

            length = end - start + 1
            candidate = s[start:end + 1]

            if length < min_len:
                min_len = length
                ans = candidate

            elif length == min_len and candidate < ans:
                ans = candidate

        return ans