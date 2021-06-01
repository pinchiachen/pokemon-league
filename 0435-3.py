## 2021/06/02

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        non_overlap = []
        for interval in intervals:
            if not non_overlap or interval[0] >= non_overlap[-1][1]:
                non_overlap.append(interval)
        return len(intervals) - len(non_overlap)