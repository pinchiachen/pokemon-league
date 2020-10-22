## 2020/10/22

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if min(p.val, q.val) <= root.val and max(p.val, q.val) >= root.val:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

class BadSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.index_p = -1
        self.index_q = -1
        self.nodes = []
        self.traversal(root, 0, p, q)
        filter_arr = self.nodes[self.index_p:self.index_q+1]\
            if self.index_q > self.index_p\
            else self.nodes[self.index_q:self.index_p+1]
        return min(filter_arr, key = lambda x: x[1])[0]

    def traversal(self, root, level, p, q):
        if not root: return
        self.traversal(root.left, level + 1, p, q)
        self.nodes.append([root, level])
        if root == p:
            self.index_p = len(self.nodes) - 1
        if root == q:
            self.index_q = len(self.nodes) - 1
        self.traversal(root.right, level + 1, p, q)