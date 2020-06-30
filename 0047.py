## 2020/06/30
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        nums.sort()
        self.res = []
        visited = [0] * len(nums)
        self.dfs(nums, [], visited)
        return self.res

    def dfs(self, nums, path, visited):
        if len(path) == len(nums):
            self.res.append(path)
            return
        for i in range(len(nums)):
            if visited[i] == 1: continue
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0: continue
            visited[i] = 1
            self.dfs(nums, path + [nums[i]], visited)
            visited[i] = 0

if __name__ == "__main__":
    solve = Solution()
    nums = [1,1,2]
    print(solve.permuteUnique(nums))
