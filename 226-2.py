# 2020/04/30
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        new_tree = TreeNode(root.val)
        new_tree.left = self.invertTree(root.right)
        new_tree.right = self.invertTree(root.left)
        return new_tree