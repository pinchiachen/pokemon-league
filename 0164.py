## 2020/10/16
from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        if len(nums) == 2: return abs(nums[0] - nums[1])
        res = 0
        pre = 0
        max_val = max(nums)
        min_val = min(nums)
        l = len(nums)
        bucket_size = (max_val - min_val) // l + 1
        bucket_count = (max_val - min_val) // bucket_size + 1
        bucket_max = [-float('inf')] * bucket_count
        bucket_min = [float('inf')] * bucket_count
        for num in nums:
            index = (num - min_val) // bucket_size
            bucket_max[index] = max(bucket_max[index], num)
            bucket_min[index] = min(bucket_min[index], num)
        for i in range(1, bucket_count):
            if bucket_max[i] == -float('inf') or bucket_min[i] == -float('inf'): continue
            res = max(res, bucket_min[i] - bucket_max[pre])
            pre = i
        return res

if __name__ == "__main__":
    print(Solution().maximumGap([3,6,9,1]))