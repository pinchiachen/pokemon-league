# 2020/05/17
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        if self.isLeaf(root.left):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)

    def isLeaf(self, root):
        if not root: return False
        return not root.right and not root.left