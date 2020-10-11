## 2020/10/11

class Solution:
    def minCut(self, s: str) -> int:
        l = len(s)
        dp = [-1] * (len(s) + 1)
        is_pal = [[False] * l for _ in range(l)]
        for i in range(l):
            dp[i+1] = i
            for j in range(i+1):
                if s[i] == s[j] and ((i-j < 2) or is_pal[j+1][i-1]):
                    is_pal[j][i] = True
                    dp[i+1] = min(dp[i+1], 1+dp[j])
        return dp[l]

if __name__ == "__main__":
    print(Solution().minCut("aab"))