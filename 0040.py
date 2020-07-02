## 2020/07/02
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        visited = [0] * len(candidates)
        self.dfs(candidates, target, 0, [], 0, visited)
        return self.res

    def dfs(self, candidates, target, cur_sum, path, index, visited):
        if cur_sum == target:
            self.res.append(path)
        for i in range(index, len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1] and visited[i - 1] == 0:
                continue
            if cur_sum + candidates[i] <= target and not visited[i]:
                visited[i] = 1
                self.dfs(candidates, target, cur_sum + candidates[i], path + [candidates[i]], i, visited)
                visited[i] = 0

if __name__ == "__main__":
    solve = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(solve.combinationSum2(candidates, target))