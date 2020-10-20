## 2020/10/20
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 0: return False
        M = len(board)
        N = len(board[0])
        self.res = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word
        for x in range(M):
            for y in range(N):
                if board[x][y] in trie:
                    self.dfs(trie, x, y, board, directions, M, N)
        return self.res

    def dfs(self, root, x0, y0, board, directions, M, N):
        char = board[x0][y0]
        node = root[char]
        word = node.pop('#', False)
        if word:
            self.res.append(word)
        board[x0][y0] = '*'
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < M and 0 <= y < N and board[x][y] in node:
                self.dfs(node, x, y, board, directions, M, N)
        board[x0][y0] = char
        if not node:
            root.pop(char)

if __name__ == "__main__":
    print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))