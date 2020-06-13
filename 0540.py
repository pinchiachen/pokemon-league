## 2020/06/13
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]

if __name__ == "__main__":
    Solve = Solution()
    # nums = [1,1,2,3,3,4,4,8,8]
    nums = [1,1,2]
    Solve.singleNonDuplicate(nums)
