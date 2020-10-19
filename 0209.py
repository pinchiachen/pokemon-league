## 2020/10/20
from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        length = len(nums)
        left = 0
        right = 0
        cur = 0
        res = float('inf')
        while right < length:
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                left += 1
                cur -= nums[left - 1]
            right += 1
        return 0 if res == float('inf') else res

if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))