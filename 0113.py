## 2020/10/07

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        res = []
        self.dfs(root, [root.val], res, sum, root.val)
        return res

    def dfs(self, root, path, res, target, tmp_sum):
        if (not root.left) and (not root.right) and (tmp_sum == target):
            res.append(path)
            return
        if root.left:
            self.dfs(root.left, path + [root.left.val], res, target, tmp_sum + root.left.val)
        if root.right:
            self.dfs(root.right, path + [root.right.val], res, target, tmp_sum + root.right.val)
        return