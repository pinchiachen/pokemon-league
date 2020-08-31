## 2020/09/01

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S = len(s)
        P = len(p)
        dp = [[False for i in range(P + 1)] for j in range(S + 1)]
        dp[0][0] = True
        for i in range(1, P + 1):
            dp[0][i] = ((p[i - 1] == '*') and dp[0][i - 1])
        for i in range(1, S + 1):
            for j in range(1, P + 1):
                if (p[j - 1] == s[i - 1]) or (p[j - 1] == '?'):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[S][P]

if __name__ == "__main__":
    print(Solution().isMatch('aa', 'a'))