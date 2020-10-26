## 2020/10/26

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = self.__build(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] + self.matrix[row1][col1]\
            if self.matrix else 0

    def __build(self, matrix):
        if not matrix or not matrix[0]: return
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0] * (N+1) for _ in range(M+1)]
        for i in range(1, M+1):
            for j in range(1, N+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]
        return dp

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)