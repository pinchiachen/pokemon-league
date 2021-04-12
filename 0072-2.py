## 2021/04/12

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        for i in range(l1+1):
            dp[i][0] = i
        for j in range(l2+1):
            dp[0][j] = j
        for x in range(1, l1+1):
            for y in range(1, l2+1):
                if word1[x-1] == word2[y-1]:
                    dp[x][y] = dp[x-1][y-1]
                else:
                    dp[x][y] = min(dp[x-1][y-1], dp[x][y-1], dp[x-1][y]) + 1
        return dp[l1][l2]