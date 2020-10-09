## 2020/10/09
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        buy_one = float('inf')
        sell_one = 0
        buy_two = float('inf')
        sell_two = 0
        for price in prices:
            buy_one = min(buy_one, price)
            sell_one = max(sell_one, price - buy_one)
            buy_two = min(buy_two, price - sell_one)
            sell_two = max(sell_two, price - buy_two)
        return sell_two

if __name__ == "__main__":
    print(Solution().maxProfit([3,3,5,0,0,3,1,4]))