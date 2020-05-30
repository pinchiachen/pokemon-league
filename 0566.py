## 2020/05/30
from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        res = [[0] * c for _ in range(r)]
        count = 0
        for i in range(m):
            for j in range(n):
                res[count // c][count % c] = nums[i][j]
                count += 1
        return res