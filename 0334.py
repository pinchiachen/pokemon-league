## 2020/10/28
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float('inf')
        second_min = float('inf')
        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True
        return False

if __name__ == "__main__":
    print(Solution().increasingTriplet([1,2,3,4,5]))
    print(Solution().increasingTriplet([1,2,1,3,1]))
    print(Solution().increasingTriplet([1,2,2,2,2]))