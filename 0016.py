## 2020/08/15
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        diff_min = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                tmp_sum = nums[i] + nums[left] + nums[right]
                tmp_diff_min = abs(tmp_sum - target)
                if tmp_diff_min < diff_min:
                    diff_min = tmp_diff_min
                    res = tmp_sum
                if tmp_sum == target:
                    return target
                elif tmp_sum < target:
                    left += 1
                else:
                    right -= 1        
        return res

if __name__ == "__main__":
    solve = Solution()
    nums = [-1,2,1,-4]
    target = 1
    print(solve.threeSumClosest(nums, target))