## 2020/10/15

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return None
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        for i in range(1, len(nodes)):
            is_insert = False
            for j in range(i-1, -1, -1):
                if is_insert:
                    break;
                if nodes[i].val > nodes[j].val:
                    is_insert = True
                    nodes.insert(j+1, nodes[i])
                    del nodes[i+1]
            if not is_insert:
                nodes.insert(0, nodes[i])
                del nodes[i+1]
        for i in range(len(nodes)):
            nodes[i].next = None if (i == len(nodes) - 1) else nodes[i+1]
        return nodes[0]
