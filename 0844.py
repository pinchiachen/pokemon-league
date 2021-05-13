## 2021/05/13

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.trimString(s) == self.trimString(t)

    def trimString(self, s):
        backspace = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '#':
                backspace += 1
                s = s[:i] + s[i+1:]
            elif backspace > 0:
                backspace -= 1
                s = s[:i] + s[i+1:]
        return s