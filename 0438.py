## 2021/05/08

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p): return res
        left = 0
        right = 0
        exist = {}
        match = 0
        for char in p:
            exist[char] = 1 if char not in exist else exist[char] + 1
        while right < len(s):
            if s[right] in exist:
                exist[s[right]] -= 1
                if exist[s[right]] == 0:
                    match += 1
            if (right - left + 1) > len(p):
                if s[left] in exist:
                    if exist[s[left]] == 0:
                        match -= 1
                    exist[s[left]] += 1
                left += 1
            if match == len(exist):
                res.append(left)
            right += 1
        return res