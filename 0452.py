## 2020/06/07
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key = lambda x: x[1])
        validArr = []
        for point in points:
            if validArr and point[0] <= validArr[-1][1]:
                continue
            else:
                validArr.append(point)
        return len(validArr)