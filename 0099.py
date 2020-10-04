## 2020/10/04

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        pointers = []
        values = []
        self.inOrder(root, pointers, values)
        values.sort()
        for i in range(len(pointers)):
            pointers[i].val = values[i]

    def inOrder(self, root, pointers, values):
        if not root: return
        self.inOrder(root.left, pointers, values)
        pointers.append(root)
        values.append(root.val)
        self.inOrder(root.right, pointers, values)