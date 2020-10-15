## 2020/10/15

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        l = len(nums)
        res = nums[0]
        max_val = [0] * l
        min_val = [0] * l
        max_val[0] = nums[0]
        min_val[0] = nums[0]
        for i in range(1, l):
            max_val[i] = max(max_val[i-1]*nums[i], min_val[i-1]*nums[i], nums[i])
            min_val[i] = min(max_val[i-1]*nums[i], min_val[i-1]*nums[i], nums[i])
            res = max(res, max_val[i], min_val[i])
        return res