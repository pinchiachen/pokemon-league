class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        res = 1
        length = 1
        start = 0
        end = 0
        exist_dict = {}
        exist_dict[s[0]] = 1
        while end < len(s) - 1:
            end += 1
            length += 1
            while s[end] in exist_dict:
                exist_dict.pop(s[start])
                start += 1
                length -= 1
            exist_dict[s[end]] = 1
            res = max(res, length)
        return res