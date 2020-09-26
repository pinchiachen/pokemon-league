## 2020/09/26
from typing import List

class Solution(object):
    def largestRectangleArea(self, heights):
        if len(heights) == 0: return 0
        stack = []
        res = 0
        heights.append(0)
        for i in range(len(heights)):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = i - stack[-1] - 1 if stack else i
                    res = max(res, h*w)
                stack.append(i)
        return res

print(Solution().largestRectangleArea([1, 2, 3, 1]))