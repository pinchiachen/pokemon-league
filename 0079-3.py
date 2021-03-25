## 2021/03/25

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        visited = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                if board[x][y] == word[0]:
                    visited[x][y] = 1
                    if self.dfs(board, x, y, M, N, visited, word[1:], directions):
                        return True
                    visited[x][y] = 0
        return False

    def dfs(self, board, x0, y0, M, N, visited, target, directions):
        if not target:
            return True
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < M and 0 <= y < N and not visited[x][y] and board[x][y] == target[0]:
                visited[x][y] = 1
                if self.dfs(board, x, y, M, N, visited, target[1:], directions):
                    return True
                visited[x][y] = 0
        return False