## 2020/11/24

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        res = []
        candidates.sort()
        self.dfs(res, candidates, target, [], 0)
        return res

    def dfs(self, res, nums, target, path, cur_sum):
        if cur_sum == target:
            res.append(path)
            return
        for idx, num in enumerate(nums):
            if cur_sum + num > target:
                break
            self.dfs(res, nums[idx:], target, path + [num], cur_sum + num)
