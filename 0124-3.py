## 2021/08/09

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float('inf')
        self.traversal(root)
        return self.res

    def traversal(self, root):
        if not root: return 0
        left = max(0, self.traversal(root.left))
        right = max(0, self.traversal(root.right))
        self.res = max(self.res, left + right + root.val)
        return root.val + max(left, right)