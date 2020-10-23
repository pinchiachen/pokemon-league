## 2020/10/23
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        exist = dict()
        for num in nums:
            exist[num] = 1 if num not in exist else exist[num] + 1
        for key in exist.keys():
            if exist[key] == 1:
                res.append(int(key))
        return res