## 2021/07/29
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = deque()
        if not root: return res
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            current_level = []
            for _ in range(length):
                current_node = queue.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            res.appendleft(current_level)
        return res