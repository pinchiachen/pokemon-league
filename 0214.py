## 2020/10/21

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s: return ''
        if len(s) == 1: return s
        end = 1
        palindrome_end = 0
        while end < len(s):
            if self.isPalindrome(s[:end+1]):
                palindrome_end = end
            end += 1
        return s[len(s)-1:palindrome_end:-1] + s

    def isPalindrome(self, s):
        return s == s[::-1]

if __name__ == "__main__":
    print(Solution().shortestPalindrome("aacecaaa"))