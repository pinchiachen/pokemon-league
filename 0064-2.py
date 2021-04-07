## 2021/04/07

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dp = [[0] * (N+1) for _ in range(M+1)]
        for x in range(M+1):
            for y in range(N+1):
                if x == 1 and y == 1:
                    dp[x][y] = grid[0][0]
                elif (x == 0) or (y == 0):
                    dp[x][y] = float('inf')
                else:
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x-1][y-1]
        return dp[M][N]