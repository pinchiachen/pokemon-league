## 2020/08/20

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            elif char == ')':
                stack.pop()
                if len(stack) == 0:
                    stack.append(index)
                else:
                    res = max(res, index - stack[-1])
        return res