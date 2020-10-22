## 2020/10/22

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.nodes = []
        self.traversal(root, k)
        return self.nodes[k-1]

    def traversal(self, root, k):
        if not root: return
        self.traversal(root.left, k)
        if len(self.nodes) >= k: return
        self.nodes.append(root.val)
        self.traversal(root.right, k)