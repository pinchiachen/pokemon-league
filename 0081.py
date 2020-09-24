## 2020/09/24
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0: return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] == nums[right]:
                left +=1
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] <= nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

if __name__ == "__main__":
    print(Solution().search([2,5,6,0,0,1,2], 0))
    print(Solution().search([2,5,6,0,0,1,2], 3))