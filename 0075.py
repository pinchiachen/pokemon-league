## 2020/09/21
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_arr = [0, 0, 0]
        index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_arr[0] += 1
            elif nums[i] == 1:
                count_arr[1] += 1
            elif nums[i] == 2:
                count_arr[2] += 1
        while index < len(nums):
            if index < count_arr[0]:
                nums[index] = 0
            elif index < count_arr[0] + count_arr[1]:
                nums[index] = 1
            else:
                nums[index] = 2
            index += 1

if __name__ == "__main__":
    print(Solution().sortColors([2,0,2,1,1,0]))
    print(Solution().sortColors([1,0]))
    print(Solution().sortColors([1,2,0]))
