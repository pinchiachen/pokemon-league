## 2020/10/27

class FenwickTree:
    def __init__(self, nums):
        l = len(nums)
        self.sums = [0] * (l+1)
        for i in range(len(nums)):
            self.update(i+1, nums[i])

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

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        sorted_arr = sorted(set(nums))
        rank_map = dict()
        freq = [0] * len(sorted_arr)
        reverse = nums[::-1]
        for i in range(1, len(sorted_arr) + 1):
            rank_map[sorted_arr[i-1]] = i
        fenwick_tree = FenwickTree(freq)
        for i in range(1, len(reverse) + 1):
            res.append(fenwick_tree.query(rank_map[reverse[i-1]]-1))
            fenwick_tree.update(rank_map[reverse[i-1]], 1)
        return res[::-1]