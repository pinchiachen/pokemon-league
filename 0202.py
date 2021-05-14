## 2021/05/14

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        exist = {}
        while n != 1:
            if n in exist:
                return False
            exist[n] = True
            cur = 0
            for c in str(n):
                cur += int(c)**2
            n = cur
        return True