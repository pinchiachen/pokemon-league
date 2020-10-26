## 2020/10/26

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = self.__build(self.nums)

    def update(self, i: int, val: int) -> None:
        for idx in range(i+1, len(self.dp)):
            self.dp[idx] += val - self.nums[i]
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]
        
    def __build(self, nums):
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            dp[i] = dp[i-1] + nums[i-1]
        return dp


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)