## 2022/10/20

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. BST -> root.left < root < root.right
# 2. if p, q < root, move to root.left
# 3. if p, q > root, move to root.right
# 4. if p <= root <= q -> root is the answer
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val-p.val)*(root.val-q.val) <= 0:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)