## 2020/12/31

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        res = 1
        char_map = {}
        char_map[s[0]] = 1
        left = 0
        right = 0
        while right < len(s) - 1:
            right += 1
            char_map[s[right]] = 1 if s[right] not in char_map else char_map[s[right]] + 1
            while left < right and (right-left+1) - max(char_map.values()) > k:
                char_map[s[left]] -= 1
                left += 1
            res = max(res, (right-left+1))
        return res

if __name__ == "__main__":
    print(Solution().characterReplacement('ABBB', 2))