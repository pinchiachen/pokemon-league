## 2020/11/05

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        char_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        self.dfs(digits, char_map, '', res)
        return res

    def dfs(self, digits, char_map, path, res):
        if not digits:
            res.append(path)
            return
        for char in char_map[digits[0]]:
            self.dfs(digits[1:], char_map, path + char, res)
