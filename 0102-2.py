## 2020/12/09

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.traversal(root, 0, res)
        return res

    def traversal(self, root, level, res):
        if not root: return
        if len(res) < level + 1:
            res.append([root.val])
        else:
            res[level].append(root.val)
        self.traversal(root.left, level + 1, res)
        self.traversal(root.right, level + 1, res)