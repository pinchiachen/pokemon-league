## 2020/10/07

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        arr = []
        self.preOrder(root, arr)
        self.setValue(root, arr, 1)
        
    def preOrder(self, root, arr):
        if not root: return
        arr.append(root.val)
        self.preOrder(root.left, arr)
        self.preOrder(root.right, arr)

    def setValue(self, root, arr, index):
        if index >= len(arr): return
        root.left = None
        root.right = TreeNode(arr[index])
        self.setValue(root.right, arr, index + 1)
