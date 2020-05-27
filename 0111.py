# 2020/05/17
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return 1 + max(left, right)
        return 1 + min(left, right)