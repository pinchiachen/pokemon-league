## 2021/05/08

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        exist1 = {}
        exist2 = {}
        left = 0
        right = 0
        for s in s1:
            exist1[s] = 1 if s not in exist1 else exist1[s] + 1
        while right < len(s2):
            exist2[s2[right]] = 1 if s2[right] not in exist2 else exist2[s2[right]] + 1
            if (right - left + 1) > len(s1):
                exist2[s2[left]] -= 1
                if exist2[s2[left]] == 0:
                    exist2.pop(s2[left])
                left += 1
            if exist1 == exist2:
                return True
            right += 1
        return False