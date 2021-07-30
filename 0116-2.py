## 2021/07/30
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            for idx in range(length):
                current_node = queue.popleft()
                current_node.next = queue[0] if idx < length - 1 else None
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return root