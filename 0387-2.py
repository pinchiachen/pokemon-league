## 2020/06/06
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        for char in chars:
            if s.count(char) == 1:
                res.append(s.index(char))
        return min(res) if len(res) > 0 else -1 

if __name__ == "__main__":
    Solution = Solution()
    s = 'leetcode'
    print(Solution.firstUniqChar(s))