## 2020/06/30
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        size = len(nums)
        self.res = []
        for i in range(len(nums)):
            self.dfs(size, nums[:i] + nums[i + 1:], [nums[i]])
        return self.res

    def dfs(self, size, nums, path):
        if len(path) == size:
            self.res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(size, nums[:i] + nums[i + 1:], path + [nums[i]])

if __name__ == "__main__":
    solve = Solution()
    nums = [1,2,3]
    print(solve.permute(nums))
