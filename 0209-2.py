## 2021/05/06

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        right = 0
        cur_sum = 0
        while right < len(nums):
            cur_sum += nums[right]
            while cur_sum >= target:
                if right == left: return 1
                res = min(res, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        return res if res != float('inf') else 0