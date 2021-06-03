## 2021/06/04

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        idx = 0
        n = len(nums)
        while idx < n:
            if nums[idx] > 0 and nums[idx] < n and nums[idx] != nums[nums[idx] - 1]:
                tmp = nums[idx] - 1
                nums[idx], nums[tmp] = nums[tmp], nums[idx]
            else:
                idx += 1
        for idx in range(n):
            if nums[idx] != idx + 1:
                return idx + 1
        return n + 1