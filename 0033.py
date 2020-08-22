## 2020/08/23
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] == target: return mid
            if nums[mid] <= nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else: right = mid - 1
            else:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            mid = (left + right) // 2
        return -1

if __name__ == "__main__":
    solve = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 3
    print(solve.search(nums, target))
