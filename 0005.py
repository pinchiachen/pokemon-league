## 2020/11/20

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        res = ''
        for mid in range(len(s)):
            ## odd
            pal_str = self.findPalindrome(s, mid, mid)
            if len(pal_str) > len(res):
                res = pal_str
            ## even
            if mid < len(s) - 1 and s[mid] == s[mid + 1]:
                pal_str = self.findPalindrome(s, mid, mid + 1)
                if len(pal_str) > len(res):
                    res = pal_str
        return res

    def findPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            r += 1
            l -= 1
        return s[l + 1:r]

if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))