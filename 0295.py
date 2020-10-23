## 2020/10/23
from heapq import *

## max heap and min heap
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
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

## Brute force
class BadMedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.start = 0
        self.end = 0

    def addNum(self, num: int) -> None:
        is_insert = False
        for i in range(len(self.arr)):
            if self.arr[i] >= num:
                self.arr.insert(i, num)
                is_insert = True
                break
        if not is_insert:
            self.arr.append(num)
        if len(self.arr) > 1:
            if len(self.arr) % 2 == 0:
                self.end += 1
            else:
                self.start += 1

    def findMedian(self) -> float:
        return (self.arr[self.start] + self.arr[self.end]) / 2

if __name__ == "__main__":
    median_finder = MedianFinder()
    median_finder.addNum(6)
    median_finder.addNum(10)
    median_finder.addNum(2)
    median_finder.addNum(6)
    median_finder.addNum(5)
    print(median_finder.findMedian())