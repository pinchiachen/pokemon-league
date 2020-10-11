## 2020/10/11

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.traversal(root, 0)
        return self.res

    def traversal(self, root, cur):
        if not root.left and not root.right:
            self.res += (cur*10 + root.val)
            return
        if root.left:
            self.traversal(root.left, cur*10 + root.val)
        if root.right:
            self.traversal(root.right, cur*10 + root.val)