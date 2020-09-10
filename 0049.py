##2020/09/09
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        str_hash = dict()
        for str in strs:
            if ''.join(sorted(str)) in str_hash:
                res[str_hash[''.join(sorted(str))]].append(str)
            else:
                res.append([str])
                str_hash[''.join(sorted(str))] = len(res) - 1
        return res

if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))