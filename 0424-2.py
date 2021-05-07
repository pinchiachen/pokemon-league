## 2021/05/07

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        right = 0
        exist = {}
        while right < len(s):
            exist[s[right]] = 1 if s[right] not in exist else exist[s[right]] + 1
            while (right - left + 1) - max(exist.values()) > k:
                exist[s[left]] -= 1
                if exist[s[left]] == 0:
                    exist.pop(s[left])
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res