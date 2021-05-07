## 2021/05/07

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        count = 0
        res = -float('inf')
        left = 0
        right = 0
        exist = {}
        while right < len(tree):
            if tree[right] not in exist or exist[tree[right]] == 0:
                count += 1
                exist[tree[right]] = 1
            else:
                exist[tree[right]] += 1
            while count > 2:
                exist[tree[left]] -= 1
                if exist[tree[left]] == 0:
                    count -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res if res != -float('inf') else 0