## 2020/10/29
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        word_map = dict()
        for idx, word in enumerate(words):
            word_map[word] = idx

        for idx, word in enumerate(words):
            if word and self.isPalindrome(word) and '' in word_map:
                res.append([idx, word_map['']])
                res.append([word_map[''], idx])
            
            rev_word = word[::-1]
            if word and rev_word in word_map and not self.isPalindrome(word):
                res.append([idx, word_map[rev_word]])

            for i in range(1, len(word)):
                left = word[:i]
                right = word[i:]
                rev_left = left[::-1]
                rev_right = right[::-1]
                if self.isPalindrome(right) and rev_left in word_map:
                    res.append([idx, word_map[rev_left]])
                if self.isPalindrome(left) and rev_right in word_map:
                    res.append([word_map[rev_right], idx])
        return res

    def isPalindrome(self, s):
        return s == s[::-1]

if __name__ == "__main__":
    print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))