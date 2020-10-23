## 2020/10/23
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])
        new_board = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                new_board[x][y] = self.transfer(board, x, y, M, N)
        for x in range(M):
            for y in range(N):
                board[x][y] = new_board[x][y]

    def transfer(self, board, x, y, M, N):
        one_count = 0
        cur = board[x][y]
        board[x][y] = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if 0 <= i < M and 0 <= j < N and board[i][j] == 1:
                    one_count += 1
        board[x][y] = cur
        if one_count < 2: return 0
        elif 2 <= one_count <= 3 and cur == 1: return 1
        elif one_count > 3: return 0
        elif one_count == 3: return 1
        else: return 0

if __name__ == "__main__":
    print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))