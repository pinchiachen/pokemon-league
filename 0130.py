## 2020/06/18
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or len(board) == 1 or len(board[0]) == 1: return board
        N = len(board)
        M = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        pathQueue = []
        for i in range(N):
            for j in range(M):
                if (i == 0 or i == N - 1 or j == 0 or j == M - 1) and board[i][j] == 'O':
                    board[i][j] = '*'
                    pathQueue.append((j ,i))
        while len(pathQueue) > 0:
            (x0, y0) = pathQueue.pop(0)
            for dx, dy in directions:
                x = x0 + dx
                y = y0 + dy
                if 0 <= x < M and 0 <= y < N and board[y][x] == 'O':
                    pathQueue.append((x, y))
                    board[y][x] = '*'
        for i in range(N):
            for j in range(M):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

if __name__ == "__main__":
    Solve = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Solve.solve(board)