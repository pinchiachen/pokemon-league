## 2020/10/10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float('inf')
        self.maxChild(root)
        return self.res

    def maxChild(self, root):
        if not root: return 0
        left = max(self.maxChild(root.left), 0)
        right = max(self.maxChild(root.right), 0)
        self.res = max(self.res, root.val + left + right)
        return root.val + max(left, right)
