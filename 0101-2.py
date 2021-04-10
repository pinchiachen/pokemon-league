## 2021/04/10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.traversal(root.left, root.right)

    def traversal(self, root_left, root_right):
        if (not root_left) and (not root_right):
            return True
        if (not root_left) or (not root_right) or (root_left.val != root_right.val):
            return False
        return self.traversal(root_left.left, root_right.right) and self.traversal(root_left.right, root_right.left)