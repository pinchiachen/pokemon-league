# 2020/05/17
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.go_left(root.left)
        self.go_right(root.right)
        return self.res

    def go_left(self, root):
        if not root: return
        if not root.left and not root.right:
            self.res += root.val
        self.go_left(root.left)
        self.go_right(root.right)

    def go_right(self, root):
        if not root: return
        self.go_left(root.left)
        self.go_right(root.right)