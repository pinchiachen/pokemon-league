## 2021/04/10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        self.traversal(root)
        return root

    def traversal(self, root):
        if not root: return
        root.right, root.left = root.left, root.right
        self.traversal(root.left)
        self.traversal(root.right)