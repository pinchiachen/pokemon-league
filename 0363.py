## 2020/10/29
from typing import List
import bisect

# top-bottom compression
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]: return 0
        res = -float('inf')
        M = len(matrix)
        N = len(matrix[0])
        for top in range(M):
            compression = [0] * N
            for bottom in range(top, M):
                for i in range(N):
                    compression[i] += matrix[bottom][i]
                target_sum = self.findTargetSum(compression, k)
                if target_sum != None:
                    res = max(res, target_sum)
        return res

    def findTargetSum(self, nums, k):
        if not nums: return 0
        cur_sum = 0
        res = -float('inf')
        sum_arr = [0]
        for num in nums:
            cur_sum += num
            target = cur_sum - k
            if target == 0:
                return k
            index = bisect.bisect_left(sum_arr, target)
            if index != len(sum_arr):
                res = max(res, cur_sum - sum_arr[index])
            bisect.insort_left(sum_arr, cur_sum)
        return res if res <= k else None

# left-right compression
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]: return 0
        res = -float('inf')
        M = len(matrix)
        N = len(matrix[0])
        for left in range(N):
            compression = [0] * M
            for right in range(left, N):
                for i in range(M):
                    compression[i] += matrix[i][right]
                target_sum = self.findTargetSum(compression, k)
                if target_sum != None:
                    res = max(res, target_sum)
        return res

    def findTargetSum(self, nums, k):
        cur_sum = 0
        res = -float('inf')
        sum_arr = [0]
        for num in nums:
            cur_sum += num
            target = cur_sum - k
            if target == 0:
                return k
            index = bisect.bisect_left(sum_arr, target)
            if index != len(sum_arr):
                res = max(res, cur_sum - sum_arr[index])
            bisect.insort_left(sum_arr, cur_sum)
        return res if res <= k else None

if __name__ == "__main__":
    print(Solution().maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))
    print(Solution().maxSumSubmatrix([[2,2,-1]], 0))
    print(Solution().maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], 0))