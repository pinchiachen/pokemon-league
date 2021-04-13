## 2021/04/13

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.travsersal(root, 0)
        return self.res

    def travsersal(self, root, depth):
        if not root: return
        cur_depth = depth + 1
        self.res = max(self.res, cur_depth)
        self.travsersal(root.left, cur_depth)
        self.travsersal(root.right, cur_depth)