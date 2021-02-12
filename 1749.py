## 2021/02/12

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        tmp_max = -float('inf')
        min_sum = float('inf')
        tmp_min = float('inf')
        for num in nums:
            tmp_max = max(tmp_max+num, num)
            max_sum = max(max_sum, tmp_max)
            tmp_min = min(tmp_min+num, num)
            min_sum = min(min_sum, tmp_min)
        return max(abs(max_sum), abs(min_sum))
