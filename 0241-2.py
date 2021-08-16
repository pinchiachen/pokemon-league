## 2021/08/16

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.diffWaysToComputeMemoized(expression, {})

    def diffWaysToComputeMemoized(self, expression, exist_map):
        if expression in exist_map:
            return exist_map[expression]
        res = []
        if (not '+' in expression) and (not '-' in expression) and (not '*' in expression):
            return [int(expression)]
        for idx, char in enumerate(expression):
            if char.isdigit():
                continue
            left_nums = self.diffWaysToComputeMemoized(expression[:idx], exist_map)
            right_nums = self.diffWaysToComputeMemoized(expression[idx+1:], exist_map)
            for left_num in left_nums:
                for right_num in right_nums:
                    if char == '+':
                        res.append(left_num + right_num)
                    elif char == '-':
                        res.append(left_num - right_num)
                    elif char == '*':
                        res.append(left_num * right_num)
        exist_map[expression] = res
        return res