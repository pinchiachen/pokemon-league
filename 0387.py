## 2020/06/06
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        charDict = dict()
        res = ''
        for char in s:
            if char not in charDict:
                charDict[char] = 1
            else:
                charDict[char] += 1
        for key, value in charDict.items():
            if value == 1:
                res = key
                break
        return -1 if res == '' else s.index(res)

if __name__ == "__main__":
    Solution = Solution()
    s = 'leetcode'
    print(Solution.firstUniqChar(s))