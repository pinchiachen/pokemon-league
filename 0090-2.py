## 2020/10/30
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = [0] * len(nums)
        self.dfs(nums, 0, [], visited, res)
        return res

    def dfs(self, nums, index, path, visited, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            visited[i] = 1
            self.dfs(nums, i + 1, path + [nums[i]], visited, res)
            visited[i] = 0

if __name__ == "__main__":
    print(Solution().subsetsWithDup([1,2,2]))
