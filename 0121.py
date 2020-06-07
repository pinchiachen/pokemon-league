## 2020/06/07
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = float('inf')
        res = 0
        for price in prices:
            if price <= curMin:
                curMin = price
            else:
                res = max(res, price - curMin)
        return res