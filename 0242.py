## 2020/12/28

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        map_s = {}
        for c in s:
            map_s[c] = map_s[c] + 1 if c in map_s else 1
        for c in t:
            if c not in map_s: return False
            map_s[c] -= 1
        for count in map_s.values():
            if count != 0: return False
        return True