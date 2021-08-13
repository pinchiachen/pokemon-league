## 2021/08/13

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.dfs('', [], n, 0)
        return self.res

    def dfs(self, s, stack, n, open_count):
        if len(s)  == n*2:
            self.res.append(s)
            return
        if open_count < n:
            self.dfs(s + '(', stack + ['('], n, open_count + 1)
        if stack and stack[-1] == '(':
            self.dfs(s + ')', stack[:-1], n, open_count)