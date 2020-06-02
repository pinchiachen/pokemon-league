## 2020/06/02
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashArr = [0] * len(nums)
        for i in range(len(nums)):
            hashArr[nums[i] - 1] += 1
        return [hashArr.index(2) + 1, hashArr.index(0) + 1]