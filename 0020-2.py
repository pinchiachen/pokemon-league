## 2020/11/23

class Solution:
    def isValid(self, s: str) -> bool:
        valid_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in s:
            if c in valid_map:
                if not stack or stack.pop() != valid_map[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0