"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and 
column to 0's.

You must do it in place.
"""

class Solution(object):
    def setZeroes(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        firstRow = False
        firstCol = False

        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True
                break

        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstRow:
            for j in range(n):
                matrix[0][j] = 0

        if firstCol:
            for i in range(m):
                matrix[i][0] = 0

print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))