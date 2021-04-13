## 2021/04/13

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = float('inf')
        self.traversal(root, 0)
        return self.res

    def traversal(self, root, depth):
        if not root: return
        if depth >= self.res: return
        cur_depth = depth + 1
        if not root.left and not root.right:
            self.res = min(self.res, cur_depth)
        self.traversal(root.left, cur_depth)
        self.traversal(root.right, cur_depth)