## 2020/09/27
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        N = len(matrix[0])
        histogram = [0] * N
        res = 0
        for row in matrix:
            for j in range(N):
                histogram[j] = 0 if row[j] == '0' else histogram[j] + 1
            res = max(res, self.calcMaxArea(histogram))
        return res

    def calcMaxArea(self, histogram):
        if not histogram: return 0
        res = 0
        histogram.append(0)
        stack = []
        for i in range(len(histogram)):
            if not stack or histogram[i] > histogram[stack[-1]]:
                stack.append(i)
            else:
                while stack and histogram[i] <= histogram[stack[-1]]:
                    h = histogram[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i
                    res = max(res, h * w)
                stack.append(i)
        return res


## dfs - Time Limit Exceeded
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if len(matrix) == 0 or len(matrix[0]) == 0: return 0
#         M = len(matrix)
#         N = len(matrix[0])
#         directions = [[0, 1], [1, 0]]
#         self.res = 0
#         for i in range(M):
#             for j in range(N):
#                 if matrix[i][j] == '1':
#                     self.dfs(matrix, i, j, i, j, directions, M, N)
#         return self.res

#     def dfs(self, matrix, s_x, s_y, e_x, e_y, directions, M, N):
#         if self.calArea([s_x, s_y], [e_x, e_y]) > self.res:
#             self.res = self.calArea([s_x, s_y], [e_x, e_y])
#         for dx, dy in directions:
#             end_x = e_x + dx
#             end_y = e_y + dy
#             if end_x >= 0 and end_x < M and end_y >= 0 and end_y < N and self.isRec(matrix, [s_x, s_y], [end_x, end_y]):
#                 self.dfs(matrix, s_x, s_y, end_x, end_y, directions, M, N)

#     def isRec(self, matrix, start, end):
#         for i in range(start[0], end[0] + 1):
#             for j in range(start[1], end[1] + 1):
#                 if matrix[i][j] == '0':
#                     return False
#         return True

#     def calArea(self, start, end):
#         return (end[0] - start[0] + 1) * (end[1] - start[1] + 1)

if __name__ == "__main__":
    print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))