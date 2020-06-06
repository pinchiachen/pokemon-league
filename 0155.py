## 2020/06/06

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        preMin = float('inf') if not self.stack else self.stack[-1][1]
        if x < preMin:
            self.stack.append([x, x])
            x = preMin
        else:
            self.stack.append([x, preMin])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None