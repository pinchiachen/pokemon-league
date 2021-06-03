## 2021/06/03

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        idx = 0
        n = len(nums)
        res = []
        while idx < n:
            while nums[idx] != nums[nums[idx]-1]:
                tmp = nums[idx] - 1
                nums[idx], nums[tmp] = nums[tmp], nums[idx]
            idx += 1
        for idx in range(n):
            if nums[idx] != (idx+1):
                res.append(idx+1)
        return res