## 2021/08/09
from heapq import *

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        res = w
        cant_do_heap = []
        can_do_heap = []
        for c, p in zip(capital, profits):
            heappush(cant_do_heap, (c, -p))
        while k > 0:
            while cant_do_heap and res >= cant_do_heap[0][0]:
                c, minus_p = heappop(cant_do_heap)
                heappush(can_do_heap, minus_p)
            if can_do_heap:
                res += -heappop(can_do_heap)
            k -= 1
        return res