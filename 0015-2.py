## 2020/11/22
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3: return res
        nums.sort()
        for left in range(len(nums) - 2):
            mid = left + 1
            right = len(nums) - 1
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            while mid < right:
                tmp_sum = nums[left] + nums[mid] + nums[right]
                if tmp_sum == 0:
                    res.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif tmp_sum > 0:
                    right -= 1
                else:
                    mid += 1
        return res

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))