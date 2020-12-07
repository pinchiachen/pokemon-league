## 2020/12/07

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        pre = 1
        cur = 2
        for _ in range(3, n + 1):
            res = cur + pre
            pre = cur
            cur = res
        return res