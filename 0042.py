## 2020/06/12
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        leftMaxArr = [0] * len(height)
        rightMaxArr = [0] * len(height)
        leftMaxArr[0] = height[0]
        rightMaxArr[-1] = height[-1]
        res = 0
        for i in range(1, len(height)):
            leftMaxArr[i] = max(leftMaxArr[i - 1], height[i])
        for j in range(len(height) - 2, -1, -1):
            rightMaxArr[j] = max(rightMaxArr[j + 1], height[j])
        for k in range(1, len(height) - 1):
            res += (min(leftMaxArr[k], rightMaxArr[k]) - height[k])
        return res

if __name__ == "__main__":
    Solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # height = [0,2,0]
    Solution.trap(height)