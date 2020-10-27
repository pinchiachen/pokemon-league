## 2020/10/27
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        res = 0
        M = len(matrix)
        N = len(matrix[0])
        path = [[-1] * N for _ in range(M)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for i in range(M):
            for j in range(N):
                res = max(res, self.dfs(matrix, i, j, M, N, directions, path))
        return res
        
    def dfs(self, matrix, x0, y0, M, N, directions, path):
        if path[x0][y0] != -1: return path[x0][y0]
        path[x0][y0] = 1
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < M and 0 <= y < N and matrix[x][y] > matrix[x0][y0]:
                path[x0][y0] = max(path[x0][y0], 1 + self.dfs(matrix, x, y, M, N, directions, path))
        return path[x0][y0]

if __name__ == "__main__":
    print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))