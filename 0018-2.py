## 2021/05/12
from  typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        l = len(nums)
        res = []
        nums.sort()
        for start in range(l-3):
            if start > 0 and nums[start] == nums[start-1]:
                continue
            for left in range(start+1, l-2):
                if left > start + 1 and nums[left] == nums[left-1]:
                    continue
                mid = left + 1
                right = l - 1
                while mid < right:
                    cur_sum = nums[start] + nums[left] + nums[mid] + nums[right]
                    if cur_sum == target:
                        res.append([nums[start], nums[left], nums[mid], nums[right]])
                        mid += 1
                        right -= 1
                        while mid < right and nums[mid] == nums[mid-1]:
                            mid += 1
                        while mid < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif cur_sum > target:
                        right -= 1
                    else:
                        mid += 1
        return res

if __name__ == '__main__':
    # print(Solution().fourSum([1,0,-1,0,-2,2],0))
    print(Solution().fourSum([-2,-1,-1,1,1,2,2],0))