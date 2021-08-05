## 2021/08/05

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.traversal(root, [], sum)

    def traversal(self, root, path, target):
        if not root: return 0
        current_path = path + [root.val]
        count = 0
        summation = 0
        for i in range(len(current_path) - 1, -1, -1):
            summation += current_path[i]
            if summation == target:
                count += 1
        return count + self.traversal(root.left, current_path, target) + self.traversal(root.right, current_path, target)