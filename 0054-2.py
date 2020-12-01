## 2020/11/30
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        N = len(matrix[0])
        res = []
        visited = [[0] * N for _ in range(M)]
        directions = ['right', 'bottom', 'left', 'top']
        x = 0
        y = 0
        while True:
            for direction in directions:
                is_end, x, y = self.goStraight(matrix, x, y, M, N, direction, visited, res)
                if is_end: break
            if is_end: break
        return res

    def goStraight(self, matrix, x, y, M, N, direction, visited, res):
        is_end = True
        while 0 <= x < M and 0 <= y < N and not visited[x][y]:
            is_end = False
            res.append(matrix[x][y])
            visited[x][y] = 1
            if direction == 'right':
                y += 1
            elif direction == 'left':
                y -= 1
            elif direction == 'bottom':
                x += 1
            elif direction == 'top':
                x -= 1
        if direction == 'right':
            x += 1
            y -= 1
        elif direction == 'left':
            x -= 1
            y += 1
        elif direction == 'bottom':
            x -= 1
            y -= 1
        elif direction == 'top':
            x += 1
            y += 1
        return (is_end, x, y)

if __name__ == "__main__":
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))