## 2020/10/19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        self.values = []
        self.traversal(root, 0)
        for values in self.values:
            res.append(values[0])
        return res

    def traversal(self, root, level):
        if not root: return
        if len(self.values) > level:
            self.values[level].append(root.val)
        else:
            self.values.append([root.val])
        self.traversal(root.right, level + 1)
        self.traversal(root.left, level + 1)