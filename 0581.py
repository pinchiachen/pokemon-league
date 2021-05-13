## 2021/05/13
from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        l = len(nums)
        cur_max = -float('inf')
        cur_min = float('inf')
        left = 0
        right = 0
        for i in range(l):
            if nums[i] < cur_max:
                right = i
            cur_max = max(cur_max, nums[i])
        for j in range(l-1, -1, -1):
            if nums[j] > cur_min:
                left = j
            cur_min = min(cur_min, nums[j])
        return 0 if left == right else (right - left + 1)

if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([1, 3, 3, 2, 2, 5]))
    print(Solution().findUnsortedSubarray([1, 2, 4, 5, 3]))
    print(Solution().findUnsortedSubarray([1, 2, 3, 4, 5]))
    print(Solution().findUnsortedSubarray([1, 3, 1, 3, 2, 1, 2, 5]))
    print(Solution().findUnsortedSubarray([1, 1, 1]))