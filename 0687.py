# 2020/05/17
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root: return 0
        left_len = self.dfs(root.left)
        right_len = self.dfs(root.right)
        left = left_len + 1 if root.left and root.val == root.left.val else 0
        right = right_len + 1 if root.right and root.val == root.right.val else 0
        self.res = max(self.res, left + right)
        return max(left, right)