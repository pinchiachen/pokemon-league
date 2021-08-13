## 2021/08/13
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        cur_chars = ['']
        for char in s:
            res = []
            for cur in cur_chars:
                if char.isnumeric():
                    res.append(cur + char)
                else:
                    for l in [char.lower(), char.upper()]:
                        res.append(cur + l)
            cur_chars = res
        return res

if __name__ == '__main__':
    print(Solution().letterCasePermutation("a1b2"))