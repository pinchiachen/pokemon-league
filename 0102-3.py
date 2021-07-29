## 2021/07/29

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.traversal(root, 0, res)
        return res

    def traversal(self, root, level, res):
        if not root: return
        if len(res) >= level + 1:
            res[level].append(root.val)
        else:
            res.append([root.val])
        self.traversal(root.left, level + 1, res)
        self.traversal(root.right, level + 1, res)

## BFS
class BFSSolution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        queue = deque()
        queue.append(root)
        while queue:
            current_level = []
            length = len(queue)
            for _ in range(length):
                current_node = queue.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            res.append(current_level)
        return res