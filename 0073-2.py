## 2020/12/07

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        rows = []
        cols = []
        for row in range(M):
            for col in range(N):
                if matrix[row][col] == 0:
                    rows.append(row)
                    cols.append(col)
        for row in set(rows):
            for col in range(N):
                matrix[row][col] = 0
        for row in range(M):
            for col in set(cols):
                matrix[row][col] = 0