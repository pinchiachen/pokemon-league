## 2021/06/04

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        for i in range(len(arr)):
            diff = arr[i] - ((i+1) + len(missing))
            while diff > 0:
                missing.append(arr[i]-diff)
                diff -= 1
                if len(missing) >= k:
                    return missing[k-1]
        return arr[-1] + k - len(missing)