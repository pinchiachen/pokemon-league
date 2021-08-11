## 2021/08/11
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_nums = [[]]
        for num in nums:
            res = []
            length = len(cur_nums[0])
            for cur_num in cur_nums:
                for i in range(length+1):
                    res.append(cur_num[0:i] + [num] + cur_num[i:length])
            cur_nums = res
        return res

if __name__ == '__main__':
    print(Solution().permute([5,4,6,2]))