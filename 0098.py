## 2020/10/03

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        left_min = -float('inf')
        right_max = float('inf')
        return self.isBST(root, left_min, right_max)

    def isBST(self, root, left_min, right_max):
        if not root: return True
        if root.val >= right_max or root.val <= left_min:
            return False
        return self.isBST(root.left, left_min, root.val) and self.isBST(root.right, root.val, right_max)
