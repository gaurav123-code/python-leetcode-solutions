"""
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0.
At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or 
nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. 
The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the 
winner, and you should also return true. You may assume that both players are playing optimally.
"""

class Solution(object):
    def predictTheWinner(self, nums):
        memo = {}

        def dfs(i, j):
            if i == j:
                return nums[i]

            if (i, j) in memo:
                return memo[(i, j)]

            left = nums[i] - dfs(i + 1, j)
            right = nums[j] - dfs(i, j - 1)

            memo[(i, j)] = max(left, right)
            return memo[(i, j)]

        return dfs(0, len(nums) - 1) >= 0

print(Solution().predictTheWinner([1,5,2]))
