"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers 
directly above it as shown:
"""

class Solution(object):
    def generate(self, numRows):

        triangle = []

        for i in range(numRows):

            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle

print(Solution().generate(3))
