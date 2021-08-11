## 2021/08/11

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        start = 0
        end = 0
        for i in range(len(nums)):
            start = end if (i > 0 and nums[i] == nums[i-1]) else 0
            end = len(res)
            for j in range(start, end):
                res.append(res[j] + [nums[i]])
        return res