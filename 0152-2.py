## 2020/12/11

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        last_max = nums[0]
        last_min = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(last_max * nums[i], last_min * nums[i], nums[i])
            cur_min = min(last_max * nums[i], last_min * nums[i], nums[i])
            res = max(res, cur_max)
            last_max = cur_max
            last_min = cur_min
        return res