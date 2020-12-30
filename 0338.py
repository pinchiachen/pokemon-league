## 2020/12/30

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, len(dp)):
            dp[i] = dp[i//2] if (i % 2 == 0) else dp[(i-1)//2] + 1
        return dp