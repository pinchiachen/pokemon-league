## 2020/10/23

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * (n + 1)
        idx_2 = 0
        idx_3 = 0
        idx_5 = 0
        for idx in range(1, n + 1):
            dp[idx] = min(2 * dp[idx_2], 3 * dp[idx_3], 5 * dp[idx_5])
            if dp[idx] == 2 * dp[idx_2]:
                idx_2 += 1
            if dp[idx] == 3 * dp[idx_3]:
                idx_3 += 1
            if dp[idx] == 5 * dp[idx_5]:
                idx_5 += 1
        return dp[n-1]


if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))
    print(Solution().nthUglyNumber(11))