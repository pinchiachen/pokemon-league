## 2020/06/07
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left = right = 0
        res = 0
        while left < len(g) and right < len(s):
            if s[right] >= g[left]:
                right += 1
                left += 1
                res += 1
            else:
                right += 1
        return res