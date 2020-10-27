## 2020/10/27
from typing import List

class FenwickTree:
    def __init__(self, nums):
        l = len(nums)
        self.sums = [0] * (l+1)
        for i in range(1, l+1):
            self.update(i, nums[i-1])

    def update(self, idx, delta):
        while idx < len(self.sums):
            self.sums[idx] += delta
            idx += self.__lowbit(idx)

    def query(self, idx):
        total = 0
        while idx > 0:
            total += self.sums[idx]
            idx -= self.__lowbit(idx)
        return total

    def __lowbit(self, val):
        return val & (-val)


class NumArray:

    def __init__(self, nums: List[int]):
        self.fenwick_tree = FenwickTree(nums)
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.fenwick_tree.update(i+1, val-self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.fenwick_tree.query(j+1) - self.fenwick_tree.query(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)