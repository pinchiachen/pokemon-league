## 2020/10/12
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        candies = [1] * l
        for i in range(1, l):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(l-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
        return sum(candies)

if __name__ == "__main__":
    print(Solution().candy([1,0,2]))