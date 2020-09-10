## 2020/09/10
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = []
        if n <= 0: return res
        self.dfs(cols, res, n)
        return res

    def check(self, cols, add_col):
        for i in range(len(cols)):
            if cols[i] == add_col: return False
            if abs(add_col - cols[i]) == (len(cols) - i): return False
        return True

    def drawBoard(self, cols):
        board = []
        for col in cols:
            board.append('.' * col + 'Q' + '.' * (len(cols) - col - 1))
        return board

    def dfs(self, cols, res, n):
        if len(cols) == n:
            res.append(self.drawBoard(cols))
            return
        for col in range(n):
            if self.check(cols, col):
                self.dfs(cols + [col], res, n)


if __name__ == "__main__":
    print(Solution().solveNQueens(4))