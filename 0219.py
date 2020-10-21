## 2020/10/21

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        exist = dict()
        for i in range(len(nums)):
            if nums[i] in exist:
                for index in exist[nums[i]]:
                    if abs(index - i) <= k:
                        return True
                exist[nums[i]].append(i)
            else:
                exist[nums[i]] = [i]
        return False