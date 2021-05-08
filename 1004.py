## 2021/05/08

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        res = 0
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res