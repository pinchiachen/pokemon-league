## 2021/08/18

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = left + (right-left)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left]