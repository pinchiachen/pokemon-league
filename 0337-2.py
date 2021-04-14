## 2021/04/14

class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.traversal(root)[1]

    def traversal(self, root):
        if not root: return [0, 0]
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        last_rub = left[1] + right[1]
        last_no_rub = left[0] + right[0]
        this_no_rub = last_rub
        this_rub = max(this_no_rub, last_no_rub + root.val)
        return [this_no_rub, this_rub]