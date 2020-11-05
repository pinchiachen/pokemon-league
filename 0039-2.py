## 2020/11/05

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, 0, [], res)
        return res

    def dfs(self, nums, target, idx, cur, path, res):
        if cur == target:
            res.append(path)
            return
        for i in range(idx, len(nums)):
            if nums[i] > target: break
            if cur + nums[i] <= target:
                self.dfs(nums, target, i, cur + nums[i], path + [nums[i]], res)