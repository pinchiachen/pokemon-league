## 2020/09/23
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        exist_dict = dict()
        for i in range(len(nums) - 1, -1, -1):
            exist_dict[nums[i]] = 1 if nums[i] not in exist_dict else exist_dict[nums[i]] + 1
            if exist_dict[nums[i]] > 2:
                del nums[i]
        return len(nums)

if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,1,2,2,3]))
    print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))