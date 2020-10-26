## 2020/10/26

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        hold = -float('inf')
        sold = 0
        rest = 0
        for price in prices:
            pre_hold = hold
            pre_sold = sold
            hold = max(pre_hold, rest - price)
            sold = pre_hold + price
            rest = max(rest, pre_sold)
        return max(sold, rest)