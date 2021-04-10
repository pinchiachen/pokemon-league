## 2021/04/10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        res = []
        path = []
        self.traversal(root, res, path)
        return res

    def traversal(self, root, res, path):
        if not root: return
        cur_path = path + [str(root.val)]
        if not root.left and not root.right:
            res.append('->'.join(cur_path))
        self.traversal(root.left, res, cur_path)
        self.traversal(root.right, res, cur_path)