"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i]):
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))