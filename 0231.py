## 2021/10/07

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n^(n-1) == 2*n-1