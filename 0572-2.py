## 2020/12/31

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or self.isSame(s, t)

    def isSame(self, s, t):
        if not t and not s: return True
        if not s or not t or s.val != t.val: return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)