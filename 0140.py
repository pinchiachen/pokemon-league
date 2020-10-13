## 2020/10/13
from typing import List
import collections

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        exist = dict()
        return self.dfs(s, words, exist)

    def dfs(self, s, words, exist):
        if s in exist: return exist[s]
        if not s: return ['']
        res = []
        for word in words:
            if s[:len(word)] == word:
                for r in self.dfs(s[len(word):], words, exist):
                    res.append(word + ('' if not r else ' ' + r))
        exist[s] = res
        return res

if __name__ == "__main__":
    print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
    print(Solution().wordBreak("bb", ["a","b","bbb","bbbb"]))