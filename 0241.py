## 2020/07/13
from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        for i in range(len(input)):
            if input[i] == '+' or input[i] == '-' or input[i] == '*':
                lefts = self.diffWaysToCompute(input[:i])
                rights = self.diffWaysToCompute(input[i+1:])
                for left in lefts:
                    for right in rights:
                        if input[i] == '+':
                            res.append(int(left) + int(right))
                        elif input[i] == '-':
                            res.append(int(left) - int(right))
                        elif input[i] == '*':
                            res.append(int(left) * int(right))
        if len(res) == 0: res.append(int(input))
        return res

if __name__ == "__main__":
    solve = Solution()
    input_str = "2*3-4*5"
    print(solve.diffWaysToCompute(input_str))