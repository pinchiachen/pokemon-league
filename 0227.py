## 2020/10/22

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_operation = '+'
        num = 0
        for idx, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if idx == len(s) - 1 or c in '+-*/':
                if pre_operation == '+':
                    stack.append(num)
                elif pre_operation == '-':
                    stack.append(-num)
                elif pre_operation == '*':
                    stack.append(stack.pop() * num)
                elif pre_operation == '/':
                    pre_num = stack.pop()
                    if pre_num // num < 0:
                        stack.append(-(-pre_num // num))
                    else:
                        stack.append(pre_num // num)
                num = 0
                pre_operation = c
        stack.append(num)
        return sum(stack)

if __name__ == "__main__":
    print(Solution().calculate("3+2*2"))