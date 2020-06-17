## 2020/06/17

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(0, n + 1):
            j = 1
            while (i + j**2) <= n:
                dp[i + j**2] = min(dp[i + j**2], dp[i] + 1)
                j += 1
        return dp[-1]

if __name__ == "__main__":
    Solve = Solution()
    n = 12
    print(Solve.numSquares(n))