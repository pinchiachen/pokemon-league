## 2020/10/21

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.traversal(root)
        return self.res

    def traversal(self, root):
        if not root: return
        self.res += 1
        self.traversal(root.left)
        self.traversal(root.right)