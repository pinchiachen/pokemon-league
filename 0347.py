## 2020/12/30
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        heap = []
        res = []
        for num in nums:
            freq_map[num] = 1 if num not in freq_map else freq_map[num] + 1
        for key, val in freq_map.items():
            heapq.heappush(heap, (-val, key))
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

if __name__ == "__main__":
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))