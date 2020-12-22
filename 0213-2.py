## 2020/12/22

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l = len(nums)
        pre_nums = nums[:-1]
        post_nums = nums[1:]
        dp_pre = [[0, 0] for _ in range(l)]
        dp_post = [[0, 0] for _ in range(l)]
        for i in range(1, l):
            dp_pre[i][0] = dp_pre[i-1][1]
            dp_pre[i][1] = max(dp_pre[i-1][1], dp_pre[i-1][0] + pre_nums[i-1])
            dp_post[i][0] = dp_post[i-1][1]
            dp_post[i][1] = max(dp_post[i-1][1], dp_post[i-1][0] + post_nums[i-1])
        return max(dp_pre[-1][1], dp_post[-1][1])