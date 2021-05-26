## 2021/05/26
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        if not firstList or not secondList:
            return res
        l1 = len(firstList)
        l2 = len(secondList)
        idx1 = 0
        idx2 = 0
        while idx1 < l1 and idx2 < l2:
            first_overlaps_second = firstList[idx1][0] >= secondList[idx2][0] and firstList[idx1][0] <= secondList[idx2][1]
            second_overlaps_first = secondList[idx2][0] >= firstList[idx1][0] and secondList[idx2][0] <= firstList[idx1][1]
            if first_overlaps_second or second_overlaps_first:
                res.append([max(firstList[idx1][0], secondList[idx2][0]), min(firstList[idx1][1], secondList[idx2][1])])
            if firstList[idx1][1] < secondList[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1
        return res

if __name__ == '__main__':
    print(Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
    print(Solution().intervalIntersection([[0,1],[2,3],[5,6],[16,17]], [[0,1],[3,4],[8,10],[12,18],[19,20]]))