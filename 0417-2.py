## 2020/12/30
from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        M = len(matrix)
        N = len(matrix[0])
        pac_visited = [[0] * N for _ in range(M)]
        atl_visited = [[0] * N for _ in range(M)]
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        res = []
        for x in range(M):
            for y in range(N):
                if x == 0 or y == 0:
                    self.dfs(matrix, pac_visited, x, y, directions, M, N)
                if x == (M - 1) or y == (N - 1):
                    self.dfs(matrix, atl_visited, x, y, directions, M, N)
        for x in range(M):
            for y in range(N):
                if pac_visited[x][y] and atl_visited[x][y]:
                    res.append([x, y])
        return res

    def dfs(self, matrix, visited, x0, y0, directions, M, N):
        visited[x0][y0] = 1
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < M and 0 <= y < N and not visited[x][y] and matrix[x][y] >= matrix[x0][y0]:
                self.dfs(matrix, visited, x, y, directions, M, N)

if __name__ == "__main__":
    print(Solution().pacificAtlantic([[1]]))