## 2020/08/08

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = dict()
        for i in range(len(nums)):
            if (target - nums[i]) not in target_dict:
                target_dict[nums[i]] = i
            else:
                return [target_dict[target - nums[i]], i]