## 2020/07/05
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        visited = [0] * len(nums)
        self.dfs(nums, [], 0, visited)
        return self.res

    def dfs(self, nums, path, index, visited):
        self.res.append(path)
        for i in range(index, len(nums)):
            if not visited[i]:
                visited[i] = 1
                self.dfs(nums, path + [nums[i]], i, visited)
                visited[i] = 0

if __name__ == "__main__":
    solve = Solution()
    nums = [1, 2, 3]
    print(solve.subsets(nums))