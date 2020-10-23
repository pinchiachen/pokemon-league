## 2020/10/23

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        pattern_map = dict()
        word_map = dict()
        if len(pattern) != len(words): return False
        for i in range(len(words)):
            if pattern[i] not in pattern_map and words[i] not in word_map:
                pattern_map[pattern[i]] = words[i]
                word_map[words[i]] = pattern[i]
            elif pattern[i] in pattern_map and pattern_map[pattern[i]] != words[i]:
                return False
            elif words[i] in word_map and word_map[words[i]] != pattern[i]:
                return False
        return True

if __name__ == "__main__":
    print(Solution().wordPattern("abba", "dog cat cat fish"))
    print(Solution().wordPattern("abba", "dog dog dog dog"))