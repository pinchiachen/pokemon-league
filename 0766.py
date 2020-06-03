## 2020/06/03
from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 1 or len(matrix[0]) == 1: return True
        x = len(matrix[0]) - 2
        y = 0
        while not (x == 0 and y == len(matrix) - 1):
            if not self.isSame(matrix[y][x], x, y, matrix):
                return False
            if x == 0:
                y += 1
            else:
                x -= 1
        return True

    def isSame(self, target, n, m, matrix):
        M = len(matrix)
        N = len(matrix[0])
        while n < N and m < M:
            if matrix[m][n] != target:
                return False
            n += 1
            m += 1
        return True
