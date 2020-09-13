## 2020/09/13
from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for idx, val in enumerate(nums):
            if idx > max_reach: return False
            max_reach = max(max_reach, idx + val)
        return True

if __name__ == "__main__":
    print(Solution().canJump([2,3,1,1,4]))
    print(Solution().canJump([3,2,1,0,4]))