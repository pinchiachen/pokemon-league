## 2020/09/17

## Time Limit Exceeded
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.count = 0
        self.res = ''
        visited = [0] * n
        self.dfs('', n, k, visited)
        return self.res

    def dfs(self, path, n, k, visited):
        if len(path) == n:
            self.count += 1
            if self.count == k:
                self.res = path
            return
        for i in range(1, n + 1):
            if visited[i - 1] == 0 and self.count < k:
                visited[i - 1] = 1
                self.dfs(path + str(i), n, k, visited)
                visited[i - 1] = 0

if __name__ == "__main__":
    print(Solution().getPermutation(3, 3))
    print(Solution().getPermutation(9, 78494))
