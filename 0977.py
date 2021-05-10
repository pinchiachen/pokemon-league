## 2021/05/10
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 1:
            return [nums[0]**2]
        left = 0
        right = l - 1
        res = [0] * l
        index = l - 1
        is_right_last = True
        while right > left:
            if abs(nums[right]) > abs(nums[left]):
                res[index] = nums[right]**2
                right -= 1
                is_right_last = True
            else:
                res[index] = nums[left]**2
                left += 1
                is_right_last = False
            index -= 1
        res[index] = nums[left]**2 if is_right_last else nums[right]**2
        return res

if __name__ == '__main__':
    print(Solution().sortedSquares([-1, 2, 2]))