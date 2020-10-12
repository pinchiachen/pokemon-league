## 2020/10/12
from typing import List

# Bad
class BadSolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost: return -1
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        diff += diff
        for start in range(len(gas)):
            cur = diff[start]
            if cur < 0: continue
            for end in range(start+1, start + len(gas)):
                cur += diff[end]
                if cur < 0: break
            if cur >= 0: return start
        return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        station = 0
        diff = 0
        for i in range(len(gas)):
            diff += (gas[i] - cost[i])
            if diff < 0:
                station = i + 1
                diff = 0
        return station


if __name__ == "__main__":
    print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(Solution().canCompleteCircuit([3,3,4], [3,4,4]))