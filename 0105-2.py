## 2020/12/09

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        value = preorder[0]
        pivot = inorder.index(value)
        root = TreeNode(value)
        root.left = self.buildTree(preorder[1:1+pivot], inorder[:pivot])
        root.right = self.buildTree(preorder[1+pivot:], inorder[pivot+1:])
        return root