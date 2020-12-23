## 2020/12/23

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exist = {}
        for num in nums:
            if num in exist:
                return True
            exist[num] = 1
        return False