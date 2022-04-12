## 2022/04/12

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid == right:
                return nums[mid]
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1