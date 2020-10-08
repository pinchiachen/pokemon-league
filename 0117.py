## 2020/10/08

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
        pointers_arr = []
        self.levelOrder(root, 0, pointers_arr)
        for pointers in pointers_arr:
            for i in range(len(pointers) - 1):
                pointers[i].next = pointers[i + 1]
            pointers[-1].next = None
        return root

    def levelOrder(self, root, level, pointers_arr):
        if not root: return
        if len(pointers_arr) < level + 1:
            pointers_arr.append([root])
        else:
            pointers_arr[level].append(root)
        self.levelOrder(root.left, level + 1, pointers_arr)
        self.levelOrder(root.right, level + 1, pointers_arr)