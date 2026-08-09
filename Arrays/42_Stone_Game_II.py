"""
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each 
pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then,
we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
"""

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, m):
            if i >= n:
                return 0

            if (i, m) in dp:
                return dp[(i, m)]

            best = 0

            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break

                opponent = solve(i + x, max(m, x))

                current = suffix[i] - opponent
                best = max(best, current)

            dp[(i, m)] = best
            return best

        return solve(0, 1)