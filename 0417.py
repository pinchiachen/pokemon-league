## 2020/06/25
from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0: return []
        M = len(matrix)
        N = len(matrix[0])
        pacific_visited = [[False] * N for i in range(M)]
        atlantic_visited = [[False] * N for i in range(M)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = []

        for i in range(M):
            self.dfs(0, i, directions, matrix, M, N, pacific_visited)
            self.dfs(N - 1, i, directions, matrix, M, N, atlantic_visited)
        
        for j in range(N):
            self.dfs(j, 0, directions, matrix, M, N, pacific_visited)
            self.dfs(j, M - 1, directions, matrix, M, N, atlantic_visited)
        
        for k in range(M):
            for l in range(N):
                if pacific_visited[k][l] and atlantic_visited[k][l]:
                    res.append([k, l])
        
        return res

    def dfs(self, x0, y0, directions, matrix, M, N, visited):
        visited[y0][x0] = True
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < N and 0 <= y < M and matrix[y][x] >= matrix[y0][x0] and not visited[y][x]:
                self.dfs(x, y, directions, matrix, M, N, visited)

if __name__ == "__main__":
    solve = Solution()
    matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(solve.pacificAtlantic(matrix))