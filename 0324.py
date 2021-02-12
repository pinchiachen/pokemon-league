## 2021/02/12
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        mid = (l+1)//2
        sorted_nums = sorted(nums)
        left = sorted_nums[:mid]
        right = sorted_nums[mid:]
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1]
        return nums

if __name__ == "__main__":
    print(Solution().wiggleSort([4,5,5,6]))
