## 2021/05/08

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        res = ''
        min_length = float('inf')
        left = 0
        right = 0
        exist = {}
        match = 0
        for char in t:
            exist[char] = 1 if char not in exist else exist[char] + 1
        while right < len(s):
            if s[right] in exist:
                exist[s[right]] -= 1
                if exist[s[right]] == 0:
                    match += 1
            while match == len(exist):
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    res = s[left:right+1]
                if s[left] in exist:
                    if exist[s[left]] == 0:
                        match -= 1
                    exist[s[left]] += 1
                left += 1
            right += 1
        return res
