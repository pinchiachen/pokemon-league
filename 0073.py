## 2020/09/20
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        rows_dict = dict()
        cols_dict = dict()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    if row not in rows_dict:
                        rows.append(row)
                        rows_dict[row] = 1
                    if col not in cols_dict:
                        cols.append(col)
                        cols_dict[col] = 1
        for row in rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0

if __name__ == "__main__":
    print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))