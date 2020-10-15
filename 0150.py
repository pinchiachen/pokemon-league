## 2020/10/15
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                calc_num = num2 * num1
                stack.append(calc_num)
            elif token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                calc_num = num2 + num1
                stack.append(calc_num)
            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                calc_num = num2 - num1
                stack.append(calc_num)
            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                calc_num = -(-num2//num1) if num2 / num1 < 0 else num2 // num1
                stack.append(calc_num)
            else:
                stack.append(int(token))
        return stack[0]

if __name__ == "__main__":
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))