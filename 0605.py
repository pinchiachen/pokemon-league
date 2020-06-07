## 2020/06/07
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed: return False
        for i in range(len(flowerbed)):
            if n <= 0: return True
            if (i != 0 and flowerbed[i - 1] == 1) or (i != len(flowerbed) - 1 and flowerbed[i + 1] == 1) or (flowerbed[i] == 1):
                pass
            else:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

if __name__ == "__main__":
    Solution = Solution()
    flowerbed = [1, 0, 0, 0, 0, 1]
    n = 2
    print(Solution.canPlaceFlowers(flowerbed, n))