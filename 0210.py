## 2020/07/27
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        path = []
        for x, y in prerequisites:
            graph[x].append(y)
        for index in range(numCourses):
            if not self.dfs(graph, index, visited, path): return []
        return path

    def dfs(self, graph, index, visited, path):
        if visited[index] == -1: return False
        if visited[index] == 1: return True
        visited[index] = -1
        for neighbor in graph[index]:
            if not self.dfs(graph, neighbor, visited, path): return False
        visited[index] = 1
        path.append(index)
        return True

if __name__ == "__main__":
    solve = Solution()
    numCourses = 5
    prerequisites = [[0,1],[1,2],[2,3],[3,4]]
    print(solve.findOrder(numCourses, prerequisites))