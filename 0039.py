## 2020/07/02
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dfs(candidates, target, 0, [], 0)
        return self.res

    def dfs(self, candidates, target, cur_sum, path, index):
        if cur_sum == target:
            self.res.append(path)
        for i in range(index, len(candidates)):
            if cur_sum + candidates[i] <= target:
                self.dfs(candidates, target, cur_sum + candidates[i], path + [candidates[i]], i)

if __name__ == "__main__":
    solve = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(solve.combinationSum(candidates, target))