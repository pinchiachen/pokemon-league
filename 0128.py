## 2020/12/10

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if (num - 1) in nums: continue
            tmp_val = num
            tmp_length = 1
            while (tmp_val + 1) in nums:
                tmp_val += 1
                tmp_length += 1
            res = max(res, tmp_length)
        return res