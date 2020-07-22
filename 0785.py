## 2020/07/22
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)
        for i in range(len(graph)):
            if graph[i] and visited[i] == 0:
                visited[i] = 1
                path_queue = [i]
                while len(path_queue) > 0:
                    index = path_queue.pop(0)
                    for neighbor in graph[index]:
                        if visited[neighbor] != 0:
                            if visited[neighbor] == visited[index]:
                                return False
                        else:
                            visited[neighbor] = visited[index] * -1
                            path_queue.append(neighbor)
        return True

if __name__ == "__main__":
    solve = Solution()
    graph = [[1,3],[0,2],[1,3],[0,2]]
    print(solve.isBipartite(graph))
