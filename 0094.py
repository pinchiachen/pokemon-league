## 2020/09/30

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        self.inorder(res, root)
        return res

    def inorder(self, res, root):
        if root.left:
            self.inorder(res, root.left)
        res.append(root.val)
        if root.right:
            self.inorder(res, root.right)
