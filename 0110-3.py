## 2022/10/21

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. declare a function to calculate the depth of root
# 2. go through all child nodes and check the criteria
# 3. terminating when fitting the criteria
# 4. if no termination, it's a Balanced-Binary-Tree
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.maxDepth(root) != -1

    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1