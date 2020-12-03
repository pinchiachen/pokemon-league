## 2020/12/03
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        elif newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        for idx, interval in enumerate(intervals):
            if newInterval[0] <= interval[0]:
                intervals.insert(idx, newInterval)
                newInterval = None
                break
        if newInterval: intervals.append(newInterval)
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

if __name__ == "__main__":
    print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))