## 2020/08/16
from typing import List

# Time Limit Exceeded
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         self.res = []
#         visited = [0] * len(nums)
#         nums.sort()
#         for i in range(len(nums)):
#             self.dfs(nums, [], visited, i, 0, target)
#         return self.res

#     def dfs(self, nums, path, visited, index, val, target):
#         if (len(path) == 4) and (val == target) and (path not in self.res):
#             self.res.append(path)
#         for i in range(index, len(nums)):
#             if len(path) < 4 and visited[i] == 0:
#                 visited[i] = 1
#                 self.dfs(nums, path + [nums[i]], visited, i, val + nums[i], target)
#                 visited[i] = 0

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            for j in range(i + 1, len(nums) - 2):
                if j > (i + 1) and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    tmp_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif tmp_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res

if __name__ == "__main__":
    solve = Solution()
    nums = [-3, -1, 0, 2, 4, 5]
    target = 2
    print(solve.fourSum(nums, target))
