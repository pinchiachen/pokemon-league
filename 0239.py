## 2020/10/22
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        monotonic_queue = collections.deque()
        for i in range(len(nums)):
            while monotonic_queue and nums[i] > monotonic_queue[-1]:
                monotonic_queue.pop()
            monotonic_queue.append(nums[i])
            if i >= k - 1:
                res.append(monotonic_queue[0])
                if nums[i - k + 1] == monotonic_queue[0]:
                    monotonic_queue.popleft()
        return res