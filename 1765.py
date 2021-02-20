## 2021/02/21
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        M = len(isWater)
        N = len(isWater[0])
        queue = []
        for x in range(M):
            for y in range(N):
                if isWater[x][y] == 0:
                    isWater[x][y] = float('inf')
                else:
                    isWater[x][y] = 0
                    queue.append([x, y, 1])
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        visited = [[0] * N for _ in range(M)]
        self.bfs(isWater, directions, M, N, visited, queue)
        return isWater

    def bfs(self, matrix, directions, M, N, visited, queue):
        while queue:
            x0, y0, level = queue.pop(0)
            for dx, dy in directions:
                x = x0 + dx
                y = y0 + dy
                if 0 <= x < M  and 0 <= y < N and not visited[x][y] and matrix[x][y] > 0:
                    visited[x][y] = 1
                    matrix[x][y] = min(matrix[x][y], level)
                    queue.append([x, y, level+1])


if __name__ == "__main__":
    print(Solution().highestPeak([[0,1],[0,0]]))
    print(Solution().highestPeak([[0,0,1],[1,0,0],[0,0,0]]))