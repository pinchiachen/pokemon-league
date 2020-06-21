## 2020/06/21
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        self.dfs(digits, 0, res, '', digitMap)
        return res

    def dfs(self, digits, index, res, path, digitMap):
        if index == len(digits):
            if path != '':
                res.append(path)
            return

        for char in digitMap[digits[index]]:
            self.dfs(digits, index + 1, res, path + char, digitMap)