## 20201/02/11
import collections
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        l = len(adjacentPairs)
        res = []
        visited = {}
        graph = collections.defaultdict(list)
        cur = None
        for nums in adjacentPairs:
            graph[nums[0]].append(nums[1])
            graph[nums[1]].append(nums[0])
        for num, neighbors in graph.items():
            if len(neighbors) == 1:
                cur = neighbors[0]
                res.append(num)
                visited[num] = 1
                break
        while len(res) < l+1:
            res.append(cur)
            visited[cur] = 1
            for num in graph[cur]:
                if num not in visited:
                    cur = num
        return res


if __name__ == "__main__":
    print(Solution().restoreArray([[2,1],[3,4],[3,2]]))
