## 2020/06/06
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charDict = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for char in s:
            if char in charDict:
                if not stack or stack[-1] != charDict[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0