## 2020/07/12
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target: return [-1, -1]
        right = left
        while True:
            if left > 0 and nums[left - 1] == target:
                left -= 1
            elif right < len(nums) - 1 and nums[right + 1] == target:
                right += 1
            else:
                break
        return [left, right]

if __name__ == "__main__":
    solve = Solution()
    nums = [5,7,7,8,8,10]
    target = 6
    print(solve.searchRange(nums, target))