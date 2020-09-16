## 2020/09/16
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        visited = [[0 for i in range(n)] for j in range(n)]
        x = 0
        y = 0
        vector = 0
        count = 0
        while count < n * n:
            if vector % 4 == 0:
                while True:
                    res[x][y] = count + 1
                    visited[x][y] = 1
                    y += 1
                    count += 1
                    if y >= n or visited[x][y] == 1:
                        y -= 1
                        x += 1
                        vector += 1
                        break
            elif vector % 4 == 1:
                while True:
                    res[x][y] = count + 1
                    visited[x][y] = 1
                    x += 1
                    count += 1
                    if x >= n or visited[x][y] == 1:
                        x -= 1
                        y -= 1
                        vector += 1
                        break
            elif vector % 4 == 2:
                while True:
                    res[x][y] = count + 1
                    visited[x][y] = 1
                    y -= 1
                    count += 1
                    if y < 0 or visited[x][y] == 1:
                        y += 1
                        x -= 1
                        vector += 1
                        break
            elif vector % 4 == 3:
                while True:
                    res[x][y] = count + 1
                    visited[x][y] = 1
                    x -= 1
                    count += 1
                    if x < 0 or visited[x][y] == 1:
                        x += 1
                        y += 1
                        vector += 1
                        break
        return res

if __name__ == "__main__":
    print(Solution().generateMatrix(3))