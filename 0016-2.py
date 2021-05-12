## 2021/05/12
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        l = len(nums)
        nums.sort()
        for start in range(l-2):
            if start > 0 and nums[start] == nums[start-1]:
                continue
            left = start + 1
            right = l - 1
            while left < right:
                cur_sum = nums[start] + nums[left] + nums[right]
                if cur_sum == target:
                    return cur_sum
                if abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                if cur_sum > target:
                    right -= 1
                else:
                    left += 1
        return res

if __name__ == '__main__':
    print(Solution().threeSumClosest([-1,2,1,-4], 1))
