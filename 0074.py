## 2020/09/21
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        M = len(matrix)
        N = len(matrix[0])
        row = 0
        left = 0
        right = N - 1
        for i in range(M):
            if matrix[i][-1] < target:
                row = i + 1
        if row >= M: return False
        while left < right:
            mid = (left + right) // 2
            if target <= matrix[row][mid]:
                right = mid
            else:
                left = mid + 1
        return matrix[row][left] == target

if __name__ == "__main__":
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 16))
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 24))
