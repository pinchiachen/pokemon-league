## 2020/10/18

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        exist_dict = dict()
        res = []
        for i in range(0, len(s)-9):
            if s[i:i+10] in exist_dict:
                if exist_dict[s[i:i+10]] <= 1:
                    res.append(s[i:i+10])
                exist_dict[s[i:i+10]] += 1
            else:
                exist_dict[s[i:i+10]] = 1
        return res