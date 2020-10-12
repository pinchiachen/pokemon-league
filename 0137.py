## 2020/10/12

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        expected_total = 0
        total = 0
        exist = {}
        for num in nums:
            if num not in exist:
                exist[num] = 1
                expected_total += num*3
            total += num
        return (expected_total - total) // 2