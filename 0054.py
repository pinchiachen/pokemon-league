## 2020/09/11
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0 or len(matrix[0]) == 0: return res
        M = len(matrix)
        N = len(matrix[0])
        x = 0
        y = 0
        count = 0
        visited = [[0 for i in range(N)] for j in range(M)]
        while len(res) < M * N:
            if count % 4 == 0:
                while True:
                    res.append(matrix[x][y])
                    visited[x][y] = 1
                    y += 1
                    if y >= N or visited[x][y] == 1:
                        y -= 1
                        x += 1
                        count += 1
                        break
            elif count % 4 == 1:
                while True:
                    res.append(matrix[x][y])
                    visited[x][y] = 1
                    x += 1
                    if x >= M or visited[x][y] == 1:
                        x -= 1
                        y -= 1
                        count += 1
                        break
            elif count % 4 == 2:
                while True:
                    res.append(matrix[x][y])
                    visited[x][y] = 1
                    y -= 1
                    if y < 0 or visited[x][y] == 1:
                        y += 1
                        x -= 1
                        count += 1
                        break
            elif count % 4 == 3:
                while True:
                    res.append(matrix[x][y])
                    visited[x][y] = 1
                    x -= 1
                    if x < 0 or visited[x][y] == 1:
                        x += 1
                        y += 1
                        count += 1
                        break
        return res

if __name__ == "__main__":
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))