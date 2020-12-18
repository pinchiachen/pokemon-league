## 2020/12/18

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[0, 0] for _ in range(l + 1)]
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = max(dp[i-1][0] + nums[i-1], dp[i-1][1])
        return max(dp[l][0], dp[l][1])