## 2020/12/08
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t): return ''
        left = 0
        right = 0
        min_len = float('inf')
        count = 0
        res = ''
        s_exist = collections.defaultdict(int)
        t_exist = collections.defaultdict(int)
        for c in t:
            t_exist[c] += 1
        while right < len(s):
            s_exist[s[right]] += 1
            if s[right] in t_exist and s_exist[s[right]] <= t_exist[s[right]]:
                count += 1
            while left <= right and count == len(t):
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    res = s[left:right+1]
                s_exist[s[left]] -= 1
                if s[left] in t_exist and s_exist[s[left]] < t_exist[s[left]]:
                    count -= 1
                left += 1
            right += 1
        return res