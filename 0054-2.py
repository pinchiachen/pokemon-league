## 2020/11/30
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        N = len(matrix[0])
        res = []
        visited = [[0] * N for _ in range(M)]
        x = -1
        y = -1
        while True:
            is_end, x, y = self.goStraight(matrix, x+1, y+1, M, N, 'right', visited, res)
            if is_end: break
            is_end, x, y = self.goStraight(matrix, x+1, y-1, M, N, 'bottom', visited, res)
            if is_end: break
            is_end, x, y = self.goStraight(matrix, x-1, y-1, M, N, 'left', visited, res)
            if is_end: break
            is_end, x, y = self.goStraight(matrix, x-1, y+1, M, N, 'top', visited, res)
            if is_end: break
        return res

    def goStraight(self, matrix, x, y, M, N, direction, visited, res):
        is_end = True
        while 0 <= x < M and 0 <= y < N and not visited[x][y]:
            is_end = False
            if direction == 'right':
                res.append(matrix[x][y])
                visited[x][y] = 1
                y += 1
            elif direction == 'left':
                res.append(matrix[x][y])
                visited[x][y] = 1
                y -= 1
            elif direction == 'bottom':
                res.append(matrix[x][y])
                visited[x][y] = 1
                x += 1
            elif direction == 'top':
                res.append(matrix[x][y])
                visited[x][y] = 1
                x -= 1
        return (is_end, x, y)

if __name__ == "__main__":
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))