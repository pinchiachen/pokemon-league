## 2021/04/09

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, root, res):
        if not root: return
        self.traversal(root.left, res)
        self.traversal(root.right, res)
        res.append(root.val)