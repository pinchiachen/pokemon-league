## 2020/10/27
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if len(words) < 2: return 0
        res = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if not set(words[i]) & set(words[j]):
                    res = max(res, len(words[i] * len(words[j])))
        return res

if __name__ == "__main__":
    print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))