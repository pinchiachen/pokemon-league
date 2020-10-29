## 2020/10/29

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.traversal(root)[1]

    def traversal(self, root):
        if not root: return [0, 0]
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        cur_rub = left[0] + right[0] + root.val
        cur_no_rub = left[1] + right[1]
        next_no_rub = max(cur_no_rub, cur_rub)
        return [cur_no_rub, next_no_rub]