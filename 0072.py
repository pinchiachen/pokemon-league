## 2020/09/19

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        visited = [[-1] * l2 for _ in range(l1)]
        return self.getDistance(word1, word2, visited, l1 - 1, l2 - 1)

    def getDistance(self, word1, word2, visited, p1, p2):
        if p1 < 0: return p2 + 1
        if p2 < 0: return p1 + 1
        if visited[p1][p2] >= 0: return visited[p1][p2]
        if word1[p1] == word2[p2]:
            res = self.getDistance(word1, word2, visited, p1 - 1, p2 - 1)
        else:
            res = min(
                self.getDistance(word1, word2, visited, p1 - 1, p2 - 1),
                self.getDistance(word1, word2, visited, p1, p2 - 1),
                self.getDistance(word1, word2, visited, p1 - 1, p2),
            ) + 1
        visited[p1][p2] = res
        return res

if __name__ == "__main__":
    print(Solution().minDistance("horse", "ros"))