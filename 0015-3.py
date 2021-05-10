## 2021/05/10
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3: return []
        res = []
        nums.sort()
        for start in range(l-2):
            if start > 0 and nums[start] == nums[start-1]:
                continue
            target = -nums[start]
            left = start + 1
            right = l - 1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == target:
                    res.append([nums[left], nums[right], nums[start]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif cur_sum > target:
                    right -= 1
                else:
                    left += 1
        return res

if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,0]))