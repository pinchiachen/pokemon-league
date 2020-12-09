## 2020/12/09

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isBST(root, float('inf'), -float('inf'))
        
    def isBST(self, root, left_max, right_min):
        if not root: return True
        if root.val >= left_max or root.val <= right_min: return False
        return self.isBST(root.left, root.val, right_min) and self.isBST(root.right, left_max, root.val)