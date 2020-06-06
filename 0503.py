## 2020/06/06
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        originLength = len(nums)
        res = [-1] * len(nums)
        stack = []
        nums = nums + nums
        for index, value in enumerate(nums):
            while stack and value > stack[-1][1]:
                res[stack[-1][0]] = value
                stack.pop()
            if index < originLength:
                stack.append([index, value])
        return res