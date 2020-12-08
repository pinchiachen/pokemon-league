## 2020/12/08

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        visited = [[0] * N for _ in range(M)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for x in range(M):
            for y in range(N):
                if board[x][y] == word[0]:
                    visited[x][y] = 1
                    if self.dfs(board, word[1:], M, N, x, y, directions, visited): return True
                    visited[x][y] = 0
        return False

    def dfs(self, board, word, M, N, x0, y0, directions, visited):
        if not word: return True
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < M and 0 <= y < N and not visited[x][y] and board[x][y] == word[0]:
                visited[x][y] = 1
                if self.dfs(board, word[1:], M, N, x, y, directions, visited): return True
                visited[x][y] = 0
        return False