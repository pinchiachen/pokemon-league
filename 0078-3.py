## 2021/08/11

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            length = len(res)
            for idx in range(length):
                res.append(res[idx] + [num])
        return res