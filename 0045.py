## 2020/09/08
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        pre_max = 0
        cur_max = 0
        cur_pos = 0
        count = 0
        while cur_max < len(nums) - 1:
            count += 1
            pre_max = cur_max
            while cur_pos <= pre_max:
                cur_max = max(cur_max, cur_pos + nums[cur_pos])
                cur_pos += 1
        return count

if __name__ == "__main__":
    print(Solution().jump([2,3,1,1,4]))