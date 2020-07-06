## 2020/07/06
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, [])
        return self.res

    def is_palindrome(self, s):
        return s == s[::-1]

    def dfs(self, s, path):
        if not s:
            self.res.append(path)
        for i in range(len(s)):
            if self.is_palindrome(s[:i+1]):
                self.dfs(s[i+1:], path + [s[:i+1]])

if __name__ == "__main__":
    solve = Solution()
    s = 'aab'
    print(solve.partition(s))