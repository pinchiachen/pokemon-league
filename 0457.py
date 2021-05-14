## 2021/05/14
from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return False
        l = len(nums)
        for i in range(l):
            idx = i + nums[i]
            while idx >= l:
                idx -= l
            while idx < 0:
                idx += l
            count = 1
            visited = {}
            if self.check(i, idx, visited, count, nums, l):
                return True
        return False

    def check(self, start, idx, visited, count, nums, l):
        while idx != start:
            if nums[idx] * nums[start] < 0:
                return False
            if idx in visited:
                return False
            visited[idx] = True
            idx += nums[idx]
            while idx < 0:
                idx += l
            while idx >= l:
                idx -= l
            count += 1
        return idx == start and count > 1

if __name__ == '__main__':
    print(Solution().circularArrayLoop([2,-1,1,2,2]))
    print(Solution().circularArrayLoop([-1,2]))
    print(Solution().circularArrayLoop([-2,1,-1,-2,-2]))
    print(Solution().circularArrayLoop([1,2,3,4,5]))
    print(Solution().circularArrayLoop([-1,-2,-3,-4,-5]))