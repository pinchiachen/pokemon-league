## 2020/10/05

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        level = 0
        res = []
        self.traversal(root, level, res)
        return res[::-1]

    def traversal(self, root, level, res):
        if not root: return
        if len(res) >= level + 1:
            res[level].append(root.val)
        else:
            res.append([root.val])
        if root.left:
            self.traversal(root.left, level + 1, res)
        if root.right:
            self.traversal(root.right, level + 1, res)