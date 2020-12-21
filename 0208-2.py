## 2020/12/21

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.end_word = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie
        while word:
            node = node.setdefault(word[0], {})
            word = word[1:]
        node[self.end_word] = self.end_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        while word:
            if word[0] not in node: return False
            node = node[word[0]]
            word = word[1:]
        return self.end_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        while prefix:
            if prefix[0] not in node: return False
            node = node[prefix[0]]
            prefix = prefix[1:]
        return True