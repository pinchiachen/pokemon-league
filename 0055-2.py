## 2020/12/02

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for idx, value in enumerate(nums):
            if idx > max_reach: return False
            max_reach = max(max_reach, idx + value)
            if max_reach >= len(nums) - 1: return True
