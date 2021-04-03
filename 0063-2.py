class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for x in range(M):
            for y in range(N):
                if x == 0 and y == 0:
                    pass
                elif obstacleGrid[x][y] == 1:
                    dp[x][y] = 0
                elif x == 0:
                    dp[x][y] = 1 if dp[x][y-1] == 1 else 0
                elif y == 0:
                    dp[x][y] = 1 if dp[x-1][y] == 1 else 0
                else:
                    dp[x][y] = dp[x-1][y] + dp[x][y-1]
        return dp[M-1][N-1]