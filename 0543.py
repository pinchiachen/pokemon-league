# 2020/04/30
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter
        
    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)