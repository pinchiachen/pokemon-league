class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for x in range(m):
            for y in range(n):
                dp[x][y] = 1 if (x == 0) or (y == 0) else dp[x-1][y] + dp[x][y-1]
        return dp[m-1][n-1]