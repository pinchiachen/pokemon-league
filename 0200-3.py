## 2021/04/02

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        visited = [[0] * N for _ in range(M)]
        res = 0
        for x in range(M):
            for y in range(N):
                if not visited[x][y] and grid[x][y] == '1':
                    self.dfs(grid, x, y, M, N, visited, directions)
                    res += 1
        return res
    
    def dfs(self, grid, x0, y0, M, N, visited, directions):
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < M and 0 <= y < N and not visited[x][y] and grid[x][y] == '1':
                visited[x][y] = 1
                self.dfs(grid, x, y, M, N, visited, directions)