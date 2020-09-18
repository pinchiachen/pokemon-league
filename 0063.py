## 2020/09/18
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        if M == 0 or obstacleGrid[0][0] == 1 or obstacleGrid[M - 1][N - 1] == 1:
            return 0
        grid = [[0 for i in range(N)] for j in range(M)]
        grid[0][0] = 1
        for i in range(1, N):
            grid[0][i] = 1 if (obstacleGrid[0][i] == 0 and grid[0][i - 1] == 1) else 0
        for i in range(1, M):
            grid[i][0] = 1 if (obstacleGrid[i][0] == 0 and grid[i - 1][0] == 1) else 0
        for i in range(1, M):
            for j in range(1, N):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1] if obstacleGrid[i][j] == 0 else 0
        return grid[M - 1][N - 1]

if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))