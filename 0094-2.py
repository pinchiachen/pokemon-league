## 2021/04/09

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, root, res):
        if not root: return
        self.traversal(root.left, res)
        res.append(root.val)
        self.traversal(root.right, res)