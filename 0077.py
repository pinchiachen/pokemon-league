## 2020/07/01
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        visited = [0] * n
        self.dfs(k, n, [], visited, 1)
        return self.res

    def dfs(self, k, n, path, visited, index):
        if len(path) == k:
            self.res.append(path)
            return
        for i in range(index, n - (k - len(path)) + 2):
            if visited[i - 1] == 0:
                visited[i - 1] = 1
                self.dfs(k, n, path + [i], visited, i)
                visited[i - 1] = 0

if __name__ == "__main__":
    solve = Solution()
    n = 4
    k = 2
    print(solve.combine(n, k))