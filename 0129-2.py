## 2021/08/05

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.traversal(root, '')

    def traversal(self, root, path):
        if not root: return 0
        current_path = path + str(root.val)
        if not root.left and not root.right:
            return int(current_path)
        return self.traversal(root.left, current_path) + self.traversal(root.right, current_path)