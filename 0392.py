## 2020/06/07
from typing import List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        pointerS = 0
        pointerT = 0
        while pointerS < len(s) and pointerT < len(t):
            if s[pointerS] == t[pointerT]:
                pointerS += 1
            pointerT += 1
        return pointerS == len(s)