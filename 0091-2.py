## 2021/04/08

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        l = len(s)
        dp = [0] * l
        for i in range(l):
            if s[i] != '0':
                dp[i] += (dp[i-1] if i > 0 else 1)
            if i > 0 and 10 <= int(s[i-1:i+1]) < 27:
                dp[i] += (dp[i-2] if i > 1 else 1)
        return dp[-1]