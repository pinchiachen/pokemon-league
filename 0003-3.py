## 2021/05/07

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        right = 0
        exist = {}
        while right < len(s):
            if s[right] not in exist:
                exist[s[right]] = 1
            else:
                exist[s[right]] += 1
            while exist[s[right]] > 1:
                exist[s[left]] -= 1
                if exist[s[left]] == 0:
                    exist.pop(s[left])
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res