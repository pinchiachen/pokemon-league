## 2020/06/19
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList = set(wordList)
        pathQueue = [(beginWord, 1)]
        while len(pathQueue) > 0:
            curWord, count = pathQueue.pop(0)
            if curWord == endWord: return count
            for index in range(len(curWord)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = curWord[:index] + char + curWord[index + 1:]
                    if newWord in wordList and newWord != curWord:
                        pathQueue.append((newWord, count + 1))
                        wordList.remove(newWord)
        return 0

if __name__ == "__main__":
    Solve = Solution()
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solve.ladderLength(beginWord, endWord, wordList))