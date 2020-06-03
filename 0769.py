## 2020/06/03
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr: return 0
        res = 0
        curMax = arr[0]
        for i in range(len(arr)):
            curMax = max(curMax, arr[i])
            if curMax == i:
                res += 1
        return res