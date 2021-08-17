## 2021/08/17

class Solution:
    def numTrees(self, n: int) -> int:
        return self.calculatePath(n, {})

    def calculatePath(self, n, exist_map):
        if n <= 1: return 1
        if n in exist_map:
            return exist_map[n]
        res = 0
        for i in range(1, n+1):
            left = self.calculatePath(i-1, exist_map)
            right = self.calculatePath(n-i, exist_map)
            res += left * right
        exist_map[n] = res
        return res

if __name__ == '__main__':
    print(Solution().numTrees(3))