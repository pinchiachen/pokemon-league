## 2021/06/03
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = (1+n)*n/2
        return int(target - sum(nums))

if __name__ == '__main__':
    print(Solution().missingNumber([3,0,1]))