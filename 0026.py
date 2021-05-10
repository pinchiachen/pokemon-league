## 2021/05/10

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == nums[i+1]:
                del nums[i]
        return len(nums)