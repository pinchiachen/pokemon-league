## 2020/10/28
from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        for ends in graph.values():
            ends.sort(reverse = True)
        self.dfs(graph, 'JFK', res)
        return res[::-1]
    
    def dfs(self, graph, start, res):
        while graph[start]:
            end = graph[start].pop()
            self.dfs(graph, end, res)
        res.append(start)

# Time Limit Exceeded
class BadSolution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.res = []
        n = len(tickets) + 1
        for idx, ticket in enumerate(tickets):
            if ticket[0] == 'JFK':
                self.dfs(tickets[:idx] + tickets[idx+1:], ticket, n, ticket[1])
        return self.res

    def dfs(self, tickets, path, n, destination):
        if len(path) == n:
            if not self.res or ''.join(path) < ''.join(self.res):
                self.res = path
            return
        for idx, ticket in enumerate(tickets):
            if ticket[0] == destination:
                self.dfs(tickets[:idx] + tickets[idx+1:], path + [ticket[1]], n, ticket[1])

if __name__ == "__main__":
    print(Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))