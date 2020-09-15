## 2020/09/15
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if len(intervals) == 0: return [newInterval]
        is_overlap = False
        for index, interval in enumerate(intervals):
            if not is_overlap and newInterval[0] < interval[0] and newInterval[1] < interval[0]:
                res.append(newInterval)
                res += intervals[index:]
                return res
            elif not is_overlap and newInterval[0] <= interval[1]:
                is_overlap = True
                start = min(interval[0], newInterval[0])
                end = max(interval[1], newInterval[1])
            elif is_overlap:
                if interval[0] <= end:
                    start = min(interval[0], start)
                    end = max(interval[1], end)
                else:
                    res.append([start, end])
                    res += intervals[index:]
                    return res
            else:
                res.append(interval)
        if not is_overlap:
            res.append(newInterval)
        else:
            res.append([start, end])
        return res

if __name__ == "__main__":
    print(Solution().insert([[1,3],[6,9]], [2,5]))
    print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))