## 2020/06/22
from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if len(M) == 0: return 0
        viseted = set()
        m = len(M)
        res = 0
        for i in range(m):
            if i not in viseted:
                self.dfs(i, m, M, viseted)
                res += 1
        return res

    def dfs(self, i, m, M, visited):
        for j in range(m):
            if M[i][j] == 1 and j not in visited:
                visited.add(j)
                self.dfs(j, m, M, visited)

if __name__ == "__main__":
    Solve = Solution()
    M = [[1,1,0],[1,1,0],[0,0,1]]
    print(Solve.findCircleNum(M))