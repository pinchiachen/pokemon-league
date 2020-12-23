## 2020/12/23

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = []
        left = [1] * (l+2)
        right = [1] * (l+2)
        tmp = 1
        for i in range(l):
            tmp *= nums[i]
            left[i+1] = tmp
        tmp = 1
        for i in range(l-1, -1, -1):
            tmp *= nums[i]
            right[i+1] = tmp
        for i in range(len(nums)):
            res.append(left[i] * right[i+2])
        return res