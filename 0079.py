## 2020/06/25
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0: return False
        M = len(board)
        N = len(board[0])
        for m in range(M):
            for n in range(N):
                if self.dfs(n, m, board, word, M, N):
                    return True
        return False

    def dfs(self, x, y, board, word, M, N):
        if len(word) == 0:
            return True
        if x < 0 or x >= N or y < 0 or y >= M or board[y][x] != word[0]:
            return False
        tmp, board[y][x] = board[y][x], '*'
        ans = (self.dfs(x + 1, y, board, word[1:], M, N) or
            self.dfs(x - 1, y, board, word[1:], M, N) or
            self.dfs(x, y + 1, board, word[1:], M, N) or
            self.dfs(x, y - 1, board, word[1:], M, N))
        board[y][x] = tmp
        return ans

if __name__ == "__main__":
    solve = Solution()
    board = [
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]
        ]
    word = "AAB"
    print(solve.exist(board, word))