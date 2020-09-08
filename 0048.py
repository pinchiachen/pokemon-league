## 2020/09/08
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):
            matrix[i], matrix[len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i], matrix[i]
        x = 0
        y = len(matrix[0]) - 1
        while x >= 0 and x < len(matrix) - 1 and y >= 0 and y < len(matrix[0]):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
            y -= 1
            if y == x:
                x += 1
                y = len(matrix[0]) - 1

if __name__ == "__main__":
    Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])
