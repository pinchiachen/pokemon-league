## 2020/06/07
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key = lambda e: e[1])
        validArr = []
        for element in intervals:
            if validArr and element[0] < validArr[-1][1]:
                continue
            else:
                validArr.append(element)
        return len(intervals) - len(validArr)