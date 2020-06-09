## 2020/06/10
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        preSum = -float('inf')
        maxSum = -float('inf')
        for num in nums:
            preSum = preSum + num if preSum > 0 else num
            maxSum = max(maxSum, preSum)
        return maxSum