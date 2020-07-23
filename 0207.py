## 2020/07/23
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for x, y in prerequisites:
            graph[x].append(y)
        for index in range(numCourses):
            if not self.dfs(graph, index, visited): return False
        return True

    def dfs(self, graph, index, visited):
        if visited[index] == -1: return False
        if visited[index] == 1: return True
        visited[index] = -1
        for neighbor in graph[index]:
            if not self.dfs(graph, neighbor, visited): return False
        visited[index] = 1
        return True

if __name__ == "__main__":
    solve = Solution()
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(solve.canFinish(numCourses, prerequisites))