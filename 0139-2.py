## 2020/11/12
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * (l+1)
        dp[0] = True
        for i in range(1, l+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[l]

if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]))