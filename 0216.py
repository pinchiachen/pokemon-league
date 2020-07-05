## 2020/07/05
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        visited = [0] * n
        self.dfs(k, n, [], 1, visited, 0)
        return self.res

    def dfs(self, k, n, path, index, visited, cur_sum):
        if len(path) == k and cur_sum == n:
            self.res.append(path)
            return
        for i in range(index, 10):
            if cur_sum + i <= n and not visited[i - 1]:
                visited[i - 1] = 1
                self.dfs(k, n, path + [i], i, visited, cur_sum + i)
                visited[i - 1] = 0

if __name__ == "__main__":
    solve = Solution()
    k = 3
    n = 9
    print(solve.combinationSum3(k, n))