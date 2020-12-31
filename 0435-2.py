## 2020/12/31

## len(intervals) - len(max_non_overlap_intervals)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        non_overlaps = []
        intervals.sort(key = lambda x: x[1])
        for interval in intervals:
            if not non_overlaps or interval[0] >= non_overlaps[-1][1]:
                non_overlaps.append(interval)
        return len(intervals) - len(non_overlaps)