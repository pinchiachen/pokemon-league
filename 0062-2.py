## 2020/12/07

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        for x in range(1, m):
            for y in range(1, n):
                grid[x][y] = grid[x-1][y] + grid[x][y-1]
        return grid[m-1][n-1]