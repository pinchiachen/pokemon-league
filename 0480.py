## 2021/08/09
import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        res = []
        for idx in range(len(nums)):
            if not max_heap:
                heapq.heappush(max_heap, -nums[idx])
            else:
                heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -nums[idx]))
            self.rebalanceHeaps(max_heap, min_heap)
            if idx < k - 1:
                continue
            median = (
                -max_heap[0]
                if len(min_heap) < len(max_heap)
                else (min_heap[0] - max_heap[0])/2
            )
            res.append(median)
            remove_element = nums[idx - k + 1]
            if remove_element > -max_heap[0]:
                self.removeElement(min_heap, remove_element)
            else:
                self.removeElement(max_heap, -remove_element)
            self.rebalanceHeaps(max_heap, min_heap)
        return res

    def removeElement(self, heap, element):
        idx = heap.index(element)
        heap[idx] = heap[-1]
        heap.pop()
        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)

    def rebalanceHeaps(self, max_heap, min_heap):
        if not min_heap or len(max_heap) >= len(min_heap):
            return
        heapq.heappush(max_heap, -heapq.heappop(min_heap))