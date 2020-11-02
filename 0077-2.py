## 2020/11/02

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(1, n, k, [], res)
        return res

    def dfs(self, idx, n, k, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(idx, n+1):
            # if cur_length + rest_element_count < k => not enough
            if len(path) + (n + 1 - idx) < k: break
            self.dfs(i + 1, n, k, path + [i], res)