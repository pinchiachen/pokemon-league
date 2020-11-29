## 2020/11/29

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = -float('inf')
        max_sum = -float('inf')
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum