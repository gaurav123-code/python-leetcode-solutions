"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

class Solution(object):

    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        # Initialize the sets and store empty cells
        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    box = (i // 3) * 3 + (j // 3)

                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)

        def solve(index):

            # Base Case
            if index == len(empty):
                return True

            row, col = empty[index]
            box = (row // 3) * 3 + (col // 3)

            for num in "123456789":

                if num not in rows[row] and \
                   num not in cols[col] and \
                   num not in boxes[box]:

                    # Make Choice
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

                    # Explore
                    if solve(index + 1):
                        return True

                    # Undo Choice (Backtrack)
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box].remove(num)

            return False

        solve(0)
        
print(Solution().solveSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))