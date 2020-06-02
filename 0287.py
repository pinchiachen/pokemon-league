## 2020/06/02
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashArr = [0] * len(nums)
        for num in nums:
            hashArr[num - 1] += 1
            if hashArr[num - 1] > 1:
                return num