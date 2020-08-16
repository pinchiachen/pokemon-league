## 2020/08/17
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != (i + 1): return (i + 1)
        return len(nums) + 1

if __name__ == "__main__":
    solve = Solution()
    nums = [7,8,9,11,12]
    print(solve.firstMissingPositive(nums))