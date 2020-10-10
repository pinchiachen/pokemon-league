# ## 2020/10/10
from typing import List

import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        res = []
        wordList = set(wordList)
        path = {}
        path[beginWord] = [[beginWord]]
        while path:
            new_path = collections.defaultdict(list)
            for p in path:
                if p == endWord:
                    res += path[p]
                else:
                    for i in range(len(p)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = p[:i] + c + p[i+1:]
                            if new_word in wordList:
                                new_path[new_word] += [old_path + [new_word] for old_path in path[p]]
            wordList -= set(new_path.keys())
            path = new_path
        return res

if __name__ == "__main__":
    print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
