# 2020/04/30
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.max_depth(root.left) - self.max_depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def max_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))