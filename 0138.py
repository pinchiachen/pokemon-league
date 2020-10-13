## 2020/10/13

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        node_dict = dict()
        dummy = Node(0, None, None)
        node_dict[head] = dummy
        new_head = dummy
        pointer = head
        while pointer:
            node = Node(pointer.val, pointer.next, None)
            node_dict[pointer] = node
            new_head.next = node
            new_head = new_head.next
            pointer = pointer.next
        pointer = head
        while pointer:
            if pointer.random:
                node_dict[pointer].random = node_dict[pointer.random]
            pointer = pointer.next
        return dummy.next