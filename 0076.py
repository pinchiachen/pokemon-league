## 2020/09/22

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t): return ''
        res = ''
        min_len = float('inf')
        left = 0
        right = 0
        count = 0
        s_dict = dict()
        t_dict = dict()
        for c in t:
            t_dict[c] = 1 if c not in t_dict else t_dict[c] + 1
        while right < len(s):
            s_dict[s[right]] = 1 if s[right] not in s_dict else s_dict[s[right]] + 1
            if s[right] in t_dict and s_dict[s[right]] <= t_dict[s[right]]:
                count += 1
            while left <= right and count == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]
                s_dict[s[left]] -= 1
                if s[left] in t_dict and s_dict[s[left]] < t_dict[s[left]]:
                    count -= 1
                left += 1
            right += 1
        return res

if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
