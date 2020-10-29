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
        last_no_rub = left[0] + right[0]
        last_rub = left[1] + right[1]
        cur_rub = max(last_no_rub + root.val, last_rub)
        return [last_rub, cur_rub]