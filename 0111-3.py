## 2021/07/30
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        res = 0
        if not root: return res
        queue = deque()
        queue.append(root)
        while queue:
            res += 1
            length = len(queue)
            for _ in range(length):
                current_node = queue.popleft()
                if not current_node.left and not current_node.right:
                    return res
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return res