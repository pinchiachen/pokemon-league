## 2020/06/25
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, path):
        if not s and len(path) == 4:
            self.res.append('.'.join(path))
            return
        if len(s) > (4 - len(path)) * 3:
            return
        for i in range(min(len(s), 3)):
            cut_s = s[:i + 1]
            if (cut_s[0] == '0' and len(cut_s) > 1) or int(cut_s) > 255:
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]])

if __name__ == "__main__":
    solve = Solution()
    s = "25525511135"
    print(solve.restoreIpAddresses(s))