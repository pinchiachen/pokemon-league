## 2020/09/11

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        cols = []
        if n <= 0: return self.res
        self.dfs(cols, n)
        return self.res

    def check(self, cols, add_col):
        for i in range(len(cols)):
            if cols[i] == add_col: return False
            if abs(add_col - cols[i]) == (len(cols) - i): return False
        return True

    def dfs(self, cols, n):
        if len(cols) == n:
            self.res += 1
            return
        for col in range(n):
            if self.check(cols, col):
                self.dfs(cols + [col], n)


if __name__ == "__main__":
    print(Solution().totalNQueens(4))