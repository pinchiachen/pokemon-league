## 2021/07/29
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        queue = deque()
        queue.append(root)
        left_to_right = True
        while queue:
            length = len(queue)
            current_level = deque()
            for _ in range(length):
                current_node = queue.popleft()
                if left_to_right:
                    current_level.append(current_node.val)
                else:
                    current_level.appendleft(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            res.append(current_level)
            left_to_right = not left_to_right
        return res