## 2020/10/08

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M = len(s)
        N = len(t)
        if M < N: return 0
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M + 1):
            dp[i][0] = 1
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) if s[i-1] == t[j-1] else dp[i-1][j]
        return dp[M][N]


if __name__ == "__main__":
    print(Solution().numDistinct("rabbbit", "rabbit"))