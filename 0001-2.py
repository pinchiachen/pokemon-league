## 2020/11/20

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist_dict = {}
        for idx, num in enumerate(nums):
            if (target - num) in exist_dict:
                return [exist_dict[target - num], idx]
            else:
                exist_dict[num] = idx