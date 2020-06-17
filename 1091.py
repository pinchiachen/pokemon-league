## 2020/06/17
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1        
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
            [1, 1],
            [-1, 1],
            [-1, -1],
            [1, -1],
        ]
        pathQueue = [(0, 0, 1)]
        length = len(grid)
        while len(pathQueue) > 0:
            x0, y0, count = pathQueue.pop(0)
            if x0 == y0 == length - 1: return count     
            for dx, dy in directions:
                x = x0 + dx
                y = y0 + dy
                if 0 <= x < length and 0 <= y < length and grid[x][y] != 1:
                    pathQueue.append((x, y, count + 1))
                    grid[x][y] = 1
        return -1

if __name__ == "__main__":
    Solve = Solution()
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    print(Solve.shortestPathBinaryMatrix(grid))