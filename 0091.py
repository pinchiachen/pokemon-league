## 2020/12/08

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i > 1 and 9 < int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]
        return dp[len(s)]

if __name__ == "__main__":
    print(Solution().numDecodings("111111111111111111111111111111111111111111111"))