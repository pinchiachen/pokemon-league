## 2021/08/09
from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        return (-self.max_heap[0] if len(self.min_heap) < len(self.max_heap) else (self.min_heap[0] - self.max_heap[0])/2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()