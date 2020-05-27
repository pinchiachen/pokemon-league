# 2020/05/14
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    def dfs(self, root, target):
        if not root: return 0
        res = 0
        if root.val == target:
            res += 1
        res += self.dfs(root.left, target - root.val) + self.dfs(root.right, target - root.val)
        return res