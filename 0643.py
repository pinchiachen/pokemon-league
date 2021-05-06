## 2021/05/06

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -float('inf')
        cur_sum = 0
        left = 0
        right = 0
        while right < len(nums):
            cur_sum += nums[right]
            if right >= (k - 1):
                res = max(res, cur_sum / k)
                cur_sum -= nums[left]
                left += 1
            right += 1
        return res