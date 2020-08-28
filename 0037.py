## 2020/08/29
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board)

    def dfs(self, board):
        for column in range(9):
            for row in range(9):
                if board[column][row] == '.':
                    for num in '123456789':
                        board[column][row] = num
                        if self.is_valid(board, column, row) and self.dfs(board):
                            return True
                        board[column][row] = '.'
                    return False
        return True

    def is_valid(self, board, x, y):
        tmp_val = board[x][y]
        board[x][y] = '*'
        for i in range(9):
            if board[i][y] == tmp_val:
                return False
        for j in range(9):
            if board[x][j] == tmp_val:
                return False
        for i in range(3):
            for j in range(3):
                if board[(x//3)*3 + i][(y//3)*3 + j] == tmp_val:
                    return False
        board[x][y] = tmp_val
        return True

if __name__ == "__main__":
    solve = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solve.solveSudoku(board)
    print(board)