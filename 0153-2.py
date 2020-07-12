## 2020/07/12

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        for num in nums:
            res = min(res, num)
        return res