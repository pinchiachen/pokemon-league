## 2021/03/16
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = nums[k]
        min_val = nums[k]
        l = len(nums)
        right = k
        left = k
        while (right + 1) < l or (left - 1) >= 0:
            if (right + 1) < l and (left - 1) >= 0 and nums[right + 1] > nums[left - 1] or (left - 1) < 0:
                min_val = min(min_val, nums[right + 1])
                res = max(res, min_val * (right + 1 - left + 1))
                right += 1
            else:
                min_val = min(min_val, nums[left - 1])
                res = max(res, min_val * (right - (left - 1) + 1))
                left -= 1
        return res

if __name__ == '__main__':
    print(Solution().maximumScore([1,4,3,7,4,5], 3))
    print(Solution().maximumScore([5,5,4,5,4,1,1,1], 0))