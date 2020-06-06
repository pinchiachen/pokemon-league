## 2020/06/06
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stackT = []
        for index, value in enumerate(T):
            while stackT and value > stackT[-1][1]:
                res[stackT[-1][0]] = index - stackT[-1][0]
                stackT.pop()
            stackT.append([index, value])
        return res