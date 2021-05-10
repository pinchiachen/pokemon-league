## 2021/05/10
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        n = len(words)
        res = []
        left = 0
        right = l*n - 1
        exist = {}
        for word in words:
            if word not in exist:
                exist[word] = 0
            exist[word] += 1
        while right < len(s):
            if self.check(s[left:right+1], exist.copy(), l):
                res.append(left)
            left += 1
            right += 1
        return res

    def check(self, s, exist, l):
        match = 0
        for i in range(0, len(s), l):
            tmp_string = s[i:i+l]
            if tmp_string not in exist:
                return False
            exist[tmp_string] -= 1
            if exist[tmp_string] == 0:
                match += 1
        return match == len(exist)

if __name__ == '__main__':
    print(Solution().findSubstring('barfoothefoobarman', ["foo","bar"]))