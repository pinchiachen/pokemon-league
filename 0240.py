## 2020/06/01
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        m = len(matrix)
        n = len(matrix[0])
        i = n - 1 
        j = 0
        while i >= 0 and j < m:
            if matrix[j][i] == target: return True
            elif matrix[j][i] < target:
                j += 1
            else:
                i -= 1
        return False