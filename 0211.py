## 2020/10/20

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_word = '#'

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_word] = self.end_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.match(0, word, self.root)

    def match(self, index, word, node):
        if not node or type(node) is not dict: return False
        if index == len(word):
            return self.end_word in node
        if word[index] == '.':
            for val in node.values():
                if self.match(index + 1, word, val):
                    return True
        else:
            if word[index] not in node:
                return False
            else:
                return self.match(index + 1, word, node[word[index]])
        return False

if __name__ == "__main__":
    wordDictionary = WordDictionary();
    # wordDictionary.addWord("bad")
    wordDictionary.addWord("a")
    wordDictionary.addWord("ab")
    wordDictionary.addWord("a")
    # wordDictionary.addWord("a")
    print(wordDictionary.root)
    # wordDictionary.addWord("dad")
    # wordDictionary.addWord("mad")
    # print(wordDictionary.search("aa"))
    # print(wordDictionary.search("pad"))
    # print(wordDictionary.search("bad"))
    # print(wordDictionary.search(".ad"))
    # print(wordDictionary.search("b.."))
    print(wordDictionary.search(".."))