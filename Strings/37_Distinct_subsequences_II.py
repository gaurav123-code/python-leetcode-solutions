class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1  # empty subsequence

        last = [0] * 26

        for i, ch in enumerate(s, 1):
            idx = ord(ch) - ord('a')

            new_dp = (2 * dp - last[idx]) % MOD

            last[idx] = dp
            dp = new_dp

        return (dp - 1) % MOD