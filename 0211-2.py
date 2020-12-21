## 2020/12/21

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.end_word = '#'

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_word] = self.end_word
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(word, self.trie)

    def dfs(self, word, node):
        if (not node) or (type(node) is not dict): return False
        if not word:
            return self.end_word in node
        if word[0] == '.':
            for char in node:
                if self.dfs(word[1:], node[char]): return True
        else:
            if word[0] not in node: return False
            return self.dfs(word[1:], node[word[0]])
        return False