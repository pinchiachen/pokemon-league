## 2020/10/18
from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            return int(y + x) - int(x + y)
        res = ''.join(sorted([str(num) for num in nums], key = cmp_to_key(cmp)))
        return '0' if res[0] == '0' else res

if __name__ == "__main__":
    print(Solution().largestNumber([10,2]))