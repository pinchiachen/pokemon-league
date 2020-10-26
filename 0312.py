## 2020/10/26

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * (n+2) for _ in range(n+2)]
        for l in range(1, n+1):
            for start in range(1, n-l+2):
                end = start + l - 1
                for mid in range(start, end+1):
                    dp[start][end] = max(dp[start][end], dp[start][mid-1] + dp[mid+1][end] + nums[start-1]*nums[mid]*nums[end+1])
        return dp[1][n]