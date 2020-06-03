## 2020/06/03
from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [0] * len(nums)
        res = 0
        for i in range(len(nums)):
            tmp = 0
            while visited[i] == 0:
                tmp += 1
                visited[i] = 1
                i = nums[i]
            res = max(res, tmp)
        return res