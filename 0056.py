## 2020/09/14
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key = lambda x: x[0])
        if len(intervals) == 0:
            return []
        tmp_min = intervals[0][0]
        tmp_max = intervals[0][1]
        for interval in intervals:
            if interval[0] > tmp_max:
                res.append([tmp_min, tmp_max])
                tmp_min = interval[0]
                tmp_max = interval[1]
                continue
            if interval[0] < tmp_min:
                tmp_min = interval[0]
            if interval[1] > tmp_max:
                tmp_max = interval[1]
        res.append([tmp_min, tmp_max])
        return res


if __name__ == "__main__":
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
