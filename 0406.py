## 2020/06/07
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people: return []
        res = []
        people.sort(key = lambda x: (-x[0], x[1]))
        for person in people:
            res.insert(person[1], person)
        return res
