## 2021/05/12
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        end = l - 1
        left = 0
        while left < end:
            while end > 0 and nums[end] == 2:
                end -= 1
            if left < end and nums[left] == 2:
                nums[left], nums[end] = nums[end], nums[left]
                end -= 1
            left += 1
        left = 0
        while left < end:
            while end > 0 and (nums[end] == 2 or nums[end] == 1):
                end -= 1
            if left < end and nums[left] == 1:
                nums[left], nums[end] = nums[end], nums[left]
                end -= 1
            left += 1

if __name__ == '__main__':
    Solution().sortColors([2, 2, 1])