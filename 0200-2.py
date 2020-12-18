## 2020/12/18

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        res = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == '1':
                    res += 1
                    self.dfs(grid, M, N, x, y, directions)
        return res

    def dfs(self, grid, M, N, x0, y0, directions):
        grid[x0][y0] = '0'
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < M and 0 <= y < N and grid[x][y] == '1':
                self.dfs(grid, M, N, x, y, directions)