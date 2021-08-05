## 2021/08/05

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.traversal(root, [], res, targetSum)
        return res

    def traversal(self, root, path, res, target):
        if not root: return
        current_path = path + [root.val]
        if root.val == target and not root.left and not root.right:
            res.append(current_path)
            return
        self.traversal(root.left, current_path, res, target - root.val)
        self.traversal(root.right, current_path, res, target - root.val)