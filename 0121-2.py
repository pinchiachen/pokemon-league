## 2020/12/09

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur_min = float('inf')
        for price in prices:
            if price < cur_min:
                cur_min = price
            res = max(res, price - cur_min)
        return res