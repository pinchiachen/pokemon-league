## 2020/11/29

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        for i in range(M // 2):
            matrix[i], matrix[M-i-1] = matrix[M-i-1], matrix[i]
        for x in range(M):
            for y in range(N):
                if y - x <= 0:
                    continue
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]