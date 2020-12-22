## 2020/12/22

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words: return []
        M = len(board)
        N = len(board[0])
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        res = []
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word
        for x in range(M):
            for y in range(N):
                if board[x][y] in trie:
                    self.dfs(trie, board, x, y, directions, res, M, N)
        return res

    def dfs(self, root, board, x0, y0, directions, res, M, N):
        char = board[x0][y0]
        node = root[char]
        if '#' in node:
            res.append(node.pop('#'))
        board[x0][y0] = '*'
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < M and  0 <= y < N and board[x][y] in node:
                self.dfs(node, board, x, y, directions, res, M, N)
        board[x0][y0] = char
        if not node:
            root.pop(char)
        return