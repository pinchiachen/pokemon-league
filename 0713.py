## 2021/05/12

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = len(nums)
        res = 0
        cur = 1
        left = 0
        for right in range(l):
            cur *= nums[right]
            while left <= right and cur >= k:
                cur /= nums[left]
                left += 1
            res += (right - left + 1)
        return res