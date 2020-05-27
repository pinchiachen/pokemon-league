# 2020/05/14
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        return self.isSame(t, s) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def isSame(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)