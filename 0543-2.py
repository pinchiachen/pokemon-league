## 2021/08/06

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.traversal(root)
        return self.diameter

    def traversal(self, root):
        if not root: return 0
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)