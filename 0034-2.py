## 2021/09/16

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        res[0] = self.binarySearch(nums, target, False)
        if res[0] != -1:
            res[1] = self.binarySearch(nums, target, True)
        return res

    def binarySearch(self, nums, target, find_max):
        index = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                index = mid
                if find_max:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index
