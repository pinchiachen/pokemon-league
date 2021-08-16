## 2021/08/16

class Solution:
    def numTrees(self, n: int) -> int:
        arr = [i for i in range(1, n+1)]
        return self.calculatePath(arr, {})

    def calculatePath(self, arr, exist_map):
        if not arr or len(arr) == 1:
            return 1
        res = 0
        map_str = f'{arr[0],arr[-1]}'
        if map_str in exist_map:
            return exist_map[map_str]
        for idx in range(len(arr)):
            left = self.calculatePath(arr[:idx], exist_map)
            right = self.calculatePath(arr[idx+1:], exist_map)
            res += left * right
        exist_map[map_str] = res
        return res

if __name__ == '__main__':
    print(Solution().numTrees(3))