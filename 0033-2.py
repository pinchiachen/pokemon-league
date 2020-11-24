## 2020/11/24

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]: # the right part is longer
                if target > nums[mid] and target <= nums[right]: # target is on the right of mid
                    left = mid + 1
                else: # target is on the left of mid
                    right = mid - 1
            else: # the left part is longer
                if target < nums[mid] and target >= nums[left]: # target is on the left of mid
                    right = mid - 1
                else: # target is on the right of mid
                    left = mid + 1
        return -1
