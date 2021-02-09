## 2021/02/09

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        if len(s) < 3: return False
        l = len(s)
        dp = [[False] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = True
        for j in range(1, l):
            for i in range(j):
                if s[i] == s[j]:
                    if (j-1)-(i+1)+1 < 2 or dp[i+1][j-1]:
                        dp[i][j] = True
        for i in range(l-1):
            for j in range(i+1, l):
                if dp[0][i] and dp[i+1][j-1] and dp[j][l-1]:
                    return True
        return False

if __name__ == "__main__":
    solve = Solution()
    print(solve.checkPartitioning("bcbddxy"))