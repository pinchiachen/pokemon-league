## 2021/08/10
from typing import List
from heapq import *

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        length = len(intervals)
        res = [-1] * length
        max_start_heap = []
        max_end_heap = []
        for idx, [start, end] in enumerate(intervals):
            heappush(max_start_heap, (-start, idx))
            heappush(max_end_heap, (-end, idx))
        for _ in range(length):
            cur_end, end_idx = heappop(max_end_heap)
            cur_start, start_idx = None, None
            while max_start_heap and (-max_start_heap[0][0] >= -cur_end):
                cur_start, start_idx = heappop(max_start_heap)
            if start_idx != None:
                res[end_idx] = start_idx
                heappush(max_start_heap, (cur_start, start_idx))
        return res

if __name__ == '__main__':
    print(Solution().findRightInterval([[3,4],[2,3],[1,2]]))
