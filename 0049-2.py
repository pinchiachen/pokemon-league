## 2020/11/29
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        exist_str = collections.defaultdict(list)
        for str in strs:
            exist_str[''.join(sorted(str))].append(str)
        return [value for value in exist_str.values()]