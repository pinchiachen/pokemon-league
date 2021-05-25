## 2021/05/26
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        elif newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        elif newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        res = []
        for interval in intervals:
            if newInterval and newInterval[0] <= interval[0]:
                res = self.mergeInterval(res, newInterval)
                newInterval = None
                res = self.mergeInterval(res, interval)
            elif newInterval:
                res.append(interval)
            else:
                res = self.mergeInterval(res, interval)
        if newInterval:
            res = self.mergeInterval(res, newInterval)
        return res

    def mergeInterval(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
        elif interval[0] > intervals[-1][1]:
            intervals.append(interval)
        else:
            intervals[-1][0] = min(intervals[-1][0], interval[0])
            intervals[-1][1] = max(intervals[-1][1], interval[1])
        return intervals

if __name__ == '__main__':
    print(Solution().insert([[1,3],[6,9],], [2,5]))
    print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(Solution().insert([], [5,7]))
    print(Solution().insert([[1,5]], [2,3]))
    print(Solution().insert([[1,5]], [2,7]))