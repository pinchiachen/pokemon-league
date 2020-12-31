## 2020/12/31

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        l = len(s)
        dp = [[False] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = True
            for j in range(i+1):
                dp[j][i] = s[i] == s[j] and (i - j < 2 or dp[j+1][i-1])
                if dp[j][i]:
                    res += 1
        return res