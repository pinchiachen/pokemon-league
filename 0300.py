## 2020/12/29

## O(n*logn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        for num in nums[1:]:
            if num > res[-1]:
                res.append(num)
            else:
                res[self.__binarySearch(res, num)] = num
        return len(res)

    def __binarySearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

## O(n**2)
class DPSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1] * (l)
        res = 1
        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    res = max(res, dp[i])
        return res