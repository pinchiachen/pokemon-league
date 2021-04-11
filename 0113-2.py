## 2021/04/11

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        path = []
        self.traversal(root, targetSum, path, res)
        return res

    def traversal(self, root, target, path, res):
        if not root: return
        new_path = path + [root.val]
        new_target = target - root.val
        if not root.left and not root.right and new_target == 0:
            res.append(new_path)
        self.traversal(root.left, new_target, new_path, res)
        self.traversal(root.right, new_target, new_path, res)