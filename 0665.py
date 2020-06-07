## 2020/06/07
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not nums: return True
        count = 0
        for i in range(len(nums) - 1):
            if count > 1: return False
            if nums[i] <= nums[i + 1]:
                continue
            count += 1
            if i > 0 and nums[i + 1] < nums[i - 1]:
                nums[i + 1] = nums[i]
            else:
                nums[i] = nums[i + 1]
        return count <= 1