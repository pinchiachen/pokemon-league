## 2020/06/02
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            count = self.countLessEqual(matrix, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return right

    def countLessEqual(self, matrix, mid):
        count = 0
        i = 0
        j = len(matrix) - 1
        while i < len(matrix[0]) and j >= 0:
            if matrix[j][i] <= mid:
                count += j + 1
                i += 1
            else:
                j -= 1
        return count

if __name__ == "__main__":
    matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15],
    ]
    k = 8
    Solution = Solution()
    assert Solution.kthSmallest(matrix, k) == 13