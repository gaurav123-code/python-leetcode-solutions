"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
"""

class Solution:
    def shiftGrid(self,grid, k):
        m = len(grid)
        n = len(grid[0])
        total_elements = m * n
        
        k = k % total_elements
        if k == 0:
            return grid
            
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                current_1d_index = i * n + j
                new_1d_index = (current_1d_index + k) % total_elements
                
                new_row = new_1d_index // n
                new_col = new_1d_index % n
                
                result[new_row][new_col] = grid[i][j]
                
        return result

print(Solution().shiftGrid([[1,2,3],[4,5,6],[7,8,9]],1))
