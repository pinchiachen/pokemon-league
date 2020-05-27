# 2020/05/25
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        start = end = res = 0
        while start <= end and end < len(s):
            res = max(res, end - start + 1)
            if s[end] not in s[start:end]:
                end += 1
            else:
                start += 1
                end = start
        return res