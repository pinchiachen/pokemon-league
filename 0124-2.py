## 2020/12/09

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = -float('inf')
        self.maxChild(root)
        return self.res

    def maxChild(self, root):
        if not root: return 0
        left = max(0, self.maxChild(root.left))
        right = max(0, self.maxChild(root.right))
        self.res = max(self.res, root.val + left + right)
        return max(root.val + left, root.val + right)