## 2021/04/05

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = -float('inf')
        res = -float('inf')
        for num in nums:
            cur_max = max(cur_max + num, num)
            res = max(res, cur_max)
        return res