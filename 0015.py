## 2020/08/13
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                tmp_sum = nums[i] + nums[left] + nums[right]
                if tmp_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif tmp_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res

if __name__ == "__main__":
    solve = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(solve.threeSum(nums))