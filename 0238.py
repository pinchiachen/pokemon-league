## 2020/06/06
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        res = [0] * len(nums)
        tmp = 1
        for i in range(len(nums)):
            tmp *= nums[i]
            left[i] = tmp
        tmp = 1
        for j in range(len(nums) - 1, -1, -1):
            tmp *= nums[j]
            right[j] = tmp
        for k in range(1, len(nums) - 1):
            res[k] = (left[k - 1] * right[k + 1])
        res[0] = (right[1])
        res[-1] = (left[-2])
        return res