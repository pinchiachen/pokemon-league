## 2020/10/22
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        target_len = len(nums) // 3
        exist = dict()
        if target_len == 0:
            return list(set(nums))
        for num in nums:
            exist[num] = 1 if num not in exist else exist[num] + 1
            if exist[num] == target_len + 1:
                res.append(num)
        return res

if __name__ == "__main__":
    print(Solution().majorityElement([3,2,3]))