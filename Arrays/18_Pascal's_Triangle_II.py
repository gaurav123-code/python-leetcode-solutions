"""Given an integer rowIndex, return the rowIndexth (0-indexed) 
row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers 
directly above it as shown:
"""

class Solution(object):
    def getRow(self, rowIndex):

        row = [1]

        for i in range(rowIndex):

            new_row = [1]

            for j in range(1, len(row)):
                new_row.append(row[j - 1] + row[j])

            new_row.append(1)
            row = new_row

        return row
    
    
print(Solution().getRow(3))