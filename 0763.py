## 2020/06/11
from typing import List 

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S: return [0]
        charDict = dict()
        charArray = []
        res = []
        for i in range(len(S)):
            if S[i] not in charDict:
                charDict[S[i]] = [i]
            else:
                charDict[S[i]] += [i]
        for key in charDict:
            charArray.append(charDict[key])
        tmpStart = charArray[0][0]
        tmpEnd = charArray[0][-1]
        for j in range(1, len(charArray)):
            if charArray[j][0] < tmpEnd:
                if charArray[j][-1] < tmpEnd:
                    continue
                else:
                    tmpEnd = charArray[j][-1]
            else:
                res.append(tmpEnd - tmpStart + 1)
                tmpStart = charArray[j][0]
                tmpEnd = charArray[j][-1]
        res.append(tmpEnd - tmpStart + 1)
        return res        

if __name__ == "__main__":
    Solution = Solution()
    S = 'ababcbacadefegdehijhklij'
    Solution.partitionLabels(S)