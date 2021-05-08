## 2021/05/08

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        exist = {}
        left = 0
        right = 0
        match = 0
        for s in s1:
            exist[s] = 1 if s not in exist else exist[s] + 1
        while right < len(s2):
            if s2[right] in exist:
                exist[s2[right]] -= 1
                if exist[s2[right]] == 0:
                    match += 1
            if (right - left + 1) > len(s1):
                if s2[left] in exist:
                    if exist[s2[left]] == 0:
                        match -= 1
                    exist[s2[left]] += 1
                left += 1
            if match == len(exist):
                return True
            right += 1
        return False