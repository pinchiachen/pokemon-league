## 2020/10/24

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s: return ['']
        self.res = []
        l = 0
        r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        self.dfs(s, 0, l, r)
        return self.res

    def dfs(self, s, start, l, r):
        if l == 0 and r == 0:
            if self.isValid(s):
                self.res.append(s)
            return
        for i in range(start, len(s)):
            if i != start and s[i] == s[i-1]: continue
            if l > 0 and s[i] == '(':
                self.dfs(s[:i]+s[i+1:], i, l-1, r)
            if r > 0 and s[i] == ')':
                self.dfs(s[:i]+s[i+1:], i, l, r-1)

    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
        return len(stack) == 0