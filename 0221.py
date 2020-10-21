## 2020/10/21
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0] * N for _ in range(M)]
        res = 0
        for i in range(N):
            dp[0][i] = 1 if matrix[0][i] == '1' else 0
            res = max(res, dp[0][i])
        for i in range(M):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
            res = max(res, dp[i][0])
        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = 0 if matrix[i][j] == '0' else min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                res = max(res, dp[i][j])
        return res**2

if __name__ == "__main__":
    print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))