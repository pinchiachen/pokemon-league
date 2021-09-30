## 2021/09/30

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        max_index = self.findMaxIndex(mountain_arr)
        key_index = self.binarySearch(mountain_arr, target, 0, max_index)
        return key_index if key_index != -1 else self.binarySearch(mountain_arr, target, max_index+1, mountain_arr.length()-1)

    def findMaxIndex(self, arr):
        left = 0
        right = arr.length() - 1
        while left < right:
            mid = left + (right-left)//2
            if arr.get(mid) < arr.get(mid+1):
                left = mid + 1
            else:
                right = mid
        return left

    def binarySearch(self, arr, target, left, right):
        is_asc = arr.get(right) > arr.get(left)
        while left <= right:
            mid = left + (right-left)//2
            if arr.get(mid) == target:
                return mid
            if is_asc:
                if arr.get(mid) < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if arr.get(mid) < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1