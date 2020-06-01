## 2020/06/01
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                res = max(res, count)
                count = 0
        return res