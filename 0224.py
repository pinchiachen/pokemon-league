## 2020/10/22

class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        sign = 1
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+' or c == '-':
                res += num * sign
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                num = 0
                res = 0
            elif c == ')':
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                sign = 1
                num = 0
        res += num * sign
        return res

if __name__ == "__main__":
    print(Solution().calculate("1 + 1"))
    print(Solution().calculate(" 2-1 + 2 "))
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))