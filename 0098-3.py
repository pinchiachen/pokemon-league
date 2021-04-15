## 2021/04/15

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, -float('inf'), float('inf'))

    def isValid(self, root, left_min, right_max):
        if not root: return True
        return root.val > left_min\
            and root.val < right_max\
            and self.isValid(root.left, left_min, min(right_max, root.val))\
            and self.isValid(root.right, max(left_min, root.val), right_max)