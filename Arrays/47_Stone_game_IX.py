"""
Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. 
You are given an integer array stones, where stones[i] is the value of the ith stone.

Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. 
The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will 
win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play optimally, return true if Alice wins and false if Bob wins.
"""

class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt = [0, 0, 0]
        for x in stones:
            cnt[x % 3] += 1

        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
        else:
            return abs(cnt[1] - cnt[2]) > 2
        
print(Solution().stoneGameIX([2,1]))