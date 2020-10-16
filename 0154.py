## 2020/10/16
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            while nums[left] == nums[right] and left < right:
                left += 1
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[right]

if __name__ == "__main__":
    print(Solution().findMin([2,2,2,0,1]))