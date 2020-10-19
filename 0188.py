## 2020/10/19
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        res = 0
        if k > len(prices) // 2:
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
        buy = [float('inf')] * (len(prices) + 1)
        sell = [0] * (len(prices) + 1)
        for price in prices:
            for i in range(1, k+1):
                buy[i] = min(buy[i], price-sell[i-1])
                sell[i] = max(sell[i], price-buy[i])
        return sell[k]

if __name__ == "__main__":
    print(Solution().maxProfit(2, [2,4,1]))
    print(Solution().maxProfit(2, [3,2,6,5,0,3]))