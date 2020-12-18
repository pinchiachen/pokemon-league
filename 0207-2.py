## 2020/12/18
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        visited = [0] * numCourses
        for x, y in prerequisites:
            graph[x].append(y)
        for idx in range(numCourses):
            if not self.dfs(graph, visited, idx): return False
        return True

    def dfs(self, graph, visited, index):
        if visited[index] == 1: return True
        elif visited[index] == -1: return False
        visited[index] = -1
        for neighbor_idx in graph[index]:
            if not self.dfs(graph, visited, neighbor_idx): return False
        visited[index] = 1
        return True